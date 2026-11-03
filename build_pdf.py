# -*- coding: utf-8 -*-
from PIL import Image
def crop(src, dst, ratio):
    im = Image.open(src); w, h = im.size
    th = w * ratio
    if h > th:
        t = int((h - th) // 2); im = im.crop((0, t, w, t + int(th)))
    else:
        tw = int(h / ratio); l = (w - tw) // 2; im = im.crop((l, 0, l + tw, h))
    im.convert('RGB').save(dst, quality=86)
for i in range(1, 5):
    crop('assets/img_prod_0%d.jpg' % i, 'assets/_cp%d.jpg' % i, 1.15)
crop('assets/img_hero.jpg', 'assets/_chm.jpg', 0.66)
from build_pdf_part1 import build
from build_pdf_part2 import continue_build
OUT = 'Alma-Cigana-Pacote-Planejamento-Prototipacao.pdf'
d = build('/tmp/_pass1.pdf', {})
continue_build(d)
toc = {n: p for n, p in d.rec}
print('toc pass1:', toc)
d2 = build(OUT, toc)
continue_build(d2)
print('OK', OUT, 'pages:', d2.page)
