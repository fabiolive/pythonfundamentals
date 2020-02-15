INSERT INTO scripts(nome, conteudo) VALUES ('HELLO.PY','print("script de teste")');developer@developer:~$ sudo su -
[sudo] senha para developer: 
root@developer:~# su - postgres
postgres@developer:~$ psql
psql: não pôde conectar ao servidor: Arquivo ou diretório inexistente
	O servidor está executando localmente e aceitando
	conexões no soquete de domínio Unix "/var/run/postgresql/.s.PGSQL.5432"?
postgres@developer:~$ systemctl start postgresqltgresql
Failed to start postgresqltgresql.service: Unit postgresqltgresql.service not found.
postgres@developer:~$ psql
psql: não pôde conectar ao servidor: Arquivo ou diretório inexistente
	O servidor está executando localmente e aceitando
	conexões no soquete de domínio Unix "/var/run/postgresql/.s.PGSQL.5432"?
postgres@developer:~$ systemctl start postgresqltgresql
Failed to start postgresqltgresql.service: Unit postgresqltgresql.service not found.
postgres@developer:~$ systemctl start postgresql
pspostgres@developer:~$ psql
psql (11.1 (Ubuntu 11.1-3.pgdg18.04+1), servidor 10.6 (Ubuntu 10.6-1.pgdg18.04+1))
Digite "help" para ajuda.

postgres=# 
postgres=# 
postgres=# 
postgres=# 
postgres=# 
postgres=# 
postgres=# 
postgres=# 
postgres=# 
postgres=# CREATE USER admin PASSWORD '4linux';
CREATE ROLE
postgres=# CREATE database projeto OWNER admin;
CREATE DATABASE
postgres=# \q
postgres@developer:~$ psql -h localhost -U admin projeto
Senha para usuário admin: 
psql (11.1 (Ubuntu 11.1-3.pgdg18.04+1), servidor 10.6 (Ubuntu 10.6-1.pgdg18.04+1))
conexão SSL (protocolo: TLSv1.3, cifra: TLS_AES_256_GCM_SHA384, bits: 256, compressão: desabilitado)
Digite "help" para ajuda.

projeto=> \dt
Did not find any relations.
projeto=> CREATE TABLE scripts(id  serial, nome varchar(50),conteudo TEXT);
CREATE TABLE
projeto=> \dt
         Lista de relações
 Esquema |  Nome   |  Tipo  | Dono  
---------+---------+--------+-------
 public  | scripts | tabela | admin
(1 registro)

projeto=> \dt
         Lista de relações
 Esquema |  Nome   |  Tipo  | Dono  
---------+---------+--------+-------
 public  | scripts | tabela | admin
(1 registro)

projeto=> \d scripst
Não encontrou nenhuma relação chamada "scripst".
projeto=> \d scripts
projeto=> 
projeto=> 
projeto=> 
projeto=> select * from scripts;
 id | nome | conteudo 
----+------+----------
(0 registro)

projeto=> select columns from scripts;
ERROR:  column "columns" does not exist
LINHA 1: select columns from scripts;
                ^
projeto=> show columns from scripts;
ERROR:  syntax error at or near "from"             "'                                                                   "'
projeto"> 
projeto">         ^                                                        p"'                                                                  i
projeto"> INSERTO INTO scripts(nome, contedudo) values ('hello.py','print("scr"' 
projeto"> 
projeto"> 
projeto"> 
projeto"> 
projeto"> 
projeto"> 
projeto"> 
projeto"> 
projeto"> INSERT INTO scripts(nome, conteudo)
projeto"> VALUES ('HELLO.PY','print("script de teste")')
projeto"> );
projeto"> select * from scripts;
projeto"> show columns from scripts;
de teste")');ERT INTO scripts(nome, conteudo) VALUES ('HELLO.PY','print("script d
projeto"> select * from scripts;
projeto"> 
projeto"> 
projeto"> 
projeto"> 
projeto"> INSERT INTO scripts(nome, conteudo) VALUES ('HELLO.PY','print("script de teste")');
projeto"> 
projeto"> 
projeto"> 
projeto"> 
projeto"> 
projeto"> insert into scripts(nome, conteudo) values ('hello.py','print('script de teste')');
projeto"> select * from scripts;
projeto"> "
projeto-> 
projeto-> ;
ERROR:  syntax error at or near "INSERTO"
LINHA 1: INSERTO INTO scripts(nome, contedudo) val"'
         ^
