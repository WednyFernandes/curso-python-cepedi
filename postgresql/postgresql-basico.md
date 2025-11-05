## PostgreSQL no Windows: Guia prático e uso com pgAdmin

Este guia foi simplificado para uso exclusivo no Windows (PowerShell). Ele cobre:
- Instalação do PostgreSQL no Windows (instalador e Chocolatey)
- Como iniciar/parar o serviço e conectar com `psql`
- Comandos `psql` úteis e criação de usuários/bancos
- Backup/restore com `pg_dump`/`pg_restore`
- Instalação e uso básico do pgAdmin (GUI)

---

## 1. Objetivo

Ter um passo a passo direto para configurar e operar um servidor PostgreSQL em máquinas Windows, além de acessar e administrar via pgAdmin (interface gráfica).

## 2. Pré-requisitos

- Acesso de administrador para instalar programas
- PowerShell para executar comandos
- Firewall/antivírus: permitir a porta 5432 quando necessário

## 3. Instalação no Windows

Opção A — Instalador oficial:

1. Baixe o instalador em https://www.postgresql.org/download/windows/
2. Execute o instalador e siga os passos. Escolha senha para o usuário `postgres` quando solicitado.
3. No final, o serviço do PostgreSQL será criado (ex.: `postgresql-x64-15`) e normalmente iniciado.

Opção B — Chocolatey (PowerShell como Administrador):

```powershell
choco install postgresql -y
# Após instalar, abra novo PowerShell e verifique psql
psql --version
```

Após a instalação, anote a senha do usuário `postgres` (vai ser usada para psql e pgAdmin).

## 4. Iniciar / Parar / Status (PowerShell)

Substitua `postgresql-x64-15` pelo nome do serviço instalado (verifique no Services.msc se necessário).

```powershell
# Iniciar
Start-Service postgresql-x64-15
# Parar
Stop-Service postgresql-x64-15
# Status
Get-Service postgresql-x64-15 | Format-List Status,DisplayName,Name
```

## 5. Acessando com psql (PowerShell)

Conectar como `postgres` no host local:

```powershell
psql -U postgres -h localhost -p 5432
```

Usando string de conexão (útil para scripts):

```powershell
psql "postgresql://postgres:SuaSenha@localhost:5432/postgres"
```

Se o comando `psql` não for encontrado, adicione o binário do PostgreSQL ao PATH (normalmente em C:\Program Files\PostgreSQL\{versão}\bin).

## 6. Criar usuário e banco (psql)

No `psql` (conectado como `postgres`):

```sql
CREATE USER meuusuario WITH PASSWORD 's3nh4f0rte';
CREATE DATABASE meusdados OWNER meuusuario;
GRANT ALL PRIVILEGES ON DATABASE meusdados TO meuusuario;
```

Evite usar `SUPERUSER` em contas de aplicação; use privilégios mínimos.

## 7. Meta-comandos `psql` úteis

- `\l` — listar bancos
- `\c nomedb` — conectar em `nomedb`
- `\dt` — listar tabelas do schema atual
- `\d tabela` — ver estrutura da tabela
- `\du` — listar roles/usuários
- `\q` — sair

Exemplo rápido (dentro do psql):

```sql
CREATE TABLE pessoa (id SERIAL PRIMARY KEY, nome TEXT, idade INT);
INSERT INTO pessoa (nome, idade) VALUES ('Ana', 30), ('Bruno', 25);
SELECT * FROM pessoa;
```

## 8. Backup e restore (linha de comando)

Dump em formato custom (recomendado):

```powershell
pg_dump -U meuusuario -h localhost -p 5432 -Fc -f C:\backups\meudb.dump nomedb
```

Restaurar com `pg_restore`:

```powershell
pg_restore -U meuusuario -h localhost -p 5432 -d nomedb C:\backups\meudb.dump
```

Dump completo (todos os bancos):

```powershell
pg_dumpall -U postgres > C:\backups\todos_bancos.sql
```

E restaurar com `psql`:

```powershell
psql -U postgres -f C:\backups\todos_bancos.sql
```

## 9. pgAdmin: instalação e uso básico

pgAdmin é a interface gráfica oficial para administração PostgreSQL. Com ela você pode conectar servidores, criar DBs/tabelas, executar queries, e fazer export/import de dados.

Instalação (Windows):

1. Baixe o instalador em https://www.pgadmin.org/download/pgadmin-4-windows/
2. Execute o instalador e siga os passos.

Abrir e conectar ao servidor local:

1. Abra o pgAdmin (menu Iniciar > pgAdmin 4).
2. No painel da esquerda, clique com o botão direito em "Servers" → "Create" → "Server...".
3. Na aba "General", dê um nome (ex.: Local Postgres).
4. Na aba "Connection":
	- Host name/address: localhost
	- Port: 5432
	- Maintenance database: postgres
	- Username: postgres
	- Password: (a senha que você definiu)
5. Salve e conecte.

Principais áreas do pgAdmin:
- Browser (esquerda): servidores, bancos, schemas, tabelas
- Query Tool: editor para executar SQL e visualizar resultados
- Object Dialogs: para criar/alterar DBs, roles e objetos

Backup/Restore pelo pgAdmin:

- Backup: clique com o botão direito no banco → Backup... → escolha formato (custom recomendado) → execute.
- Restore: clique no banco de destino → Restore... → escolha o arquivo `.dump` e execute.

Exportar dados (CSV) via Query Tool:

1. Abra Query Tool em um DB
2. Execute sua consulta
3. Use o botão de export (disk icon) para salvar resultados em CSV/Excel

Gerenciar roles/usuários:

- No Browser: Login/Group Roles → clique direito → Create → role
- Defina permissões e itens de membership via abas

Dica: pgAdmin facilita visualmente operações de backup/restore e inspeção de objetos; ainda use `pg_dump`/`pg_restore` para automação/rotinas.

## 10. Segurança e boas práticas (Windows)

- Não exponha o PostgreSQL para a internet sem VPN/firewall e sem restringir `pg_hba.conf`.
- Use senhas fortes e roles de menor privilégio para aplicações.
- Agende backups automáticos (Task Scheduler + scripts PowerShell que chamam `pg_dump`).

Exemplo simples de script PowerShell de backup (uma linha):

```powershell
pg_dump -U postgres -h localhost -p 5432 -Fc -f "C:\backups\meudb_$(Get-Date -Format yyyyMMdd).dump" nomedb
```

## 11. Referências rápidas

- PostgreSQL docs: https://www.postgresql.org/docs/
- pgAdmin docs: https://www.pgadmin.org/docs/

---

Se quiser que eu gere:
- um `script` PowerShell completo para instalação e backup automático;
- um passo-a-passo com screenshots para configurar o pgAdmin;
- um `docker-compose.yml` para ambiente de desenvolvimento (opcional).

Arquivo atualizado: `postgresql/postgresql-basico.md`
