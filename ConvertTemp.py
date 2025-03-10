def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

escolha = input("Converter de (C)elsius para Fahrenheit ou de (F)ahrenheit para Celsius? (C/F): ").upper()
valor = float(input("Digite a temperatura: "))

if escolha == 'C':
    print(f"{valor}°C equivale a {celsius_para_fahrenheit(valor)}°F")
elif escolha == 'F':
    print(f"{valor}°F equivale a {fahrenheit_para_celsius(valor)}°C")
else:
    print("Escolha inválida.")