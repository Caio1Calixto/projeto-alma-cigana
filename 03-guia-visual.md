# 03 — Guia Visual (Identidade aplicada ao projeto)

**Projeto:** Site Alma Cigana — joias e acessórios
**Etapa:** Ciclo 0 — Planejamento e prototipação
**Base:** identidade definida pelo cliente no Painel Mestre (marsala e dourado) + direção estética sofisticada, minimalista, editorial e comercial.
**Princípio-guia:** *o marsala é a base; o dourado é o acabamento; o branco e o creme são o respiro.*

---

## 1. Paleta cromática

| Cor | HEX | Papel no site | Onde aparece |
|---|---|---|---|
| Marsala | `#7A1220` | **Cor principal** | Botões primários, títulos sobre fundo claro, seções de destaque, links ativos |
| Marsala profundo | `#4A0710` | Profundidade | Fundo do cabeçalho ao rolar, seções escuras (institucional, CTA WhatsApp), rodapé, estado hover do marsala |
| Dourado | `#C6A15B` | **Acabamento** | Filetes, bordas de botões, ornamentos, ícones, sublinhados, detalhes de cartões |
| Dourado claro | `#EBD9A9` | Apoio do dourado | Texto dourado sobre marsala, realces sutis, divisórias claras |
| Creme | `#F7F3EC` (apoio) | Respiro | Fundo geral das páginas, cartões, alternância de seções claras |
| Branco | `#FFFFFF` (apoio) | Respiro | Cartões de produto, textos sobre marsala |
| Texto corrido escuro | `#2B1A1D` (apoio neutro derivado do marsala) | Legibilidade | Parágrafos sobre fundo claro |

### Regras de uso (proporção e restrições)

1. **Marsala como base:** seções, botões, títulos e destaques. É a cor que assina a marca.
2. **Dourado nunca como fundo dominante:** entra em filetes de 1–2 px, bordas, ornamentos, ícones e pequenos realces. Regra prática de proporção: ~60% marsala/profundos nas áreas de marca, ~30% creme/branco nas áreas de conteúdo, ~10% dourado em detalhes.
3. **Branco e creme apenas como apoio:** fundos de leitura e cartões; nunca combinados com tipografia dourada de baixo contraste.
4. **Contraste obrigatório:** texto claro (`#FFFFFF` / `#EBD9A9`) sobre marsala e marsala profundo; texto escuro (`#2B1A1D` / marsala) sobre creme e branco. Dourado `#C6A15B` só como texto em fundos escuros.
5. **Nenhuma cor fora desta paleta** no site final. Ícones de redes sociais e o símbolo do WhatsApp recebem tratamento monocromático (dourado/creme sobre marsala, ou marsala sobre creme) para não descaracterizar a identidade.

---

## 2. Tipografia

| Uso | Família recomendada | Por quê |
|---|---|---|
| Títulos e display | **Cormorant Garamond** (serifada, pesos Medium/SemiBold; itálico para assinaturas) | Serifada editorial, elegante e gratuita para uso comercial; ecoa o lettering do logotipo |
| Textos, menus, UI | **Inter** (pesos Regular/Medium/SemiBold) | Sans-serif neutra, altamente legível em telas pequenas; usada também no Painel Mestre |
| Alternativas/fallback | Georgia / Times (serifada) e Helvetica/Arial (sans), caso as fontes web não carreguem | Garantia de funcionamento offline |

### Escala tipográfica (desktop → mobile)

| Elemento | Desktop | Mobile | Estilo |
|---|---|---|---|
| Display (banner) | 56–64 px | 34–40 px | Cormorant SemiBold, entrelinha 1.1 |
| Título de seção | 36–40 px | 26–30 px | Cormorant SemiBold |
| Subtítulo / olhos-de-página | 12–13 px | 11–12 px | Inter Medium, caixa alta, espaçamento +0.18em, cor dourada sobre escuro / marsala sobre claro |
| Texto corrido | 16–17 px | 15–16 px | Inter Regular, entrelinha 1.6 |
| Preços | 18–20 px | 16–18 px | Inter SemiBold, cor marsala |
| Legendas / apoios | 12–13 px | 12 px | Inter Regular, cor neutra escura |

---

## 3. Estilo dos botões

| Tipo | Composição | Uso |
|---|---|---|
| **Primário** | Fundo marsala `#7A1220`, texto creme/branco, filete de 1 px dourado `#C6A15B`, cantos retos levemente arredondados (2–4 px), caixa alta espaçada Inter Medium 13–14 px, padding 14×28 px | CTAs principais ("Ver catálogo", "Pedir pelo WhatsApp") |
| Primário · hover | Fundo marsala profundo `#4A0710`, filete dourado claro | Estados interativos |
| **Secundário** | Fundo transparente, borda 1 px marsala, texto marsala; sobre fundos escuros: borda e texto dourado claro | CTAs alternativos ("Conhecer a marca") |
| **WhatsApp** | Mesma grammática do primário (marsala + filete dourado) com glifo de comunicação à esquerda — mantém a identidade; **não** usar verde fora do glifo, se aparecer | Todos os pontos de pedido/atendimento |
| **Link textual** | Marsala sobre claro / dourado claro sobre escuro, sublinhado fino dourado | Navegações secundárias ("Ver todos os produtos") |

