#!/usr/bin/env python3
"""
用法: python scripts/publish.py _inbox/文章名.md
"""

import sys
import re
import subprocess
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).parent.parent
SECTIONS = {"spirit", "culture", "travel", "reading"}


def parse_frontmatter(text):
    meta = {}
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].splitlines():
                if ":" in line:
                    key, _, val = line.partition(":")
                    meta[key.strip()] = val.strip()
            body = text[end + 4:].strip()
    return meta, body


def slugify(name):
    name = re.sub(r"[^\w一-鿿]+", "-", name)
    return name.strip("-").lower()


def normalize_date(date_str):
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S"):
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%dT%H:%M:%S+08:00")
        except ValueError:
            continue
    return date_str


def run(cmd, cwd=ROOT):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        print(f"失败: {' '.join(cmd)}")
        print(result.stderr)
        sys.exit(1)
    return result


def main():
    if len(sys.argv) < 2:
        print("用法: python scripts/publish.py <文件路径>")
        sys.exit(1)

    src = Path(sys.argv[1])
    if not src.exists():
        print(f"文件不存在: {src}")
        sys.exit(1)

    text = src.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)

    title = meta.get("title", "").strip()
    if not title:
        title = input("文章标题: ").strip()

    section = meta.get("section", "").lower().strip()
    if section not in SECTIONS:
        print(f"板块 ({'/'.join(SECTIONS)}): ", end="")
        section = input().strip().lower()
        if section not in SECTIONS:
            print(f"无效板块: {section}")
            sys.exit(1)

    raw_date = meta.get("date", datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00"))
    date_str = normalize_date(raw_date)

    slug = slugify(src.stem)

    escaped_title = title.replace('"', '\\"')
    hugo_fm = f"""+++
date = '{date_str}'
draft = false
title = "{escaped_title}"
+++

"""

    dest = ROOT / "content" / section / f"{slug}.md"
    dest.write_text(hugo_fm + body, encoding="utf-8")
    print(f"[1/4] 写入 content/{section}/{slug}.md")

    print("[2/4] 运行 hugo ...")
    run(["hugo"])
    print("      hugo 构建完成")

    print("[3/4] git commit ...")
    run(["git", "add", f"content/{section}/{slug}.md", "docs/"])
    run(["git", "commit", "-m", f"发布: {title}"])

    print("[4/4] git push ...")
    run(["git", "push"])

    print(f"\n完成! https://benlai.me/{section}/{slug}/")


if __name__ == "__main__":
    main()
