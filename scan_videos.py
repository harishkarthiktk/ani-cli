#!/usr/bin/env python3
"""
scan_videos.py - Scan video files for corruption using ffmpeg.

Usage:
    python scan_videos.py -d /path/to/folder
    python scan_videos.py -d /path/to/folder -o
    python scan_videos.py -d /path/to/folder -o report.txt
"""

import argparse
import subprocess
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm", ".m4v", ".ts", ".m2ts"}


def check_ffmpeg():
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        print("ERROR: ffmpeg not found. Please install ffmpeg and ensure it is in your PATH.")
        sys.exit(1)


def scan_file(path: Path) -> dict:
    # Get duration
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    raw = result.stdout.strip()
    try:
        duration = format_duration(float(raw))
    except ValueError:
        duration = "unknown"

    # Scan for errors with streaming
    proc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-i", str(path), "-f", "null", "-"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )
    kept, count = [], 0
    for line in proc.stderr:
        line = line.rstrip()
        if line:
            count += 1
            if count <= 50:
                kept.append(line)
    proc.wait()

    return {
        "path": path,
        "duration": duration,
        "error_count": count,
        "errors": kept,
    }


def format_duration(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def scan_folder(folder: Path) -> list:
    files = sorted(
        f for f in folder.rglob("*") if f.suffix.lower() in VIDEO_EXTENSIONS
    )
    if not files:
        print(f"No video files found in: {folder}")
        sys.exit(0)
    return files


def build_report(results: list, folder: Path) -> str:
    lines = []
    lines.append("=" * 70)
    lines.append("VIDEO INTEGRITY SCAN REPORT")
    lines.append(f"Folder : {folder}")
    lines.append(f"Files  : {len(results)}")

    ok = [r for r in results if r["error_count"] == 0]
    bad = [r for r in results if r["error_count"] > 0]

    lines.append(f"Healthy: {len(ok)}   Corrupted: {len(bad)}")
    lines.append("=" * 70)
    lines.append("")

    lines.append(f"{'FILE':<50} {'DURATION':<12} {'STATUS'}")
    lines.append("-" * 70)
    for r in results:
        name = r["path"].name
        name_col = (name[:47] + "...") if len(name) > 50 else name
        duration = r["duration"]
        if r["error_count"] == 0:
            status = "OK"
        else:
            status = f"CORRUPTED ({r['error_count']} error lines)"
        lines.append(f"{name_col:<50} {duration:<12} {status}")

    if bad:
        lines.append("")
        lines.append("=" * 70)
        lines.append("CORRUPTION DETAILS")
        lines.append("=" * 70)
        for r in bad:
            lines.append("")
            lines.append(f"File: {r['path'].name}")
            lines.append(f"Total error lines: {r['error_count']}")
            lines.append("Sample errors (first 10):")
            for err in r["errors"][:10]:
                lines.append(f"  {err}")
            if r["error_count"] > 10:
                lines.append(f"  ... and {r['error_count'] - 10} more lines.")
            lines.append("-" * 70)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Scan video files for corruption using ffmpeg."
    )
    parser.add_argument(
        "-d", "--directory", required=True,
        help="Folder containing video files to scan."
    )
    parser.add_argument(
        "-o", "--output", nargs="?", const="report.txt", default=None,
        metavar="FILE",
        help="Save report to file. Defaults to 'report.txt' if no filename given."
    )
    args = parser.parse_args()

    check_ffmpeg()

    folder = Path(args.directory).resolve()
    if not folder.is_dir():
        print(f"ERROR: Not a valid directory: {folder}")
        sys.exit(1)

    files = scan_folder(folder)
    total = len(files)

    print(f"Found {total} video file(s) in: {folder}")

    results = []
    with ThreadPoolExecutor(max_workers=min(4, total)) as executor:
        futures = {executor.submit(scan_file, f): f for f in files}
        for future in tqdm(as_completed(futures), total=total, unit="file", desc="Scanning", position=0, leave=True):
            result = future.result()
            results.append(result)
            path = result["path"]
            if result["error_count"] == 0:
                tqdm.write(f"{path.name} ... OK")
            else:
                tqdm.write(f"{path.name} ... CORRUPTED ({result['error_count']} error lines)")

    # Sort by filename for consistent report output
    results.sort(key=lambda r: r["path"].name)

    print()
    report = build_report(results, folder)
    print(report)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(report, encoding="utf-8")
        print(f"\nReport saved to: {out_path.resolve()}")


if __name__ == "__main__":
    main()
