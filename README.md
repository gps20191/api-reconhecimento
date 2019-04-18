# API-RECONHECIMENTO

### Depedencias
A aplicação tem como base a biblioteca disponibilizada por [Adam Geitgey](https://github.com/ageitgey/face_recognition). Sendo assim necessaria instalação da biblioteca disponibilizada no link.



### Uso
Apos a instalação da biblioteca basta clonar o repositorio e executar os seguintes

```sh
api-reconhecimento$ python Treinamento/train_code.py
api-reconhecimento$ python Reconhecimento/recognition_code.py
```
Os comando devem ser executados na orde exposta, uma vez que é necessario o arquivo de reinamento gerado atraves do primeiro comando executado.

Atualmente a aplicação não esta fazendo uso de banco de dados, os dados  utilizados, tanto para treinamento e reconhecimento estao sendo extraidos a partir de diretorios no projeto, as imagens para treinamento deve estar dentro da pasta [train_img](https://github.com/gps20191/api-reconhecimento/tree/master/train_img), pasta na qual onde deve ser criada uma outra pasta com o nome da pessoa no qual irá ser informada as fotos do rosto da mesma, essas fotos devem ter somente a pessoa em questao, tendo assim tendo apenas os dados referente ao rosto da pessoa X.
Para efetuar o reconhecimento as imagens devem estar na pastar [test](https://github.com/gps20191/api-reconhecimento/tree/master/test), nesta pasta nao é necessario nenhuma outra operação apenas a adição das imagens na qual a aplicação deve fazer o reconhecimento.
