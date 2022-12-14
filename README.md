<!-- cSpell:disable -->
# Referêncial Teórico TCC

## Definições

Essa API foi desenvolvida a fim de prover maior facilidade na busca de artigos para pesquisa, sendo desenvolvida na [Linguagem de Programação Python](https://www.python.org/) com o [Micro-Framework Web Flask](https://flask.palletsprojects.com/en/2.2.x/) e com a [Biblioteca Requests](https://pypi.org/project/requests/), tendo os dois últimos em um [Ambiente Virtual](https://docs.python.org/3/library/venv.html). Será utlizada a [Scopus Search API](https://dev.elsevier.com/documentation/SCOPUSSearchAPI.wadl), aplicação mantida pela [Elsevier](https://www.elsevier.com/pt-br), uma empresa especializada em conteúdo científico. Essa API da Scopus permite realizar pesquisas no cluster [Scopus](https://www.scopus.com/home.uri), que é o maior banco de dados de resumos e citações de literatura de pesquisa e fontes da web de qualidade.

---

## Uso

### 1. Link de Busca

Essa API é acessada por um link no qual devem ser inseridos os parâmetros necessários para busca de artigos na Scopus. O returno desse Endpoint será um arquivo **.csv** contendo as informações dos artigos encontrados.

```bash
# É necessário inserir a API-Key e as palavras-chave
/scopus-api?apikey=...&keywords=...
```

### 2. API-KEY

É necessário obter uma chave de acesso para utilizar a API Scopus e buscar artigos. Essa chave pode ser obtida acessando o site [Elsevier Developer Portal](https://dev.elsevier.com/), selecionando a opção "**I want an API Key**" e realizando um cadastro.

```bash
# Exemplo de API-Key
apikey=a333dem09d942bddc5e8a0fc590602c8
```

### 3. Keywords

As palavras-chave serão usadas como parâmetro e filtro na busca de artigos na API Scopus, elas devem ser definidas em **inglês** após a API-Key e separadas por vírgula, e serão procuradas nos artigos todas ao mesmo tempo.

```bash
# Exemplo de Keywords
keywords=artificial intelligence,robots,machine learning,deep learning
```

É possível utilizar o operador **OR** para ampliar as pesquisas.

```bash
# Exemplo de Keywords com OR
keywords=artificial intelligence OR machine learning,robots
```

### 4. Exemplo de Link/URL Completo

```bash
# Exemplo de Link Completo
/scopus-api?apikey=a333dem09d942bddc5e8a0fc590602c8&keywords=artificial intelligence,robots,machine learning,deep learning
```

---

## Tabelas

### 1º Tabela: Palavras-Chave

Tabela com quatro palavras-chave, as quais serão usadas para buscar documentos e artigos com conteúdo relacionado

### Levantamento de Dados

Buscar cada palavra-chave no **Título**, **Resumo**, e **Palavras-Chave**

1. Opção: 4 palavras-chave encontradas
2. Opção: 3 palavras-chave encontradas
3. Opção: 2 palavras-chave encontradas

### 2° Tabela: Quantidade de Palavras-Chave Encontradas

Tabela que lista todos os resultados e os ordena com base na quantidade de palavras-chave encontradas por **Opção**

### 3° Tabela: Sem Repetição

Tabela com o conteúdo da **Tabela 2** mas removendo os resultados repetidos

### 4° Tabela: Filtragem

Tabela com o conteúdo da **Tabela 3** mas removendo os resultados de mesmo título e mesmo autor

---

Developed by **Mauricio**
