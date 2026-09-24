"""Gera os arquivos finais do gerador de cardápios a partir de src/cardapio.html.

- index.html   -> versão para abrir direto no navegador (duplo clique)
- artifact.html -> mesma página, sem o cabeçalho HTML (para publicar como Artifact)
Os logos são embutidos como data URI, então cada arquivo funciona sozinho.
"""
import base64, io, pathlib
from PIL import Image

AQUI = pathlib.Path(__file__).parent

def data_uri(nome):
    buf = io.BytesIO()
    Image.open(AQUI / nome).save(buf, "WEBP", quality=90, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()

src = (AQUI / "src" / "cardapio.html").read_text(encoding="utf-8")
src = src.replace("__LOGO__", data_uri("logo.png")).replace("__TALHERES__", data_uri("talheres.png"))

(AQUI / "artifact.html").write_text(src, encoding="utf-8")
cabeca = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
          '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n')
titulo_fim = src.index("</style>") + len("</style>")
(AQUI / "index.html").write_text(cabeca + src[:titulo_fim] + "\n</head>\n<body>\n" + src[titulo_fim:] + "\n</body>\n</html>\n", encoding="utf-8")
print("ok")
