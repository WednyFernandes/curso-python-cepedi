# 🎮 Prompt Seccionado - PC Upgrade Assistant

> **Ordem de Prioridade:** Os milestones estão organizados do essencial (MVP) ao avançado (escala)

---

## 📋 MILESTONE 1: Setup Inicial e Estrutura do Projeto

```prompt
Preciso criar um projeto web para análise e sugestão de upgrades de PC para gamers.

**Stack Tecnológica:**
- Frontend: Next.js 14+ com React, TypeScript e Tailwind CSS
- Backend: Next.js API Routes (serverless) ou FastAPI (Python)
- Banco de Dados: Neo4j para grafos de produtos e relações

**Estrutura do Projeto:**
1. Crie a estrutura inicial de pastas para um projeto Next.js
2. Configure TypeScript, ESLint e Prettier
3. Configure Tailwind CSS com tema gaming (cores vibrantes, gradientes)
4. Sugira a melhor arquitetura de pastas (components, lib, api, types, etc)
5. Configure variáveis de ambiente necessárias

**Requisitos específicos:**
- Suporte para PWA (Progressive Web App)
- Dark mode por padrão com tema gaming
- Configuração de SEO otimizada
- Analytics e tracking de conversões (Google Analytics 4)

Me forneça os comandos de instalação e a estrutura completa de arquivos.
```

---

## 📋 MILESTONE 2: Landing Page e UX/UI Design System

```prompt
Crie a landing page do meu app de sugestão de upgrades de PC com design system completo.

**Design System:**
- Paleta de cores: tema gaming com gradientes (roxo, ciano, pink neon)
- Tipografia moderna e jovial (sugestão: Inter ou Poppins)
- Componentes reutilizáveis (Button, Card, Badge, Modal, etc)
- Animações sutis com Framer Motion
- Ícones: Lucide React ou Hero Icons

**Landing Page deve conter:**
1. Hero Section com CTA principal
2. Botão de "Analisar Meu PC" grande e chamativo
3. Seção de benefícios (3-4 cards): velocidade, economia, facilidade
4. Depoimentos/Social Proof (pode ser mock inicial)
5. FAQ acordeão
6. Footer com links importantes:
   - Política de Privacidade
   - Termos de Uso
   - Contato
   - Sobre

**Compliance & Legal (obrigatório):**
- Banner de cookies (LGPD compliant) com opt-in/opt-out claro
- Disclaimer visível: "Recebemos comissões de lojas parceiras. Preços e disponibilidade sujeitos a alteração."
- Link para Política de Privacidade acessível em todas as páginas

**UX Writing para o botão principal (escolha o melhor):**
- "🚀 Descobrir Meu Upgrade Ideal"
- "⚡ Analisar Meu Setup Agora"
- "🎮 Turbinar Meu PC"
- "💎 Ver Upgrades Perfeitos"

Crie componentes React com TypeScript, totalmente responsivos e acessíveis (WCAG 2.1).
```

---

## 📋 MILESTONE 3: Sistema de Análise de Hardware (EXE + API)

```prompt
Preciso criar um sistema para coletar informações de hardware do PC do usuário.

**Parte 1 - Executável Windows (.exe):**
- Desenvolva um script Python que usa bibliotecas como `wmi`, `psutil` ou `py-cpuinfo`
- O script deve coletar: CPU, GPU, RAM (quantidade e velocidade), Placa-mãe, Armazenamento, PSU (se possível)
- Compile para .exe com PyInstaller com assinatura digital
- O .exe deve fazer POST para API do Next.js/FastAPI

**IMPORTANTE - Consentimento e Transparência (LGPD):**
- Antes do .exe executar, mostre modal/tela de consentimento explícito:
  * "Coletaremos apenas dados de hardware do seu PC (CPU, GPU, RAM, etc.)"
  * "Os dados serão usados exclusivamente para sugerir upgrades"
  * "Nenhum dado pessoal ou arquivo será acessado"
  * Botões: "Aceito e Continuar" / "Cancelar"
- Salve timestamp e hash do consentimento junto com os dados
- Opção de recusar sem consequências (apenas não faz a análise)

**Parte 2 - API Endpoint:**
- Crie endpoint `/api/analyze-hardware` (Next.js) ou FastAPI
- Receba os dados do hardware via POST
- Valide e sanitize os dados recebidos
- Salve em cookie seguro (httpOnly, sameSite) ou sessionStorage
- Retorne um token de sessão único
- **Salve log de consentimento:** user_id/session_id, timestamp, consent_given: true, ip_hash (hash SHA256)

**Segurança:**
- Rate limiting (máximo 5 análises por IP/hora)
- Validação de origem do request
- Sanitização de dados
- CORS configurado
- **Retenção de dados:** Deletar dados de hardware após 7 dias (TTL automático)
- **Hash de IP:** Nunca salve IP completo, use hash SHA256 para compliance LGPD

Me forneça o código Python para o .exe e o endpoint da API.
```

