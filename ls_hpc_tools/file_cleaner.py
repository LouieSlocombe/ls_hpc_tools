#!/usr/bin/env python3
"""
clean_slurm.py  –  Recursively find and delete files whose names start with 'slurm'

Usage examples
--------------
# Show what would be deleted from the current directory, but don’t do it
python3 clean_slurm.py --dry-run

# Delete immediately without asking for confirmation
python3 clean_slurm.py --force

# Search /scratch/jobs, ask before deleting
python3 clean_slurm.py /scratch/jobs
"""

from pathlib import Path
import argparse
import sys

def find_slurm_files(root: Path):
    """Yield every regular file under *root* whose basename starts with 'slurm'."""
    for path in root.rglob('slurm*'):
        if path.is_file():
            yield path

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Recursively delete files whose names begin with 'slurm'.")
    parser.add_argument(
        "root", nargs="?", default=".",
        help="Directory to start searching (default: current directory)")
    parser.add_argument(
        "-n", "--dry-run", action="store_true",
        help="List matching files but do NOT delete them")
    parser.add_argument(
        "-f", "--force", action="store_true",
        help="Delete without asking for confirmation")
    args = parser.parse_args()

    root_dir = Path(args.root).expanduser().resolve()
    matches = list(find_slurm_files(root_dir))

    if not matches:
        print("No matching files found.")
        return

    print(f"Found {len(matches)} file(s) whose name starts with 'slurm':")
    for p in matches:
        print("  ", p)

    if args.dry_run:
        print("\nDry-run mode – nothing deleted.")
        return

    if not args.force:
        resp = input("\nDelete all of these files? [y/N] ").strip().lower()
        if resp not in {"y", "yes"}:
            print("Aborted – no files deleted.")
            return

    # Attempt deletion
    failed = []
    for p in matches:
        try:
            p.unlink()
        except Exception as exc:
            failed.append((p, exc))

    deleted = len(matches) - len(failed)
    print(f"\nDeleted {deleted} file(s).")
    if failed:
        print("The following files could not be removed:", file=sys.stderr)
        for p, exc in failed:
            print(f"  {p}: {exc}", file=sys.stderr)

if __name__ == "__main__":
    main()
