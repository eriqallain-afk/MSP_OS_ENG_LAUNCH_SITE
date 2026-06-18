#!/usr/bin/env python3
"""
scan_anonymisation.py — Garde-fou d'anonymisation (portable, CI Linux/macOS/Windows).

Détecte tout motif de **billet réel** dans les fichiers du site (HTML, MD, JS, JSON, CSS, YAML, TXT).
Port Python de `scan-anonymisation.ps1` — mêmes motifs, mêmes règles, mais exécutable en CI
GitHub Actions (runners Linux) sans PowerShell.

Règle EA|IA (CLAUDE_GLOBAL §6.10) : aucune occurrence tolérée avant mise en ligne.
Sortie : code 0 si 0 occurrence, 1 sinon (bloque la CI).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN_SUFFIXES = {".html", ".htm", ".md", ".txt", ".js", ".json", ".css", ".yml", ".yaml"}
EXCLUDE_PARTS = {".git", "node_modules", "scripts"}

# Motifs de billets réels — port exact de scan-anonymisation.ps1
PATTERNS = [
    re.compile(r"Service\s+Ticket\s+#?\s*T?17\d{5}", re.I),
    re.compile(r"Billet\s+#?\s*T?17\d{5}", re.I),
    re.compile(r"Ticket\s+#?\s*T?17\d{5}", re.I),
    re.compile(r"#T?17\d{5}"),
    re.compile(r"T17\d{5}"),
    re.compile(r"(?<!\d)17\d{5}(?!\d)"),
]


def included(path: Path) -> bool:
    if path.suffix.lower() not in SCAN_SUFFIXES:
        return False
    return not any(part in EXCLUDE_PARTS for part in path.parts)


def main() -> int:
    findings: list[str] = []
    scanned = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or not included(path):
            continue
        scanned += 1
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            for rx in PATTERNS:
                if rx.search(line):
                    rel = path.relative_to(ROOT)
                    findings.append(f"{rel}:{n}: {line.strip()[:160]}")
                    break  # une ligne signalée une fois suffit

    if findings:
        print("❌ ANONYMISATION — motifs de billets réels détectés :\n")
        for f in findings:
            print(f"  {f}")
        print(f"\n{len(findings)} occurrence(s) sur {scanned} fichiers scannés. "
              "Anonymiser AVANT toute mise en ligne (règle EA|IA non négociable).")
        return 1

    print(f"✅ ANONYMISATION OK — 0 occurrence sur {scanned} fichiers scannés.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
