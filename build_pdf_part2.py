# -*- coding: utf-8 -*-
"""Alma Cigana — PDF consolidado: capítulos 03 a 08 + pranchas."""
from reportlab.lib.colors import HexColor
from build_pdf_part1 import (Doc, opener, W, H, ML, MR, MT, MB, CW, MARS, DEEP, GOLD, GOLDL,
                             CREAM, WHITE, INK, SOFT, PAPER, LINEG, GRAY, GRAY2, FILL, FILL2,
                             IMG, sw)

def side_bullets(d, x, maxw, items, s=8.0, col=INK):
    for it in items:
        lead = s * 1.42
        lines = d.wrap(it, 'IN4', s, maxw)
        d.ensure(len(lines) * lead + 3)
        for i, ln in enumerate(lines):
            d.y -= lead
            if i == 0:
                d.c.setFont('IN6', s); d.c.setFillColor(GOLD); d.c.drawString(x, d.y, '•')
            d.c.setFont('IN4', s); d.c.setFillColor(col); d.c.drawString(x + 10, d.y, ln)
        d.y -= 3

# =====================================================================
def sec03(d):
    opener(d, '03', 'Arquitetura do site', 'Entregável 2 · estrutura e navegação',
           'Estrutura de navegação do site: hierarquia de páginas, sistema de navegação global e contextual, '
           'jornada do visitante e regras arquiteturais desta versão.')
    d.h2('Hierarquia das páginas', '3.1')
    nodes = [
        (0, 'PÁGINA INICIAL  (/)', True),
        (1, 'SOBRE A MARCA  (/sobre) — história e identidade comercial', False),
        (1, 'CATÁLOGO DE PRODUTOS  (/catalogo) — grade com até 15 produtos', False),
        (2, 'filtro por categoria · cada cartão conduz à página de produto', False),
        (1, 'CATEGORIAS  (/categoria/[slug]) — uma página por categoria definida pelo cliente', False),
        (2, 'grade filtrada dos produtos daquela categoria', False),
        (1, 'PÁGINA DE PRODUTO  (/produto/[slug])', False),
        (2, 'fotografias · nome · preço · descrição · botão "Pedir pelo WhatsApp"', False),
        (2, 'trilho de navegação: Início > Catálogo > Categoria > Produto', False),
        (2, 'produtos relacionados da mesma categoria', False),
        (1, 'CONTATO  (/contato) — WhatsApp, redes e informações institucionais', False),
        (1, 'RODAPÉ INSTITUCIONAL  (global, em todas as páginas)', False),
        (2, 'mapa do site · categorias · contato e redes · institucional · copyright', False),
    ]
    for lvl, t, strong in nodes:
        d.ensure(16); d.y -= 13
        x = ML + 4 + lvl * 16
        if lvl > 0:
            d.hair(x - 8, d.y + 2.6, x - 3, d.y + 2.6, GOLD, .7)
            d.c.setFillColor(GOLD); d.c.rect(x - 1.6, d.y + 1, 3.2, 3.2, stroke=0, fill=1)
        else:
            d.star(x, d.y + 2.6, 3.4, MARS)
        f = 'IN6' if strong else 'IN4'
        d.c.setFont(f, 8.6 if strong else 8.4)
        d.c.setFillColor(DEEP if strong else SOFT)
        d.c.drawString(x + 8, d.y, t)
    d.y -= 6
    d.para('Profundidade máxima: nenhum conteúdo fica a mais de três cliques da home '
           '(home > catálogo > categoria > produto). Categorias não possuem subcategorias nesta versão.',
           'IN4', 8.4, SOFT, sa=8)
    d.h2('Sistema de navegação', '3.2')
    d.table([104, CW - 104], ['Elemento', 'Comportamento'], [
        [{'t': 'Cabeçalho', 'b': True}, 'Global e fixo no topo: logotipo à esquerda (clique volta à home), menu ao centro-direita e CTA de WhatsApp à direita'],
        [{'t': 'Menu principal', 'b': True}, 'Início · Sobre · Catálogo · Contato; item ativo com sublinhado dourado'],
        [{'t': 'Item "Catálogo"', 'b': True}, 'Exibe as categorias como submenu; no mobile, categorias listadas dentro do menu expandido'],
        [{'t': 'Trilho (breadcrumb)', 'b': True}, 'Nas páginas de categoria e produto: Início > Catálogo > Categoria > Produto'],
        [{'t': 'CTAs de WhatsApp', 'b': True}, 'Em três profundidades: cabeçalho (global), cartão e página do produto (pedido específico), seções de chamada (atendimento geral)'],
        [{'t': 'Rodapé', 'b': True}, 'Repete o mapa do site em todas as páginas: nenhuma tela é um beco sem saída'],
    ])
    d.h2('Jornada do visitante', '3.3')
    d.ensure(252)
    steps = [
        ('Acessa o site e conhece a marca', 'Página inicial: banner, apresentação da marca e seção institucional.'),
        ('Explora o catálogo', 'Menu "Catálogo", vitrine de categorias da home ou grade completa com filtro.'),
        ('Seleciona um produto', 'Cartão de produto abre a página individual com fotos, preço e descrição.'),
        ('Entra em contato pelo WhatsApp', 'Botão do produto abre a conversa com mensagem pré-preenchida com o nome da peça.'),
        ('Finaliza a negociação', 'Fora do site: pagamento e entrega combinados diretamente com a loja.'),
    ]
    for i, (t, desc) in enumerate(steps):
        d.ensure(34)
        d.circle(ML + 8, d.y - 4, 8, fill=MARS)
        d.c.setFont('IN6', 8); d.c.setFillColor(GOLDL); d.c.drawCentredString(ML + 8, d.y - 6.8, str(i + 1))
        if i < len(steps) - 1:
            d.hair(ML + 8, d.y - 14, ML + 8, d.y - 26, GOLD, .8)
        d.c.setFont('IN6', 9.4); d.c.setFillColor(DEEP); d.c.drawString(ML + 24, d.y - 4, t)
        d.y -= 15
        for ln in d.wrap(desc, 'IN4', 8.4, CW - 26):
            d.c.setFont('IN4', 8.4); d.c.setFillColor(SOFT); d.c.drawString(ML + 24, d.y, ln); d.y -= 11
        d.y -= 6
    d.h3('Caminhos alternativos previstos')
    d.bullets([
        'Quem já conhece a marca: home > Sobre > Contato / WhatsApp;',
        'Quem chega por rede social: link direto para uma categoria ou produto > WhatsApp;',
        'Quem entra pelo catálogo: filtro por categoria > produto > WhatsApp.',
    ], s=8.6)
    d.box('Princípio de navegação',
          'Toda página tem um caminho de avanço (catálogo ou produto), um caminho de saída (WhatsApp) e um caminho '
          'de retorno (menu, trilho ou rodapé). Nenhuma tela depende de cadastro, senha ou etapa de pagamento.')
    d.h2('Inventário de páginas e blocos', '3.4')
    d.table([96, CW - 96], ['Página', 'Blocos de conteúdo, em ordem'], [
        [{'t': 'Inicial', 'b': True}, 'Cabeçalho · banner principal · apresentação da marca · categorias · produtos em destaque · seção institucional · chamada WhatsApp · redes sociais · rodapé'],
        [{'t': 'Sobre', 'b': True}, 'Banner de abertura · texto institucional · imagem de apoio · pilares · chamadas para catálogo e WhatsApp · rodapé'],
        [{'t': 'Catálogo', 'b': True}, 'Título e introdução · barra de filtro por categoria · grade de produtos (até 15) · chamada WhatsApp · rodapé'],
        [{'t': 'Categoria', 'b': True}, 'Título e descrição curta · grade filtrada · links para demais categorias · rodapé'],
        [{'t': 'Produto', 'b': True}, 'Trilho · galeria · nome · preço · descrição · características · botão WhatsApp · informações de atendimento · relacionados · rodapé'],
        [{'t': 'Contato', 'b': True}, 'Botão e número do WhatsApp · redes sociais · informações institucionais de contato · rodapé'],
        [{'t': 'Rodapé', 'b': True}, 'Navegação · categorias · contato e redes · institucional · linha final com copyright e créditos'],
    ])
    d.h2('Regras arquiteturais desta versão', '3.5')
    d.bullets([
        'Sem fluxos de compra no site: nenhum bloco sugere carrinho, checkout ou pagamento; todo CTA comercial aponta para o WhatsApp;',
        'Catálogo finito e curado: até 15 produtos; os destaques da home são um subconjunto escolhido pela loja;',
        'Uma taxonomia só: categorias únicas, sem subcategorias e sem tags públicas;',
        'Conteúdo comercial rastreável: nomes, preços e descrições exibidos são exatamente os aprovados pelo cliente; placeholders não vão para o ar;',
        'Estrutura evolutiva: checkout, estoque e painel administrativo poderão entrar em etapa futura, com orçamento próprio, sem refazer as páginas.',
    ], s=8.8)