---

## 📋 MILESTONE 4: Formulário Complementar (Gabinete e Fonte)

```prompt
Crie o fluxo de formulário multi-step após a análise do hardware.

**Steps do Formulário:**

**Step 1 - Gabinete:**
- Grid de cards com imagens de tipos de gabinete
- Opções: Mini-ITX, Mid Tower, Full Tower, Desktop (ATX)
- Cards visuais com foto, nome e descrição curta
- Seleção única com feedback visual (border highlight + checkmark)

**Step 2 - Fonte (se não detectada):**
- Input numérico com sufixo "W" (Watts)
- Sugestões rápidas em badges: 450W, 550W, 650W, 750W+
- Tooltip: "Verifique a etiqueta da sua fonte"
- Validação: mínimo 300W, máximo 2000W

**UX/UI:**
- Indicador de progresso (progress bar ou steps)
- Botões "Voltar" e "Continuar"
- Validação em tempo real
- Animações de transição entre steps (Framer Motion)
- Loading states em todos os pontos

Crie os componentes React com TypeScript e a lógica de gerenciamento de estado (Zustand ou Context API).
```

---

## 📋 MILESTONE 5: Banco de Dados Neo4j - Modelagem e Relacionamentos

```prompt
Modele o banco de dados de grafos Neo4j para produtos e relacionamentos de upgrade.

**Modelagem de Nós:**

1. **Product (Produto)**
   - Propriedades: id, name, brand, model, category, price, oldPrice, imageUrl, url, store, stock, lastUpdated

2. **Component (Componente genérico)**
   - Propriedades: type (CPU/GPU/RAM/etc), specs (JSON)

3. **UserConfig (Hardware do usuário)**
   - Propriedades: cpu, gpu, ram, mobo, storage, psu

4. **PriceHistory (Histórico de preços)**
   - Propriedades: productId, price, date

**Relacionamentos:**

- `(Product)-[:UPGRADES_TO]->(Product)` - upgrade direto
- `(Product)-[:COMPATIBLE_WITH]->(Product)` - compatibilidade entre peças
- `(Product)-[:ALTERNATIVE_TO]->(Product)` - alternativas similares
- `(Product)-[:REQUIRES]->(Product)` - dependências (ex: CPU requer placa-mãe compatível)
- `(PriceHistory)-[:BELONGS_TO]->(Product)` - histórico de preços

**Queries Cypher:**
- Salvar produto no Neo4j (com verificação de duplicata)
- Buscar upgrades compatíveis baseado no hardware do usuário
- Detectar mudanças de preço
- Remover produtos indisponíveis

**Exemplo de Query para Evitar Duplicatas:**
```cypher
MERGE (p:Product {url: $url, store: $store})
ON CREATE SET 
  p.id = randomUUID(),
  p.name = $name,
  p.brand = $brand,
  p.model = $model,
  p.category = $category,
  p.price = $price,
  p.imageUrl = $imageUrl,
  p.stock = $stock,
  p.createdAt = timestamp(),
  p.lastUpdated = timestamp()
ON MATCH SET
  p.price = $price,
  p.oldPrice = p.price,
  p.stock = $stock,
  p.lastUpdated = timestamp()
RETURN p
```

Forneça o schema Neo4j e as queries Cypher básicas.
```

---

## 📋 MILESTONE 6: Backend - Web Scraping e Catalogação

