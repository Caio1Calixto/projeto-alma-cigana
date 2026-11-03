# -*- coding: utf-8 -*-
"""Alma Cigana — consolidação do pacote de planejamento em um único PDF diagramado."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

for nm, f in [('CG5','CG-500.ttf'), ('CG6','CG-600.ttf'), ('CG7','CG-700.ttf'),
              ('CG5i','CG-500i.ttf'), ('IN4','IN-400.ttf'), ('IN5','IN-500.ttf'), ('IN6','IN-600.ttf')]:
    pdfmetrics.registerFont(TTFont(nm, os.path.join('fonts', f)))

W, H = A4
ML, MR, MT, MB = 52, 52, 66, 54
CW = W - ML - MR

MARS   = HexColor('#7A1220')
DEEP   = HexColor('#4A0710')
GOLD   = HexColor('#C6A15B')
GOLDL  = HexColor('#EBD9A9')
CREAM  = HexColor('#FAF6EE')
WHITE  = HexColor('#FFFFFF')
INK    = HexColor('#2B1A1D')
SOFT   = HexColor('#6E565B')
PAPER  = HexColor('#FFFDF8')
LINEG  = HexColor('#E4D6BA')
GRAY   = HexColor('#9A9A9A')
GRAY2  = HexColor('#B5B5B5')
FILL   = HexColor('#F2F2F2')
FILL2  = HexColor('#E4E4E4')

IMG = dict(logo='assets/logo-alma-cigana.jpg', foto='assets/foto-referencia-cliente.jpg',
           hero='assets/img_hero.jpg', p1='assets/img_prod_01.jpg', p2='assets/img_prod_02.jpg',
           p3='assets/img_prod_03.jpg', p4='assets/img_prod_04.jpg',
           c1='assets/img_cat_01.jpg', c2='assets/img_cat_02.jpg',
           cp1='assets/_cp1.jpg', cp2='assets/_cp2.jpg', cp3='assets/_cp3.jpg', cp4='assets/_cp4.jpg', chm='assets/_chm.jpg')

def sw(t, f, s): return pdfmetrics.stringWidth(t, f, s)

class Doc:
    def __init__(self, path, toc=None):
        self.c = canvas.Canvas(path, pagesize=A4)
        self.c.setTitle('Alma Cigana — Pacote de Planejamento e Prototipação (Ciclo 0)')
        self.c.setAuthor('Agente 01 — Planejamento e Prototipação')
        self.page = 0; self.y = 0; self.section = ''; self.toc = toc or {}; self.rec = []
    # ---------- pages ----------
    def new_page(self, bg=None, running=True):
        if self.page: self.c.showPage()
        self.page += 1
        if bg:
            self.c.setFillColor(bg); self.c.rect(0, 0, W, H, stroke=0, fill=1)
        if running and self.page > 1 and not bg:
            c = self.c
            c.setFont('IN6', 7.2); c.setFillColor(MARS); c.drawString(ML, H-40, 'ALMA CIGANA')
            c.setFont('IN4', 7.2); c.setFillColor(SOFT)
            c.drawString(ML + sw('ALMA CIGANA', 'IN6', 7.2) + 6, H-40, '· PACOTE DE PLANEJAMENTO E PROTOTIPAÇÃO · CICLO 0')
            if self.section:
                c.drawRightString(W-MR, H-40, self.section.upper())
            c.setStrokeColor(GOLD); c.setLineWidth(.7); c.line(ML, H-48, W-MR, H-48)
            c.setStrokeColor(LINEG); c.setLineWidth(.6); c.line(ML, 44, W-MR, 44)
            c.setFont('IN4', 7); c.setFillColor(SOFT)
            c.drawString(ML, 34, 'Ciclo 0 — planejamento e prototipação · este documento não é o site finalizado')
            c.setFont('IN5', 7); c.drawRightString(W-MR, 34, 'p. %d' % self.page)
        self.y = H - MT
    def ensure(self, h):
        if self.y - h < MB: self.new_page()
    # ---------- primitives ----------
    def hair(self, x1, y1, x2, y2, col=GOLD, w=.6, dash=None):
        c = self.c; c.setStrokeColor(col); c.setLineWidth(w)
        c.setDash(dash or [], 0); c.line(x1, y1, x2, y2); c.setDash([], 0)
    def rrect(self, x, y, w, h, r, fill=None, stroke=None, lw=.8, dash=None):
        c = self.c
        if fill: c.setFillColor(fill)
        if stroke: c.setStrokeColor(stroke)
        c.setLineWidth(lw); c.setDash(dash or [], 0)
        c.roundRect(x, y, w, h, r, stroke=1 if stroke else 0, fill=1 if fill else 0)
        c.setDash([], 0)
    def circle(self, x, y, r, fill=None, stroke=None, lw=.8):
        c = self.c
        if fill: c.setFillColor(fill)
        if stroke: c.setStrokeColor(stroke)
        c.setLineWidth(lw); c.circle(x, y, r, stroke=1 if stroke else 0, fill=1 if fill else 0)
    def star(self, x, y, r, col=GOLD):
        c = self.c; c.setFillColor(col); p = c.beginPath()
        k = r * .22
        p.moveTo(x, y+r); p.lineTo(x+k, y+k); p.lineTo(x+r, y); p.lineTo(x+k, y-k)
        p.lineTo(x, y-r); p.lineTo(x-k, y-k); p.lineTo(x-r, y); p.lineTo(x-k, y+k)
        p.close(); c.drawPath(p, stroke=0, fill=1)
    def tag(self, n, x, y, col=INK, txt=WHITE):
        self.circle(x, y, 8, fill=col)
        self.c.setFont('IN6', 8); self.c.setFillColor(txt)
        self.c.drawCentredString(x, y-2.8, str(n))
    # ---------- text ----------
    def wrap(self, t, f, s, maxw):
        out, cur = [], ''
        for w in t.split(' '):
            trial = (cur + ' ' + w).strip()
            if sw(trial, f, s) <= maxw or not cur: cur = trial
            else: out.append(cur); cur = w
        if cur: out.append(cur)
        return out
    def para(self, t, f='IN4', s=9.3, col=INK, lead=None, maxw=CW, x=ML, sa=6, align='l', it=None):
        lead = lead or s * 1.5
        lines = self.wrap(t, f, s, maxw)
        self.ensure(len(lines) * lead + sa)
        for ln in lines:
            self.y -= lead
            self.c.setFont(f, s); self.c.setFillColor(col)
            if align == 'c': self.c.drawCentredString(x + maxw/2, self.y, ln)
            elif align == 'r': self.c.drawRightString(x + maxw, self.y, ln)
            else: self.c.drawString(x, self.y, ln)
        self.y -= sa
        return lines
    def runs(self, parts, s=9.3, lead=None, maxw=CW, x=ML, sa=6):
        """parts = [(texto, fonte, cor)] — parágrafo com estilos mistos."""
        lead = lead or s * 1.5
        toks = []
        for t, f, col in parts:
            for i, w in enumerate(t.split(' ')):
                if w: toks.append((w, f, col))
        lines, cur, curw = [], [], 0
        for w, f, col in toks:
            ww = sw(w + ' ', f, s)
            if curw + ww > maxw and cur:
                lines.append(cur); cur, curw = [], 0
            cur.append((w, f, col)); curw += ww
        if cur: lines.append(cur)
        self.ensure(len(lines) * lead + sa)
        for ln in lines:
            self.y -= lead; xx = x
            for w, f, col in ln:
                self.c.setFont(f, s); self.c.setFillColor(col)
                self.c.drawString(xx, self.y, w); xx += sw(w + ' ', f, s)
        self.y -= sa
    def h2(self, t, num=None):
        self.ensure(46); self.y -= 14
        if num:
            self.c.setFont('CG6', 15); self.c.setFillColor(GOLD); self.c.drawString(ML, self.y, num)
            self.c.drawString(ML + sw(num, 'CG6', 15) + 8, self.y, '')
            x = ML + sw(num, 'CG6', 15) + 8
        else:
            x = ML
        self.c.setFont('CG6', 15); self.c.setFillColor(DEEP); self.c.drawString(x, self.y, t)
        self.y -= 6
        self.hair(ML, self.y, ML + 46, self.y, GOLD, 1)
        self.y -= 12
    def h3(self, t):
        self.ensure(30); self.y -= 8
        self.c.setFont('IN6', 8.4); self.c.setFillColor(MARS); self.c.drawString(ML, self.y, t.upper())
        self.y -= 10
    def bullets(self, items, s=9.0, maxw=CW-14, col=INK, marker='•'):
        for it in items:
            lead = s * 1.45
            lines = self.wrap(it, 'IN4', s, maxw)
            self.ensure(len(lines) * lead + 3)
            for i, ln in enumerate(lines):
                self.y -= lead
                self.c.setFont('IN4', s); self.c.setFillColor(col)
                if i == 0:
                    self.c.setFillColor(GOLD); self.c.setFont('IN6', s)
                    self.c.drawString(ML + 2, self.y, marker)
                    self.c.setFillColor(col); self.c.setFont('IN4', s)
                self.c.drawString(ML + 14, self.y, ln)
            self.y -= 3
    def box(self, title, text, bg=CREAM, bd=GOLD, tcol=MARS, s=8.6):
        lead = s * 1.45
        lt = self.wrap(text, 'IN4', s, CW - 36)
        h = 16 + (12 if title else 0) + len(lt) * lead + 10
        self.ensure(h + 6); self.y -= 4
        y0 = self.y - h
        self.rrect(ML, y0, CW, h, 3, fill=bg, stroke=bd, lw=.9)
        self.hair(ML + 10, y0 + h - (16 if title else 8), ML + 10, y0 + 8, bd, 2)
        yy = self.y - 13
        if title:
            self.c.setFont('IN6', s); self.c.setFillColor(tcol); self.c.drawString(ML + 18, yy, title)
            yy -= 12
        self.c.setFont('IN4', s); self.c.setFillColor(INK)
        for ln in lt:
            self.c.drawString(ML + 18, yy, ln); yy -= lead
        self.y = y0 - 10
    # ---------- chips / dots ----------
    def chip(self, x, y, text, kind):
        styles = {'ok': (MARS, GOLDL), 'pend': (WHITE, MARS), 'par': (GOLD, DEEP), 'tec': (DEEP, GOLDL)}
        bg, fg = styles[kind]
        w = sw(text, 'IN6', 6.6) + 10
        self.rrect(x, y - 2.5, w, 11, 2, fill=bg, stroke=(MARS if kind == 'pend' else None), lw=.7)
        self.c.setFont('IN6', 6.6); self.c.setFillColor(fg); self.c.drawString(x + 5, y, text)
        return w
    def dotp(self, x, y, kind):
        col = {'r': MARS, 'y': GOLD, 'g': GRAY2}[kind]
        self.circle(x + 3, y + 2.4, 3, fill=col)
    # ---------- tables ----------
    def table(self, colw, header, rows, hs=7.0, bs=8.0, pad=6, zebra=True, aligns=None):
        c = self.c
        lead = bs * 1.38
        def cell_lines(cell):
            if isinstance(cell, dict):
                t = cell.get('t', '')
            else:
                t = cell
            f = 'IN4'
            if isinstance(cell, dict) and cell.get('b'): f = 'IN5'
            return self.wrap(t, f, bs, colw[i] - 2 * pad) if t else ['']
        # header
        def draw_header():
            hh = 16
            self.ensure(hh + 20)
            self.y -= hh
            c.setFillColor(DEEP); c.rect(ML, self.y, sum(colw), hh, stroke=0, fill=1)
            xx = ML
            for i, htxt in enumerate(header):
                c.setFont('IN6', hs); c.setFillColor(GOLDL)
                c.drawString(xx + pad, self.y + 5, htxt.upper())
                xx += colw[i]
        draw_header()
        for r_i, row in enumerate(rows):
            wraps = []
            for i, cell in enumerate(row):
                t = cell.get('t', '') if isinstance(cell, dict) else cell
                f = 'IN5' if (isinstance(cell, dict) and cell.get('b')) else 'IN4'
                wraps.append(self.wrap(t, f, bs, colw[i] - 2 * pad) if t else [''])
            n = max(len(w) for w in wraps)
            rh = n * lead + 2 * pad - 2
            if self.y - rh < MB:
                self.new_page(); draw_header()
            self.y -= rh
            y0 = self.y
            if zebra and r_i % 2 == 0:
                c.setFillColor(CREAM); c.rect(ML, y0, sum(colw), rh, stroke=0, fill=1)
            c.setStrokeColor(LINEG); c.setLineWidth(.5)
            c.line(ML, y0, ML + sum(colw), y0)
            xx = ML
            for i, cell in enumerate(row):
                ty = y0 + rh - pad - bs * .95
                if isinstance(cell, dict) and cell.get('chip'):
                    self.chip(xx + pad, ty + 1, cell['t'], cell['chip'])
                elif isinstance(cell, dict) and cell.get('dot'):
                    self.dotp(xx + pad, ty, cell['dot'])
                    c.setFont('IN4', bs); c.setFillColor(INK)
                    for ln in wraps[i]:
                        c.drawString(xx + pad + 11, ty, ln); ty -= lead
                else:
                    f = 'IN5' if (isinstance(cell, dict) and cell.get('b')) else 'IN4'
                    col = INK
                    if isinstance(cell, dict) and cell.get('col'): col = cell['col']
                    c.setFont(f, bs); c.setFillColor(col)
                    for ln in wraps[i]:
                        c.drawString(xx + pad, ty, ln); ty -= lead
                xx += colw[i]
            xx = ML
            c.setStrokeColor(LINEG); c.setLineWidth(.4)
            for i in range(len(colw) - 1):
                xx += colw[i]; c.line(xx, y0 + 2, xx, y0 + rh - 2)
        c.setStrokeColor(GOLD); c.setLineWidth(.8)
        c.line(ML, self.y, ML + sum(colw), self.y)
        self.y -= 12

def opener(d, num, title, kick, lead=None):
    d.section = title
    d.new_page()
    d.rec.append((num, d.page))
    d.y -= 26
    d.c.setFont('IN6', 8); d.c.setFillColor(GOLD); d.c.drawString(ML, d.y, kick.upper())
    d.y -= 44
    d.c.setFont('CG6', 40); d.c.setFillColor(GOLD); d.c.drawString(ML, d.y, num)
    d.c.setFont('CG6', 27); d.c.setFillColor(DEEP)
    d.c.drawString(ML + sw(num, 'CG6', 40) + 16, d.y + 4, title)
    d.y -= 12
    d.hair(ML, d.y, ML + 70, d.y, GOLD, 1.2)
    d.star(ML + 82, d.y, 4)
    d.y -= 20
    if lead:
        d.para(lead, 'IN4', 9.6, SOFT, maxw=CW, sa=10)

# =====================================================================
def build(path, toc):
    d = Doc(path, toc)
    c = d.c
    # ---------------- CAPA ----------------
    d.new_page(bg=DEEP, running=False)
    c.setStrokeColor(GOLD); c.setLineWidth(1.1); c.rect(24, 24, W-48, H-48, stroke=1, fill=0)
    c.setStrokeColor(GOLDL); c.setLineWidth(.4); c.rect(30, 30, W-60, H-60, stroke=1, fill=0)
    c.setFont('IN6', 9); c.setFillColor(GOLDL)
    c.drawCentredString(W/2, H-92, 'A L M A   C I G A N A')
    d.star(W/2, H-112, 5, GOLD)
    # logo
    lw, lh = 300, 214
    c.drawImage(IMG['logo'], (W-lw)/2, H-352, lw, lh, mask=None)
    c.setStrokeColor(GOLD); c.setLineWidth(.9); c.rect((W-lw)/2, H-352, lw, lh, stroke=1, fill=0)
    y = H-392
    c.setStrokeColor(GOLD); c.setLineWidth(.6); c.line(W/2-110, y, W/2-14, y); c.line(W/2+14, y, W/2+110, y)
    d.star(W/2, y, 4.5, GOLD)
    y -= 40
    c.setFont('CG6', 33); c.setFillColor(GOLDL)
    c.drawCentredString(W/2, y, 'Pacote de Planejamento'); y -= 38
    c.drawCentredString(W/2, y, 'e Prototipação'); y -= 26
    c.setFont('CG5i', 14); c.setFillColor(GOLD)
    c.drawCentredString(W/2, y, 'site de joias e acessórios · catálogo digital · pedidos pelo WhatsApp'); y -= 40
    c.setStrokeColor(GOLD); c.setLineWidth(.4); c.line(W/2-70, y, W/2+70, y); y -= 24
    c.setFont('IN4', 8.6); c.setFillColor(HexColor('#E6D3C3'))
    for ln in ['Ciclo 0 — planejamento e prototipação · versão 1.0 · 03 de novembro de 2026',
               'Consolidação dos entregáveis 1 a 5 · lista de materiais pendentes · termo de aprovação',
               'Documento de origem: Painel Mestre do Projeto, v2.0 (02/11/2026)']:
        c.drawCentredString(W/2, y, ln); y -= 14
    bw, bh = 372, 22
    c.setFillColor(MARS); c.rect((W-bw)/2, 58, bw, bh, stroke=0, fill=1)
    c.setStrokeColor(GOLD); c.setLineWidth(.6); c.rect((W-bw)/2, 58, bw, bh, stroke=1, fill=0)
    c.setFont('IN6', 7.6); c.setFillColor(GOLDL)
    c.drawCentredString(W/2, 66.5, 'ESTE DOCUMENTO É PLANEJAMENTO E PROTÓTIPO — NÃO É O SITE FINALIZADO')

    # ---------------- ÍNDICE ----------------
    d.new_page(); d.section = 'Índice do pacote'
    d.y -= 6
    c.setFont('CG6', 24); c.setFillColor(DEEP); c.drawString(ML, d.y, 'Índice do pacote')
    d.y -= 8; d.hair(ML, d.y, ML + 60, d.y, GOLD, 1.2); d.y -= 22
    entries = [
        ('01', 'Apresentação e síntese do pacote', 'como ler, conteúdo e próximos passos'),
        ('02', 'Entregável 1 — Levantamento e organização', 'informações disponíveis e ausentes'),
        ('03', 'Entregável 2 — Arquitetura do site', 'hierarquia, navegação e jornada'),
        ('04', 'Entregável 3 — Guia visual', 'paleta, tipografia, componentes, fotos, mobile'),
        ('05', 'Entregável 4 — Wireframe da página inicial', 'pranchas desktop e mobile anotadas'),
        ('06', 'Entregável 5 — Protótipo visual', 'pranchas em cor da página inicial'),
        ('07', 'Materiais pendentes do cliente', 'checklist priorizado de envio'),
        ('08', 'Aprovação e próximos passos', 'registro formal de aprovação do Ciclo 0'),
    ]
    for num, tit, sub in entries:
        pg = toc.get(num, '–')
        d.ensure(34)
        c.setFont('CG6', 16); c.setFillColor(GOLD); c.drawString(ML, d.y, num)
        c.setFont('CG6', 13.5); c.setFillColor(DEEP); c.drawString(ML + 30, d.y, tit)
        tw_ = sw(tit, 'CG6', 13.5)
        c.setFont('IN4', 8); c.setFillColor(SOFT); c.drawString(ML + 30, d.y - 11, sub)
        x0 = ML + 34 + tw_; x1 = W - MR - 24
        c.setStrokeColor(LINEG); c.setLineWidth(.6); c.setDash([1, 2.4], 0)
        c.line(x0, d.y + 2.5, x1, d.y + 2.5); c.setDash([], 0)
        c.setFont('IN6', 10); c.setFillColor(MARS); c.drawRightString(W - MR, d.y, str(pg))
        d.y -= 30
    d.y -= 6
    d.box('Como ler este pacote',
          'Os capítulos 05 e 06 são pranchas estáticas (wireframe e protótipo) reproduzidas neste PDF para aprovação. '
          'As versões interativas, em alta resolução e com simulação de celular, acompanham o pacote nos arquivos '
          '04-wireframe-home.html e 05-prototipo-home.html. Textos entre [colchetes] são espaços reservados para '
          'conteúdo do cliente; imagens de joias são referências provisórias. Nenhuma informação comercial foi inventada.')
    d.y -= 4
    d.h3('Arquivos que acompanham este PDF')
    d.bullets([
        'README.md — índice do pacote e resumo executivo;',
        '01 a 06 (.md / .html) — entregáveis completos e versões interativas;',
        'assets/ e ref/ — imagens de referência provisória, logotipo e foto extraídos do Painel Mestre;',
        'fonts/ — fontes do projeto (Cormorant Garamond e Inter), embutidas neste PDF.',
    ], s=8.6)
    d.y -= 2
    d.h3('Ciclos do projeto (Painel Mestre)')
    d.table([46, 108, CW - 154], ['Ciclo', 'Parcela', 'Entregas'], [
        [{'t': 'Ciclo 0', 'b': True}, 'R$ 100 · entrada recebida', 'Planejamento e prototipação: organização dos materiais, identidade, estrutura das páginas, wireframe e protótipo — este pacote'],
        [{'t': 'Ciclo 1', 'b': True}, 'R$ 325 · primeira parcela', 'Cabeçalho e navegação, página inicial, banner, apresentação da marca, estrutura do catálogo, categorias, primeiros produtos e responsividade inicial'],
        [{'t': 'Ciclo 2', 'b': True}, 'R$ 325 · segunda parcela', 'Produtos restantes, páginas individuais, botões de WhatsApp, redes sociais, rodapé, testes em celular e computador, publicação e entrega de acessos'],
    ])
    d.y -= 2
    d.h3('O projeto em números (Painel Mestre)')
    d.ensure(66); d.y -= 2
    y0 = d.y
    stats = [('R$ 750', 'valor total contratado'), ('R$ 100', 'entrada recebida'),
             ('R$ 650', 'saldo em duas parcelas'), ('7-12', 'dias úteis de produção ativa')]
    sw4 = (CW - 36) / 4
    for i, (v, l) in enumerate(stats):
        sx = ML + i * (sw4 + 12)
        d.rrect(sx, y0 - 40, sw4, 40, 3, fill=CREAM, stroke=GOLD, lw=.7)
        c.setFont('CG6', 15); c.setFillColor(MARS); c.drawCentredString(sx + sw4 / 2, y0 - 17, v)
        c.setFont('IN4', 6.6); c.setFillColor(SOFT); c.drawCentredString(sx + sw4 / 2, y0 - 29, l)
    d.y = y0 - 50
    c.setFont('IN4', 7); c.setFillColor(SOFT)
    c.drawString(ML, d.y, 'Valores e prazos registrados no Painel Mestre v2.0 — este pacote não altera condições comerciais.')
    d.y -= 10

    # ---------------- 01 APRESENTAÇÃO ----------------
    opener(d, '01', 'Apresentação e síntese do pacote', 'Ciclo 0 · leitura em 3 minutos',
           'Este documento consolida, em um único volume, todo o pacote de planejamento e prototipação do site '
           'Alma Cigana: levantamento de informações, arquitetura, guia visual, wireframe e protótipo da página '
           'inicial, além da lista de materiais pendentes e do termo de aprovação da etapa.')
    d.h2('Direção proposta em cinco pontos')
    d.bullets([
        'Catálogo + WhatsApp, sem e-commerce — o site apresenta a marca e até 15 produtos; o pedido nasce como mensagem de WhatsApp com o nome do produto pré-preenchido. Negociação, pagamento e entrega acontecem direto com a loja;',
        'Marsala é a base, dourado é acabamento — #7A1220 e #4A0710 sustentam seções, títulos e botões; #C6A15B e #EBD9A9 entram em filetes e realces, nunca como fundo dominante. Branco e creme são apoio;',
        'Estética editorial e minimalista — espaçamento generoso, fotografia em destaque, serifada elegante nos títulos e fonte neutra nos textos;',
        'Mobile primeiro na prática — o celular é o canal principal de acesso do público: menu compacto, grades adaptadas e WhatsApp sempre à mão;',
        'Nada de informação inventada — produtos, preços, categorias, contatos e redes aparecem apenas como espaços reservados até o envio dos materiais.',
    ])
    d.h2('O que se espera do cliente agora')
    d.bullets([
        'Aprovar (ou ajustar) a direção estética e estrutural deste pacote — o registro da aprovação encerra o Ciclo 0 (capítulo 08);',
        'Enviar os materiais pendentes do capítulo 07: logotipo original, fotografias, produtos completos, categorias, WhatsApp comercial, redes sociais e texto institucional;',
        'Confirmar os itens administrativos em aberto no Painel Mestre: quantidade definitiva de produtos, domínio e hospedagem, responsible por textos e políticas, datas.',
    ])
    d.box('Regra do cronograma',
          'A contagem do prazo de produção ativa (7 a 12 dias úteis, conforme o Painel Mestre) começa quando os '
          'materiais chegarem completos. O que faltar é enviado depois e o cronograma é reajustado pela nova data '
          'de recebimento.')

    # ---------------- 02 LEVANTAMENTO ----------------
    opener(d, '02', 'Levantamento e organização', 'Entregável 1 · informações da marca',
           'Organização de tudo o que se sabe sobre a Alma Cigana e identificação clara do que ainda falta. '
           'Nenhuma informação comercial foi criada nesta etapa.')
    d.h3('Legenda de situação')
    d.ensure(20)
    x = ML
    for txt, kind in [('DEFINIDO', 'ok'), ('PENDENTE', 'pend'), ('PARCIAL', 'par'), ('DEFINIÇÃO TÉCNICA', 'tec')]:
        x += d.chip(x, d.y, txt, kind) + 10
    d.y -= 8
    d.para('DEFINIDO: informado pelo cliente ou registrado no Painel Mestre · PENDENTE: depende de envio do cliente · '
           'PARCIAL: existe em parte · DEFINIÇÃO TÉCNICA: decisão desta etapa, sujeita a aprovação.', 'IN4', 8.2, SOFT, sa=10)
    C = [118, 84, CW-202]
    d.h2('Informações institucionais', '1.1')
    d.table(C, ['Item', 'Situação', 'Conteúdo disponível'], [
        [{'t': 'Nome da marca', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, 'Alma Cigana'],
        [{'t': 'Ramo de atuação', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, 'Joias e acessórios'],
        [{'t': 'Modelo comercial', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, 'Site institucional + catálogo + pedidos pelo WhatsApp; sem carrinho, checkout ou pagamento'],
        [{'t': 'Limites da versão', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, 'Até 15 produtos; acima disso, negociação. Publicação após quitação'],
        [{'t': 'Posicionamento', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, 'Sofisticado, minimalista, editorial e comercial, com foco nas fotografias'],
        [{'t': 'Texto institucional', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'História e apresentação da marca serão fornecidas e aprovadas pelo cliente'],
        [{'t': 'CNPJ, endereço, horários', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Não informados; só entram no rodapé se fornecidos'],
        [{'t': 'Políticas da loja', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Trocas, devoluções, envio e cuidados — aprovação é do cliente'],
        [{'t': 'Slogan / assinatura', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Não informado; nenhum slogan foi criado nesta etapa'],
    ])
    d.box('Observação de análise',
          'O arquivo de logotipo presente no Painel Mestre traz o descritivo "CARTOMANCIA" sob o nome da marca, '
          'enquanto o escopo do site é joias e acessórios. É preciso confirmar qual versão do logotipo será usada '
          'no site (capítulo 07, item 2).')
    d.h2('Identidade visual', '1.2')
    d.table(C, ['Item', 'Situação', 'Conteúdo disponível'], [
        [{'t': 'Marsala (principal)', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, '#7A1220 — base de seções, botões, títulos e destaques'],
        [{'t': 'Marsala profundo', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, '#4A0710 — profundidade, fundos escuros, hover'],
        [{'t': 'Dourado', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, '#C6A15B — acabamento: filetes, ornamentos, realces; nunca fundo dominante'],
        [{'t': 'Dourado claro', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, '#EBD9A9 — apoio do dourado, textos sobre marsala'],
        [{'t': 'Branco e creme', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, 'Apenas como cores de apoio'],
        [{'t': 'Logotipo', 'b': True}, {'t': 'PARCIAL', 'chip': 'par'}, 'Lua, estrela e rosa em dourado sobre marsala. JPEG 2100×1500 extraído do painel; arquivo original pendente'],
        [{'t': 'Foto de referência', 'b': True}, {'t': 'PARCIAL', 'chip': 'par'}, 'Uma imagem no painel (joias douradas sobre tecido creme, luz quente) guia o clima fotográfico'],
        [{'t': 'Tipografia', 'b': True}, {'t': 'DEFINIÇÃO TÉCNICA', 'chip': 'tec'}, 'Cormorant Garamond (títulos) + Inter (textos) — proposta detalhada no capítulo 04'],
        [{'t': 'Referências visuais', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Cliente pode enviar referências de sites e estilos que admire'],
    ])
    d.h2('Categorias de produtos', '1.3')
    d.table(C, ['Item', 'Situação', 'Conteúdo disponível'], [
        [{'t': 'Lista de categorias', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'A definir pelo cliente (organização por tipo de acessório); nada foi inventado'],
        [{'t': 'Quantidade', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Sugestão técnica: 3 a 5 categorias iniciais para um catálogo de até 15 produtos'],
        [{'t': 'Nomes e ordem', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Cliente define nomes e prioridade de exibição'],
        [{'t': 'Navegação', 'b': True}, {'t': 'DEFINIÇÃO TÉCNICA', 'chip': 'tec'}, 'Página por categoria + filtro no catálogo (capítulo 03)'],
    ])
    d.h2('Dados necessários para cada produto', '1.4')
    d.table(C, ['Campo', 'Situação', 'Observação'], [
        [{'t': 'Nome do produto', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Fornecido pelo cliente'],
        [{'t': 'Fotografia(s)', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Arquivos originais, sem compressão de mensagem; boa iluminação'],
        [{'t': 'Preço', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Informação comercial de responsabilidade do cliente'],
        [{'t': 'Descrição', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Texto aprovado pelo cliente'],
        [{'t': 'Categoria', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Vínculo com a lista de categorias'],
        [{'t': 'Material e composição', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Quando aplicável — importante para joias'],
        [{'t': 'Dimensões e tamanhos', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Quando aplicável'],
        [{'t': 'Cores e variações', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Quando aplicável'],
        [{'t': 'Cuidados de conservação', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Quando aplicável'],
        [{'t': 'Estoque', 'b': True}, {'t': 'DEFINIÇÃO TÉCNICA', 'chip': 'tec'}, 'Sem controle automatizado nesta versão; disponibilidade combinada no atendimento'],
    ])
    d.h2('Contato e redes sociais', '1.5')
    d.table(C, ['Item', 'Situação', 'Conteúdo disponível'], [
        [{'t': 'WhatsApp comercial', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Canal central de pedidos; o painel traz apenas link de exemplo, a substituir'],
        [{'t': 'Mensagem de pedido', 'b': True}, {'t': 'DEFINIDO', 'chip': 'ok'}, 'Pré-preenchida com o nome do produto: "Olá! Tenho interesse em comprar o produto [nome]."'],
        [{'t': 'E-mail, endereço, horários', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Não informados'],
        [{'t': 'Canais sociais', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Cliente informará quais canais mantém'],
        [{'t': 'Links dos perfis', 'b': True}, {'t': 'PENDENTE', 'chip': 'pend'}, 'Nenhum handle foi presumido no protótipo'],
    ])
    d.h2('Requisitos técnicos', '1.6')
    d.h3('Confirmados no Painel Mestre')
    d.bullets([
        'Layout responsivo (celular e computador) · navegação entre páginas e categorias · botões de pedido via WhatsApp com mensagem pré-preenchida · links de redes sociais · catálogo organizado com até 15 produtos · páginas de inicial, sobre, catálogo, categorias, produto e contato · rodapé institucional · HTTPS e carregamento razoável na publicação.',
    ], s=8.8)
    d.h3('Fora do escopo desta versão')
    d.bullets([
        'Carrinho de compras · checkout no site · pagamento integrado · cálculo de frete · controle automatizado de estoque · painel administrativo personalizado · aplicativo próprio · cadastro ilimitado de produtos · integrações personalizadas · manutenção contínua.',
    ], s=8.8)
    d.h3('Definições técnicas desta etapa (sujeitas a aprovação)')
    d.table([130, CW-130], ['Item', 'Proposta'], [
        [{'t': 'URLs', 'b': True}, 'Curtas e legíveis: / · /sobre · /catalogo · /categoria/[slug] · /produto/[slug] · /contato'],
        [{'t': 'Links de pedido', 'b': True}, 'https://wa.me/[número]?text=[mensagem com o nome do produto]'],
        [{'t': 'Fontes web', 'b': True}, 'Cormorant Garamond e Inter, abertas para uso comercial, com fallbacks seguros'],
        [{'t': 'Acessibilidade', 'b': True}, 'Contraste suficiente, alvos de toque de 44 px ou mais, texto alternativo nas fotos'],
        [{'t': 'Domínio e hospedagem', 'b': True}, 'Responsável ainda não definido no Painel Mestre — confirmar (capítulo 07)'],
    ])
    d.h2('Síntese', '1.7')
    d.runs([('Existe hoje: ', 'IN6', MARS), ('nome e ramo da marca, modelo comercial catálogo + WhatsApp, limites de escopo, '
            'identidade cromática completa, composição do logotipo, estrutura de páginas e funcionalidades, fluxo comercial '
            'do visitante, critérios de qualidade, uma fotografia de referência e uma versão JPEG do logotipo.', 'IN4', INK)], s=9.0, sa=8)
    d.runs([('Falta para desenvolver: ', 'IN6', MARS), ('texto institucional, logotipo em arquivo original, fotografias reais, '
            'produtos completos, categorias definidas, WhatsApp comercial, redes sociais, políticas e dados do rodapé, '
            'confirmações administrativas. O detalhamento operacional está no capítulo 07.', 'IN4', INK)], s=9.0, sa=8)
    return d