# =====================================================================
def sec04(d):
    c = d.c
    opener(d, '04', 'Guia visual', 'Entregável 3 · identidade aplicada ao projeto',
           'Direção visual do site: paleta e regras de uso, tipografia, botões, cartões, cabeçalho, espaçamento, '
           'direção fotográfica e comportamento em dispositivos móveis. Princípio-guia: o marsala é a base, '
           'o dourado é o acabamento, o branco e o creme são o respiro.')
    d.h2('Paleta cromática', '4.1')
    pal = [
        ('Marsala', '#7A1220', MARS, 'Cor principal: seções, botões, títulos e destaques', False),
        ('Marsala profundo', '#4A0710', DEEP, 'Profundidade: fundos escuros, rodapé, estado hover', False),
        ('Dourado', '#C6A15B', GOLD, 'Acabamento: filetes de 1-2 px, bordas, ornamentos, ícones, realces', False),
        ('Dourado claro', '#EBD9A9', GOLDL, 'Apoio do dourado: texto dourado sobre marsala, divisórias claras', False),
        ('Creme', '#FAF6EE', CREAM, 'Apoio: fundo geral das páginas, alternância de seções claras', True),
        ('Branco', '#FFFFFF', WHITE, 'Apoio: cartões de produto, textos sobre marsala', True),
        ('Texto escuro', '#2B1A1D', INK, 'Apoio neutro derivado do marsala: parágrafos sobre fundo claro', False),
    ]
    for name, hx, col, role, bord in pal:
        d.ensure(34); d.y -= 6
        c.setFillColor(col); c.rect(ML, d.y - 20, 46, 20, stroke=0, fill=1)
        if bord: c.setStrokeColor(LINEG); c.setLineWidth(.6); c.rect(ML, d.y - 20, 46, 20, stroke=1, fill=0)
        c.setStrokeColor(GOLD); c.setLineWidth(.5); c.rect(ML, d.y - 20, 46, 20, stroke=1, fill=0)
        c.setFont('IN6', 9); c.setFillColor(DEEP); c.drawString(ML + 56, d.y - 6, name)
        c.setFont('IN5', 8); c.setFillColor(SOFT); c.drawString(ML + 56 + sw(name, 'IN6', 9) + 8, d.y - 6, hx)
        c.setFont('IN4', 8); c.setFillColor(SOFT); c.drawString(ML + 56, d.y - 17, role)
        d.y -= 26
    d.h3('Regras de uso')
    d.bullets([
        'Marsala como base: é a cor que assina a marca, presente em seções, botões, títulos e destaques;',
        'Dourado nunca como fundo dominante: proporção prática de 60% marsala e profundos nas áreas de marca, 30% creme e branco nas áreas de conteúdo, 10% dourado em detalhes;',
        'Branco e creme apenas como apoio: fundos de leitura e cartões;',
        'Contraste obrigatório: texto claro sobre marsala e profundos; texto escuro sobre creme e branco; dourado como texto somente sobre fundos escuros;',
        'Nenhuma cor fora da paleta: ícones de redes e o símbolo do WhatsApp recebem tratamento monocromático para não descaracterizar a identidade.',
    ], s=8.6)
    d.h3('Usos proibidos')
    d.bullets([
        'Dourado como fundo dominante ou como fundo de seções;',
        'Texto em dourado claro sobre creme ou branco (contraste insuficiente);',
        'Cores fora da paleta — incluindo o verde do WhatsApp como fundo de botões ou ícones;',
        'Cantos muito arredondados ou sombras marcadas fora dos padrões deste guia.',
    ], s=8.6)
    d.ensure(158)
    d.h2('Tipografia', '4.2')
    d.ensure(70); d.y -= 8
    c.setFont('CG6', 25); c.setFillColor(DEEP); c.drawString(ML, d.y, 'Joias e acessórios com alma')
    c.setFont('IN4', 7.4); c.setFillColor(SOFT)
    c.drawString(ML, d.y - 13, 'Cormorant Garamond SemiBold — títulos e display (serifada editorial, ecoa o lettering do logotipo)')
    d.y -= 34
    c.setFont('IN4', 11); c.setFillColor(INK)
    c.drawString(ML, d.y, 'Catálogo organizado, atendimento pessoal e identidade em cada página.')
    c.setFont('IN4', 7.4); c.setFillColor(SOFT)
    c.drawString(ML, d.y - 13, 'Inter Regular — textos, menus e interface (sans-serif neutra e legível, também usada no Painel Mestre)')
    d.y -= 26
    d.ensure(196)
    d.table([118, 56, 56, CW - 230], ['Elemento', 'Desktop', 'Mobile', 'Estilo'], [
        ['Display do banner', '56-64 px', '34-40 px', 'Cormorant SemiBold, entrelinha 1.1'],
        ['Título de seção', '36-40 px', '26-30 px', 'Cormorant SemiBold'],
        ['Olho-de-página', '12-13 px', '11-12 px', 'Inter Medium, caixa alta, espaçamento +0.18em'],
        ['Texto corrido', '16-17 px', '15-16 px', 'Inter Regular, entrelinha 1.6'],
        ['Preços', '18-20 px', '16-18 px', 'Inter SemiBold, cor marsala'],
        ['Legendas', '12-13 px', '12 px', 'Inter Regular, neutro escuro'],
    ])
    d.h2('Botões', '4.3')
    d.ensure(64); d.y -= 10
    y0 = d.y
    d.rrect(ML, y0 - 26, 118, 26, 3, fill=MARS, stroke=GOLD, lw=.9)
    c.setFont('IN6', 7.6); c.setFillColor(GOLDL); c.drawCentredString(ML + 59, y0 - 16, 'VER CATÁLOGO')
    c.setFont('IN4', 6.8); c.setFillColor(SOFT); c.drawCentredString(ML + 59, y0 - 36, 'primário: marsala + filete dourado')
    d.rrect(ML + 140, y0 - 26, 132, 26, 3, fill=None, stroke=MARS, lw=.9)
    c.setFont('IN6', 7.6); c.setFillColor(MARS); c.drawCentredString(ML + 206, y0 - 16, 'CONHECER A MARCA')
    c.setFont('IN4', 6.8); c.setFillColor(SOFT); c.drawCentredString(ML + 206, y0 - 36, 'secundário: contorno marsala')
    d.rrect(ML + 294, y0 - 26, 150, 26, 3, fill=MARS, stroke=GOLD, lw=.9)
    d.circle(ML + 310, y0 - 13, 5.5, fill=None, stroke=GOLDL, lw=.8)
    c.setFont('IN6', 7.6); c.setFillColor(GOLDL); c.drawString(ML + 322, y0 - 16, 'PEDIR PELO WHATSAPP')
    c.setFont('IN4', 6.8); c.setFillColor(SOFT); c.drawCentredString(ML + 369, y0 - 36, 'whatsapp: mesma gramática do primário')
    d.y = y0 - 48
    c.setFont('IN6', 8); c.setFillColor(MARS); c.drawString(ML, d.y, 'Pedir pelo WhatsApp')
    d.hair(ML, d.y - 2.5, ML + sw('Pedir pelo WhatsApp', 'IN6', 8), d.y - 2.5, GOLD, .9)
    c.setFont('IN4', 6.8); c.setFillColor(SOFT); c.drawString(ML + 110, d.y, 'link textual com sublinhado dourado')
    d.y -= 14
    d.bullets(['Raio de canto máximo de 4 px em botões e cartões (linguagem editorial); hover do primário em marsala profundo; altura mínima de toque de 44-48 px no mobile.'], s=8.4)
    d.h2('Cartão de produto', '4.4')
    d.ensure(150); d.y -= 4
    y0 = d.y
    cx = ML
    c.setFillColor(WHITE); c.rect(cx, y0 - 176, 118, 176, stroke=0, fill=1)
    c.setStrokeColor(LINEG); c.setLineWidth(.6); c.rect(cx, y0 - 176, 118, 176, stroke=1, fill=0)
    c.drawImage(IMG['p1'], cx, y0 - 147, 118, 147, mask=None)
    c.setStrokeColor(GOLD); c.setLineWidth(1); c.line(cx, y0 - 147, cx + 118, y0 - 147)
    c.setFont('CG6', 9.5); c.setFillColor(DEEP); c.drawString(cx + 8, y0 - 156, '[Nome do produto]')
    c.setFont('IN4', 6); c.setFillColor(SOFT); c.drawString(cx + 8, y0 - 164.5, '[CATEGORIA DEFINIDA PELO CLIENTE]')
    c.setFont('IN6', 8); c.setFillColor(MARS); c.drawString(cx + 8, y0 - 173, 'R$ [000,00]')
    d.y = y0 - 2
    side_bullets(d, ML + 140, CW - 150, [
        'Fundo branco sobre página creme, sombra quase imperceptível;',
        'Fotografia retrato 4:5 no topo, com zoom sutil de 4% no hover;',
        'Filete dourado de 1 px que surge sob a foto no hover — acabamento, não decoração fixa;',
        'Nome em Cormorant SemiBold, categoria em legenda caixa alta, preço em Inter SemiBold marsala;',
        'Ação "Pedir pelo WhatsApp" como link textual com glifo;',
        'Grade: 4 colunas no desktop, 2 no tablet e no mobile (1 em telas menores que 360 px);',
        'Sem selos de promoção ou urgência: linguagem comercial sóbria.',
    ], s=8.2)
    d.y = min(d.y, y0 - 186) - 8
    d.ensure(176)
    d.h2('Cabeçalho', '4.5')
    d.ensure(190); d.y -= 4
    y0 = d.y
    c.setFillColor(CREAM); c.rect(ML, y0 - 34, CW, 34, stroke=0, fill=1)
    c.setStrokeColor(LINEG); c.setLineWidth(.6); c.rect(ML, y0 - 34, CW, 34, stroke=1, fill=0)
    d.circle(ML + 20, y0 - 17, 7, fill=GOLD)
    d.circle(ML + 23.5, y0 - 17, 5.6, fill=CREAM)
    c.setFont('CG6', 10); c.setFillColor(DEEP); c.drawString(ML + 34, y0 - 20, 'ALMA CIGANA')
    nav = 'INÍCIO      SOBRE      CATÁLOGO      CONTATO'
    c.setFont('IN5', 7); c.setFillColor(DEEP); c.drawRightString(ML + CW - 96, y0 - 20, nav)
    d.hair(ML + CW - 96 - sw('CATÁLOGO', 'IN5', 7) - 22, y0 - 23, ML + CW - 96 - 22, y0 - 23, GOLD, 1)
    d.rrect(ML + CW - 84, y0 - 26, 72, 18, 2, fill=MARS, stroke=GOLD, lw=.7)
    c.setFont('IN6', 6.6); c.setFillColor(GOLDL); c.drawCentredString(ML + CW - 48, y0 - 20, 'WHATSAPP')
    d.y = y0 - 44
    d.bullets([
        'Barra única creme no topo da home; ao rolar e nas páginas internas, fundo marsala profundo com texto creme;',
        'Logotipo à esquerda (40-48 px no desktop, 32-36 px no mobile); menu ao centro-direita em caixa alta espaçada; CTA à direita;',
        'Mobile: logotipo + ícone de menu; painel expandido em marsala profundo com itens empilhados e CTA fixo no rodapé do painel;',
        'Altura: 72-80 px no desktop, 56-64 px no mobile.',
    ], s=8.4)
    d.ensure(220)
    d.h2('Padrão de espaçamento', '4.6')
    d.y -= 4
    vals = [8, 16, 24, 32, 48, 64, 96, 128]
    for i, v in enumerate(vals):
        col = GOLD if i % 2 == 0 else MARS
        c.setFillColor(col); c.rect(ML, d.y - 6, v * 1.12, 5, stroke=0, fill=1)
        c.setFont('IN5', 6.6); c.setFillColor(SOFT); c.drawString(ML + v * 1.12 + 6, d.y - 5, str(v))
        d.y -= 12
    d.y -= 4
    c.setFont('IN4', 7.2); c.setFillColor(SOFT); c.drawString(ML, d.y, 'Escala base de 8 px usada em todo o site')
    d.y -= 16
    d.table([168, CW - 168], ['Aplicação', 'Medida'], [
        ['Margem lateral do conteúdo', '24 px no mobile · 48-64 px no desktop · largura máxima 1200 px'],
        ['Respiração entre seções da home', '96-128 px no desktop · 64-80 px no mobile'],
        ['Espaço entre cartões', '24-32 px no desktop · 16 px no mobile'],
        ['Padding interno de cartões', '16-24 px'],
        ['Distância do título ao conteúdo', '24-32 px'],
        ['Altura do banner principal', '70-85% da tela no desktop · 60-70% no mobile'],
    ], bs=7.6, pad=4)
    d.box('Princípio editorial',
          'O espaço em branco (creme) é parte do design: seções densas demais descaracterizam a estética sofisticada '
          'e editorial da marca.')
    d.ensure(170)
    d.h2('Direção estética das fotografias', '4.7')
    d.ensure(120); d.y -= 4
    y0 = d.y
    c.drawImage(IMG['foto'], ML, y0 - 92, 138, 92, mask=None)
    c.setStrokeColor(GOLD); c.setLineWidth(.6); c.rect(ML, y0 - 92, 138, 92, stroke=1, fill=0)
    c.drawImage(IMG['c1'], ML + 150, y0 - 92, 74, 92, mask=None)
    c.setStrokeColor(GOLD); c.setLineWidth(.6); c.rect(ML + 150, y0 - 92, 74, 92, stroke=1, fill=0)
    c.setFont('IN4', 6.4); c.setFillColor(SOFT)
    c.drawString(ML, y0 - 102, 'Referência do cliente (Painel Mestre)')
    c.drawString(ML + 150, y0 - 102, 'Ref. provisória gerada')
    d.y = y0 - 2
    side_bullets(d, ML + 240, CW - 244, [
        'Luz natural ou simulada, quente e lateral, sombras suaves;',
        'Fundos creme e linho para catálogo; marsala ou seda escura para peças de clima;',
        'Composição minimalista, produto protagonista, espaço negativo generoso;',
        'Mesmo tratamento de cor e proporções: 4:5 para produtos, 16:9 ou 3:2 para banners;',
        'Arquivos originais sem compressão; otimização web no desenvolvimento; evitar fundos fora da paleta, flash estourado e texto queimado.',
    ], s=8.0)
    d.y = min(d.y, y0 - 114) - 8
    d.ensure(150)
    d.h2('Comportamento em dispositivos móveis', '4.8')
    d.bullets([
        'Mobile é o canal principal do público: toda decisão de layout é testada primeiro em 390 px de largura;',
        'Menu recolhido; categorias no painel do menu; CTA de WhatsApp sempre visível, com botão flutuante discreto opcional;',
        'Grades: produtos e categorias em 2 colunas, ou carrossel horizontal com snap; tipografia reduzida conforme a escala de 4.2;',
        'Alvos de toque de 44 px ou mais; carrosséis com arraste natural; imagens servidas no tamanho adequado à tela;',
        'Seções escuras mantêm o ritmo vertical com padding reduzido a dois terços do desktop.',
    ], s=8.6)
    d.h2('Aplicação da marca gráfica', '4.9')
    d.bullets([
        'O logotipo (lua, estrela e rosa em dourado sobre marsala profundo) é o ponto de partida de toda a aplicação;',
        'Sobre fundos claros, versão com elementos em marsala e dourado; sobre fundos escuros, versão dourada;',
        'Ornamentos derivados (filete com estrela de quatro pontas, arcos de lua) pontuam divisórias de seção, sempre em traço fino dourado;',
        'Enquanto o arquivo original não chega, o protótipo usa reprodução vetorial provisória do símbolo, identificada como tal.',
    ], s=8.6)
    d.h2('Proporção e provas de aplicação', '4.10')
    d.ensure(150)
    d.y -= 4
    y0 = d.y
    seg = [(0.60, MARS, '60% marsala e profundos — áreas de marca'),
           (0.30, CREAM, '30% creme e branco — áreas de leitura'),
           (0.10, GOLD, '10% dourado — detalhes')]
    xx = ML
    for frac, col, lab in seg:
        wdt = CW * frac
        c.setFillColor(col); c.rect(xx, y0 - 16, wdt, 16, stroke=0, fill=1)
        c.setStrokeColor(GOLD); c.setLineWidth(.4); c.rect(xx, y0 - 16, wdt, 16, stroke=1, fill=0)
        xx += wdt
    d.y = y0 - 26
    xx = ML
    for frac, col, lab in seg:
        wdt = CW * frac
        c.setFont('IN4', 7); c.setFillColor(SOFT); c.drawString(xx + 4, d.y, lab)
        xx += wdt
    d.y -= 16
    d.h3('Provas de aplicação da marca')
    d.ensure(76); d.y -= 2
    y0 = d.y
    locks = [(DEEP, GOLD, GOLDL), (MARS, GOLDL, GOLDL), (CREAM, MARS, DEEP)]
    lw3 = (CW - 24) / 3
    for i, (bg, mark, txt) in enumerate(locks):
        lx = ML + i * (lw3 + 12)
        c.setFillColor(bg); c.rect(lx, y0 - 44, lw3, 44, stroke=0, fill=1)
        c.setStrokeColor(GOLD); c.setLineWidth(.5); c.rect(lx, y0 - 44, lw3, 44, stroke=1, fill=0)
        d.circle(lx + 16, y0 - 22, 7, fill=mark)
        d.circle(lx + 19, y0 - 22, 5.6, fill=bg)
        d.star(lx + 24, y0 - 27, 2.2, mark)
        c.setFont('CG6', 9); c.setFillColor(txt); c.drawString(lx + 32, y0 - 25, 'ALMA CIGANA')
    d.y = y0 - 54
    c.setFont('IN4', 7.2); c.setFillColor(SOFT)
    c.drawString(ML, d.y, 'Dourado sobre fundos escuros, dourado claro sobre marsala e marsala sobre creme — conferência final com o arquivo definitivo do cliente.')
    d.y -= 12
    d.ensure(212)
    d.h2('Componentes e estados — referência rápida', '4.11')
    d.table([92, 168, CW - 260], ['Componente', 'Estado normal', 'Hover / ativo'], [
        [{'t': 'Botão primário', 'b': True}, 'Marsala com filete dourado e texto claro', 'Marsala profundo com filete dourado claro'],
        [{'t': 'Botão secundário', 'b': True}, 'Contorno marsala sobre fundo claro', 'Preenchido em marsala com texto claro'],
        [{'t': 'Botão WhatsApp', 'b': True}, 'Marsala (seções claras) ou marsala profundo (faixas escuras), com glifo', 'Marsala profundo com filete dourado claro'],
        [{'t': 'Cartão de produto', 'b': True}, 'Branco, sem borda visível, foto 4:5', 'Sombra suave, filete dourado sob a foto e zoom de 4%'],
        [{'t': 'Link textual', 'b': True}, 'Marsala ou dourado claro com sublinhado dourado', 'Sublinhado em dourado claro'],
        [{'t': 'Cabeçalho', 'b': True}, 'Creme translúcido na home', 'Marsala profundo com texto creme ao rolar e nas internas'],
        [{'t': 'Menu mobile', 'b': True}, 'Recolhido em ícone sobre creme', 'Painel marsala profundo com itens dourado claro'],
    ], bs=7.4, pad=4)
    d.ensure(290)
    d.h2('Checklist de aplicação do guia', '4.12')
    d.table([86, CW - 86], ['Item', 'Verificação antes de fechar qualquer tela'], [
        [{'t': 'Cor', 'b': True}, 'Fundos e textos dentro da paleta, proporção 60/30/10 e contrastes obrigatórios de 4.1'],
        [{'t': 'Tipografia', 'b': True}, 'Tamanhos e pesos conforme a tabela de 4.2; serifada apenas em títulos e destaques'],
        [{'t': 'Componentes', 'b': True}, 'Botões, cartões, links e cabeçalho conforme os estados normais e ativos de 4.11'],
        [{'t': 'Espaçamento', 'b': True}, 'Escala de 8 px e respirações entre seções conforme a tabela de 4.6'],
        [{'t': 'Imagens', 'b': True}, 'Direção de 4.7 e proporções 4:5 para produtos, 16:9 ou 3:2 para banners'],
        [{'t': 'Mobile', 'b': True}, 'Prova em 390 px: menu, grades, alvos de toque e legibilidade sobre marsala (4.8)'],
        [{'t': 'Marca', 'b': True}, 'Logotipo definitivo aplicado assim que o arquivo chegar; até lá, reprodução provisória identificada (4.9)'],
    ], bs=7.6, pad=4)
    d.box('Vigência deste guia',
          'Este guia orienta todas as telas dos Ciclos 1 e 2. Qualquer mudança de cor, tipografia, componente ou '
          'espaçamento passa por aprovação escrita do cliente e por atualização deste volume.')
    d.h2('Glossário rápido de termos do projeto', '4.13')
    d.table([92, CW - 92], ['Termo', 'Significado neste projeto'], [
        [{'t': 'Filete dourado', 'b': True}, 'Linha fina dourada de contorno e destaque, usada em botões, molduras e divisórias'],
        [{'t': 'Tile de categoria', 'b': True}, 'Cartão de acesso às categorias, em marsala profundo com ícone e nome dourado'],
        [{'t': 'Cartão 4:5', 'b': True}, 'Proporção vertical das fotos de produto nas grades e nos destaques'],
        [{'t': 'Snap de carrossel', 'b': True}, 'Parada do arraste em cada item, com indicador discreto'],
        [{'t': 'Alvo de toque', 'b': True}, 'Área clicável de 44 px ou mais no mobile'],
        [{'t': 'Dobra da página', 'b': True}, 'Região visível sem rolagem; o CTA de WhatsApp aparece já na primeira dobra'],
        [{'t': 'Reprodução provisória', 'b': True}, 'Substituto vetorial ou imagem gerada, identificado como tal até chegar o arquivo definitivo'],
        [{'t': 'Ciclos 0 / 1 / 2', 'b': True}, 'Etapas do projeto: planejamento e prototipação; construção; complementos e publicação'],
    ], bs=7.6, pad=4)