```prompt
Desenvolva o sistema de web scraping para lojas brasileiras de hardware.

**Arquitetura:**
- Python com Scrapy ou Playwright (JavaScript rendering)
- Schedule com Celery + Redis para jobs diários
- Proxy rotation para evitar bloqueios

**Fluxo de Scraping:**

1. **Descoberta de URLs:**
   - Crawl inicial dos sitemaps das lojas
   - Filtragem de URLs: apenas páginas de produtos
   - Regex patterns para identificar produtos (ex: `/produto/`, `/p/`, `-p-`)

2. **Extração de Dados:**
   - Nome do produto (normalizado)
   - Preço atual
   - Preço anterior (se disponível)
   - Imagem principal (URL)
   - Disponibilidade em estoque
   - Especificações técnicas (parsear do HTML/JSON-LD)
   - URL da página

3. **Normalização:**
   - Categorização automática: CPU, GPU, RAM, SSD, etc.
   - Extração de marca e modelo (regex patterns)
   - Padronização de especificações

4. **Deduplicação:**
   - Crie identificador único: hash(url + store) ou composite key
   - Antes de salvar, verifique se produto já existe no Neo4j
   - Se existir: apenas atualize preço, estoque e lastUpdated
   - Se não existir: crie novo nó
   - Evite duplicatas da mesma URL na mesma loja

**Lojas Brasileiras (sugira os seletores CSS/XPath):**
- Kabum
- Pichau
- Terabyte Shop
- Amazon.br

Crie os spiders Scrapy modulares e o pipeline de processamento de dados.
```

---

## 📋 MILESTONE 7: Lógica de Sugestão de Upgrades (IA/ML)

```prompt
Crie a lógica de sugestão de upgrades de PC de forma simples e funcional.

**Abordagem Sugerida (sem ML complexo):**

**Sistema de Pontuação por Regras:**

1. **Análise de Gargalos:**
   - Compare cada componente com benchmarks conhecidos
   - Identifique o componente mais fraco (bottleneck)
   - Atribua prioridade: Crítico (10), Alto (7), Médio (5), Baixo (3)

2. **Matriz de Compatibilidade:**
   - Socket CPU vs Placa-mãe
   - Wattage GPU vs PSU
   - RAM type vs Placa-mãe
   - Tamanho GPU vs Gabinete

3. **Algoritmo de Sugestão:**
   ```
   PARA CADA categoria prioritária:
     - Busque produtos compatíveis no Neo4j
     - Filtre por disponibilidade e orçamento
     - Remova duplicatas: um produto por (nome + modelo + loja)
     - Calcule score: (performance_gain * 0.4) + (price_value * 0.3) + (compatibility * 0.3)
     - Ordene por score
     - Pegue top 3-5 por categoria
   ```

4. **Otimização de Combos:**
   - Algoritmo guloso para minimizar frete
   - Agrupe produtos por loja
   - Calcule economia total

<!-- **Alternativa Simples com LLM (OpenAI API):**
- Envie specs do usuário + produtos disponíveis para GPT-4
- Prompt engineering: "Você é um especialista em hardware..."
- Parse da resposta estruturada (JSON mode) -->

**Métricas de Performance:**
- FPS estimado em jogos populares (banco de dados de benchmarks)
- Render time em apps (After Effects, Blender, etc)
- Percentual de ganho geral

Implemente a lógica em TypeScript/Python com comentários detalhados.
```

---

## 📋 MILESTONE 8: Sistema de Links de Afiliado

```prompt
Implemente sistema modular de inserção de links de afiliado (referral).

**Configuração por Loja:**
```json
{
  "kabum": {
    "type": "query_param",
    "param": "partner_id",
    "value": "SEU_ID"
  },
  "amazon": {
    "type": "tag",
    "param": "tag",
    "value": "SEU_TAG-20"
  },
  "pichau": {
    "type": "subdomain",
    "prefix": "parceiro",
    "value": "SEU_ID"
  }
}
```

**Transformer de URLs:**
- Função que recebe URL original + loja
- Aplica transformação baseada na config
- Valida URL final (teste de acesso)
- Logging de cliques (analytics)
- **Disclosure de afiliados:** Em cada link de produto, adicione texto:
  * "🔗 Link com comissão - Recebemos uma pequena comissão se você comprar através deste link, sem custo adicional para você."
  * Posição: Abaixo do botão "Ver na Loja" em fonte pequena mas legível

**Tipos de Afiliação:**
1. Query Parameter: `?ref=id`
2. Subdomain: `parceiro.loja.com.br`
3. Path Prefix: `/aff/id/produto`
4. Cookie-based: Redirect via URL intermediária

**Tracking:**
- Gere short URLs únicas (bit.ly API ou próprio)
- Salve cliques no banco (product_id, timestamp, ip_hash)
- Dashboard de conversões

Crie o sistema de URL transformation e tracking básico.
```

