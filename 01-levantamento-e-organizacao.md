# 01 — Levantamento e Organização das Informações

**Projeto:** Site Alma Cigana — joias e acessórios
**Etapa:** Ciclo 0 — Planejamento e prototipação
**Fonte primária:** Painel Mestre do Projeto, v2.0 (02/11/2026)
**Regra observada:** nenhuma informação comercial foi inventada. Cada item abaixo está classificado como:

- ✅ **DEFINIDO** — informado pelo cliente / registrado no Painel Mestre;
- 🕓 **PENDENTE** — ainda não fornecido, depende do cliente (detalhado em `06-materiais-pendentes-cliente.md`);
- 🛠 **DEFINIÇÃO TÉCNICA** — decisão desta etapa de planejamento (proposta para aprovação).

---

## 1. Informações institucionais

| Item | Situação | Conteúdo disponível |
|---|---|---|
| Nome da marca | ✅ DEFINIDO | Alma Cigana |
| Ramo de atuação | ✅ DEFINIDO | Joias e acessórios |
| Modelo comercial do site | ✅ DEFINIDO | Site institucional + catálogo digital + encaminhamento de pedidos pelo WhatsApp. **Não é e-commerce**: sem carrinho, sem checkout, sem pagamento integrado nesta versão |
| Limites comerciais da versão | ✅ DEFINIDO | Até 15 produtos inicialmente; quantidade maior entra em negociação de valor e prazo. Publicação definitiva após quitação |
| Posicionamento estético | ✅ DEFINIDO | Sofisticado, minimalista, editorial e comercial, com foco nas fotografias dos produtos |
| História / texto institucional ("Sobre a marca") | 🕓 PENDENTE | Cliente fornecerá o texto aprovado. No protótipo, o espaço está reservado como placeholder |
| Razão social / CNPJ / endereço / horários | 🕓 PENDENTE | Não informados. Só entram no rodapé quando fornecidos |
| Políticas da loja (trocas, devoluções, cuidados, entrega) | 🕓 PENDENTE | A aprovação de textos e políticas é responsabilidade do cliente, conforme o painel |
| Assinatura verbal / slogan | 🕓 PENDENTE | Não informado; não foi criado nenhum slogan nesta etapa |

**Observação de análise (não é informação comercial):** o arquivo de logotipo presente no Painel Mestre traz o descritivo "CARTOMANCIA" sob o nome da marca, enquanto o escopo do site trata de joias e acessórios. É preciso **confirmar com o cliente qual versão do logotipo** será usada no site (ver `06-materiais-pendentes-cliente.md`, item 1).

---

## 2. Identidade visual

| Item | Situação | Conteúdo disponível |
|---|---|---|
| Cor principal | ✅ DEFINIDO | Marsala `#7A1220` — base de seções, botões, títulos e destaques |
| Marsala profundo | ✅ DEFINIDO | `#4A0710` — variações de profundidade (fundos de seções escuras, hovers) |
| Dourado | ✅ DEFINIDO | `#C6A15B` — acabamento: filetes, ornamentos, realces. **Nunca fundo dominante** |
| Dourado claro | ✅ DEFINIDO | `#EBD9A9` — apoios do dourado (textos sobre marsala, detalhes) |
| Cores de apoio | ✅ DEFINIDO | Branco e creme, apenas como apoio |
| Composição do logotipo | ✅ DEFINIDO | Lua, estrela e rosa em dourado sobre marsala profundo |
| Arquivo do logotipo | 🟡 PARCIAL | Existe uma versão JPEG (2100×1500 px) extraída do Painel Mestre, suficiente para prototipação. O **arquivo original em alta resolução / vetor** segue pendente para o site final |
| Fotografia de referência do cliente | 🟡 PARCIAL | O painel contém 1 fotografia de referência (joias douradas sobre tecido creme, luz quente) — usada como indicação de clima fotográfico |
| Tipografia | 🛠 DEFINIÇÃO TÉCNICA | Não definida pelo cliente. Esta etapa recomenda par serifada editorial + sans-serif legível (detalhes em `03-guia-visual.md`) |
| Referências visuais adicionais | 🕓 PENDENTE | Cliente pode enviar referências de sites/estilos que admire |

---

## 3. Categorias de produtos

| Item | Situação | Conteúdo disponível |
|---|---|---|
| Lista de categorias | 🕓 PENDENTE | A definir pelo cliente ("organização por tipo de acessório", conforme o painel). Nenhuma categoria foi inventada |
| Quantidade de categorias | 🕓 PENDENTE | Recomenda-se partir de 3 a 5 categorias iniciais para não fragmentar o catálogo de até 15 produtos (sugestão técnica, sujeita a aprovação) |
| Nomes e ordem de exibição | 🕓 PENDENTE | Cliente define nomes e prioridade |
| Estrutura de navegação por categoria | 🛠 DEFINIÇÃO TÉCNICA | Página de categoria + filtro no catálogo (ver `02-arquitetura-do-site.md`) |

---

## 4. Dados necessários para cada produto

Campos que cada produto precisará ter (base: Painel Mestre, seção 04):

