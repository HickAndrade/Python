'''
2º-)  O seu programa solicitará o nível de acesso 
de uma pessoa que pode ser: ADM, USR ou GUEST e o gênero dessa pessoa, caso o nível seja ADM, 
ele deverá exibir “Olá administrador” para os homens ou “Olá administradora” para as mulheres.
Se o nível for USR, deverá exibir “Olá usuário” para os homens ou “Olá usuária” para as mulheres.
Se o nível for GUEST, a mensagem deverá ser “Olá visitante”, e se o nível digitado for 
diferente de ADM, USR ou GUEST deverá exibir a mensagem “Olá desconhecido(a)”.
'''

print("=============== Bem vindo ao nosso Sistema =================")
nome=input("Qual seu nome: ").title()
access= input("Qual seu nivel de Acesso?").upper()
genero = input("Qual seu gênero?").upper()

if (genero=="HOMEM" or genero=="MASCULINO")and(access=="ADM"):
    print("Ola administrador, ",nome,".")
elif (genero=="MULHER"or genero=="FEMININO")and(access=="ADM"):
    print("Ola administradora, ",nome,".")
elif (genero=="MULHER"or genero=="FEMININO")and(access=="USR"):
    print("Ola Usuária, ",nome,".")
elif(genero=="HOMEM"or genero=="MASCULINO")and(access=="USR"):
    print("Ola Usuário",nome,".")
elif access=="GUEST":
    print("Ola Visitante, ",nome,".")
else:
    print("Olá desconhecido, ",nome,". ")





