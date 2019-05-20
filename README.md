# API-RECONHECIMENTO

### Depedencias
A aplicação tem como base a biblioteca disponibilizada por [Adam Geitgey](https://github.com/ageitgey/face_recognition). Sendo assim necessaria instalação da biblioteca disponibilizada no link.<br>



### Uso
Apos a instalação da biblioteca basta clonar o repositorio e executar os seguintes

```sh
api-reconhecimento$ python Treinamento/train_code.py
api-reconhecimento$ python Reconhecimento/recognition_code.py
```
Os comando devem ser executados na orde exposta, uma vez que é necessario o arquivo de reinamento gerado atraves do primeiro comando executado.<br>

Atualmente a aplicação não esta fazendo uso de banco de dados, os dados  utilizados, tanto para treinamento e reconhecimento estao sendo extraidos a partir de diretorios no projeto, as imagens para treinamento deve estar dentro da pasta [train_img](https://github.com/gps20191/api-reconhecimento/tree/master/train_img), pasta na qual onde deve ser criada uma outra pasta com o nome da pessoa no qual irá ser informada as fotos do rosto da mesma, essas fotos devem ter somente a pessoa em questao, tendo assim tendo apenas os dados referente ao rosto da pessoa X.
Para efetuar o reconhecimento as imagens devem estar na pastar [test](https://github.com/gps20191/api-reconhecimento/tree/master/test), nesta pasta nao é necessario nenhuma outra operação apenas a adição das imagens na qual a aplicação deve fazer o reconhecimento.<br>

### Envio de imagem para processamento
Para o envio de uma imagem para o processamento, a aplicação "app-mobile" deve efetuar uma requisição POST atraves da URL {link api aqui} informando os seguintes dados.<br>
<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/POST_RECEIVE.png"> <br>
<em>Os campos coloridos não devem ser informado para o usuario, é apenas o escopo de como deve ser guardado no banco de dados.</em> 
</p>

### Fluxo da aplicação
A aplicação irá operar com base nas requisições efetuadas via API disponibilizada, ao verificar requisições nao processadas no banco o aplicação irá efetuar o processamento e analise de imagem, caso seja encontrado algum suspeito com base nos dados disponibilizados para o treinamento é feito um envio de alerta para a API-WEB, que então irá tomar as medidas cabiveis.

### Organização dos dados
Os dados na aplicação serão mantidos da seguinte forma:

<p align="center">
<img src="https://github.com/gps20191/api-reconhecimento/blob/master/DOC_APP/Imagens/logic_db.png"> 
</p><br>

A tabelaAlertRequest já foi explicada em [topicos anteriores](https://github.com/gps20191/api-reconhecimento#envio-de-imagem-para-processamento), as tabelas AlertArchive e AlertNotified representam parte do processamento citado no topico anterior, caso seja emitido um alerta para o cliente WEB a data de envio desse alerta é salva, juntamente com os dados da requisição que causou o seu disparo, já a tabela AlertArchive mantem as solicitações que não tiveram a identificação, guardando data e as informações da requisição que não teve sucesso. A tabela procurados é a tabela do banco que representa as informações utilizadas para o treinamento da aplicação, onde é mantido os dados referente ao rosto do procurado(FaceData) e o nome do procurado.
