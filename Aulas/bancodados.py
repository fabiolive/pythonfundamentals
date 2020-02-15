#conectando com banco postgres via python!

#sudo apt install python3-psycopg2 --via terminal


import psycopg2
try:
    con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")


    cur = con.cursor()


    cur.execute("insert into scripts(nome,conteudo) values('testetry.py','teste de tratamento de excessão com o banco de dados')")

    con.commit()


except Exception as e:
    print("Erro{}".format(e))
    print("Fazendo rollback")
    con.rollback()


finally:
    print("Finalizando conexão com o banco de dados")
    cur.close()
    con.close()

    