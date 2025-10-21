# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado : 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dias = float(input("Por quantos dias o carro foi alugado"))
km =  float(input("Quantos km o carro rodou"))
preco_dias = dias * 60 
preco_km = km * 0.15
aluguel_total = preco_dias + preco_km
print (f"o carro foi alugado por {dias} dias você rodou {km} km o preço a se pagar é {aluguel_total}")