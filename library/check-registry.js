#!/usr/bin/env node
// Verify library/registry.json against the skills on disk.
// Checks: valid JSON; every registry entry maps to an existing SKILL.md at its
// declared location; every SKILL.md on disk (active + library) is in the registry.
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const registryPath = path.join(__dirname, 'registry.json');
const activeDir = path.join(root, '.claude', 'skills');
const libDir = path.join(__dirname, 'skills');

let errors = [];

let registry;
try {
  registry = JSON.parse(fs.readFileSync(registryPath, 'utf8'));
} catch (e) {
  console.error('FAIL: registry.json is not valid JSON: ' + e.message);
  process.exit(1);
}
console.log('OK: registry.json is valid JSON');

const skills = registry.skills || [];
const registryNames = new Set();

for (const s of skills) {
  if (!s.name || !s.category || !s.summary || !Array.isArray(s.triggers) || !s.location) {
    errors.push('entry missing required field: ' + JSON.stringify(s));
    continue;
  }
  registryNames.add(s.name);
  const base = s.location === 'active' ? activeDir : libDir;
  const skillFile = path.join(base, s.name, 'SKILL.md');
  if (!fs.existsSync(skillFile)) {
    errors.push('registry entry "' + s.name + '" (location ' + s.location + ') has no SKILL.md at ' + skillFile);
  }
}

function dirSkills(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .filter(d => fs.existsSync(path.join(dir, d.name, 'SKILL.md')))
    .map(d => d.name);
}

const activeOnDisk = dirSkills(activeDir);
const libOnDisk = dirSkills(libDir);

for (const name of [...activeOnDisk, ...libOnDisk]) {
  if (!registryNames.has(name)) {
    errors.push('SKILL.md on disk for "' + name + '" is not in the registry');
  }
}

// Cross-check that on-disk location matches registry location for active skills.
for (const s of skills) {
  if (s.location === 'active' && !activeOnDisk.includes(s.name)) {
    errors.push('"' + s.name + '" marked active but not found in .claude/skills/');
  }
  if (s.location === 'library' && !libOnDisk.includes(s.name) && !activeOnDisk.includes(s.name)) {
    errors.push('"' + s.name + '" marked library but no folder found');
  }
}

console.log('Registry entries: ' + skills.length);
console.log('Active skills on disk: ' + activeOnDisk.length + ' (' + activeOnDisk.sort().join(', ') + ')');
console.log('Library skills on disk: ' + libOnDisk.length + ' (' + libOnDisk.sort().join(', ') + ')');

if (errors.length) {
  console.error('\nFAIL: ' + errors.length + ' problem(s):');
  errors.forEach(e => console.error('  - ' + e));
  process.exit(1);
}
console.log('\nPASS: registry and disk are in sync.');
