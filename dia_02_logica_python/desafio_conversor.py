def converter_celsius_para_fahrenheit(celsius):
    """Recebe uma temperatura em Celsius e retorna o valor em Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# --- Execução do Código ---
temp_celsius = 150
temp_fahrenheit = converter_celsius_para_fahrenheit(temp_celsius)

print(f"{temp_celsius}° Celsius equivalem a {temp_fahrenheit}° Fahrenheit.")