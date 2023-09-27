nome = input("digite o seu nome")
sexo = input("digite seu sexo(ferminino, masculino)")
estadocivil = input("digite seu estado civil")
tempocasamento = input("digite seu tempo de casamento")
if sexo =="F" and estadocivil =="casada":
   tempocasamento = int(input("digite quantos anos de casada em anos"))
   print("{nome} está casada a {tempocasamento} anos")