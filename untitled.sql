
.grant all privileges on projetos.* to admin@'localhost' identified by '4linux' with grant option;


create table clientes(
id int primary key not null auto_increment,
nome varchar(255),
endereco varchar (255)
);


insert into clientes(nome, endereco) values('Mariana','Rua vergueiro');
update from clientes Set endereco='Paulista' where nome = 'Mariana';



db.fila.insert({"_id":1, "servico":"intranet", "status":0})


db.fila.insert({"empresa":"coronaLoja", "produtos": [{"nome":"CoronaCamiseta", "preco": 19.90}, {"nome":"CoronaCalca", "preco":159.90}]})
WriteResult({ "nInserted" : 1 }) 

	db.fila.find()
db.fila.remove()

sudo apt install python3-psycopg2