# 02 — Arquitetura do Site

**Projeto:** Site Alma Cigana — joias e acessórios
**Etapa:** Ciclo 0 — Planejamento e prototipação
**Escopo:** site institucional com catálogo digital e encaminhamento de pedidos pelo WhatsApp (sem carrinho, checkout ou pagamento).

---

## 1. Hierarquia das páginas

```
ALMA CIGANA — MAPA DO SITE
│
├── 1. PÁGINA INICIAL  (/)
│     ├── apresentação da marca (resumo) ──► 2. SOBRE
│     ├── vitrine de categorias ──────────► 4. CATEGORIAS
│     ├── produtos em destaque ───────────► 5. PÁGINA DE PRODUTO
│     └── chamada WhatsApp / redes sociais
│
├── 2. SOBRE A MARCA  (/sobre)
│     └── história, identidade comercial e valores
│
├── 3. CATÁLOGO DE PRODUTOS  (/catalogo)
│     ├── filtro por categoria (mesma taxonomia das páginas de categoria)
│     ├── grade com todos os produtos (até 15 nesta versão)
│     └── cada cartão ──► 5. PÁGINA DE PRODUTO
│
├── 4. CATEGORIAS  (/categoria/[slug])
│     ├── uma página por categoria definida pelo cliente
│     ├── grade filtrada dos produtos daquela categoria
│     └── cada cartão ──► 5. PÁGINA DE PRODUTO
│
├── 5. PÁGINA INDIVIDUAL DE PRODUTO  (/produto/[slug])
│     ├── fotografia(s), nome, preço e descrição
│     ├── botão "Pedir pelo WhatsApp" (mensagem pré-preenchida com o nome do produto)
│     ├── trilho de navegação: Início › Catálogo › [Categoria] › [Produto]
│     └── produtos relacionados (mesma categoria) ──► outras páginas de produto
│
├── 6. CONTATO  (/contato)
│     ├── WhatsApp comercial (botão e número)
│     ├── redes sociais
│     └── informações institucionais de contato fornecidas pelo cliente
│
└── 7. RODAPÉ INSTITUCIONAL  (global — presente em todas as páginas)
      ├── mapa do site (links para 1–6)
      ├── redes sociais
      ├── informações institucionais (CNPJ/endereço apenas se fornecidos)
      └── créditos e aviso de direitos
```

**Níveis de profundidade:** nenhum conteúdo fica a mais de 3 cliques da home
(home → catálogo → categoria → produto). Categorias não possuem subcategorias
nesta versão; se a lista de produtos crescer em etapa futura, a taxonomia pode
ganhar um nível sem refazer a estrutura.

---

## 2. Sistema de navegação

### 2.1 Cabeçalho (global, fixo no topo)

| Elemento | Comportamento |
|---|---|
| Logotipo | Canto esquerdo; clique leva à página inicial |
| Menu principal | Início · Sobre · Catálogo · Contato |
| Item "Catálogo" | Exibe as **categorias** como submenu (lista definida pelo cliente); no mobile, as categorias aparecem dentro do menu expandido |
| CTA permanente | Botão "WhatsApp" à direita, visível em todas as páginas |
| Mobile | Menu recolhido em ícone; categorias e CTA acessíveis com o polegar |

### 2.2 Navegação contextual

- **Trilho (breadcrumb)** nas páginas de categoria e de produto: `Início › Catálogo › Categoria › Produto`.
- **Botão "Voltar ao catálogo"** na página de produto.
- **Produtos relacionados** ao final da página de produto (mesma categoria).
- **CTAs de WhatsApp** em três profundidades: cabeçalho (global), cartão de produto (pedido específico) e seções de chamada (atendimento geral).

### 2.3 Rodapé (global)

Repete o mapa do site para quem rola até o fim de qualquer página: links de
navegação, categorias, contato, redes sociais e informações institucionais.
Garante que nenhuma página seja um "beco sem saída".

---

## 3. Como o visitante navega (jornada)

Fluxo comercial definido no Painel Mestre, traduzido para a navegação do site:

