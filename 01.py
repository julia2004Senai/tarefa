num1 = float(input("Digite o valor do primeiro número"))
num2 = float(input("Digite o valor do segundo número"))
num3 = float(input("Digite o valor do terceiro número"))

if num1 > num2 + num3 or num2 > num1 + num3 or num3 > num1 + num2:
    print ("Existe um número maior que a soma de dois")

else:
    print ("Não existe um número maior na soma")