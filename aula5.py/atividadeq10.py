nome = (input("digite seu nome"))
peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))
imc = peso/altura ** 2 
print (imc)

if imc <= 18.5:
    print("voce esta abaico do peso")
elif imc <= 25:
    print("voce esta no peso ideal")
elif imc <= 30:
    print("voce esta acima do peso")
else:
    print("obeso") 