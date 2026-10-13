"""Load, apply patches and version-control translator/evaluator skills."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any


class Skill:
    def __init__(self, path: Path):
        self.path = path
        self.raw = path.read_text(encoding="utf-8")
        self.meta, self.body = self._parse(self.raw)
        self.name = self.meta.get("name", path.stem)
        self.version = self.meta.get("version", "v0")

    @staticmethod
    def _parse(text: str) -> tuple[dict, str]:
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                import yaml
                meta = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return meta, body
        return {}, text.strip()

    def render(self) -> str:
        return self.body

    def clone(self, version: str) -> "Skill":
        new_skill = Skill.__new__(Skill)
        new_skill.path = self.path
        new_skill.raw = self.raw
        new_skill.meta = dict(self.meta)
        new_skill.body = self.body
        new_skill.name = self.name
        new_skill.version = version
        return new_skill


class SkillManager:
    def __init__(self, skills_dir: str | Path):
        self.dir = Path(skills_dir)
        self.dir.mkdir(parents=True, exist_ok=True)

    def load(self, name: str) -> Skill:
        # name may be "translator_skill_v0" or full filename
        candidates = [self.dir / f"{name}.md", self.dir / name]
        for cand in candidates:
            if cand.exists():
                return Skill(cand)
        raise FileNotFoundError(f"skill {name} not found in {self.dir}")

    def save(self, skill: Skill, version: str | None = None) -> Path:
        version = version or skill.version
        out_path = self.dir / f"{skill.name}_{version}.md"
        lines = ["---"]
        meta = dict(skill.meta)
        meta["version"] = version
        import yaml
        lines.append(yaml.dump(meta, allow_unicode=True, sort_keys=False).strip())
        lines.append("---")
        lines.append(skill.body)
        out_path.write_text("\n".join(lines), encoding="utf-8")
        return out_path

    @staticmethod
    def apply_patch(skill: Skill, patch: str, new_version: str) -> Skill:
        """Apply a diff-style patch to the skill body.

        Supported simple patch format:
        - # ADD AFTER: <marker>\n<text>   -> insert text after first occurrence of marker
        - # REPLACE: <marker>\n<text>    -> replace first occurrence of marker with text
        - raw text appended at the end otherwise
        """
        new_skill = skill.clone(new_version)
        body = new_skill.body

        # collect operations
        adds = re.findall(r"#\s*ADD\s+AFTER:\s*(.+?)\n(.*?)(?=\n#\s*(?:ADD\s+AFTER|REPLACE):|\Z)", patch, re.DOTALL)
        replaces = re.findall(r"#\s*REPLACE:\s*(.+?)\n(.*?)(?=\n#\s*(?:ADD\s+AFTER|REPLACE):|\Z)", patch, re.DOTALL)

        for marker, text in adds:
            marker = marker.strip()
            text = text.strip()
            idx = body.find(marker)
            if idx != -1:
                insert_pos = idx + len(marker)
                body = body[:insert_pos] + "\n" + text + body[insert_pos:]

        for marker, text in replaces:
            marker = marker.strip()
            text = text.strip()
            body = body.replace(marker, text, 1)

        if not adds and not replaces:
            # fallback: append raw patch
            body = body + "\n\n" + patch.strip()

        new_skill.body = body.strip()
        new_skill.version = new_version
        return new_skill
