nome = input("Nome do paciente: ")
idade = int(input("Idade do paciente: "))
risco = input("Paciente possui asma?").upper()

if risco!="SIM" and risco!="NAO":  
        print("dado de risco invalido, digite novamente: ")
        risco = input("Paciente possui asma?").upper()

if idade<15 or idade>60:
    print("O senhor(a)",nome,"Está vuneravel a corona virus!!")
elif risco == "SIM":
    print("O senhor(a)",nome,"Possui um risco e acaba ficando vulneravel ao corona virus... ")
else:
    print("O senhor(a)",nome," Está limpo e Invulneravel ao Virus.")
         