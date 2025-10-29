# Aprendizado: Comandos Git — Guia rápido

Este arquivo resume os comandos Git mais úteis para quem está aprendendo. Inclui explicações curtas e exemplos práticos em linha de comando (PowerShell).

## 1. Configuração inicial
- git config --global user.name "Seu Nome"
- git config --global user.email "seu@exemplo.com"
- git config --global core.editor "code --wait"

Esses comandos definem identidade e editor padrão.

## 2. Criar e clonar repositórios
- git init
  - Inicia um repositório Git local na pasta atual.
- git clone <url>
  - Clona um repositório remoto para uma nova pasta local.

Exemplo:
- git clone https://github.com/usuario/projeto.git

## 3. Fluxo básico (adição, commit, histórico)
- git status
  - Mostra arquivos modificados/pendentes.
- git add <arquivo|.>
  - Adiciona arquivos à área de stage.
- git commit -m "Mensagem explicativa"
  - Salva um snapshot com uma mensagem.
- git log --oneline --graph --decorate
  - Histórico compacto e visual.
- git diff
  - Mostra diferenças entre working tree e index ou commits.

Exemplo de fluxo:
- git add .
- git commit -m "Implementa feature X"

## 4. Branches (ramificações)
- git branch
  - Lista branches locais.
- git branch nome-da-branch
  - Cria uma nova branch.
- git checkout nome-da-branch
  - Muda para outra branch.
- git checkout -b nova-branch
  - Cria e troca para a nova branch.
- git merge nome-da-branch
  - Junta outra branch na branch atual.
- git rebase master
  - Reaplica commits em cima de outra base (cuidado em branches compartilhadas).

## 5. Trabalhando com remotes (GitHub/GitLab)
- git remote -v
  - Lista remotes configurados.
- git remote add origin <url>
  - Adiciona um remote chamado `origin`.
- git fetch
  - Baixa atualizações sem mesclar automaticamente.
- git pull
  - Faz fetch + merge (ou fetch + rebase se configurado).
- git push origin nome-da-branch
  - Envia commits locais para o remoto.
- git push -u origin nome-da-branch
  - Define upstream para facilitar futuros `git push`/`git pull`.

## 6. Recuperação e correções
- git restore <arquivo>
  - Restaura arquivo para última versão do commit (equivalente a checkout para arquivos).
- git restore --staged <arquivo>
  - Remove arquivo do stage (mantém alterações no working tree).
- git reset --soft HEAD~1
  - Remove último commit, mantendo alterações staged.
- git reset --hard HEAD~1
  - Remove último commit e descarta alterações (perigoso).
- git revert <commit>
  - Cria um novo commit que desfaz um commit antigo (seguro para histórico compartilhado).

## 7. Stash (guardar mudanças temporariamente)
- git stash
  - Salva mudanças não commitadas e limpa a working tree.
- git stash pop
  - Reaplica o stash e remove da lista.
- git stash list
  - Lista stashes salvos.

## 8. Tags
- git tag v1.0.0
  - Marca um commit com uma tag leve.
- git tag -a v1.0.0 -m "Release 1.0.0"
  - Tag anotada com mensagem.
- git push origin v1.0.0
  - Envia tag para o remoto.

## 9. .gitignore
Crie um arquivo `.gitignore` para listar padrões de arquivos a ignorar (ex.: `*.pyc`, `venv/`, `.env`).

## 10. Boas práticas e dicas
- Mensagens de commit claras: explique o porquê, não só o que.
- Use branches para features e correções; mantenha `main`/`master` estável.
- Faça rebase interativo apenas em commits locais (não faça rebase em branch compartilhada sem coordenar).
- Use `git pull --rebase` para um histórico mais linear quando apropriado.
- Antes de `push`, sempre `git status` e `git log --oneline -n 5`.

## 11. Exemplos práticos rápidos
- Criar repositório local e enviar para GitHub (resumido):
  1. git init
  2. git add .
  3. git commit -m "Primeiro commit"
  4. git remote add origin https://github.com/usuario/repo.git
  5. git branch -M main
  6. git push -u origin main

- Recuperar de um erro simples (commit errado):
  - git revert <hash>

## 12. Links e recursos úteis
- Documentação oficial: https://git-scm.com/doc
- Pro Git (livro gratuito): https://git-scm.com/book/pt-br

---
Se quiser, eu posso:
- criar também um `.gitignore` inicial para projetos Python,
- inicializar um repositório Git local e fazer o primeiro commit,
- ou preparar instruções para criar um repositório remoto no GitHub e dar push.

Escolha o próximo passo que prefere.