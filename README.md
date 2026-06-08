# Gate Challenger Skill

This repository contains the canonical source for the `gate-challenger` skill.

It routes Gate 2, 1st Stream Review, and Gate 3 / SR 2 documents to stage-specific rubrics while sharing the same evidence, output, synthesis, and verdict contracts.

The installable skill package is:

- [`skills/gate-challenger`](/Users/iseremenko/Projects/Gate2-challenger/skills/gate-challenger)

Copy the whole folder as-is. The package is self-contained and includes:

- `SKILL.md`
- `references/`
- `scripts/pdf_to_md_docling.py`

## Repository Layout

```text
skills/
  gate-challenger/
    SKILL.md
    references/
    scripts/
```

## Install in Codex

Install as a personal skill:

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/Gate2-challenger/skills/gate-challenger ~/.codex/skills/
```

Example for this repository checkout:

```bash
mkdir -p ~/.codex/skills
cp -R /Users/iseremenko/Projects/Gate2-challenger/skills/gate-challenger ~/.codex/skills/
```

After copying, restart Codex or start a new session so the skill is discovered.

## Install in Claude

Install as a personal Claude Code skill:

```bash
mkdir -p ~/.claude/skills
cp -R /path/to/Gate2-challenger/skills/gate-challenger ~/.claude/skills/
```

Example for this repository checkout:

```bash
mkdir -p ~/.claude/skills
cp -R /Users/iseremenko/Projects/Gate2-challenger/skills/gate-challenger ~/.claude/skills/
```

You can also install it as a project skill by copying the same folder into `.claude/skills/` inside a repository.

After copying, restart Claude Code or start a new session so the skill is discovered.

## Notes

- Keep the directory name `gate-challenger`.
- Copy the entire folder, not only `SKILL.md`.
- Before running a review from a checkout, verify the skill is current with git:
  `python3 skills/gate-challenger/scripts/check_git_freshness.py`.
- For PDF review mode, the helper script writes Markdown into a `review-documents/` folder next to the source PDF.
- The PDF conversion helper requires `docling`.
