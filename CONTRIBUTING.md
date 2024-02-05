# Semantic Commit Messages with Emojis

Commit format: `<commit_type>: <subject>. <issue_reference>`

## Example
```
feat: Add a new feature. Closes: #
^--^  ^---------------^  ^------^
|     |                  |
|     |                  +--> (Optional) Issue reference: if the commit closes or fixes an issue
|     |
|     +---------------------> Commit summary
|
+--------------------------------------> Commit type: feat, fix, docs, refactor, test, style, chore, build, perf or ci
```

**The commit message will be:**

> feat: Add a new feature. Closes #1

## Commit Message Types

- 💥 **breaking**: introducing a breaking change to the codebase
- ✨ **feat**: introducing a new feature to the codebase
- 🐛 **fix**: fixing a bug in the codebase
- ⚡ **perf**: changes related to backward-compatible performance improvements
- ♻️ **refactor**: refactoring the production code
- 🚀 **chore**: updating grunt tasks etc. (no production code change)
- 📖 **docs**: adding or updating the documentation
- ✅ **test**: adding tests (no production code change)
- 🤖 **ci**: changes related to the continuous integration and deployment system
- 🎨 **style**: improving structure/format of the code e.g. missing semi colons (no production code change)
- 🏗 **build**: changes related to the build system (involving scripts, configurations) and package dependencies

## Issue Referencing
Keywords to close an related issue with the commit:
- close
- closes
- closed
- fix
- fixes
- fixed
- resolve
- resolves
- resolved

You can use the phrase: `Fixes: #1` or `Fixes #1`.
Once the branch is merged into the default branch, the issue will close.
