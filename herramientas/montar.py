"""Monta la copia: python3 -I montar.py <scratch> <repo>
<scratch> contiene arts.tsv (id<TAB>titulo), a/<id>/index.html, db/<id>/..., docs/<id>/..., files/<id>/...
Cada artifact queda en artifacts/<titulo>__<id>/ y se regenera README.md."""
import os, sys, re, shutil, unicodedata, datetime
S, R = sys.argv[1], sys.argv[2]
def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-")[:70] or "sin-titulo"
rows = [l.rstrip("\n").split("\t", 1) for l in open(os.path.join(S, "arts.tsv"), encoding="utf-8") if "\t" in l]
base = os.path.join(R, "artifacts")
if os.path.isdir(base): shutil.rmtree(base)
os.makedirs(base)
idx = []
for aid, title in rows:
    d = os.path.join(base, f"{slug(title)}__{aid}")
    os.makedirs(d)
    parts = []
    src = os.path.join(S, "a", aid, "index.html")
    if os.path.exists(src): shutil.copy2(src, os.path.join(d, "index.html")); parts.append("página")
    for sub, dest, label in (("db", "datos", "datos"), ("docs", "documento", "documento"), ("files", "archivos", "archivos")):
        p = os.path.join(S, sub, aid)
        if os.path.isdir(p) and any(os.scandir(p)):
            shutil.copytree(p, os.path.join(d, dest)); parts.append(label)
    idx.append((title, aid, os.path.basename(d), ", ".join(parts)))
hoy = datetime.date.today().isoformat()
with open(os.path.join(R, "README.md"), "w", encoding="utf-8") as f:
    f.write(f"# Copia de seguridad de Claude\n\nÚltima copia: {hoy}. {len(idx)} artifacts.\n\n")
    f.write("Cada carpeta de `artifacts/` tiene la página (`index.html`), y según el caso los datos guardados (`datos/`, JSON por documento), el documento exportado (`documento/`, Markdown o PDF) y archivos publicados (`archivos/`).\n\n")
    f.write("Las conversaciones no se copian aquí: se exportan a mano en claude.ai → Ajustes → Privacidad → Exportar datos.\n\n")
    f.write("| Artifact | Contenido | Enlace |\n|---|---|---|\n")
    for title, aid, folder, parts in sorted(idx, key=lambda x: x[0].lower()):
        f.write(f"| [{title.replace('|','/')}](artifacts/{folder}/) | {parts} | [abrir](https://claude.ai/artifact/{aid}) |\n")
print(len(idx), "artifacts")
