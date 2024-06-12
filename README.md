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

1. Python
2. Pip

## Instalação (Linux)

Primeiro, crie um novo [ambiente virtual](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) na pasta:

```
python -m venv .venv
```

Depois, ative o ambiente:

```
source .venv/bin/activate
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

Primeiro, crie um novo [ambiente virtual](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) na pasta:

```
py -m venv .venv
```

Depois, ative o ambiente:

```
.venv\Scripts\activate
```

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
