# Aplicativo para detectar fraudes bancárias

## Introdução

O aplicativo tem como objetivo detectar fraudes bancárias a partir dos parâmetros passados.

Além disso, é possível visualizar os dados em gráficos e dashboards.

## Sobre a base de dados

A base de dados escolhida representa um conjunto de transações financeiras simuladas gerado pelo simulador PaySim. O PaySim utiliza um conjunto de dados sintético que se assemelha às transações financeiras reais e injeta comportamento malicioso para avaliar posteriormente o desempenho dos métodos de detecção de fraude. A base de dados original possui 24.000.000 linhas e foi reduzida em ¼ (6.000.000 linhas) para a plataforma Kaggle.

Para fins de análise de dados, decidimos simplificar a base de dados para 50.000 linhas.

Link para a base de dados original: https://www.kaggle.com/datasets/ealaxi/paysim1

## Tecnologias

1. [Sklearn](https://scikit-learn.org/stable/)
2. [Pandas](https://pandas.pydata.org/)
3. [Streamlit](https://streamlit.io/)

## Pré-requisitos

1. [Python](https://www.python.org/)
2. [Pip](https://pypi.org/project/pip/)
3. [Git](https://www.git-scm.com/)

## Instalação (Linux)

Clone esse repositório:

```
git clone https://github.com/renanleitev/fraude-bancaria.git
```

Acesse a pasta do projeto:

```
cd fraude-bancaria
```

Após, crie um novo [ambiente virtual](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) na pasta:

```
python -m venv .venv
```

Depois, ative o ambiente:

```
source .venv/bin/activate
```

[VSCODE] Troque o ambiente Python pelo ambiente virtual:

```
https://code.visualstudio.com/docs/python/environments
```

Para instalar as dependências, basta executar o comando abaixo no seu terminal:

```
pip install -r requirements.txt
```

Depois, execute o comando abaixo para rodar o aplicativo na sua máquina:

```
streamlit run app.py
```

## Instalação (Windows)

Clone esse repositório:

```
git clone https://github.com/renanleitev/fraude-bancaria.git
```

Acesse a pasta do projeto:

```
cd fraude-bancaria
```

Após, crie um novo [ambiente virtual](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) na pasta:

```
py -m venv .venv
```

Depois, ative o ambiente:

```
.venv\Scripts\activate
```

[VSCODE] Troque o ambiente Python pelo ambiente virtual:

```
https://code.visualstudio.com/docs/python/environments
```

Caso encontre um erro desse tipo:

```
"Não pode ser carregado porque a execução de scripts foi desabilitada neste sistema."
```

Siga esses tutoriais:

1. https://pt.stackoverflow.com/questions/220078/o-que-significa-o-erro-execu%C3%A7%C3%A3o-de-scripts-foi-desabilitada-neste-sistema
2. https://github.com/gr-knowledge/vscode/issues/5

Para instalar as dependências, basta executar o comando abaixo no seu terminal:

```
pip install -r requirements.txt
```

Depois, execute o comando abaixo para rodar o aplicativo na sua máquina:

```
streamlit run app.py
```

## Equipe

1. Flávio Raposo
2. João Pedro Marinho
3. José Adeilton
4. Renan Leite Vieira
5. Rian Vinícius
6. Robério José
