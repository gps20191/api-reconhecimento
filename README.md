# API-RECONHECIMENTO

### Depedencias
A aplicação tem como base a biblioteca disponibilizada por [Adam Geitgey](https://github.com/ageitgey/face_recognition). Sendo assim necessaria instalação da biblioteca disponibilizada no link.

Além da biblioteca de reconhecimento, a aplicação faz uso da ORM da linguagem Python chamada [Peewee](http://docs.peewee-orm.com/en/latest/).



### Demonstração de uso
Apos a instalação da biblioteca basta clonar o repositorio e executar os seguintes

Nas imagens a seguir sera exibido um dos modos de execução da aplicação.

<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/ENV_ACTIVE.PNG"> <br>
<em>Neste caso as instalações necessarias foram feitas em um ambiente virtual python, sendo necessario ativa-lo</em> 
</p>
<br>

Apos o processo anterior é necessario que faça o treinamento da aplicação. Em nossa aplicação as imagens ficam salva no banco de dados no formato base64, mais informações sobre o banco de dados será falado mais à frente.

<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/TREINAMENTO.PNG"> <br>
<em>Processo de treinamento da aplicação</em> 
</p>
<br>

Uma vez que o treinamento foi feito com sucesso podemos processar as requisições enviadas pelo os usuario do aplicativo movel.

<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/REQUISICOES.PNG"> <br>
<em>Consumo das requisições ainda não processadas disponivel no banco de dados</em> 
</p>
<br>

### Estrutura do banco de dados

A aplicação faz uso de duas tabelas, e essas duas tabelas estão em bancos distindos, logo abaixo é mostrata a estrutura das tabelas e seus componentes.

<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/data_base.svg"> <br>
</p>
<br>

Exibição da tabela de suspeitos
```sql
SELECT * FROM SUSPEITOS
```
<br>
<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/SELECT_SUSPEITOS.PNG"> <br>
</p>
<br>

Exibição da tabela de requisições
```sql
SELECT * FROM ALERTREQUEST
```
<br>
<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/SELECT_ALERT.PNG"> <br>
<em>Toda vez que é recebida uma requição os parametros "processed", "match" e "alerted" são atribuidos como falso</em>
</p>
<br>

### Recebimento de requisições
O nosso sistema trabalha em volta das requisições envidas pelo o usuario do aplicativo mobile, essas requisições são recebidas via metodo POST através do link https://api-process.herokuapp.com/ e devem informar os seguintes parametros
<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/post_parameters.svg"> <br>
<em>Listagem dos parametros de cima para abaixo, idphoto, urlphoto, latitude, longitude, requestdate, numbus, blobimg</em>
</p>
<br>

### Fluxo de operação
A partir do momento que o sistema recebe uma requisição, ele opera da seguinte maneira:
<br>
<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/REQUEST_FLOW.svg"> <br>
<em>Toda vez que é recebida uma requição os parametros "processed", "match" e "alerted" são atribuidos como falso</em>
</p>
<br>