---

## 📋 MILESTONE 9: Página de Resultados e Sugestões

```prompt
Desenvolva a página de exibição de sugestões de upgrade com UX premium.

**Layout da Página:**

1. **Header de Resumo:**
   - Hardware atual do usuário (cards compactos)
   - Score atual vs Score projetado (gauge chart animado)
   - Economia total estimada (destaque)

2. **Sugestões Principais (Cards):**
   - Grid responsivo (1-3 colunas)
   - Card de produto com:
     * Imagem do produto (lazy load)
     * Badge "MELHOR CUSTO-BENEFÍCIO" / "MAIS POTENTE"
     * Nome + especificações principais
     * Preço do produto
     * Estimativa de frete: "+ Frete ~R$ 100" (texto simples, sem cálculo)
     * Disclaimer: "⚠️ As sugestões são informativas. Verifique compatibilidade antes de comprar."
     * Botão "Ver na Loja" (abre em nova aba)
     * Ícone da loja
     * Texto pequeno: "🔗 Link com comissão"

3. **Comparador de Performance:**
   - Gráfico de barras: Antes vs Depois
   - Métricas: FPS médio (3 jogos populares), Render time, Score geral
   - Porcentagens de ganho em destaque

4. **Simulador de Jogos:**
   - Cards de jogos populares (Cyberpunk, GTA V, etc)
   - FPS atual vs projetado
   - Settings recomendados (Low/Med/High/Ultra)

5. **Controles:**
   - Slider de orçamento máximo
   - Botão "🎲 Gerar Novas Sugestões" (reroll)
   - Filtros: categoria, marca, loja

**Animações:**
- Skeleton loading durante processamento
- Fade-in dos cards
- CountUp nos números
- Hover effects nos cards

Crie os componentes React com dados mockados inicialmente.
```

---

## 📋 MILESTONE 10: Sistema de Reroll e Ajuste de Orçamento

```prompt
Implemente o sistema de regeneração de sugestões com ajuste de orçamento.

**Funcionalidades:**

1. **Slider de Orçamento:**
   - Range: R$ 500 - R$ 10.000
   - Incremento: R$ 100
   - Display em tempo real com formatação de moeda
   - Debounce de 500ms antes de atualizar

2. **Botão Reroll:**
   - Loading state durante nova busca
   - Animação de "embaralhar" os cards
   - Mantém critérios de compatibilidade
   - Busca alternativas na mesma faixa de performance

3. **Algoritmo de Reroll:**
   ```
   - Pega produtos da mesma categoria
   - Exclui produtos já sugeridos anteriormente (histórico)
   - Aplica mesmo filtro de compatibilidade
   - Remove duplicatas: garanta que não repita produto+loja
   - Prioriza diferença de preço ±15% do sugerido anterior baseado no slider de orçamento
   - Randomiza dentro do score similar (±10%)
   ```

4. **Histórico de Sugestões:**
   - Armazene últimas 3 sugestões em state
   - Botão "Voltar para sugestão anterior"
   - Comparador lado a lado (modal)

5. **Persistência:**
   - Salve preferências em localStorage
   - Restore na próxima visita
   - TTL de 7 dias

Implemente a lógica de reroll e o gerenciamento de estado (Zustand recomendado).
```

---

## 📋 MILESTONE 11: Agendamento e Manutenção do Scraper

```prompt
Configure o sistema de execução diária do scraper e limpeza de dados.

**Infraestrutura:**

1. **Scheduler (escolha uma):**
   - **Opção A:** Celery + Redis + Celery Beat (Python)
   - **Opção B:** Node-cron + Bull Queue (Node.js)
   - **Opção C:** GitHub Actions (serverless, grátis até certo ponto)

2. **Jobs Diários:**
   - **Job 1 (02:00):** Scraping completo de todas as lojas
   - **Job 2 (08:00):** Validação de disponibilidade (quick check)
   - **Job 3 (14:00):** Atualização de preços (produtos em promoção)
   - **Job 4 (20:00):** Limpeza de produtos desatualizados

3. **Limpeza de Dados:**
   ```python
   - DELETE produtos WHERE lastUpdated > 7 dias
   - DELETE produtos WHERE stock = false AND lastChecked > 2 dias
   - ARCHIVE histórico de preços > 90 dias (mover para cold storage)
   ```

4. **Monitoramento:**
   - Logs estruturados (Winston/Pino)
   - Alertas via email/Telegram se scraper falhar
   - Dashboard com métricas: produtos ativos, taxa de sucesso, tempo de execução

5. **Rate Limiting:**
   - Máx 1 request/segundo por loja
   - Rotate user-agents
   - Respeite robots.txt

Crie os scripts de scheduling e o sistema de cleanup.
```

