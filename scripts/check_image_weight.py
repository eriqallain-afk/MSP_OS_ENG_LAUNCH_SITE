#!/usr/bin/env python3
"""
check_image_weight.py — Garde-fou de poids des images (NE MODIFIE AUCUNE image).

But : empêcher le site de s'alourdir. Lit uniquement la TAILLE des fichiers image — ne recompresse,
ne réécrit, ne supprime rien.

Budget : 500 Ko/image (CI_IMAGE_BUDGET_KB pour ajuster).

Cliquet (ratchet) via allowlist `scripts/image_weight_allowlist.txt` :
  - image > budget, ABSENTE de l'allowlist        -> ERREUR (nouvelle image trop lourde).
  - image > budget, PRÉSENTE, taille <= référence -> OK (grandfather : tolérée telle quelle).
  - image > budget, PRÉSENTE, taille  > référence -> ERREUR (une grandfathered ne doit que rétrécir).
  - entrée d'allowlist désormais <= budget / absente -> WARN (à retirer : cliquet terminé).

Usage :
  python scripts/check_image_weight.py                   # vérifie (exit 1 si ERREUR)
  python scripts/check_image_weight.py --update-allowlist # régénère l'allowlist sur l'état courant

Référencé par `.github/workflows/image-weight.yml`.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ALLOWLIST = REPO / "scripts" / "image_weight_allowlist.txt"
BUDGET = int(os.environ.get("CI_IMAGE_BUDGET_KB", "500")) * 1024

IMG_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".bmp", ".tiff", ".tif"}
SIGS = (b"\x89PNG", b"\xff\xd8\xff", b"GIF8", b"RIFF", b"BM")
EXCLUDE_PARTS = {".git", "node_modules", "scripts"}


def is_image(p: Path) -> bool:
    if p.suffix.lower() in IMG_EXT:
        return True
    try:
        with open(p, "rb") as f:
            head = f.read(4)
        return any(head.startswith(s) for s in SIGS)
    except OSError:
        return False


def scan_images() -> dict[str, int]:
    out = {}
    for p in REPO.rglob("*"):
        if not p.is_file() or any(part in EXCLUDE_PARTS for part in p.parts):
            continue
        if is_image(p):
            out[p.relative_to(REPO).as_posix()] = p.stat().st_size
    return out


def load_allowlist() -> dict[str, int]:
    entries = {}
    if not ALLOWLIST.exists():
        return entries
    for line in ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        size_str, _, path = line.partition(" ")
        try:
            entries[path.strip()] = int(size_str)
        except ValueError:
            continue
    return entries


def write_allowlist(over: dict[str, int]) -> None:
    lines = [
        "# Allowlist du garde-fou de poids des images (grandfather).",
        f"# Budget : {BUDGET // 1024} Ko. Format : <octets> <chemin>.",
        "# Une image listée ne doit que RÉTRÉCIR. Retire la ligne quand elle passe sous le budget.",
        "# Régénérer : python scripts/check_image_weight.py --update-allowlist",
        "",
    ]
    for path in sorted(over):
        lines.append(f"{over[path]} {path}")
    ALLOWLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    images = scan_images()
    over = {p: s for p, s in images.items() if s > BUDGET}

    if "--update-allowlist" in sys.argv[1:]:
        write_allowlist(over)
        print(f"Allowlist régénérée : {len(over)} image(s) grandfathered (> {BUDGET//1024} Ko).")
        return 0

    allow = load_allowlist()
    errors, warns = [], []

    for path, size in sorted(over.items()):
        kb = size / 1024
        if path not in allow:
            errors.append(f"{path} : {kb:.0f} Ko > {BUDGET//1024} Ko (nouvelle image trop lourde)")
        elif size > allow[path]:
            errors.append(f"{path} : {kb:.0f} Ko > référence {allow[path]/1024:.0f} Ko "
                          "(une image grandfathered ne doit que rétrécir)")

    for path, ref in allow.items():
        cur = images.get(path)
        if cur is None:
            warns.append(f"{path} : dans l'allowlist mais introuvable -> retirer la ligne")
        elif cur <= BUDGET:
            warns.append(f"{path} : désormais {cur/1024:.0f} Ko ≤ budget -> retirer de l'allowlist (cliquet OK)")

    for w in warns:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERREUR  {e}")

    print(f"\ncheck_image_weight : budget {BUDGET//1024} Ko · {len(images)} images · "
          f"{len(over)} > budget ({len(allow)} grandfathered) · "
          f"{len(errors)} erreur(s) · {len(warns)} avertissement(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
