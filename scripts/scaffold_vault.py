#!/usr/bin/env python3
"""Create a starter Obsidian content flywheel structure."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


FOLDERS = [
    "00_Workflow",
    "01_Inbox",
    "02_Knowledge_Atoms",
    "03_Topic_Seeds",
    "04_COPE_Drafts",
    "99_Templates",
]

TEMPLATE_FILES = [
    "source-note.md",
    "knowledge-matrix.md",
    "topic-seed.md",
    "cope-draft.md",
]


def scaffold(vault: Path, force: bool = False) -> list[str]:
    skill_root = Path(__file__).resolve().parents[1]
    template_root = skill_root / "templates"
    created: list[str] = []

    vault.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        target = vault / folder
        if not target.exists():
            target.mkdir(parents=True)
            created.append(str(target))

    for name in TEMPLATE_FILES:
        source = template_root / name
        target = vault / "99_Templates" / name
        if target.exists() and not force:
            continue
        shutil.copy2(source, target)
        created.append(str(target))

    return created


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a starter Obsidian content flywheel structure."
    )
    parser.add_argument("vault", help="Path to the Obsidian vault or output folder.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite template files in 99_Templates if they already exist.",
    )
    args = parser.parse_args()

    created = scaffold(Path(args.vault).expanduser().resolve(), force=args.force)
    if created:
        print("Created or updated:")
        for item in created:
            print(f"- {item}")
    else:
        print("No changes. Folders and templates already exist.")


if __name__ == "__main__":
    main()