| Campo | Situação | Observação |
|---|---|---|
| Nome do produto | 🕓 PENDENTE | Fornecido pelo cliente |
| Fotografia(s) | 🕓 PENDENTE | Sem compressão de aplicativo de mensagem; boa iluminação e qualidade |
| Preço | 🕓 PENDENTE | Informação comercial de responsabilidade do cliente |
| Descrição | 🕓 PENDENTE | Texto aprovado pelo cliente |
| Categoria | 🕓 PENDENTE | Vínculo com a lista de categorias |
| Material / composição | 🕓 PENDENTE (quando aplicável) | Importante para joias e acessórios |
| Dimensões e tamanhos | 🕓 PENDENTE (quando aplicável) | Idem |
| Cores / variações | 🕓 PENDENTE (quando aplicável) | Idem |
| Cuidados de conservação | 🕓 PENDENTE (quando aplicável) | Idem |
| Disponibilidade / estoque | 🛠 DEFINIÇÃO TÉCNICA | **Não haverá controle de estoque automatizado** nesta versão; qualquer indicação de disponibilidade será manual e combinada |
| Código / SKU interno | 🕓 PENDENTE (opcional) | Útil para o atendimento no WhatsApp, se a loja já usar |

**Quantidade:** até 15 produtos nesta versão (✅ DEFINIDO no painel). A quantidade definitiva é item em aberto do painel.

---

## 5. Informações de contato

| Item | Situação | Conteúdo disponível |
|---|---|---|
| WhatsApp comercial | 🕓 PENDENTE | Canal central de pedidos. O painel traz apenas um **link de exemplo** (`https://wa.me/5511999999999?text=…`), explicitamente marcado como substituto futuro do número real |
| Formato da mensagem de pedido | ✅ DEFINIDO | Mensagem pré-preenchida com o nome do produto (ex.: "Olá! Tenho interesse em comprar o produto [nome].") |
| E-mail comercial | 🕓 PENDENTE | Não informado |
| Endereço físico / atendimento | 🕓 PENDENTE | Não informado; não será exibido sem confirmação |
| Horários de atendimento | 🕓 PENDENTE | Não informado |

---

## 6. Redes sociais

| Item | Situação | Conteúdo disponível |
|---|---|---|
| Canais existentes (Instagram, TikTok, etc.) | 🕓 PENDENTE | Cliente informará quais canais a marca mantém |
| Usuários / links (handles) | 🕓 PENDENTE | Nenhum handle foi presumido no protótipo |
| Onde aparecem no site | 🛠 DEFINIÇÃO TÉCNICA | Seção própria na home + rodapé + página de contato (ver arquitetura) |

---

## 7. Requisitos técnicos

### 7.1 Requisitos confirmados no Painel Mestre

| Requisito | Situação |
|---|---|
| Layout responsivo (celular e computador) | ✅ DEFINIDO |
| Navegação entre páginas e categorias | ✅ DEFINIDO |
| Botões de pedido pelo WhatsApp com mensagem pré-preenchida | ✅ DEFINIDO |
| Links para redes sociais | ✅ DEFINIDO |
| Catálogo com até 15 produtos e organização visual/comercial | ✅ DEFINIDO |
| Páginas: inicial, sobre, catálogo, categorias, produto, contato, rodapé | ✅ DEFINIDO |
| HTTPS na publicação | ✅ DEFINIDO (critério de qualidade) |
| Desempenho com carregamento razoável | ✅ DEFINIDO (critério de qualidade) |
| Conteúdo comercial correto (conferência final do cliente) | ✅ DEFINIDO |

### 7.2 Fora do escopo desta versão (✅ DEFINIDO no painel)

Carrinho de compras · checkout no site · pagamento integrado · cálculo automático de frete · controle automatizado de estoque · painel administrativo personalizado · aplicativo próprio · cadastro ilimitado de produtos · integrações e automações personalizadas · manutenção contínua após a entrega.

### 7.3 Definições técnicas propostas nesta etapa (🛠 sujeitas a aprovação)

| Item | Proposta |
|---|---|
| Estrutura de URLs | Curtas e legíveis: `/`, `/sobre`, `/catalogo`, `/categoria/[slug]`, `/produto/[slug]`, `/contato` |
| Padrão de links de pedido | `https://wa.me/[número]?text=[mensagem com nome do produto]`, número a substituir pelo real |
| Fontes web | Fontes abertas de uso comercial, com fallbacks seguros (ver guia visual) |
| Imagens | Otimizadas para web no Ciclo 1/2; proporções padronizadas (ver guia visual) |
| Acessibilidade básica | Contraste suficiente entre texto e fundo, alvos de toque ≥ 44 px, textos alternativos nas fotos |
| Domínio e hospedagem | Responsável **ainda não definido** no painel — item em aberto a confirmar |

### 7.4 Critérios de qualidade que o site deverá atender (✅ DEFINIDO no painel)

Responsividade (celular e computador) · navegação (menus, links, categorias) · catálogo (produtos e informações) · fotografias (qualidade e carregamento) · WhatsApp (número e mensagens) · redes sociais (destinos corretos) · design (consistência visual) · desempenho · segurança (HTTPS) · conteúdo (informações comerciais corretas).

---

## 8. Síntese do que existe × do que falta

**Existe hoje (base sólida para prototipar):** nome e ramo da marca · modelo comercial catálogo+WhatsApp · limites de escopo e de quantidade · identidade cromática completa · composição do logotipo · estrutura de páginas e funcionalidades · fluxo comercial do visitante · critérios de qualidade · uma fotografia de referência e uma versão JPEG do logotipo.

**Falta para desenvolver (depende do cliente):** texto institucional · logotipo em arquivo original · fotografias reais · produtos completos (nome, preço, descrição, categoria, características) · categorias definidas · WhatsApp comercial · redes sociais · políticas e informações institucionais do rodapé · confirmações administrativas (domínio/hospedagem, datas, quantidade definitiva).

O detalhamento operacional do que falta está em **`06-materiais-pendentes-cliente.md`**.