---

## 📋 MILESTONE 12: Notificações de Queda de Preço

```prompt
Implemente sistema de alertas de queda de preço para usuários.

**Fluxo:**

1. **Opção "Avisar quando baixar" em cada produto:**
   - Modal com input de email
   - Checkbox obrigatório: "Aceito receber notificações de preço por email"
   - Link para Política de Privacidade
   - Threshold: "Avisar se cair X% ou R$ Y"
   - **Double opt-in:** Envie email de confirmação antes de ativar alerta

2. **Banco de Dados:**
   - Tabela `price_alerts`: user_email, product_id, threshold_percent, threshold_value, created_at

3. **Detecção de Queda:**
   - No job de scraping, compare preço atual vs último preço
   - Se diferença >= threshold, trigger notificação
   - Mark alert como "notified" para não enviar duplicados

4. **Sistema de Envio:**
   - **Email:** SendGrid/Resend/Amazon SES
   - **Push Notification:** OneSignal (para PWA)
   - Template bonito com:
     * Imagem do produto
     * Preço anterior vs atual (destaque na economia)
     * Botão CTA "Ver Oferta" (com link de afiliado)
     * Disclaimer: "Este é um link de afiliado. Recebemos comissão."
     * Link para "Cancelar alertas" (unsubscribe de 1 clique)

5. **Compliance (LGPD obrigatório):**
   - **Double opt-in:** Envie email "Confirme seu alerta de preço" antes de ativar
   - **Unsubscribe fácil:** Link de cancelamento em TODOS os emails (footer)
   - **Consentimento explícito:** Checkbox + texto claro sobre uso do email
   - **Direito ao esquecimento:** Botão "Excluir meus dados" na página de configurações
   - **Logs de consentimento:** Salve timestamp + IP hash de cada opt-in

Implemente o sistema de alertas com email template incluso.
```

---

## 📋 MILESTONE 13: Dashboard Administrativo

```prompt
Crie um dashboard admin para monitorar e gerenciar o sistema.

**Autenticação:**
- Next-Auth com provider de email/senha
- Apenas 1-2 usuários admin (hardcoded)
- 2FA com TOTP (Google Authenticator)

**Páginas do Dashboard:**

1. **Overview:**
   - Total de produtos no banco
   - Taxa de disponibilidade por loja
   - Produtos em promoção (top 10)
   - Gráfico de preços médios por categoria (últimos 30 dias)
   - Total de análises de hardware (últimos 7 dias)

2. **Produtos:**
   - Tabela paginada com busca e filtros
   - Colunas: imagem, nome, loja, preço, estoque, última atualização
   - Ações: editar, deletar, forçar re-scrape

3. **Scraper Status:**
   - Últimas execuções (sucesso/falha)
   - Logs em tempo real (WebSocket)
   - Botão "Executar Scraper Agora" (manual trigger)
   - Config de schedule (editar horários)

4. **Analytics:**
   - Top produtos mais sugeridos
   - Taxa de clique nos links de afiliado
   - Conversão estimada
   - Mapa de calor de CEPs (onde estão os usuários)

5. **Configurações:**
   - Gerenciar lojas (ativar/desativar)
   - IDs de afiliado por loja
   - Thresholds de compatibilidade
   - Pesos do algoritmo de sugestão

**Stack do Admin:**
- Shadcn/ui + Tailwind
- React Hook Form para formulários
- TanStack Table para tabelas
- Recharts para gráficos

Crie a estrutura do admin com as páginas principais.
```

---

## 📋 MILESTONE 14: Deploy e Infraestrutura

