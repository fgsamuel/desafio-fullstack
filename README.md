# Desafio Fullstack
A idéia deste desafio é nos permitir avaliar melhor as habilidades de candidatos à vagas de desenvolvedor, de vários níveis.

Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

## Instruções de entrega do desafio
1. Primeiro, faça um fork deste projeto para sua conta no Github (crie uma se você não possuir).
1. Em seguida, implemente o projeto tal qual descrito abaixo, em seu próprio fork.
1. Por fim, empurre todas as suas alterações para o seu fork no Github e envie um pull request para este repositório original. Se você já entrou em contato com alguém da Labr Dev sobre uma vaga, avise também essa pessoa por email, incluindo no email o seu usuário no Github.

## Instruções alternativas de entrega do desafio (caso você não queira que sua submissão seja pública)
1. Faça um clone deste repositório.
1. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
1. Por fim, envie via email um arquivo patch para seu contato na Labr Dev.

## Descrição do projeto

Desenvolver um sistema para cadastrar estados e cidades Brasileiras.

Sua tarefa é criar uma interface web que aceite o cadastro de estados e cidades Brasileiras, normalize os dados e armazene-os em um banco de dados relacional.

Sua aplicação web DEVE:

1. Aceitar (via um formulário e via API) o cadastro de estados
1. Aceitar (via um formulário e via API) o cadastro de cidades
1. Listar todas as cidades e estados cadastrados
1. Ser escrita obrigatoriamente em Ruby 2.0+, Python 3.6+, Java 7+ ou PHP 5.3+ (caso esteja entrevistando para uma vaga específica, utilize a linguagem solicitada pela vaga).
1. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.

Sua aplicação web não precisa:

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
1. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).
1. Ter uma aparência bonita.

## Avaliação
Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
1. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
1. Você seguiu as instruções de envio do desafio?
1. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.

# Documentação da entrega

## Instalação do projeto
Versão de python utilizada no projeto: *Python 3.9.1*

Após fazer o download do código fonte é necessário criar um virtual env para isolar as bibliotecas do projeto

Para isso, acesse a pasta raiz do projeto via terminal e digite o seguinte comando:

```
python -m venv .venv
```

Este comando cria uma virutal env em uma pasta chamada `.venv`.

Para ativar a virtual env recém criada, utilize o seguinte comando:

```
# windows
.venv\Scrips\activate.bat

# linux
source .venv/bin/activate
```

Para instalar todas as dependências do projeto, rode o comando abaixo:

```
pip install -r requirements.txt
```

## Variáveis de ambiente

As variáveis de ambiente são desacopladas do código, e para funcionar você deve fazer uma cópia do arquivo
`.env-sample` com o nome `.env` e trocar as variáveis conforme a necessidade do seu ambiente

## Subindo o projeto para fazer testes locais

Ainda dentro da pasta do projeto digite o seguinte comando para iniciar o servidor interno da aplicação

```
# Criando o banco de dados
python manage.py migrate

# Executando os testes unitários
python manage.py test

# executando o servidor embutido
python manage.py runserver
```

Após isso é possível acessar a aplicação na url `http://localhost:8000`

## Acessando a aplicação

A aplicação e a api rest estão protegidas para acesso autenticado.

Para efetuar testes é necessário primeiramente criar um usuário administrador através do comando

```
python manage.py createsuperuser
```

Você deverá informar os campos solicitados após o comando.

Feito isso, utilize esse mesmo usuário e senha para fazer login na aplicação e na api

### Fazendo login na api

A api tem dois endpoints de dados
* localhost:8000/api/estados/
* localhost:8000/api/cidades/

e para autenticação ela utiliza um token JWT que pode ser obtido no seguinte endpoint

* localhost:8000/api/token/

os dados a serem enviados no post para obter um token são:

```
{
    "username": <seu usuario>,
    "password": <sua senha>
}
```

E o retorno da api tem o seguinte formato, caso você seja autenticado:

```
{
    "refresh": <hash para atualizar o token>,
    "access": <hash do token>
}
```

E para fazer as requisições autenticadas você deve adicionar um header na sua requisição com o nome
`Authorization` e o valor deve ser `Bearer <hash do token>`

### Observação importante quanto ao uso da api de cidades

Para facilitar o trabalho com os dados da cidade (que tem relação com o estado) ela tem o formato
de apresentação diferente do formato de inclusão/alteração dos dados.

Para exibição ela tem o seguinte formato:

```
{
    "id": <id da cidade>,
    "estado": {
        "id": <id do estado>,
        "sigla": <sigla do estado>,
        "nome": <nome do estado>
    },
    "nome": <nome da cidade>
}
```

E para inclusão ou alteração de dados ela usa o seguinte formato

```
{
    "id": <id da cidade>,
    "estado": <id do estado>,
    "nome": <nome da cidade>
}
```

## Normalização dos dados

Tanto quando inserido por formulário ou por api, o sistema faz a seguinte normalização dos dados
Sigla do estado toda em maiúsculo
Nome do estado ou da cidade com a primeira letra de cada palavra maiúscula e as demais minúsculas.