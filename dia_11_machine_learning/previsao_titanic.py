import pandas as pd

print("--- Iniciando Script de Previsão de Sobrevivência no Titanic ---")

# ===================================================================
# 1. CARREGAR E LIMPAR OS DADOS (Revisão dos Dias 4 e 5)
# ===================================================================
try:
    # Carregar os dados
    caminho_arquivo = "dia_04_pandas/datasets/titanic.csv"
    df = pd.read_csv(caminho_arquivo)
    print("Dataset do Titanic carregado.")

    # Limpeza: Preencher 'Age' com a média
    media_idade = df['Age'].mean()
    df['Age'] = df['Age'].fillna(media_idade)

    # Limpeza: Remover 'Cabin' por ter muitos dados nulos
    df.drop('Cabin', axis=1, inplace=True)

    # Limpeza: Remover as 2 linhas onde 'Embarked' é nulo
    df.dropna(subset=['Embarked'], inplace=True)
    print("Limpeza inicial dos dados concluída.")

except FileNotFoundError:
    print(f"ERRO: Arquivo não encontrado no caminho: {caminho_arquivo}")
    exit()

# (Aqui vamos preparar os dados para o modelo)

# ===================================================================
# 2. PREPARAÇÃO DOS DADOS PARA O MODELO (Engenharia de Features)
# ===================================================================
print("\nPreparando dados para o modelo...")

# A coluna 'Sex' é texto ('male', 'female'). Modelos de ML não entendem texto.
# Vamos converter para números: male -> 0, female -> 1.
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
print("- Coluna 'Sex' convertida para formato numérico.")

# Para nosso primeiro modelo, vamos escolher 3 'pistas' (features) que parecem importantes.
features = ['Pclass', 'Sex', 'Age']

# O nosso 'alvo' (target) é o que queremos prever.
target = 'Survived'

# Agora, criamos as variáveis que o Scikit-learn espera.
# X (maiúsculo) -> DataFrame com todas as nossas features.
# y (minúsculo) -> Series com a nossa coluna alvo.
X = df[features]
y = df[target]

print("Features (X) e Target (y) foram definidos.")
print("\nPrévia das features (X) que o modelo vai usar para aprender:")
print(X.head())

# ===================================================================
# 3. DIVIDINDO OS DADOS EM TREINO E TESTE
# ===================================================================
from sklearn.model_selection import train_test_split

# A função train_test_split divide os dados para nós.
# test_size=0.2 significa que 20% dos dados serão separados para o teste.
# random_state=42 garante que a divisão aleatória seja sempre a mesma,
# tornando nosso experimento reproduzível.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nDados divididos em conjuntos de treino e teste.")
print(f"Tamanho do conjunto de treino: {X_train.shape[0]} passageiros")
print(f"Tamanho do conjunto de teste: {X_test.shape[0]} passageiros")

# ===================================================================
# 4. TREINANDO O MODELO DE MACHINE LEARNING
# ===================================================================
from sklearn.ensemble import RandomForestClassifier

print("\nTreinando o modelo de Machine Learning...")

# Criar o modelo. n_estimators=100 significa que teremos 100 "árvores" na nossa floresta.
modelo = RandomForestClassifier(n_estimators=100, random_state=42)

# Treinar o modelo usando os dados de TREINO.
# O método .fit() é o momento em que o "aprendizado" acontece.
modelo.fit(X_train, y_train)

print("Modelo treinado com sucesso!")


# ===================================================================
# 5. FAZENDO PREVISÕES COM OS DADOS DE TESTE
# ===================================================================
print("\nFazendo previsões com o conjunto de teste (dados que o modelo nunca viu)...")

# Usar o modelo treinado para prever os resultados do conjunto de teste (X_test).
previsoes = modelo.predict(X_test)

print("Previsões geradas com sucesso.")

# ===================================================================
# 6. AVALIANDO A PERFORMANCE DO MODELO
# ===================================================================
from sklearn.metrics import accuracy_score

# Comparamos as respostas reais (y_test) com as previsões do modelo (previsoes)
acuracia = accuracy_score(y_test, previsoes)

print("\n--- Avaliação do Modelo ---")
print(f"A acurácia do nosso modelo é: {acuracia * 100:.2f}%")
print(f"\nIsso significa que o modelo acertou a previsão para {acuracia * 100:.0f}% dos passageiros do conjunto de teste.")