```prompt
Configure o deploy e infraestrutura do projeto.

**Hospedagem:**

**Frontend:**
- **Opção A:** Vercel (recomendado para Next.js)
  - Deploy automático via GitHub
  - Edge Functions para APIs
  - Preview deployments para PRs

- **Opção B:** Netlify
  - Serverless functions
  - Deploy previews

**Backend/Scraper:**
- **Opção A:** Railway/Render (Python)
  - Container Docker
  - Cron jobs nativos
  
- **Opção B:** AWS Lambda + EventBridge
  - Serverless
  - Mais complexo mas escalável

**Banco de Dados:**
- Neo4j AuraDB (managed, free tier disponível)
- Redis Cloud (Upstash) para cache

**Storage:**
- Cloudflare R2 ou AWS S3 para imagens de produtos

**CI/CD:**
- GitHub Actions:
  - Testes automáticos em PRs
  - Deploy automático em merge para main
  - Linting e type-checking

**Configurações:**
- Variáveis de ambiente por ambiente (dev/staging/prod)
- Secrets management (GitHub Secrets ou Doppler)
- CDN para assets estáticos (Cloudflare)

**Monitoramento:**
- Uptime monitoring (UptimeRobot)
- Error tracking (Sentry)
- Logs centralizados (Logtail/Datadog)

Forneça os arquivos de configuração: Dockerfile, docker-compose.yml, .github/workflows/deploy.yml
```

---

## 📋 MILESTONE 15: Testes e Otimização

```prompt
Implemente testes e otimizações de performance no projeto.

**Testes:**

1. **Frontend (Jest + React Testing Library):**
   - Testes unitários: componentes isolados
   - Testes de integração: fluxo completo de análise
   - Testes de snapshot: UI components
   - Coverage mínimo: 70%

2. **Backend (Pytest ou Jest):**
   - Testes de API endpoints
   - Testes de scraper (com fixtures HTML)
   - Testes de lógica de sugestão
   - Testes de compatibilidade

3. **E2E (Playwright):**
   - Fluxo completo: landing → análise → sugestões
   - Teste de formulário multi-step
   - Teste de reroll
   - Teste de links de afiliado (verificar se abrem correto)

**Otimizações:**

1. **Performance:**
   - Lazy loading de imagens (next/image)
   - Code splitting por rota
   - Caching agressivo (SWR/React Query)
   - Compressão de imagens (Sharp)
   - Minificação de bundles

2. **SEO:**
   - Meta tags dinâmicas por página
   - Sitemap.xml gerado automaticamente
   - Robots.txt otimizado
   - Schema.org markup (Product, Organization)
   - Open Graph tags

3. **Acessibilidade:**
   - Lighthouse score > 90
   - Navegação por teclado
   - Screen reader friendly
   - Contraste WCAG AA

4. **Monitoramento:**
   - Sentry para error tracking
   - Vercel Analytics ou Google Analytics 4
   - Core Web Vitals tracking

Configure os testes básicos e otimizações essenciais.
```

---

## 🎯 MILESTONE 16: Polish e Launch