# =====================================================================
def _wf_ph(d, x, y, w, h, label=''):
    c = d.c
    c.setFillColor(FILL2); c.rect(x, y, w, h, stroke=0, fill=1)
    c.setStrokeColor(GRAY2); c.setLineWidth(.5); c.rect(x, y, w, h, stroke=1, fill=0)
    c.line(x, y, x + w, y + h); c.line(x + w, y, x, y + h)
    if label:
        c.setFont('IN5', 5.6); c.setFillColor(GRAY)
        c.drawCentredString(x + w / 2, y + h / 2 + 3, label.upper())
        c.setFillColor(FILL2); c.rect(x + w/2 - sw(label.upper(), 'IN5', 5.6)/2 - 3, y + h/2 + 1, sw(label.upper(), 'IN5', 5.6) + 6, 8, stroke=0, fill=1)
        c.setFillColor(GRAY); c.drawCentredString(x + w / 2, y + h / 2 + 2.4, label.upper())

def _wf_line(d, x, y, w, h=3.4, t=False):
    c = d.c
    c.setFillColor(FILL2 if not t else GRAY2); c.rect(x, y, w, h, stroke=0, fill=1)
    c.setStrokeColor(GRAY2); c.setLineWidth(.4); c.rect(x, y, w, h, stroke=1, fill=0)

def _wf_btn(d, x, y, w, label, ghost=False):
    c = d.c
    if ghost:
        c.setStrokeColor(GRAY); c.setLineWidth(.6); c.setDash([2, 1.6], 0); c.rect(x, y, w, 11, stroke=1, fill=0); c.setDash([], 0)
    else:
        c.setFillColor(FILL2); c.rect(x, y, w, 11, stroke=0, fill=1)
        c.setStrokeColor(INK); c.setLineWidth(.6); c.rect(x, y, w, 11, stroke=1, fill=0)
    c.setFont('IN6', 5.2); c.setFillColor(INK); c.drawCentredString(x + w / 2, y + 3.6, label.upper())

def _wf_lbl(d, x, y, t):
    d.c.setFont('IN5', 5.6); d.c.setFillColor(GRAY); d.c.drawString(x, y, t.upper())