| Passo | Ação do visitante | Onde acontece |
|---|---|---|
| 1 | Acessa o site e conhece a marca | Página inicial: banner, apresentação e seção institucional |
| 2 | Explora o catálogo | Menu "Catálogo", vitrine de categorias da home ou grade completa |
| 3 | Seleciona um produto | Cartão de produto → página individual com fotos, preço e descrição |
| 4 | Entra em contato pelo WhatsApp | Botão do produto abre conversa com mensagem pré-preenchida: *"Olá! Tenho interesse em comprar o produto [nome]."* |
| 5 | Finaliza a negociação | Fora do site: pagamento e entrega combinados diretamente com a loja |

**Caminhos alternativos previstos:**
- Visitante que já conhece a marca: home → Sobre → Contato/WhatsApp.
- Visitante vindo de rede social: link direto para uma categoria ou produto → WhatsApp.
- Visitante que chega pelo catálogo: filtro por categoria → produto → WhatsApp.

**Princípio de navegação:** toda página tem (a) um caminho de avanço para o
catálogo/produto, (b) um caminho de saída para o WhatsApp e (c) um caminho de
retorno (menu, trilho ou rodapé). Nenhuma tela depende de cadastro, senha ou
qualquer etapa de pagamento.

---

## 4. Inventário de páginas e blocos de conteúdo

### 4.1 Página inicial (/)

| Bloco (ordem de exibição) | Conteúdo |
|---|---|
| 1 Cabeçalho | Logo, menu, CTA WhatsApp |
| 2 Banner principal | Imagem de clima da marca + título + CTA para catálogo e WhatsApp |
| 3 Apresentação da marca | Texto institucional curto + fotografia + link para /sobre |
| 4 Categorias | Grade de cartões por categoria (nomes definidos pelo cliente) |
| 5 Produtos em destaque | Grade com até 4 destaques escolhidos pela loja |
| 6 Seção institucional | Faixa em marsala com pilares da marca + link para /sobre |
| 7 Chamada WhatsApp | Faixa de conversão com botão de atendimento |
| 8 Redes sociais | Ícones/links dos canais da marca |
| 9 Rodapé | Mapa do site + institucional |

*(Finalidade detalhada de cada bloco: ver anotações do wireframe em `04-wireframe-home.html`.)*

### 4.2 Sobre a marca (/sobre)

Banner de abertura · texto institucional (história e identidade comercial) ·
imagem de apoio · pilares/valores · chamada para catálogo e WhatsApp · rodapé.

### 4.3 Catálogo (/catalogo)

Cabeçalho · título e introdução curta · barra de filtro por categoria ·
grade de produtos (até 15) · chamada WhatsApp · rodapé.

### 4.4 Categoria (/categoria/[slug])

Cabeçalho · título da categoria + descrição curta (se o cliente fornecer) ·
grade filtrada · links para as demais categorias · rodapé.

### 4.5 Produto (/produto/[slug])

Cabeçalho · trilho · galeria de fotografias · nome · preço · descrição ·
características (material, dimensões, variações — quando fornecidas) ·
botão "Pedir pelo WhatsApp" · informações de atendimento (pedido, pagamento e
entrega combinados com a loja) · produtos relacionados · rodapé.

### 4.6 Contato (/contato)

Cabeçalho · botão e número do WhatsApp comercial · redes sociais ·
informações institucionais de contato (se fornecidas) · rodapé.

### 4.7 Rodapé institucional (global)

Coluna de navegação · coluna de categorias · coluna de contato e redes ·
coluna institucional (CNPJ/endereço apenas se o cliente fornecer) · linha final
com copyright e créditos.

---

## 5. Regras arquiteturais desta versão

1. **Sem fluxos de compra no site:** nenhum bloco sugere carrinho, checkout ou pagamento; todo CTA comercial aponta para o WhatsApp.
2. **Catálogo finito e curado:** até 15 produtos; destaques da home são um subconjunto escolhido pela loja, não uma lista automática infinita.
3. **Uma taxonomia só:** categorias únicas, sem subcategorias, sem tags públicas.
4. **Conteúdo comercial sempre rastreável:** nomes, preços e descrições exibidos são exatamente os aprovados pelo cliente; placeholders não vão para o ar.
5. **Estrutura evolutiva:** a arquitetura suporta, em etapa futura e com orçamento próprio, a adição de checkout, estoque e painel administrativo sem refazer páginas existentes.
