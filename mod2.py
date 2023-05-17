import datetime as dt

agora = dt.datetime.now()

dia_atual = agora.strftime('%d/%m/%y')

hora_atual = agora.strftime('%H:%M:%S')

saudacao = ''
hora = agora.hour

if 6 <= hora < 12:
    saudacao = 'bom dia recrutador (a)!'

elif 12 <= hora < 18 :
    saudacao ='boa tarde recrutador (a) !'

else:
    saudacao = 'boa noite recrutador (a)!'

print('data:', dia_atual)
print('hora', hora_atual)
print(saudacao)


print('Olá Recrutador(a). Seja bem vindo a plataforma de processos seletivos! ')
nome_recrutador= str(input('Digite seu nome :'))

num_de_candidatos = int(input("Digite o número de candidatos que participaram da entrevista: "))
candidato_zero = 0    
ID_candidato = 1    
lista_candidatos = [] 

while candidato_zero < num_de_candidatos:
    lista_notas = []                           
    
    entrevista = int(input(f"Digite a nota do canditato(a) {ID_candidato} na entrevista: "))
    teorico = int(input(f"Digite a nota do canditato(a) {ID_candidato} no teste teórico: "))
    pratico = int(input(f"Digite a nota do canditato(a) {ID_candidato} no teste prático: "))
    softskills = int(input(f"Digite a nota do canditato(a) {ID_candidato} na avaliação das softskills: "))

    lista_notas.append(entrevista)                      
    lista_notas.append(teorico)
    lista_notas.append(pratico)
    lista_notas.append(softskills)

    lista_candidatos.append(lista_notas)       
    candidato_zero += 1
    ID_candidato += 1

lista_notas_minimas = []                        

e_nota_minima = int(input('Digite a nota minima para aprovação na entrevista: '))             
t_nota_minima = int(input('Digite a nota minima para aprovação no teste teórico: '))
p_nota_minima = int(input('Digite a nota minima para aprovaçâo no teste prático: '))
s_nota_minima = int(input('Digite a nota minima para aprovação no teste soft skills: '))

lista_notas_minimas.append(e_nota_minima)                       
lista_notas_minimas.append(t_nota_minima)
lista_notas_minimas.append(p_nota_minima)
lista_notas_minimas.append(s_nota_minima)

print("Segue a lista com os candidatos aprovados: ")


def imprime(lista_candidatos, lista_notas_minimas):
    coun1 = 0
    candidatos_aprovados = []                                       
    for concorrentes, notas in enumerate(lista_candidatos):
        for indice, valor in enumerate(notas):
            if lista_notas_minimas[indice] <= valor:
                coun1 += 1
        if coun1 == 4: 
            candidatos_aprovados.append(lista_candidatos[concorrentes])
            coun1 = 0
    for finalistas, notas in enumerate (candidatos_aprovados):                          
        print(f' Resultados do candidato  aprovado ID {finalistas}: e{notas[0]}_t{notas[1]}_p{notas[2]}_s{notas[3]}')
            
imprime(lista_candidatos, lista_notas_minimas)