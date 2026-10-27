#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

FILES = ["README.md", "story-bible.md", "world.md", "characters/index.md", "outline/volume-01.md", "outline/timeline.md", "chapters/001-title.md"]

def init_project(out: Path, title: str):
    if not title.strip(): raise ValueError("needs_clarification: 作品名不能为空")
    for rel in FILES:
        p = out / rel; p.parent.mkdir(parents=True, exist_ok=True)
        if not p.exists():
            text = f"# {title}\n\n待填写。\n" if rel in ("README.md", "story-bible.md", "world.md") else "# 待填写\n\n"
            p.write_text(text, encoding="utf-8")
    return out

def check_project(root: Path) -> dict:
    missing = [f for f in FILES if not (root/f).exists()]
    chapters = sorted((root/"chapters").glob("*.md")) if (root/"chapters").exists() else []
    return {"status": "pass" if not missing else "needs_review", "missing": missing, "chapter_count": len(chapters)}

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True); sub.add_parser("self-test"); i=sub.add_parser("init"); i.add_argument("--output",required=True); i.add_argument("--title",required=True); c=sub.add_parser("check"); c.add_argument("--input",required=True); a=p.parse_args()
    if a.cmd=="self-test":
        root=Path(__file__).parents[1]; tmp=Path("/tmp/fiction-crafter-self-test"); init_project(tmp,"测试作品"); result=check_project(tmp); assert result["status"]=="pass" and result["chapter_count"]==1
        failure=check_project(root/"examples/failure-project"); assert failure["status"]=="needs_review"
        print("self-test: PASS (init + continuity failure sample)"); return
    try:
        if a.cmd=="init": print(f"initialized {init_project(Path(a.output),a.title)}")
        else: print(json.dumps(check_project(Path(a.input)),ensure_ascii=False,indent=2))
    except (OSError,ValueError) as e: print(e,file=sys.stderr); return 1
if __name__=="__main__": sys.exit(main() or 0)