**Raio de canto:** máximo 4 px em botões e cartões (linguagem editorial, não "bolhada").
**Altura mínima de toque no mobile:** 44–48 px.

---

## 4. Cartões de produto

- **Fundo:** branco, borda invisível; sombra quase imperceptível apenas para separar do creme.
- **Fotografia:** proporção **4:5 (retrato)**, ocupando o topo do cartão, fundo da foto creme ou marsala conforme a direção fotográfica; zoom sutil (4%) no hover.
- **Filete dourado:** linha de 1 px que surge sob a foto no hover — acabamento, não decoração fixa.
- **Conteúdo:** nome do produto (Cormorant SemiBold 18–20 px, marsala escuro) · categoria em legenda pequena (Inter 12 px, caixa alta) · preço (Inter SemiBold, marsala) · ação "Pedir pelo WhatsApp" como link textual com glifo.
- **Grade:** 4 colunas no desktop · 2 colunas no tablet · 2 colunas compactas no mobile (1 coluna opcional em telas < 360 px).
- **Sem selos de promoção/urgência:** linguagem comercial sóbria; qualquer indicação de disponibilidade será informação manual fornecida pela loja.

---

## 5. Organização do cabeçalho

- **Barra única, fundo creme/branco translúcido** no topo da home; ao rolar (e nas páginas internas), fundo marsala profundo com texto creme — garante contraste e presença da marca.
- **Esquerda:** logotipo (altura 40–48 px no desktop, 32–36 px no mobile).
- **Centro-direita:** menu horizontal (Início · Sobre · Catálogo · Contato), Inter Medium 13–14 px, caixa alta espaçada; item ativo com sublinhado dourado.
- **Direita:** botão primário "WhatsApp".
- **Mobile:** logotipo à esquerda + ícone de menu à direita; painel expandido em fundo marsala profundo com itens empilhados, categorias listadas sob "Catálogo" e CTA WhatsApp fixo no rodapé do painel.
- **Altura:** 72–80 px desktop · 56–64 px mobile.

---

## 6. Padrão de espaçamento

Escala base de 8 px: **8 · 16 · 24 · 32 · 48 · 64 · 96 · 128**.

| Aplicação | Medida |
|---|---|
| Margem lateral do conteúdo | 24 px mobile · 48–64 px desktop (conteúdo centralizado, largura máxima 1200 px) |
| Respiração entre seções da home | 96–128 px desktop · 64–80 px mobile |
| Espaço entre cartões (gutter) | 24–32 px desktop · 16 px mobile |
| Padding interno de cartões | 16–24 px |
| Distância título → conteúdo | 24–32 px |
| Altura do banner principal | 70–85 vh desktop · 60–70 vh mobile |

**Princípio editorial:** o espaço em branco (creme) é parte do design; seções densas demais descaracterizam a estética sofisticada.

---

## 7. Direção estética das fotografias

1. **Luz:** natural ou simulada, quente e lateral, com sombras suaves — referência: fotografia de joias douradas sobre tecido creme presente no Painel Mestre.
2. **Fundos:** creme/linho claro para catálogo e produtos; marsala ou seda escura para peças de clima (banner, seções de marca).
3. **Composição:** minimalista, produto como protagonista, espaço negativo generoso; sem excesso de props (no máximo tecido, pedra ou elemento orgânico discreto).
4. **Consistência:** mesmo tratamento de cor (tons quentes, dourado realçado), mesmas proporções (4:5 retrato para produtos; 16:9 ou 3:2 para banners).
5. **Qualidade:** arquivos originais sem compressão de mensagem; exportação web otimizada no ciclo de desenvolvimento.
6. **O que evitar:** fundos coloridos fora da paleta, flash estourado, poluição visual, textos queimados na imagem.

---

## 8. Comportamento visual em dispositivos móveis

- **Mobile é o canal principal do público:** toda decisão de layout é testada primeiro em 390 px de largura.
- Menu recolhido; categorias acessíveis no painel do menu; CTA WhatsApp sempre visível (cabeçalho e/ou botão flutuante discreto no canto inferior).
- Grades: produtos em 2 colunas; categorias em 2 colunas ou carrossel horizontal com snap; banner com texto acima da dobra.
- Tipografia reduzida conforme escala do item 2; entrelinhas generosas mantidas.
- Alvos de toque ≥ 44 px; carrosséis com arraste natural e indicadores discretos.
- Imagens servidas em tamanho adequado à tela (performance), mantendo a direção fotográfica.
- Seções escuras (marsala profundo) preservam o mesmo ritmo vertical, com padding reduzido (~2/3 do desktop).

---

## 9. Aplicação da marca gráfica

- O logotipo (lua, estrela e rosa em dourado sobre marsala profundo) é o ponto de partida de toda a aplicação.
- Sobre fundos claros, usa-se a versão do logotipo com elementos em marsala/dourado; sobre fundos escuros, a versão dourada — conforme arquivos originais que o cliente enviará.
- Ornamentos derivados (filete com estrela de quatro pontas, arcos de lua) podem pontuar divisórias de seção, sempre em dourado e em traço fino.
- Enquanto o arquivo original não chega, o protótipo usa **reprodução vetorial provisória** do símbolo, claramente identificada.
