import streamlit as st
import pandas as pd
import numpy as np
import requests
from io import StringIO
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

file_id = '1OnX0UXo5UI5TqjaRp2b-vUVpt1U5HIJ0'
url = f"https://drive.google.com/uc?id={file_id}"

try:
    response = requests.get(url)
    response.raise_for_status()
    csv_raw = StringIO(response.text)
    df = pd.read_csv(csv_raw, sep=',',  on_bad_lines='skip')
except requests.RequestException as e:
    st.error(f"Erro ao acessar o arquivo: {e}")

# Renomeando o nome das colunas (camelCase)
df = df.rename(columns={'oldbalanceOrg':'oldBalanceOrig', 'newbalanceOrig':'newBalanceOrig', \
                        'oldbalanceDest':'oldBalanceDest', 'newbalanceDest':'newBalanceDest'})

# Obtendo uma lista dos valores únicos
unique_values = df['type'].unique()

# Convertendo os valores de type para númerico
for index, x in enumerate(unique_values):
    df['type'] = df['type'].replace(x, index+1)

# Tipos de pagamento
# PAYMENT == 1   
# TRANSFER == 2
# CASH_OUT == 3
# DEBIT == 4
# CASH_IN == 5

# Convertendo os tipos para exibir os labels corretamente
def convert_type(type):
    if type == 'PAYMENT':
        return 1
    if type == 'TRANSFER':
        return 2
    if type == 'CASH_OUT':
        return 3
    if type == 'DEBIT':
        return 4
    if type == 'CASH_IN':
        return 5

  
# Removendo as variáveis que não são númericas e/ou irrelevantes
df = df.drop(['nameOrig', 'nameDest', 'isFlaggedFraud', 'step'], axis=1)

def prever_fraude(model, attributes, df_template):
    """
    Função para prever a probabilidade de fraude com base em atributos fornecidos.
    
    Parâmetros:
    - model: O modelo treinado (DecisionTreeClassifier).
    - attributes: Um dicionário contendo os atributos necessários para a predição.
    - df_template: DataFrame usado como template para manter a ordem e colunas corretas.
    
    Retorna:
    - probabilidade: A probabilidade de fraude.
    - classificacao: 1 se houve fraude, 0 caso contrário.
    """
    
    # Cria um DataFrame a partir do dicionário de atributos
    df_attributes = pd.DataFrame([attributes])
    
    # Alinha os atributos com o DataFrame template
    # Removendo a coluna isFraud
    df_attributes = df_attributes[df_template.drop(['isFraud'], axis=1, errors='ignore').columns].fillna(0)
    
    # Prever a probabilidade de fraude
    probabilidade = model.predict_proba(df_attributes)[0][1]
    
    # Prever a classificação de fraude (1 para fraude, 0 caso contrário)
    classificacao = model.predict(df_attributes)[0]
    
    return probabilidade, classificacao

# X = variaveis explicativas
X = df[['type', 'amount', 'oldBalanceOrig', 'newBalanceOrig', 'oldBalanceDest', 'newBalanceDest']] 
# Y = variavel resposta
Y = df['isFraud']

# Treinando o modelo
random_seed = 77
test_size = 0.25
np.random.seed(random_seed)
X_resampled, Y_resampled = SMOTE().fit_resample(X, Y)
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X_resampled, Y_resampled, test_size=test_size)

# Fazendo o fit do modelo
model = DecisionTreeClassifier()
model.fit(X_treino, Y_treino)

# Streamlit App
st.title("Previsão de Fraude Bancária")

with st.form(key='fraud_form'):
    # Inputs
    type = st.selectbox("Tipo de transação", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
    amount = st.number_input("Quantidade", min_value=0)
    oldBalanceOrig = st.number_input("Saldo Anterior (Origem)", min_value=0)
    newBalanceOrig = st.number_input("Novo Saldo (Origem)", min_value=0)
    oldBalanceDest = st.number_input("Saldo Anterior (Destino)", min_value=0)
    newBalanceDest = st.number_input("Novo Saldo (Destino)", min_value=0)
    
    submit_button = st.form_submit_button(label='Prever Fraude')

if submit_button:
    attributes = {
      'type': convert_type(type),
      'amount': amount,
      'oldBalanceOrig': oldBalanceOrig,
      'newBalanceOrig': newBalanceOrig,
      'oldBalanceDest': oldBalanceDest,
      'newBalanceDest': newBalanceDest,
    }

    probabilidade, classificacao = prever_fraude(model, attributes, df)
    st.write(f"Probabilidade de Fraude: {probabilidade:.2f}")
    st.write(f"Classificação: {'Fraude' if classificacao == 1 else 'Não Fraude'}")