```prompt
Finalize o projeto para lançamento público.

**Checklist de Lançamento:**

**Legal/Compliance (PRIORIDADE MÁXIMA):**
- [ ] **Política de Privacidade (LGPD compliant):**
  * Explicar quais dados coletamos (hardware, email, cookies)
  * Finalidade: sugestões de upgrade, alertas de preço
  * Base legal: consentimento explícito
  * Retenção: 7 dias (hardware), até cancelamento (emails)
  * Direitos do titular: acesso, correção, exclusão, portabilidade
  * Contato do responsável: email visível
  * Template: use gerador LGPD ou advogado especializado
  
- [ ] **Termos de Uso:**
  * Isenção de responsabilidade: "Sugestões são informativas, não garantimos compatibilidade"
  * Limitação de responsabilidade por compras
  * Uso aceitável do serviço
  * Propriedade intelectual
  
- [ ] **Cookie Consent Banner:**
  * Banner visível ao entrar no site
  * Opções: "Aceitar Todos" / "Apenas Essenciais" / "Configurar"
  * Salvar preferência em localStorage
  * Documentar cookies usados (Analytics, sessão, preferências)
  
- [ ] **Affiliate Disclosure:**
  * Página dedicada "/afiliados" explicando modelo de receita
  * Texto em cada produto: "Recebemos comissão se você comprar"
  * Compliance com termos de cada loja (Kabum, Amazon, etc)
  
- [ ] **Página "Sobre":**
  * Quem somos, missão, contato
  
- [ ] **Contato/Suporte:**
  * Email visível para LGPD: privacidade@seudominio.com
  * Formulário de contato

**Marketing:**
- [ ] Logo profissional (Figma)
- [ ] Favicon e app icons (PWA)
- [ ] Open Graph images para redes sociais
- [ ] Vídeo demo (30s) para landing page
- [ ] Screenshots para compartilhamento

**Documentação:**
- [ ] README.md completo
- [ ] Documentação de API
- [ ] Changelog
- [ ] **Documentação de Compliance:**
  * Processo de tratamento de dados (LGPD)
  * Logs de consentimento e exclusões
  * Procedimento para atender requisições de dados

**Performance Final:**
- [ ] Lighthouse score > 90 (todas as métricas)
- [ ] Testes de carga (Loader.io)
- [ ] Otimização de banco de dados (índices)
- [ ] Rate limiting em produção
- [ ] **Testes de compliance:**
  * Testar fluxo completo de opt-in/opt-out
  * Verificar se dados são deletados após TTL
  * Validar que unsubscribe funciona em 1 clique

**Lançamento Soft:**
1. Beta fechado: 50 usuários selecionados
2. Coletar feedback e bugs
3. Iterar por 2 semanas
4. Lançamento público

**Growth Hacks:**
- Referral program: "Indique e ganhe"
- Gamificação: badges, streak de análises
- Blog com guias de hardware
- Newsletter semanal com promoções

Crie os documentos legais, página About e checklist final.
```

---

## 📚 Recursos Adicionais Sugeridos

### Bibliotecas Úteis

**Frontend:**
- `chart.js` / `recharts` - Gráficos e visualizações
- `framer-motion` - Animações fluidas
- `zustand` - Gerenciamento de estado
- `zod` - Validação de schemas
- `react-hook-form` - Formulários
- `tailwindcss` - Estilização
- `lucide-react` - Ícones modernos
- `next-themes` - Dark mode

**Backend:**
- `scrapy` - Framework de scraping (Python)
- `playwright` - Browser automation
- `celery` - Task queue
- `redis` - Cache e queue
- `fastapi` - API framework (Python)
- `pydantic` - Validação de dados

**Scraping:**
- `beautifulsoup4` - Parse HTML
- `selenium` - Browser automation
- `requests-html` - HTTP com JS rendering

### APIs Recomendadas

- **ViaCEP** - Busca de endereço por CEP (grátis)
- **OpenAI API** - LLM para sugestões inteligentes (pago)
- **SendGrid** / **Resend** - Envio de emails transacionais
- **Bit.ly API** - Encurtador de URLs
- **Google Analytics 4** - Analytics
- **Sentry** - Error tracking

### Bancos de Benchmark

- **UserBenchmark** - Comparação de hardware (scraping)
- **TechPowerUp GPU Database** - Especificações de GPUs
- **CPU-Monkey** - Benchmarks de CPUs
- **PassMark** - Scores de performance

### Ferramentas de Desenvolvimento

- **VS Code** - IDE recomendada
- **Postman** / **Insomnia** - Testes de API
- **Neo4j Browser** - Visualização do grafo
- **Redis Commander** - GUI para Redis
- **Docker Desktop** - Containers locais

### Recursos de Design

- **Figma** - Design de interfaces
- **Unsplash** / **Pexels** - Imagens stock
- **Coolors** - Paletas de cores
- **Google Fonts** - Tipografia
- **Heroicons** - Ícones SVG

---

## 🚀 Roadmap de Desenvolvimento Estimado

