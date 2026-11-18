#!/usr/bin/env python3
"""Canonicalize agent knowledge JSON and render Markdown without generation/network."""
import argparse
import copy
import hashlib
import html
import json
from pathlib import Path


def canonical_payload(payload):
    value = copy.deepcopy(payload)
    for source in value['sources']:
        for field in ('symbol', 'start_line', 'end_line'):
            source.setdefault(field, None)
    for entity in value['entities']:
        for field, default in (('owner', None), ('aliases', []), ('identifiers', [])):
            entity.setdefault(field, default)
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def render(payload, catalog):
    ontology = payload['ontology']
    if ontology['revision_id'] != catalog['revisionId'] or ontology['fingerprint'] != catalog['fingerprint']:
        raise ValueError('Payload and catalog ontology identities differ; refresh and revalidate')
    labels = {t['id']: t['label'] for group in ('vertices', 'edges') for t in catalog[group] if t['status'] == 'active'}
    sources = {s['id']: s for s in payload['sources']}
    entities = {e['id']: e for e in payload['entities']}
    text = lambda value: html.escape(str(value), quote=False)

    def evidence(record):
        anchors = []
        for key in record['evidence']:
            source = sources[key]
            anchor = source['path']
            if source.get('start_line') is not None:
                anchor += f":{source['start_line']}"
                if source.get('end_line') is not None:
                    anchor += f"–{source['end_line']}"
            if source.get('symbol'):
                anchor += ' — ' + source['symbol']
            anchors.append(text(anchor))
        return '; '.join(anchors)

    lines = [f"# {text(payload['title'])}", '', '## Entities', '']
    for entity in payload['entities']:
        lines += [f"### {text(entity['name'])}", '', f"Entity: {text(entity['name'])}",
            f"ID: {text(entity['id'])}", f"Type: {text(labels[entity['type_id']])}",
            f"Description: {text(entity['description'])}", f"Evidence: {evidence(entity)}"]
        for field in ('owner', 'aliases', 'identifiers'):
            if entity.get(field):
                lines.append(f"{field.capitalize()}: {text(json.dumps(entity[field], ensure_ascii=False))}")
        lines.append('')
    lines += ['## Relationships', '']
    for r in payload['relations']:
        lines += [f"ID: {text(r['id'])}", f"Source: {text(entities[r['source']]['name'])} ({text(r['source'])})",
            f"Relationship type: {text(labels[r['type_id']])}",
            f"Target: {text(entities[r['target']]['name'])} ({text(r['target'])})",
            f"Description: {text(r['description'])}", f"Evidence: {evidence(r)}", '']
    repo = payload['repository']
    digest = hashlib.sha256(canonical_payload(payload).encode('utf-8')).hexdigest()
    lines += ['## Provenance', '', f"Repository: {text(repo['name'])}", f"Commit: {text(repo['commit_sha'])}",
        f"Working tree dirty: {repo['working_tree_dirty']}", f"Context: {text(catalog['contextId'])}",
        f"Ontology revision: {text(ontology['revision_id'])}", f"Ontology fingerprint: {text(ontology['fingerprint'])}",
        f"Schema version: {payload['schema_version']}", f"Canonical payload SHA-256: {digest}", '',
        'Source anchors and file hashes are client-supplied provenance.', '']
    lines += [f"- {text(s['id'])}: {text(s['path'])} — SHA-256 {s['sha256']}" for s in payload['sources']]
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('payload', type=Path)
    parser.add_argument('--ontology', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    payload = json.loads(args.payload.read_text(encoding='utf-8'))
    catalog = json.loads(args.ontology.read_text(encoding='utf-8'))
    markdown, content = render(payload, catalog), canonical_payload(payload)
    output = args.output or args.payload.with_name(args.payload.name.removesuffix('.knowledge.json') + '.md')
    if output.resolve() in (args.payload.resolve(), args.ontology.resolve()):
        parser.error('Markdown output must differ from payload and ontology paths')
    args.payload.write_text(content, encoding='utf-8')
    output.write_text(markdown, encoding='utf-8')
    print(hashlib.sha256(content.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
