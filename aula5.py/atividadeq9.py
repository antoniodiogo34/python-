altura = float(input("digite a altura da pessoa em metros"))
sexo = input("digite o sexo da pessoa (M para masculino, F para feminino): ")

calcm = (72.7 * altura) - 58 
calcf = (62.1 * altura) - 44.7 

if sexo == 'F':
    print(calcf)
else:
    print(calcm) 
     
