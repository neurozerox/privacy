"""Copy each app's PRIVACY_POLICY.md into <app>/index.md for GitHub Pages.

Usage: python tools/sync.py F:/ProyectosDCB/apps
"""
import pathlib
import sys

apps_dir = pathlib.Path(sys.argv[1])
root = pathlib.Path(__file__).resolve().parent.parent
rows = []
for app in sorted(p for p in apps_dir.iterdir() if p.is_dir()):
    src = app / "PRIVACY_POLICY.md"
    if not src.exists():
        continue
    text = src.read_text(encoding="utf-8")
    first = text.splitlines()[0].lstrip("# ").strip()
    name = first.split("—", 1)[-1].split(":", 1)[-1].strip() if ("—" in first or ":" in first) else app.name
    out = root / app.name / "index.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(f"---\ntitle: \"{name} — Privacy Policy / Política de privacidad\"\n---\n\n{text}", encoding="utf-8")
    rows.append((name, app.name))

lines = [
    "---", "title: neurozerox — Privacy policies", "---", "",
    "# neurozerox — Políticas de privacidad / Privacy policies", "",
    "Contacto / Contact: david.cheuquen@gmail.com", "",
]
lines += [f"- [{n}](./{d}/)" for n, d in sorted(rows, key=lambda r: r[0].lower())]
(root / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(len(rows), "policies")
