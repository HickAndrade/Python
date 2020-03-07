'''
1) Monte um programa em Python que solicite ao usuário o tipo de graduação que realiza.
Se o usuário entrar com Tecnólogo o sistema deverá exibir 2 até 3 anos
Se o usuário entrar com Bacharelado o sistema deverá exibir 4 até 6 anos
'''
 
while True:
    graduacao = input("Qual seu tipo de graduação? \n graduação: ").upper()
    print("Tipo de graduação Invalida !!")   
 
    if graduacao == "TECNOLOGO" or graduacao == "BACHARELADO":
        break
    

if graduacao == "TECNOLOGO":
    print("Tecnólogo - 2 até 3 anos de curso.")
elif graduacao[:5] =="BACHARELADO":
    print("Bacharelado - 4 até 6 anos de curso.")