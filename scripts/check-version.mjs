#!/usr/bin/env node
// Fails unless every file of a component that declares a version declares the one being released.
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const jsonVersion = (text) => JSON.parse(text).version;
const tomlProjectVersion = (text) => /^version\s*=\s*"([^"]+)"/m.exec(text)?.[1];
const pythonDunderVersion = (text) => /^__version__\s*=\s*"([^"]+)"/m.exec(text)?.[1];

const DECLARATIONS = {
    desktop: [
        ['package.json', jsonVersion],
        ['src-tauri/tauri.conf.json', jsonVersion],
        ['src-vscode/package.json', jsonVersion]
    ],
    cli: [
        ['pyproject.toml', tomlProjectVersion],
        ['src/specforge_cli/__init__.py', pythonDunderVersion]
    ]
};

const [component, root, expected] = process.argv.slice(2);
const declarations = DECLARATIONS[component];
if (!declarations || !root || !expected) {
    console.error('usage: check-version.mjs <desktop|cli> <checkout> <version>');
    process.exit(2);
}

let mismatches = 0;
for (const [file, read] of declarations) {
    const declared = read(readFileSync(join(root, file), 'utf-8'));
    if (declared !== expected) {
        console.error(`::error::${file} declares ${declared}, not ${expected}`);
        mismatches += 1;
    }
}
process.exit(mismatches === 0 ? 0 : 1);
