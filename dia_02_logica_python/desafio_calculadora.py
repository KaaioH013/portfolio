# --- Definição das Funções ---
# Cada função tem uma responsabilidade única: fazer um cálculo específico.
# Elas recebem os ingredientes (num1, num2) e devolvem (return) o resultado.

def somar(num1, num2):
    """Esta função recebe dois números e retorna a soma deles."""
    return num1 + num2

def subtrair(num1, num2):
    """Esta função recebe dois números e retorna a subtração deles."""
    return num1 - num2

def multiplicar(num1, num2):
    """Esta função recebe dois números e retorna a multiplicação deles."""
    return num1 * num2

def dividir(num1, num2):
    """
    Esta função recebe dois números e retorna a divisão.
    Inclui uma verificação para não dividir por zero.
    """
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return num1 / num2

# --- Execução do Código ---
# Aqui nós efetivamente usamos as funções que criamos.

numero_a = 500
numero_b = 20

# Chamamos cada função, passamos nossos números e guardamos os resultados.
resultado_soma = somar(numero_a, numero_b)
resultado_subtracao = subtrair(numero_a, numero_b)
resultado_multiplicacao = multiplicar(numero_a, numero_b)
resultado_divisao = dividir(numero_a, numero_b)

# Imprimimos os resultados de forma organizada.
print("--- Calculadora Simples ---")
print(f"Soma de {numero_a} + {numero_b} = {resultado_soma}")
print(f"Subtração de {numero_a} - {numero_b} = {resultado_subtracao}")
print(f"Multiplicação de {numero_a} * {numero_b} = {resultado_multiplicacao}")
print(f"Divisão de {numero_a} / {numero_b} = {resultado_divisao}")