projeto=> 
projeto=> 
projeto=> 
projeto=> 
projeto=> 
projeto=> INSERTO INTO scripts(nome, contedudo) val"'
          show columns from scripts;
          INSERTO INTO scripts(nome, contedudo) val"'

          INSERTO INTO scripts(nome, contedudo) val"'


projeto=> ]
projeto-> 
projeto-> 
projeto-> 
projeto-> 
projeto-> ;
ERROR:  syntax error at or near "]"
LINHA 1: ]
         ^
projeto=> ssfszdf
projeto-> 
projeto-> 
projeto-> 
projeto-> 
projeto-> d
projeto-> d
projeto-> d
projeto-> d
projeto-> d
projeto-> ;
ERROR:  syntax error at or near "ssfszdf"
LINHA 1: ssfszdf
         ^
projeto=> 
projeto=> 
projeto=> 
projeto=> INSERT INTO scripts(nome, conteudo) VALUES ('HELLO.PY','print("script de teste")');
INSERT 0 1
projeto=> select * from scripts;
 id |   nome   |         conteudo         
----+----------+--------------------------
  1 | HELLO.PY | print("script de teste")
(1 registro)

projeto=> UPDATE scripts SET nome = 'update.py' where id =1;
UPDATE 1
projeto=> \d
              Lista de relações
 Esquema |      Nome      |   Tipo    | Dono  
---------+----------------+-----------+-------
 public  | scripts        | tabela    | admin
 public  | scripts_id_seq | sequência | admin
(2 registros)

projeto=> select * from scripts;
 id |   nome    |         conteudo         
----+-----------+--------------------------
  1 | update.py | print("script de teste")
(1 registro)

projeto=> truncate scripts;
TRUNCATE TABLE
projeto=> select * from scripts;
 id | nome | conteudo 
----+------+----------
(0 registro)

projeto=> INSERT INTO scripts(nome, conteudo) VALUES ('HELLO.PY','print("script de teste")');
INSERT 0 1
projeto=> select * from scripts;
 id |   nome   |         conteudo         
----+----------+--------------------------
  2 | HELLO.PY | print("script de teste")
(1 registro)

projeto=> select * from scripts;
 id |   nome   |         conteudo         
----+----------+--------------------------
  2 | HELLO.PY | print("script de teste")
(1 registro)

projeto=> \q
postgres@developer:~$ 
postgres@developer:~$ 
postgres@developer:~$ 
postgres@developer:~$ 
postgres@developer:~$ 
postgres@developer:~$ 
postgres@developer:~$ 
postgres@developer:~$ 
postgres@developer:~$ sudo -u
sudo: a opção requer um argumento -- “u”
usage: sudo -h | -K | -k | -V
usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] [VAR=value] [-i|-s] [<command>]
usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] file ...
postgres@developer:~$ su -
Senha: 
su: Falha de autenticação
postgres@developer:~$ \q

Command 'q' not found, but can be installed with:

apt install python-q-text-as-data 
apt install python3-q-text-as-data

Ask your administrator to install one of them.

postgres@developer:~$ sair
root@developer:~# sair
developer@developer:~$ sudo su -
[sudo] senha para developer: 
root@developer:~# 
root@developer:~# 
root@developer:~# 
root@developer:~# 
root@developer:~# 
root@developer:~# 
root@developer:~# 
root@developer:~# 
root@developer:~# 
root@developer:~# 






























