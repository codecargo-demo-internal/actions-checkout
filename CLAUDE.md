# CLAUDE.md

## Project Overview
This is the `actions/checkout` GitHub Action - a TypeScript-based action that checks out repositories in GitHub Actions workflows. It's one of the most widely used GitHub Actions.

## Tech Stack
- **Language**: TypeScript
- **Runtime**: Node.js (node24)
- **Testing**: Jest
- **Build**: @vercel/ncc (compiles TypeScript to single JS file)
- **Key Dependencies**: @actions/core, @actions/exec, @actions/github, @actions/io

## Project Structure
- `src/` - TypeScript source code
  - `main.ts` - Entry point
  - `git-*.ts` - Git operations (auth, commands, directory management, version handling)
  - `*-helper.ts` - Various helper modules
  - `misc/` - Utility scripts
- `__test__/` - Jest tests and verification scripts
- `action.yml` - Action metadata and input/output definitions
- `lib/` - Compiled JavaScript output (generated, not in repo)

## Development Commands
- `npm run build` - Compile TypeScript, bundle with ncc, generate docs
- `npm run test` - Run Jest test suite
- `npm run lint` - Lint TypeScript files with ESLint
- `npm run format` - Format code with Prettier
- `npm run format-check` - Check code formatting

## Key Features
- Checks out repositories in GitHub Actions workflows
- Supports authentication via token or SSH key
- Handles submodules, LFS, sparse checkout
- Credential management with security improvements in v6
- Falls back to REST API when Git 2.18+ not available

## Testing
Run tests with `npm test`. Tests cover git operations, input parsing, URL handling, and various checkout scenarios.

## Build Process
The build process compiles TypeScript and bundles everything into `lib/main.js` using ncc. Always run `npm run build` before committing changes.

## Important Notes
- This is a public repository maintained by GitHub
- Not currently accepting external contributions (see README)
- Requires Actions Runner v2.327.1+ for node24 runtime
- Security issues should follow security.md guidelines