| Milestone | Duração Estimada | Complexidade | Fase |
|-----------|------------------|--------------|------|
| 1 - Setup | 1-2 dias | ⭐ Baixa | MVP |
| 2 - Landing Page | 3-5 dias | ⭐⭐ Média | MVP |
| 3 - Hardware Analyzer | 4-7 dias | ⭐⭐⭐ Alta | MVP |
| 4 - Formulário | 2-3 dias | ⭐⭐ Média | MVP |
| 5 - Neo4j Modelagem | 3-5 dias | ⭐⭐⭐ Alta | MVP |
| 6 - Web Scraping | 7-14 dias | ⭐⭐⭐⭐ Muito Alta | MVP |
| 7 - Lógica Sugestões | 5-10 dias | ⭐⭐⭐⭐ Muito Alta | MVP |
| 8 - Links Afiliado | 2-3 dias | ⭐⭐ Média | MVP |
| 9 - Página Resultados | 4-6 dias | ⭐⭐⭐ Alta | MVP |
| 10 - Sistema Reroll | 2-4 dias | ⭐⭐ Média | Otimização |
| 11 - Scheduler | 3-5 dias | ⭐⭐⭐ Alta | Otimização |
| 12 - Notificações | 3-5 dias | ⭐⭐⭐ Alta | Otimização |
| 13 - Dashboard Admin | 5-7 dias | ⭐⭐⭐ Alta | Escala |
| 14 - Deploy | 2-4 dias | ⭐⭐ Média | Escala |
| 15 - Testes | 5-7 dias | ⭐⭐⭐ Alta | Escala |
| 16 - Polish | 3-5 dias | ⭐⭐ Média | Escala |

**Total Estimado:** 55-90 dias (2-3 meses de desenvolvimento full-time)

**Fases:**
- **MVP (Milestones 1-9):** ~35-60 dias - Funcionalidade básica completa
- **Otimização (Milestones 10-12):** ~8-14 dias - Melhorias de UX e backend
- **Escala (Milestones 13-16):** ~15-24 dias - Produção e monetização

---

## 💡 Dicas Importantes

### Ordem de Prioridade para Desenvolvimento

**🎯 Fase 1: MVP (Milestones 1-9) - ESSENCIAL**
Foco em entregar a funcionalidade core do produto. Ao final desta fase, você terá um produto funcional que pode começar a gerar receita através dos links de afiliado.

**⚡ Fase 2: Otimização (Milestones 10-12) - IMPORTANTE**
Melhorias que aumentam retenção e conversão. Implementar após validar o MVP com usuários reais.

**🚀 Fase 3: Escala (Milestones 13-16) - DESEJÁVEL**
Ferramentas para gestão e crescimento. Implementar quando já houver tração e demanda.

---

### Possíveis Desafios

⚠️ **Web Scraping:**
- Lojas podem bloquear bots (use proxies e rate limiting)
- Estrutura HTML pode mudar (monitore e ajuste)
- CAPTCHAs (considere serviços de resolução)
- **Deduplicação crítica:** Mesma URL + Loja = mesmo produto (não duplicar!)
- **Compliance:** Respeite robots.txt, use rate limiting (1 req/s), identifique seu bot no User-Agent
- **Propriedade intelectual:** Salve apenas dados factuais (preço, specs), não copie textos/imagens marketing
- **Documentação:** Mantenha log de sources (URL + timestamp + hash) para auditoria

⚠️ **Estimativa de Frete:**
- Utilizar valor aproximado fixo ("~R$ 100") simplifica muito o desenvolvimento
- Pode ajustar valores por região posteriormente se necessário
- Foco principal: qualidade da sugestão de hardware, não precisão do frete

⚠️ **Compatibilidade de Hardware:**
- Banco de dados de compatibilidade é extenso
- Necessita validação constante com novos lançamentos

⚠️ **Legal e Compliance (CRÍTICO):**
- **LGPD obrigatória:** Política de Privacidade + Termos + Consentimentos explícitos
- **Disclaimers visíveis:** "Sugestões informativas, verifique compatibilidade"
- **Afiliados:** Disclosure claro em todos os links
- **Retenção de dados:** TTL de 7 dias para hardware, logs de consentimento
- **Direito ao esquecimento:** Implementar fluxo de exclusão de dados
- **Recomendação:** Contratar advogado especialista em LGPD antes do lançamento público

### Monetização

💰 **Fontes de Receita:**
1. Comissões de afiliado (principal)
2. Anúncios discretos (Google AdSense)
3. Plano premium (alertas ilimitados, histórico)
4. Partnerships com lojas (destaque pago)

---

**Suporte e Comunidade:**

Considere criar:
- Discord server para early adopters
- Blog com artigos técnicos
- YouTube channel com tutoriais

---

**Boa sorte com o projeto! 🚀🎮**

*"O melhor momento para começar era ontem. O segundo melhor momento é agora."*
