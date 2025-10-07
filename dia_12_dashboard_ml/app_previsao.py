import streamlit as st
import pandas as pd
import joblib

# --- TÍTULO E CABEÇALHO ---
st.title("Previsão de Sobrevivência no Titanic")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/1920px-RMS_Titanic_3.jpg", caption="RMS Titanic")
st.header("Este app utiliza um modelo de Machine Learning para prever se um passageiro sobreviveria.")

# --- CARREGAR O MODELO SALVO ---
# Usamos try/except para garantir que o app não quebre se o arquivo do modelo não for encontrado
try:
    # O caminho agora é relativo a ESTE script. Como estão na mesma pasta, só o nome do arquivo basta.
    modelo = joblib.load("C:\\Users\\Hrsca\\OneDrive\\Área de Trabalho\\Portifolio\\portfolio\\dia_12_dashboard_ml\\modelo_titanic.joblib")
except FileNotFoundError:
    st.error("Arquivo do modelo não encontrado! Verifique se o arquivo 'modelo_titanic.joblib' está na mesma pasta que o app.")
    st.stop() # Para a execução do app se o modelo não for encontrado

# --- INTERFACE DO USUÁRIO (INPUTS) ---
st.subheader("Por favor, insira as características do passageiro para a previsão:")

# Widgets de input do Streamlit para coletar dados do usuário
pclass = st.selectbox("Classe do Ticket (Pclass):", [1, 2, 3])
sex = st.selectbox("Sexo:", ["Masculino", "Feminino"])
age = st.slider("Idade:", min_value=0, max_value=100, value=30, step=1)

# (Aqui virá a lógica do botão "Prever" e a exibição do resultado)

# --- LÓGICA DE PREVISÃO E EXIBIÇÃO DO RESULTADO ---

# Criar um botão que, ao ser clicado, executa o código abaixo
if st.button("Fazer Previsão"):

    # 1. Converter os inputs do usuário para o formato numérico que o modelo espera
    sex_num = 1 if sex == "Feminino" else 0

    # 2. Criar um DataFrame com os dados de entrada para o modelo
    # A estrutura (nomes e ordem das colunas) deve ser EXATAMENTE a mesma que usamos no treino
    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [sex_num],
        'Age': [age]
    })

    # 3. Usar o modelo para fazer a previsão
    previsao = modelo.predict(input_data)
    probabilidade = modelo.predict_proba(input_data)

    # 4. Exibir o resultado de forma clara
    st.subheader("Resultado da Previsão:")

    if previsao[0] == 1:
        st.success("Este passageiro provavelmente SOBREVIVERIA! ✅")
        st.write(f"Confiança da previsão (probabilidade de sobreviver): {probabilidade[0][1]*100:.2f}%")
    else:
        st.error("Este passageiro provavelmente NÃO SOBREVIVERIA... ❌")
        st.write(f"Confiança da previsão (probabilidade de sobreviver): {probabilidade[0][1]*100:.2f}%")
        