print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
idade: int = int(input("Qual é a sua idade? "))
print(f"Tu tens {idade} anos...")

print("Vamos fazer uma conta?")
num1: float = float(input("Digite o primeiro número: "))
num2: float = float(input("Digite o segundo número: "))
soma: float = num1 + num2
print(f"A soma de {num1} e {num2} é: {soma}")

print("conta de multiplicação")
mult: float = num1 * num2
print(f"A multiplicação de {num1} e {num2} é: {mult}")

print("conta de divisão")
if num2 != 0:
    div: float = num1 / num2
    print(f"A divisão de {num1} por {num2} é: {div}")
    
print("conta de subtração")
sub: float = num1 - num2
print(f"A subtração de {num1} por {num2} é: {sub}")