preço = 10
pagamento1 = str(input("digite se vc prefere pagar a vista ou em cheque"))
pagamento2 = str(input("digite se vc prefere pagar a vista no cartão de crédito"))
pagamento3= str(input("digite se vc prefere pagar duas vezes, preço normal de etiqueta sem juros"))
pagamento4 = str(input("digite se vc prefere pagar duas vezes, preço normal de etiqueta com juros"))
if pagamento1:
    input(preço - (preço * 0.10))
elif pagamento2:
    input(preço - (preço * 0.15))
if pagamento3:
    input(preço)
elif pagamento4:
    input(preço + (preço * 0.10))