def wf_desktop(d, x, ytop, w):
    c = d.c
    y = ytop
    gap = 6
    blocks = []
    # heights
    Hs = dict(hdr=22, hero=112, about=78, cats=70, feat=106, inst=50, wa=44, soc=32, foot=58)
    c.setStrokeColor(GRAY); c.setLineWidth(.8)
    c.setFillColor(WHITE); c.rect(x - 4, ytop - (sum(Hs.values()) + gap * 8) - 6, w + 8, sum(Hs.values()) + gap * 8 + 10, stroke=1, fill=1)
    def blk(key, n, label, lx=None, dark=False):
        nonlocal y
        h = Hs[key]
        y -= h
        c.setFillColor(FILL); c.rect(x, y, w, h, stroke=0, fill=1)
        if dark:
            c.setFillColor(FILL2); c.rect(x + 1, y + 1, w - 2, h - 2, stroke=0, fill=1)
        c.setStrokeColor(GRAY2); c.setLineWidth(.6); c.setDash([2.4, 2], 0); c.rect(x, y, w, h, stroke=1, fill=0); c.setDash([], 0)
        d.tag(n, x + 1, y + h - 1, col=INK)
        _wf_lbl(d, lx or (x + 12), y + h - 8, label)
        return y
    # 1 header
    yy = blk('hdr', 1, 'Cabeçalho · logo + navegação + cta', lx=x + 52)
    c.setStrokeColor(INK); c.setLineWidth(.6); c.rect(x + 12, yy + 4, 34, 13, stroke=1, fill=0)
    c.setFont('IN6', 5); c.setFillColor(INK); c.drawCentredString(x + 29, yy + 8.5, 'LOGO')
    c.setFont('IN5', 5.4); c.setFillColor(GRAY)
    c.drawRightString(x + w - 70, yy + 8.5, 'INÍCIO   SOBRE   CATÁLOGO   CONTATO')
    _wf_btn(d, x + w - 60, yy + 5, 48, 'whatsapp')
    y -= gap
    # 2 hero
    yy = blk('hero', 2, 'Banner principal · primeira dobra')
    lx, lw2 = x + 12, w * .48
    _wf_line(d, lx, yy + 66, lw2 * .5)
    _wf_line(d, lx, yy + 56, lw2 * .95, 7, t=True)
    _wf_line(d, lx, yy + 46, lw2 * .72, 7, t=True)
    _wf_line(d, lx, yy + 36, lw2 * .8)
    _wf_btn(d, lx, yy + 16, 52, 'ver catálogo')
    _wf_btn(d, lx + 58, yy + 16, 62, 'whatsapp', ghost=True)
    _wf_ph(d, x + w * .52, yy + 8, w * .44, Hs['hero'] - 24, 'imagem de clima')
    y -= gap
    # 3 about
    yy = blk('about', 3, 'Apresentação da marca')
    _wf_ph(d, x + 12, yy + 10, w * .38, Hs['about'] - 26, 'foto / logo')
    rx = x + w * .42
    _wf_line(d, rx, yy + 56, w * .3)
    _wf_line(d, rx, yy + 47, w * .5, 6, t=True)
    _wf_line(d, rx, yy + 38, w * .52)
    _wf_line(d, rx, yy + 31, w * .52)
    _wf_line(d, rx, yy + 24, w * .34)
    _wf_btn(d, rx, yy + 8, 66, 'conhecer a marca', ghost=True)
    y -= gap
    # 4 cats
    yy = blk('cats', 4, 'Categorias · grade 4 colunas')
    tw = (w - 24 - 3 * 8) / 4
    for i in range(4):
        tx = x + 12 + i * (tw + 8)
        _wf_ph(d, tx, yy + 18, tw, 34, 'cat. 0%d' % (i + 1))
        _wf_line(d, tx + tw * .1, yy + 10, tw * .6)
    y -= gap
    # 5 feat
    yy = blk('feat', 5, 'Produtos em destaque · grade 4 colunas')
    for i in range(4):
        tx = x + 12 + i * (tw + 8)
        _wf_ph(d, tx, yy + 44, tw, 42, 'foto 4:5')
        _wf_line(d, tx + 4, yy + 34, tw - 8)
        _wf_line(d, tx + 4, yy + 27, tw * .45)
        c.setFont('IN4', 4.8); c.setFillColor(GRAY); c.drawString(tx + 4, yy + 18, 'PEDIR PELO WHATSAPP')
    _wf_btn(d, x + w / 2 - 44, yy + 4, 88, 'ver catálogo completo', ghost=True)
    y -= gap
    # 6 inst
    yy = blk('inst', 6, 'Seção institucional · faixa escura (marsala)', dark=True)
    for i in range(3):
        cx0 = x + 14 + i * (w - 28) / 3
        _wf_line(d, cx0, yy + 30, (w - 28) / 3 * .6, 5, t=True)
        _wf_line(d, cx0, yy + 21, (w - 28) / 3 * .9)
        _wf_line(d, cx0, yy + 14, (w - 28) / 3 * .8)
    y -= gap
    # 7 wa
    yy = blk('wa', 7, 'Chamada para atendimento via whatsapp')
    _wf_line(d, x + w / 2 - w * .26, yy + 26, w * .52, 6, t=True)
    _wf_line(d, x + w / 2 - w * .18, yy + 18, w * .36)
    _wf_btn(d, x + w / 2 - 40, yy + 5, 80, 'chamar no whatsapp')
    y -= gap
    # 8 social
    yy = blk('soc', 8, 'Redes sociais')
    for i in range(3):
        d.circle(x + w / 2 - 22 + i * 22, yy + 14, 8, fill=None, stroke=INK, lw=.6)
    y -= gap
    # 9 foot
    yy = blk('foot', 9, 'Rodapé institucional', dark=True)
    for i in range(4):
        cx0 = x + 14 + i * (w - 28) / 4
        _wf_line(d, cx0, yy + 40, (w - 28) / 4 * .6, 5, t=True)
        _wf_line(d, cx0, yy + 31, (w - 28) / 4 * .85)
        _wf_line(d, cx0, yy + 24, (w - 28) / 4 * .6)
        _wf_line(d, cx0, yy + 17, (w - 28) / 4 * .75)
    _wf_line(d, x + 14, yy + 7, w - 28)
    return ytop - y

