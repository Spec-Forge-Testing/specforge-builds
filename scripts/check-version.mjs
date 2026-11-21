#!/usr/bin/env node
// Fails unless the desktop app and the extension both declare the version being released.
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const [root, expected] = process.argv.slice(2);
const DECLARATIONS = ['package.json', 'src-tauri/tauri.conf.json', 'src-vscode/package.json'];

let mismatches = 0;
for (const file of DECLARATIONS) {
    const declared = JSON.parse(readFileSync(join(root, file), 'utf-8')).version;
    if (declared !== expected) {
        console.error(`::error::${file} declares ${declared}, not ${expected}`);
        mismatches += 1;
    }
}
process.exit(mismatches === 0 ? 0 : 1);