def wf_mobile(d, x, ytop, w):
    c = d.c
    y = ytop
    gap = 5
    c.setStrokeColor(GRAY); c.setLineWidth(.8); c.setFillColor(WHITE)
    total = 20 + 46 + 74 + 52 + 62 + 66 + 34 + 34 + 26 + 44 + gap * 9 + 8
    c.rect(x - 4, ytop - total, w + 8, total + 6, stroke=1, fill=1)
    def blk(h, n, label=None):
        nonlocal y
        y -= h
        c.setFillColor(FILL); c.rect(x, y, w, h, stroke=0, fill=1)
        c.setStrokeColor(GRAY2); c.setLineWidth(.5); c.setDash([2, 1.8], 0); c.rect(x, y, w, h, stroke=1, fill=0); c.setDash([], 0)
        if n: d.tag(n, x + 1, y + h - 1, col=INK)
        if label: _wf_lbl(d, x + 11, y + h - 7, label)
        return y
    yy = blk(20, 1)
    c.setStrokeColor(INK); c.setLineWidth(.5); c.rect(x + 10, yy + 5, 26, 10, stroke=1, fill=0)
    c.setFont('IN6', 4); c.setFillColor(INK); c.drawCentredString(x + 23, yy + 8.4, 'LOGO')
    for i in range(3): c.line(x + w - 16, yy + 7 + i * 3.4, x + w - 8, yy + 7 + i * 3.4)
    c.setStrokeColor(INK); c.setLineWidth(.7)
    for i in range(3): c.line(x + w - 16, yy + 7 + i * 3.4, x + w - 8, yy + 7 + i * 3.4)
    y -= gap
    yy = blk(46, None, 'menu expandido (estado aberto)')
    for i, t in enumerate(['INÍCIO', 'SOBRE', 'CATÁLOGO + CATEGORIAS', 'CONTATO', 'WHATSAPP']):
        c.setFont('IN5', 4.6); c.setFillColor(GRAY); c.drawString(x + 10, yy + 30 - i * 7, t)
        c.setStrokeColor(GRAY2); c.setLineWidth(.3); c.line(x + 10, yy + 28 - i * 7, x + w - 10, yy + 28 - i * 7)
    y -= gap
    yy = blk(74, 2)
    _wf_ph(d, x + 8, yy + 34, w - 16, 30, 'imagem de clima')
    _wf_line(d, x + 8, yy + 25, w * .8, 5, t=True)
    _wf_line(d, x + 8, yy + 18, w * .6)
    _wf_btn(d, x + 8, yy + 5, 44, 'catálogo')
    _wf_btn(d, x + 56, yy + 5, 44, 'whatsapp', ghost=True)
    y -= gap
    yy = blk(52, 3)
    _wf_ph(d, x + 8, yy + 24, w - 16, 20, 'foto / logo')
    _wf_line(d, x + 8, yy + 15, w * .7, 4.6, t=True)
    _wf_line(d, x + 8, yy + 9, w * .8)
    y -= gap
    yy = blk(62, 4)
    tw2 = (w - 16 - 6) / 2
    for i in range(4):
        tx = x + 8 + (i % 2) * (tw2 + 6); ty = yy + 30 - (i // 2) * 26
        _wf_ph(d, tx, ty, tw2, 20, 'cat. 0%d' % (i + 1))
    y -= gap
    yy = blk(66, 5)
    for i in range(2):
        tx = x + 8 + i * (tw2 + 6)
        _wf_ph(d, tx, yy + 26, tw2, 26, '4:5')
        _wf_line(d, tx + 2, yy + 18, tw2 - 4)
        _wf_line(d, tx + 2, yy + 12, tw2 * .5)
    y -= gap
    yy = blk(34, 6)
    c.setFillColor(FILL2); c.rect(x + 1, yy + 1, w - 2, 32, stroke=0, fill=1)
    _wf_line(d, x + 8, yy + 22, w * .6, 4.6, t=True)
    _wf_line(d, x + 8, yy + 15, w * .8)
    _wf_line(d, x + 8, yy + 9, w * .7)
    y -= gap
    yy = blk(34, 7)
    _wf_line(d, x + w * .12, yy + 20, w * .76, 5, t=True)
    _wf_btn(d, x + w / 2 - 30, yy + 6, 60, 'whatsapp')
    y -= gap
    yy = blk(26, 8)
    for i in range(3): d.circle(x + w / 2 - 16 + i * 16, yy + 12, 6, fill=None, stroke=INK, lw=.5)
    y -= gap
    yy = blk(44, 9)
    c.setFillColor(FILL2); c.rect(x + 1, yy + 1, w - 2, 42, stroke=0, fill=1)
    for i in range(4): _wf_line(d, x + 8, yy + 32 - i * 7, w * (.6 if i % 2 else .5), 4)
    d.circle(x + w - 14, yy + 10, 9, fill=FILL2, stroke=INK, lw=.8)
    c.setFont('IN6', 5); c.setFillColor(INK); c.drawCentredString(x + w - 14, yy + 8.2, 'WA')
    return ytop - y

def sec05(d):
    c = d.c
    opener(d, '05', 'Wireframe da página inicial', 'Entregável 4 · estrutura sem cor de marca',
           'Diagrama estrutural da página inicial em tons de cinza: caixas tracejadas com X são áreas de imagem, '
           'barras horizontais são linhas de texto e retângulos rotulados são botões. Os números identificam as '
           'nove seções, cuja finalidade e posição estão na tabela ao lado das pranchas.')
    d.box('Como ler',
          'Wireframe não é o site: cores, tipografia e fotografias reais aparecem apenas no protótipo visual '
          '(capítulo 06). As mesmas nove seções existem no desktop e no mobile, reorganizadas para uma coluna.')
    d.h2('Anotações — finalidade e posição de cada seção')
    d.table([16, 88, 200, CW - 304], ['#', 'Seção', 'Finalidade', 'Posição na página'], [
        ['1', {'t': 'Cabeçalho com logotipo e navegação', 'b': True},
         'Orientação permanente: identifica a marca, dá acesso a todas as páginas e mantém o CTA de WhatsApp visível. Único elemento fixo.',
         'Topo, global e fixo. No mobile, recolhido em menu.'],
        ['2', {'t': 'Banner principal', 'b': True},
         'Primeiro impacto: comunica o universo da marca, traz o título principal e os dois caminhos de entrada — catálogo ou WhatsApp.',
         'Primeira dobra, após o cabeçalho. Altura de 70-85% da tela no desktop.'],
        ['3', {'t': 'Apresentação da marca', 'b': True},
         'Contextualiza quem é a Alma Cigana em um parágrafo curto com apoio visual e conduz à página Sobre.',
         'Segunda dobra, após o banner. Layout alternado texto e imagem.'],
        ['4', {'t': 'Categorias de produtos', 'b': True},
         'Organiza o catálogo por tipo de acessório e oferece atalhos diretos às páginas de categoria.',
         'Meio superior, após a apresentação. Grade de 4 colunas (2 no mobile).'],
        ['5', {'t': 'Produtos em destaque', 'b': True},
         'Vitrine comercial: antecipa a experiência do catálogo com peças escolhidas pela loja, no padrão do cartão.',
         'Meio da página, após categorias, com link para o catálogo completo.'],
        ['6', {'t': 'Seção institucional', 'b': True},
         'Reforça confiança e identidade: pilares da marca em faixa escura de contraste, quebrando o ritmo claro.',
         'Após os destaques, antes da conversão. Faixa plena em marsala profundo.'],
        ['7', {'t': 'Chamada para atendimento (WhatsApp)', 'b': True},
         'Ponto de conversão principal: transforma a visita em conversa, com botão de atendimento direto.',
         'Termo da narrativa comercial, após a seção institucional.'],
        ['8', {'t': 'Redes sociais', 'b': True},
         'Conecta o site aos canais onde a marca já vive; facilita a divulgação cruzada.',
         'Após a chamada de WhatsApp, antes do rodapé.'],
        ['9', {'t': 'Rodapé institucional', 'b': True},
         'Fecho institucional e segunda navegação: mapa do site, categorias, contato, redes, informações legais.',
         'Fim da página, global em todas as telas do site.'],
    ])
    d.new_page(); d.section = 'Wireframe da página inicial'
    d.h3('Prancha A — desktop (1024 px ou mais)')
    d.y -= 2
    ytopA = d.y
    hgtA = wf_desktop(d, ML + 6, d.y, CW - 12)
    d.y = ytopA - hgtA - 14
    c.setFont('IN4', 7.4); c.setFillColor(SOFT)
    c.drawString(ML, d.y, 'Ordem de leitura de cima para baixo · largura de conteúdo centralizada em 1200 px no site real.')
    d.y -= 11
    c.drawString(ML, d.y, 'A numeração das seções corresponde à tabela de anotações deste capítulo e ao protótipo do capítulo 06.')
    d.new_page(); d.section = 'Wireframe da página inicial'
    d.h3('Prancha B — mobile (390 px)')
    d.y -= 2
    yt = d.y
    hgt = wf_mobile(d, ML + 10, d.y, 148)
    items = [
        'Seção 1: menu vira painel expansível; categorias listadas dentro de "Catálogo";',
        'Seção 2: imagem acima ou abaixo do texto, altura de 60-70% da tela;',
        'Seções 4 e 5: grades de 4 colunas viram 2 colunas, ou carrossel com arraste;',
        'Seção 6: pilares empilhados verticalmente;',
        'Seções 7 e 8: centralizadas, com botão em largura confortável ao polegar;',
        'Seção 9: colunas empilhadas, copyright ao final;',
        'Botão flutuante de WhatsApp discreto no canto inferior direito (opcional, a aprovar).',
    ]
    d.y = yt - 4
    d.c.setFont('IN6', 8.4); d.c.setFillColor(MARS)
    d.c.drawString(ML + 186, d.y, 'ADAPTAÇÕES MOBILE PREVISTAS'); d.y -= 12
    side_bullets(d, ML + 186, CW - 196, items, s=8.2)
    d.y = min(d.y, yt - hgt - 16)
    d.ensure(120)
    d.h3('Verificações de usabilidade previstas no mobile (Ciclo 1)')
    d.bullets([
        'Menu e painel operáveis com uma só mão, sem rolagem lateral;',
        'Alvos de toque de 44 px ou mais, incluindo cartões e links de pedido;',
        'Botão flutuante de WhatsApp sem cobrir conteúdo nem o rodapé;',
        'Carrosséis com arraste natural, snap e indicadores discretos;',
        'Textos legíveis sob luz forte, com contraste suficiente sobre marsala.',
    ], s=8.4)
    d.y -= 4
    d.box('Do wireframe ao protótipo',
          'A estrutura aprovada nestas pranchas recebe cor, tipografia e fotografias no capítulo 06, sem mudança '
          'de ordem ou de hierarquia das seções. Qualquer alteração de estrutura pedida pelo cliente deve ser '
          'registrada por escrito antes de virar trabalho do Ciclo 1.')

# =====================================================================
def sec06(d):
    c = d.c
    opener(d, '06', 'Protótipo visual da página inicial', 'Entregável 5 · direção estética em cor',
           'Representação estática da página inicial na identidade Alma Cigana: marsala como base, dourado como '
           'acabamento, creme como respiro. Textos entre [colchetes] são espaços reservados para o conteúdo do '
           'cliente; as imagens de joias são referências provisórias, identificadas como tais.')
    d.box('Versão interativa',
          'As pranchas a seguir reproduzem o protótipo em alta fidelidade. A versão interativa, com alternador '
          'desktop e celular, acompanha o pacote no arquivo 05-prototipo-home.html — abra em qualquer navegador, '
          'sem necessidade de internet.')
    d.h3('Convenções das pranchas')
    d.bullets([
        'A ordem e a numeração das nove seções são as mesmas do wireframe (capítulo 05);',
        'Textos entre [colchetes] são espaços reservados: nenhum nome, preço, categoria ou contato foi inventado;',
        'Fotografias de joias marcadas como "referência provisória" simulam proporção e clima, e serão substituídas;',
        'O logotipo aplicado é a versão JPEG extraída do Painel Mestre, até chegar o arquivo original;',
        'Botões e links de WhatsApp usam o link de exemplo do painel, a substituir pelo número comercial real.',
    ], s=8.6)
    d.h3('Como revisar as pranchas')
    d.bullets([
        'Confira a hierarquia: título serifado, olho-de-página dourado, texto neutro e preço em marsala;',
        'Confira a proporção das cores: marsala nas áreas de marca, creme nas de leitura, dourado só em detalhes;',
        'Confira o ritmo: seções claras e escuras alternadas, com respiração generosa entre elas;',
        'Registre ajustes por escrito — aprovações e combinados datados encerram o Ciclo 0.',
    ], s=8.6)
    d.h2('Tratamento visual por seção')
    d.table([74, 148, CW - 222], ['Seção', 'Fundo', 'Tratamento e destaques'], [
        ['1 · Cabeçalho', 'Creme; marsala profundo ao rolar e nas internas', 'Logotipo à esquerda, menu em caixa alta, CTA marsala com filete dourado'],
        ['2 · Banner', 'Marsala profundo', 'Título serifado dourado claro e fotografia em moldura com filete dourado'],
        ['3 · Apresentação', 'Creme', 'Logotipo em moldura arqueada, texto neutro e link com sublinhado dourado'],
        ['4 · Categorias', 'Branco', 'Tiles em marsala profundo com ícone e nome em dourado'],
        ['5 · Destaques', 'Creme', 'Cartões brancos com foto 4:5, filete dourado no hover e preço em marsala'],
        ['6 · Institucional', 'Marsala profundo', 'Três pilares em dourado e creme dentro de moldura de filete'],
        ['7 · WhatsApp', 'Marsala', 'Botão central em marsala profundo com filete dourado'],
        ['8 · Redes', 'Creme', 'Ícones outline dourado em círculos'],
        ['9 · Rodapé', 'Marsala muito profundo', 'Colunas com títulos dourados e texto creme suave'],
    ])
    d.new_page(); d.section = 'Protótipo visual'
    d.h3('Prancha A — desktop')
    d.y -= 2
    ytopP = d.y
    hgtP = pm_desktop(d, ML, d.y, CW)
    d.y = ytopP - hgtP - 14
    c.setFont('IN4', 7.4); c.setFillColor(SOFT)
    c.drawString(ML, d.y, 'Mesmas nove seções do wireframe, em cor · largura de conteúdo centralizada em 1200 px no site real.')
    d.y -= 11
    c.drawString(ML, d.y, 'Placeholders entre [colchetes] e imagens provisórias serão substituídos pelos materiais do cliente no Ciclo 2.')
    d.new_page(); d.section = 'Protótipo visual'
    d.h3('Prancha B — mobile (moldura de 390 px)')
    d.y -= 2
    y0 = d.y
    hgtM = pm_mobile(d, ML + 24, d.y, 168)
    d.y = y0 - 6
    d.c.setFont('IN6', 8.4); d.c.setFillColor(MARS)
    d.c.drawString(ML + 226, d.y, 'O QUE A PRANCHA DEMONSTRA'); d.y -= 12
    side_bullets(d, ML + 226, CW - 236, [
        'Hierarquia visual: título serifado, olhos-de-página dourados e texto neutro;',
        'Cores: marsala e profundos nas áreas de marca, creme nas áreas de leitura, dourado em filetes;',
        'Distribuição das imagens: clima no banner, logotipo em moldura, produtos em cartões 4:5;',
        'Produtos em destaque com nome, categoria, preço e pedido via WhatsApp;',
        'Placeholders: nenhum nome, preço, categoria ou contato foi inventado.',
    ], s=8.2)
    d.y -= 8
    d.c.setFont('IN6', 8.4); d.c.setFillColor(MARS)
    d.c.drawString(ML + 226, d.y, 'CHECKLIST MOBILE DO CICLO 1'); d.y -= 12
    side_bullets(d, ML + 226, CW - 236, [
        'Menu recolhido em painel expansível, operável com uma mão;',
        'Grades de 2 colunas e alvos de toque de 44 px ou mais;',
        'WhatsApp flutuante discreto, sem cobrir conteúdo;',
        'Imagens servidas no tamanho da tela, preservando a direção fotográfica.',
    ], s=8.2)
    d.y = min(d.y, y0 - hgtM - 16)
    d.box('Referências provisórias',
          'As fotografias de joias destas pranchas são ilustrativas (geradas para simular proporção e clima) e o '
          'logotipo é a versão JPEG extraída do Painel Mestre. Tudo será substituído pelos materiais definitivos '
          'do cliente no Ciclo 2.')

def pm_desktop(d, x, ytop, w):
    c = d.c
    y = ytop
    # header
    hh = 20
    y -= hh
    c.setFillColor(CREAM); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setStrokeColor(LINEG); c.setLineWidth(.5); c.rect(x, y, w, hh, stroke=1, fill=0)
    d.circle(x + 14, y + 10, 5.0, fill=GOLD); d.circle(x + 16.4, y + 10, 4.0, fill=CREAM)
    d.star(x + 20.4, y + 13, 1.6, GOLD)
    c.setFont('CG6', 8.2); c.setFillColor(DEEP); c.drawString(x + 25, y + 7, 'ALMA CIGANA')
    c.setFont('IN5', 5.4); c.setFillColor(DEEP)
    c.drawRightString(x + w - 60, y + 7.4, 'INÍCIO     SOBRE     CATÁLOGO     CONTATO')
    d.rrect(x + w - 52, y + 3.6, 44, 12.6, 2, fill=MARS, stroke=GOLD, lw=.6)
    c.setFont('IN6', 5.0); c.setFillColor(GOLDL); c.drawCentredString(x + w - 30, y + 8, 'WHATSAPP')
    # hero
    hh = 96
    y -= hh
    c.setFillColor(DEEP); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setFont('IN6', 5.2); c.setFillColor(GOLD); c.drawString(x + 16, y + 80, 'ALMA CIGANA · JOIAS & ACESSÓRIOS')
    c.setFont('CG6', 15); c.setFillColor(GOLDL)
    c.drawString(x + 16, y + 64, 'Joias e acessórios')
    c.drawString(x + 16, y + 49, 'com alma')
    c.setFont('CG5i', 7.4); c.setFillColor(GOLD); c.drawString(x + 16 + sw('com alma', 'CG6', 15) + 8, y + 50, '[frase de assinatura da marca]')
    c.setFont('CG5i', 6.2); c.setFillColor(HexColor('#D8C3B4'))
    c.drawString(x + 16, y + 37, '[Texto de abertura do banner — mensagem institucional')
    c.drawString(x + 16, y + 29.5, 'a ser fornecida pelo cliente.]')
    d.rrect(x + 16, y + 12, 54, 13, 2, fill=MARS, stroke=GOLD, lw=.6)
    c.setFont('IN6', 5.0); c.setFillColor(GOLDL); c.drawCentredString(x + 43, y + 16.4, 'VER CATÁLOGO')
    d.rrect(x + 76, y + 12, 64, 13, 2, fill=None, stroke=GOLD, lw=.6)
    c.setFont('IN6', 5.0); c.setFillColor(GOLDL); c.drawCentredString(x + 108, y + 16.4, 'FALAR NO WHATSAPP')
    iw = 82
    ix = x + w - iw - 16
    c.setStrokeColor(GOLD); c.setLineWidth(.7); c.rect(ix - 3.5, y + 8, iw + 7, iw + 7, stroke=1, fill=0)
    c.drawImage(IMG['hero'], ix, y + 11.5, iw, iw, mask=None)
    c.setFont('IN4', 4.2); c.setFillColor(GOLDL); c.drawRightString(ix + iw, y + 3, 'imagem ilustrativa · referência provisória')
    # about
    hh = 76
    y -= hh
    c.setFillColor(CREAM); c.rect(x, y, w, hh, stroke=0, fill=1)
    lx, lw2 = x + 14, 60
    c.saveState()
    p = c.beginPath(); p.roundRect(lx, y + 8, lw2, 60, 24); c.clipPath(p, stroke=0, fill=0)
    c.drawImage(IMG['logo'], lx, y + 8, lw2, 60, mask=None)
    c.restoreState()
    c.setStrokeColor(GOLD); c.setLineWidth(.7)
    p = c.beginPath(); p.roundRect(lx, y + 8, lw2, 60, 24); c.drawPath(p, stroke=1, fill=0)
    rx = x + 90
    c.setFont('IN6', 5.2); c.setFillColor(MARS); c.drawString(rx, y + 60, 'SOBRE A MARCA')
    c.setFont('CG6', 11); c.setFillColor(DEEP); c.drawString(rx, y + 47, 'A história que o ouro conta')
    c.setStrokeColor(GOLD); c.setLineWidth(.8); c.line(rx, y + 41.5, rx + 26, y + 41.5)
    c.setFont('CG5i', 6.0); c.setFillColor(SOFT)
    c.drawString(rx, y + 32, '[Texto institucional da Alma Cigana — versão final será')
    c.drawString(rx, y + 24.5, 'escrita e aprovada pelo cliente. Neste espaço entram a origem')
    c.drawString(rx, y + 17, 'da marca e o cuidado com cada peça.]')
    c.setFont('IN6', 5.4); c.setFillColor(MARS); c.drawString(rx, y + 7, 'CONHECER A MARCA')
    c.setStrokeColor(GOLD); c.setLineWidth(.6); c.line(rx, y + 5, rx + sw('CONHECER A MARCA', 'IN6', 5.4), y + 5)
    # cats
    hh = 66
    y -= hh
    c.setFillColor(WHITE); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setStrokeColor(LINEG); c.setLineWidth(.4); c.line(x, y + hh, x + w, y + hh)
    c.setFont('IN6', 5.2); c.setFillColor(MARS); c.drawString(x + 14, y + 54, 'CATÁLOGO ORGANIZADO')
    c.setFont('CG6', 10); c.setFillColor(DEEP); c.drawString(x + 14 + 74, y + 54, 'Categorias')
    tw = (w - 28 - 3 * 8) / 4
    for i in range(4):
        tx = x + 14 + i * (tw + 8)
        c.setFillColor(DEEP); c.rect(tx, y + 8, tw, 40, stroke=0, fill=1)
        c.setStrokeColor(GOLD); c.setLineWidth(.5); c.rect(tx, y + 8, tw, 40, stroke=1, fill=0)
        d.star(tx + tw / 2, y + 36, 3.6, GOLD)
        c.setFont('CG6', 7.2); c.setFillColor(GOLDL); c.drawCentredString(tx + tw / 2, y + 23, 'Categoria 0%d' % (i + 1))
        c.setFont('IN4', 4.2); c.setFillColor(HexColor('#C9A98F')); c.drawCentredString(tx + tw / 2, y + 15.5, 'nome a definir pelo cliente')
    # feat
    hh = 180
    y -= hh
    c.setFillColor(CREAM); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setFont('IN6', 5.2); c.setFillColor(MARS); c.drawString(x + 14, y + 168, 'VITRINE')
    c.setFont('CG6', 10); c.setFillColor(DEEP); c.drawString(x + 14 + 30, y + 168, 'Produtos em destaque')
    imgs = [IMG['cp1'], IMG['cp2'], IMG['cp3'], IMG['cp4']]
    cw2 = (w - 28 - 3 * 8) / 4
    ih = cw2 * 1.15
    for i in range(4):
        tx = x + 14 + i * (cw2 + 8)
        c.setFillColor(WHITE); c.rect(tx, y + 8, cw2, ih + 30, stroke=0, fill=1)
        c.setStrokeColor(LINEG); c.setLineWidth(.4); c.rect(tx, y + 8, cw2, ih + 30, stroke=1, fill=0)
        c.drawImage(imgs[i], tx, y + 8 + ih + 30 - ih, cw2, ih, mask=None)
        c.setStrokeColor(GOLD); c.setLineWidth(.7); c.line(tx, y + 8 + 30, tx + cw2, y + 8 + 30)
        c.setFont('CG6', 6.4); c.setFillColor(DEEP); c.drawString(tx + 5, y + 30, '[Nome do produto %d]' % (i + 1))
        c.setFont('IN4', 4.2); c.setFillColor(SOFT); c.drawString(tx + 5, y + 24, '[CATEGORIA]')
        c.setFont('IN6', 5.4); c.setFillColor(MARS); c.drawString(tx + 5, y + 17, 'R$ [000,00]')
        c.setFont('IN6', 4.2); c.setFillColor(MARS); c.drawString(tx + 5, y + 11, 'PEDIR PELO WHATSAPP')
        c.setStrokeColor(GOLD); c.setLineWidth(.4); c.line(tx + 5, y + 9.6, tx + 5 + sw('PEDIR PELO WHATSAPP', 'IN6', 4.2), y + 9.6)
    d.rrect(x + w / 2 - 44, y + 1, 88, 6, 1, fill=None, stroke=MARS, lw=.4)
    c.setFont('IN6', 3.8); c.setFillColor(MARS); c.drawCentredString(x + w / 2, y + 2.7, 'VER CATÁLOGO COMPLETO')
    # inst
    hh = 50
    y -= hh
    c.setFillColor(DEEP); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setStrokeColor(GOLD); c.setLineWidth(.4); c.rect(x + 6, y + 5, w - 12, hh - 10, stroke=1, fill=0)
    c.setFont('CG6', 9); c.setFillColor(GOLDL); c.drawString(x + 16, y + 36, 'Uma marca autoral, do primeiro desenho ao atendimento')
    cols = [('Atendimento pessoal', 'Cada pedido vira uma conversa com a loja.'),
            ('Catálogo curado', 'Vitrine organizada por categorias e preços.'),
            ('Identidade autoral', 'Marsala e dourado, lua, estrela e rosa.')]
    for i, (t, s2) in enumerate(cols):
        cx0 = x + 16 + i * (w - 32) / 3
        c.setFont('CG6', 6.8); c.setFillColor(GOLD); c.drawString(cx0, y + 24, t)
        c.setFont('IN4', 5); c.setFillColor(HexColor('#D8C3B4'))
        c.drawString(cx0, y + 16, s2)
    d.star(x + w - 20, y + 38, 3, GOLD)
    # wa
    hh = 40
    y -= hh
    c.setFillColor(MARS); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setFont('CG6', 9.6); c.setFillColor(WHITE); c.drawCentredString(x + w / 2, y + 27, 'Peça a sua peça pelo WhatsApp')
    c.setFont('IN4', 5.2); c.setFillColor(HexColor('#F0DCC9'))
    c.drawCentredString(x + w / 2, y + 19, 'A mensagem abre no número comercial da loja com o nome da peça escrito — sem cadastro, sem carrinho, sem checkout.')
    d.rrect(x + w / 2 - 40, y + 6, 80, 10.5, 2, fill=DEEP, stroke=GOLD, lw=.6)
    c.setFont('IN6', 4.8); c.setFillColor(GOLDL); c.drawCentredString(x + w / 2, y + 9.4, 'CHAMAR NO WHATSAPP')
    # social
    hh = 30
    y -= hh
    c.setFillColor(CREAM); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setFont('CG6', 8.2); c.setFillColor(DEEP); c.drawCentredString(x + w / 2, y + 20, 'Redes sociais')
    for i in range(3):
        d.circle(x + w / 2 - 16 + i * 16, y + 11, 5, fill=None, stroke=GOLD, lw=.6)
    c.setFont('IN4', 4.0); c.setFillColor(SOFT)
    c.drawCentredString(x + w / 2, y + 3, 'canais e links reais serão conectados quando o cliente enviar os perfis · ícones ilustrativos')
    # footer
    hh = 48
    y -= hh
    c.setFillColor(HexColor('#20080C')); c.rect(x, y, w, hh, stroke=0, fill=1)
    d.circle(x + 18, y + 34, 4.4, fill=GOLD); d.circle(x + 20.1, y + 34, 3.5, fill=HexColor('#20080C'))
    c.setFont('CG6', 7); c.setFillColor(GOLDL); c.drawString(x + 27, y + 31, 'ALMA CIGANA')
    c.setFont('IN4', 4.4); c.setFillColor(HexColor('#B39A8E'))
    c.drawString(x + 14, y + 23, '[Descrição institucional curta —')
    c.drawString(x + 14, y + 17.5, 'texto do cliente.]')
    for i, (t, ls) in enumerate([('NAVEGAÇÃO', ['Início', 'Sobre a marca', 'Catálogo', 'Contato']),
                                 ('CATEGORIAS', ['[categoria 1]', '[categoria 2]', '[categoria 3]', '[categoria 4]']),
                                 ('CONTATO', ['WhatsApp: [número]', 'E-mail: [e-mail]', '[endereço]', '[horários]'])]):
        cx0 = x + 128 + i * (w - 140) / 3
        c.setFont('IN6', 4.4); c.setFillColor(GOLD); c.drawString(cx0, y + 34, t)
        for j, ln in enumerate(ls):
            c.setFont('IN4', 4.4); c.setFillColor(HexColor('#CBB1A4')); c.drawString(cx0, y + 27 - j * 5.6, ln)
    c.setStrokeColor(GOLD); c.setLineWidth(.3); c.line(x + 14, y + 8, x + w - 14, y + 8)
    c.setFont('IN4', 4.0); c.setFillColor(HexColor('#A98D81'))
    c.drawString(x + 14, y + 3, '© 2026 Alma Cigana · [razão social / CNPJ pendentes]')
    c.drawRightString(x + w - 14, y + 3, 'Protótipo visual · Ciclo 0 · não é o site finalizado')
    return ytop - y

def pm_mobile(d, x, ytop, w):
    c = d.c
    fh = 538
    c.setFillColor(HexColor('#0D0809'))
    c.roundRect(x - 8, ytop - fh - 4, w + 16, fh + 12, 16, stroke=0, fill=1)
    c.setStrokeColor(HexColor('#3C2B2E')); c.setLineWidth(.8)
    c.roundRect(x - 8, ytop - fh - 4, w + 16, fh + 12, 16, stroke=1, fill=0)
    y = ytop - 4
    # header
    hh = 18
    y -= hh
    c.setFillColor(CREAM); c.rect(x, y, w, hh, stroke=0, fill=1)
    d.circle(x + 12, y + 9, 4.4, fill=GOLD); d.circle(x + 14, y + 9, 3.5, fill=CREAM)
    c.setFont('CG6', 7); c.setFillColor(DEEP); c.drawString(x + 21, y + 6.4, 'ALMA CIGANA')
    c.setStrokeColor(DEEP); c.setLineWidth(.9)
    for i in range(3): c.line(x + w - 14, y + 5.4 + i * 3, x + w - 6, y + 5.4 + i * 3)
    # hero
    hh = 152
    y -= hh
    c.setFillColor(DEEP); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.drawImage(IMG['chm'], x + 8, y + 44, w - 16, (w - 16) * .66, mask=None)
    c.setStrokeColor(GOLD); c.setLineWidth(.5); c.rect(x + 8, y + 44, w - 16, (w - 16) * .66, stroke=1, fill=0)
    c.setFont('IN6', 4.6); c.setFillColor(GOLD); c.drawString(x + 8, y + 36, 'ALMA CIGANA · JOIAS & ACESSÓRIOS')
    c.setFont('CG6', 10.5); c.setFillColor(GOLDL); c.drawString(x + 8, y + 26, 'Joias e acessórios com alma')
    c.setFont('CG5i', 5.2); c.setFillColor(HexColor('#D8C3B4')); c.drawString(x + 8, y + 18, '[frase de assinatura da marca]')
    d.rrect(x + 8, y + 6, 46, 10, 2, fill=MARS, stroke=GOLD, lw=.5)
    c.setFont('IN6', 4.2); c.setFillColor(GOLDL); c.drawCentredString(x + 31, y + 9.4, 'VER CATÁLOGO')
    d.rrect(x + 58, y + 6, 52, 10, 2, fill=None, stroke=GOLD, lw=.5)
    c.setFont('IN6', 4.2); c.setFillColor(GOLDL); c.drawCentredString(x + 84, y + 9.4, 'WHATSAPP')
    # about
    hh = 40
    y -= hh
    c.setFillColor(CREAM); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.saveState()
    p = c.beginPath(); p.roundRect(x + 8, y + 6, 30, 28, 12); c.clipPath(p, stroke=0, fill=0)
    c.drawImage(IMG['logo'], x + 8, y + 6, 30, 28, mask=None)
    c.restoreState()
    c.setStrokeColor(GOLD); c.setLineWidth(.5)
    p = c.beginPath(); p.roundRect(x + 8, y + 6, 30, 28, 12); c.drawPath(p, stroke=1, fill=0)
    c.setFont('CG6', 8); c.setFillColor(DEEP); c.drawString(x + 44, y + 26, 'A história que o ouro conta')
    c.setFont('CG5i', 4.8); c.setFillColor(SOFT)
    c.drawString(x + 44, y + 18, '[Texto institucional — versão final')
    c.drawString(x + 44, y + 12, 'será aprovada pelo cliente.]')
    # cats 2x2
    hh = 62
    y -= hh
    c.setFillColor(WHITE); c.rect(x, y, w, hh, stroke=0, fill=1)
    tw2 = (w - 16 - 6) / 2
    for i in range(4):
        tx = x + 8 + (i % 2) * (tw2 + 6); ty = y + 32 - (i // 2) * 27
        c.setFillColor(DEEP); c.rect(tx, ty, tw2, 24, stroke=0, fill=1)
        c.setStrokeColor(GOLD); c.setLineWidth(.4); c.rect(tx, ty, tw2, 24, stroke=1, fill=0)
        d.star(tx + tw2 / 2, ty + 15, 3, GOLD)
        c.setFont('CG6', 5.6); c.setFillColor(GOLDL); c.drawCentredString(tx + tw2 / 2, ty + 6, 'Categoria 0%d' % (i + 1))
    # feat 2 cols
    hh = 120
    y -= hh
    c.setFillColor(CREAM); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setFont('CG6', 8); c.setFillColor(DEEP); c.drawString(x + 8, y + 110, 'Produtos em destaque')
    imgs = [IMG['cp1'], IMG['cp2']]
    ih2 = tw2 * 1.15
    for i in range(2):
        tx = x + 8 + i * (tw2 + 6)
        c.setFillColor(WHITE); c.rect(tx, y + 6, tw2, ih2 + 16, stroke=0, fill=1)
        c.setStrokeColor(LINEG); c.setLineWidth(.4); c.rect(tx, y + 6, tw2, ih2 + 16, stroke=1, fill=0)
        c.drawImage(imgs[i], tx, y + 6 + 16, tw2, ih2, mask=None)
        c.setFont('CG6', 5.4); c.setFillColor(DEEP); c.drawString(tx + 4, y + 14, '[Nome do produto]')
        c.setFont('IN6', 4.6); c.setFillColor(MARS); c.drawString(tx + 4, y + 8.4, 'R$ [000,00]')
    # inst
    hh = 34
    y -= hh
    c.setFillColor(DEEP); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setFont('CG6', 7); c.setFillColor(GOLDL); c.drawString(x + 8, y + 24, 'Uma marca autoral')
    c.setFont('IN4', 4.4); c.setFillColor(HexColor('#D8C3B4'))
    c.drawString(x + 8, y + 16, 'Atendimento pessoal, catálogo curado e')
    c.drawString(x + 8, y + 10, 'identidade autoral em cada detalhe.')
    # wa
    hh = 34
    y -= hh
    c.setFillColor(MARS); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setFont('CG6', 7.6); c.setFillColor(WHITE); c.drawCentredString(x + w / 2, y + 22, 'Peça pelo WhatsApp')
    d.rrect(x + w / 2 - 34, y + 8, 68, 10, 2, fill=DEEP, stroke=GOLD, lw=.5)
    c.setFont('IN6', 4.2); c.setFillColor(GOLDL); c.drawCentredString(x + w / 2, y + 11.4, 'CHAMAR NO WHATSAPP')
    # social + foot
    hh = 22
    y -= hh
    c.setFillColor(CREAM); c.rect(x, y, w, hh, stroke=0, fill=1)
    for i in range(3): d.circle(x + w / 2 - 14 + i * 14, y + 11, 4.4, fill=None, stroke=GOLD, lw=.5)
    hh = 56
    y -= hh
    c.setFillColor(HexColor('#20080C')); c.rect(x, y, w, hh, stroke=0, fill=1)
    c.setFont('CG6', 6.4); c.setFillColor(GOLDL); c.drawString(x + 8, y + 46, 'ALMA CIGANA')
    for j, ln in enumerate(['Início · Sobre · Catálogo · Contato', '[categoria 1] · [categoria 2] · [categoria 3]',
                            'WhatsApp: [número comercial]', '© 2026 Alma Cigana · [CNPJ pendente]']):
        c.setFont('IN4', 4.2); c.setFillColor(HexColor('#CBB1A4')); c.drawString(x + 8, y + 36 - j * 7, ln)
    d.circle(x + w - 14, y + 44, 7, fill=MARS, stroke=GOLD, lw=.6)
    c.setFont('IN6', 4.4); c.setFillColor(GOLDL); c.drawCentredString(x + w - 14, y + 42.2, 'WA')
    return ytop - y

# =====================================================================
def sec07(d):
    opener(d, '07', 'Materiais pendentes do cliente', 'Checklist de envio · dependência do cliente',
           'Lista priorizada de materiais e confirmações necessários para o desenvolvimento. A produção ativa '
           'começa quando os materiais chegarem completos; o que faltar é enviado depois e o cronograma é '
           'reajustado pela nova data de recebimento.')
    d.ensure(20)
    x = ML
    for kind, lab in [('r', 'bloqueia o desenvolvimento'), ('y', 'bloqueia o conteúdo final'), ('g', 'complementa')]:
        d.dotp(x, d.y, kind)
        d.c.setFont('IN4', 8); d.c.setFillColor(SOFT); d.c.drawString(x + 11, d.y, lab)
        x += 11 + sw(lab, 'IN4', 8) + 22
    d.y -= 14
    C = [14, 116, 104, 30, CW - 264]
    d.h2('Identidade e marca', 'A')
    d.table(C, ['#', 'Material', 'Formato sugerido', '', 'Observação'], [
        ['1', {'t': 'Logotipo — arquivo original', 'b': True}, 'Vetor (SVG, AI, PDF) ou PNG transparente de 2000 px ou mais, versões para fundo claro e escuro', {'dot': 'r'}, 'Hoje existe apenas o JPEG extraído do Painel Mestre (2100×1500): suficiente para protótipo, não para o site final'],
        ['2', {'t': 'Confirmação da versão do logotipo', 'b': True}, 'Resposta por escrito', {'dot': 'r'}, 'O arquivo disponível traz o descritivo "CARTOMANCIA"; o site é de joias e acessórios. Confirmar qual versão usar'],
        ['3', {'t': 'Referências visuais adicionais', 'b': True}, 'Links ou imagens', {'dot': 'g'}, 'Sites, posts ou climas estéticos que a marca admire'],
    ])
    d.h2('Catálogo', 'B')
    d.table(C, ['#', 'Material', 'Formato sugerido', '', 'Observação'], [
        ['4', {'t': 'Lista de categorias', 'b': True}, 'Texto com nomes e ordem de exibição', {'dot': 'r'}, 'Nenhuma categoria foi inventada; o protótipo usa espaços reservados'],
        ['5', {'t': 'Lista de produtos (até 15)', 'b': True}, 'Planilha ou documento, um bloco por produto', {'dot': 'r'}, 'Quantidade definitiva é item em aberto do Painel Mestre'],
        ['6', {'t': 'Campos de cada produto', 'b': True}, 'Na mesma planilha', {'dot': 'r'}, 'Nome, preço, descrição, categoria, material, dimensões, cores, variações e cuidados (quando aplicáveis)'],
        ['7', {'t': 'Fotografias dos produtos', 'b': True}, 'Arquivos originais, sem compressão; proporção retrato 4:5', {'dot': 'r'}, 'Mínimo de 1 foto por produto; 2 a 3 enriquecem a página individual'],
        ['8', {'t': 'Destaques da home', 'b': True}, 'Indicação de até 4 produtos', {'dot': 'y'}, 'Quais peças abrem a vitrine da página inicial'],
        ['9', {'t': 'Fotos de clima (banner e seções)', 'b': True}, '2 a 4 imagens em paisagem', {'dot': 'y'}, 'Se a marca não tiver, combina-se imagens substitutas seguindo a direção fotográfica'],
    ])
    d.h2('Canais e contato', 'C')
    d.table(C, ['#', 'Material', 'Formato sugerido', '', 'Observação'], [
        ['10', {'t': 'Número do WhatsApp comercial', 'b': True}, 'Número com DDI e DDD', {'dot': 'r'}, 'O protótipo usa o link de exemplo do Painel Mestre; o número real entra no Ciclo 2'],
        ['11', {'t': 'Redes sociais', 'b': True}, 'Lista de canais e links completos dos perfis', {'dot': 'y'}, 'O protótipo exibe ícones ilustrativos com perfis pendentes'],
        ['12', {'t': 'E-mail comercial', 'b': True}, 'Texto', {'dot': 'y'}, 'Opcional, recomendado para o rodapé'],
        ['13', {'t': 'Endereço e horários', 'b': True}, 'Texto', {'dot': 'g'}, 'Exibir apenas se a loja quiser'],
    ])
    d.h2('Textos institucionais', 'D')
    d.table(C, ['#', 'Material', 'Formato sugerido', '', 'Observação'], [
        ['14', {'t': 'Texto "Sobre a marca"', 'b': True}, 'Dois parágrafos aprovados', {'dot': 'y'}, 'História, significado do nome e proposta de valor'],
        ['15', {'t': 'Frase de assinatura do banner', 'b': True}, 'Uma linha', {'dot': 'y'}, 'Espaço reservado no protótipo'],
        ['16', {'t': 'Descrição curta do rodapé', 'b': True}, 'Uma a duas linhas', {'dot': 'g'}, ''],
        ['17', {'t': 'Políticas da loja', 'b': True}, 'Texto aprovado', {'dot': 'y'}, 'Trocas, devoluções, envio e cuidados; conferência final é do cliente'],
        ['18', {'t': 'Dados institucionais', 'b': True}, 'Razão social e CNPJ, se desejar exibir', {'dot': 'g'}, ''],
    ])
    d.h2('Confirmações administrativas (em aberto no Painel Mestre)', 'E')
    d.table([14, CW - 44, 30], ['#', 'Confirmação', ''], [
        ['19', 'Quantidade definitiva de produtos desta versão (limite contratado: 15)', {'dot': 'r'}],
        ['20', 'Responsável pelos custos de domínio e hospedagem', {'dot': 'r'}],
        ['21', 'Responsável por fornecer e aprovar textos, preços e políticas', {'dot': 'y'}],
        ['22', 'Datas estimadas de início e entrega, e vencimentos das parcelas', {'dot': 'y'}],
        ['23', 'Titularidade das contas (domínio, plataforma, serviços) — recomendação do painel: pertencer ao cliente', {'dot': 'y'}],
    ])
    d.h2('Como enviar')
    d.bullets([
        'Uma pasta compartilhada única (Drive ou similar), com subpastas: 01-logotipo, 02-fotografias, 03-produtos, 04-textos, 05-contatos;',
        'Arquivos originais, sem compressão de aplicativo de mensagem;',
        'Textos já revisados — a conferência final é sempre do cliente;',
        'Avisar por mensagem quando a pasta estiver completa, para iniciar a contagem do prazo de produção ativa (7 a 12 dias úteis).',
    ], s=8.8)
    d.h2('O que já está disponível (não precisa reenviar, só confirmar)')
    d.bullets([
        'Identidade cromática completa: marsala #7A1220, marsala profundo #4A0710, dourado #C6A15B, dourado claro #EBD9A9;',
        'Composição do logotipo: lua, estrela e rosa em dourado sobre marsala — faltam o arquivo original e a confirmação do descritivo;',
        'Uma fotografia de referência de clima, presente no Painel Mestre, que guia a direção fotográfica;',
        'Escopo, limites e fluxo comercial do site, registrados no Painel Mestre v2.0.',
    ], s=8.8)

# =====================================================================
def sec08(d):
    c = d.c
    opener(d, '08', 'Aprovação e próximos passos', 'Encerramento do Ciclo 0',
           'Este pacote existe para que o cliente visualize e aprove a direção estética e estrutural antes do '
           'desenvolvimento funcional. O registro da aprovação encerra o Ciclo 0 e libera o Ciclo 1 — construção '
           'da estrutura, conforme o Painel Mestre.')
    d.h2('Termo de aprovação da etapa')
    d.ensure(150); d.y -= 4
    y0 = d.y
    bh = 150
    d.rrect(ML, y0 - bh, CW, bh, 4, fill=CREAM, stroke=GOLD, lw=1)
    d.hair(ML + 12, y0 - 12, ML + 12, y0 - bh + 12, GOLD, 2)
    yy = y0 - 24
    c.setFont('IN4', 9); c.setFillColor(INK)
    for ln in d.wrap('Declaro que revisei o pacote de planejamento e prototipação do site Alma Cigana '
                     '(levantamento, arquitetura, guia visual, wireframe e protótipo da página inicial) e '
                     'APROVO a direção estética e estrutural apresentada, ciente de que se trata de '
                     'representação de planejamento — não do site finalizado — e de que textos, produtos, '
                     'preços, categorias, contatos e redes sociais serão inseridos após o envio e a '
                     'conferência dos materiais relacionados no capítulo 07.', 'IN4', 9, CW - 44):
        c.drawString(ML + 22, yy, ln); yy -= 12.6
    yy -= 10
    for i, lab in enumerate(['Cliente — Alma Cigana', 'Responsável pelo projeto']):
        sx = ML + 22 + i * (CW - 44) / 2
        c.setStrokeColor(INK); c.setLineWidth(.7); c.line(sx, yy - 16, sx + (CW - 64) / 2, yy - 16)
        c.setFont('IN5', 7.6); c.setFillColor(SOFT); c.drawString(sx, yy - 26, lab)
        c.setFont('IN4', 7.2); c.setFillColor(SOFT); c.drawString(sx, yy - 35, 'nome e data:')
    d.y = y0 - bh - 16
    d.h2('Próximas ações, em ordem de prioridade')
    acts = [
        ('Formalizar o acordo financeiro e o escopo', 'Registrar preço, entrada recebida, parcelas, limites e condições de entrega, conforme o Painel Mestre.'),
        ('Enviar os materiais do cliente', 'Logotipo original, fotografias, produtos com nomes, preços e descrições, categorias, WhatsApp comercial, redes e texto institucional.'),
        ('Registrar a aprovação deste pacote', 'Assinatura do termo acima, ou aprovação por escrito em canal compartilhado com data e ciência das duas partes.'),
        ('Iniciar o Ciclo 1 — construção da estrutura', 'Cabeçalho e navegação, página inicial, banner, catálogo, categorias e primeiros produtos, com primeira versão responsiva.'),
    ]
    for i, (t, s2) in enumerate(acts):
        d.ensure(34)
        d.circle(ML + 8, d.y - 4, 8, fill=MARS)
        d.c.setFont('IN6', 8); d.c.setFillColor(GOLDL); d.c.drawCentredString(ML + 8, d.y - 6.8, str(i + 1))
        d.c.setFont('IN6', 9.4); d.c.setFillColor(DEEP); d.c.drawString(ML + 24, d.y - 4, t)
        d.y -= 15
        for ln in d.wrap(s2, 'IN4', 8.4, CW - 26):
            d.c.setFont('IN4', 8.4); d.c.setFillColor(SOFT); d.c.drawString(ML + 24, d.y, ln); d.y -= 11
        d.y -= 6
    d.box('Lembrete importante',
          'Nada neste documento é o site finalizado: é planejamento e prototipação. Ajustes de direção estética '
          'desta etapa estão incluídos no escopo; novas funcionalidades entram em orçamento próprio, conforme as '
          'regras de trabalho do Painel Mestre.')
    d.y -= 2
    d.hair(ML, d.y, W - MR, d.y, GOLD, .8)
    d.y -= 16
    d.star(W / 2, d.y, 5, GOLD)
    d.y -= 16
    c.setFont('CG5i', 11); c.setFillColor(MARS)
    c.drawCentredString(W / 2, d.y, 'Alma Cigana — marsala como base, dourado como acabamento.')
    d.y -= 14
    c.setFont('IN4', 7.6); c.setFillColor(SOFT)
    c.drawCentredString(W / 2, d.y, 'Pacote de Planejamento e Prototipação · Ciclo 0 · versão 1.0 · 03 de novembro de 2026')

def continue_build(d):
    sec03(d); sec04(d); sec05(d); sec06(d); sec07(d); sec08(d)
    d.c.save()
