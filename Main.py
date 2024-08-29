import datetime
import csv
    
def getData(ind1, ind2):
    with open('grade.csv', newline='', encoding='utf-8') as csvfile:
        grade = csv.DictReader(csvfile)
        for row in grade:
            if row['ind1'] == ind1 and row['ind2'] == ind2:
                return row['aula'], row['sala'], row['professor']

def changeData():
    return 0

def exibirAulas(hoje):
    if dia_sem > 5:
        print('Hoje não tem aula! :D')
    else:
        if hoje:
            aula, sala, professor = getData(str(dia_sem), '1')
            aula2, sala2, professor2 = getData(str(dia_sem), '2')
            print('-'*50, '\nA primeira aula será', aula, 'professor', professor, 'sala:', sala)
            print('-'*50, '\nA segunda aula será', aula2, 'professor', professor2, 'sala:', sala2)
        else:
            dia = str(input('Insira o dia desejado, entre 0 e 7, sendo 0 segunda-feira:'))
            aula, sala, professor = getData(str(dia), '1')
            aula2, sala2, professor2 = getData(str(dia), '2')
            print('-'*50, '\nA primeira aula será', aula, 'professor', professor, 'sala:', sala)
            print('-'*50, '\nA segunda aula será', aula2, 'professor', professor2, 'sala:', sala2)
            
        

def menu():
    print('\nSeja bem-vindo ao ClassClock!\nAqui você consegue visualizar a sua grade de aulas\nFavor selecionar o que deseja fazer em seguida:')
    print('-'*50)
    print('\n1 - Exibir aulas de hoje;\n2 - Exibir aulas de um dia específico;\n3 - Alterar suas aulas;')
    escolha = int(input(':'))
    match escolha:
        case 1:
            exibirAulas(True)
        case 2:
            exibirAulas(False)
        case 3:
            return 0 
data_d = datetime.date.today() #Define a data atual no formato aaaa.mm.dd
dia_num = data_d.strftime("%d/%m/%Y") #Converte a data para dd.mm.aaaa
dia_sem = data_d.weekday() #Vincula o dia da semana à um número, 0-7 Seg-Dom

dia_ext = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"][dia_sem] 
#Define o dia da variável de acordo com o número definido na variável acima
#Valores da variável é definido com base no valor textual do 1º colchete, escolhido pelo valor numérico no 2º colchete 

menu()


    

# running = 1
# while running == 1:

#     s_dej = input("Insira a semana desejada: \n"); 

#     print('Hoje é:','\n',dia_ext,'\n',dia_num,'\n')

#     if dia_sem == 0 :
#         print ("Hoje as aulas são:"'\n',a01, '\n', a02)
#     elif dia_sem == 1:
#         print ("Hoje as aulas são:"'\n',a11, '\n', a12)
#     elif dia_sem == 2:
#         print ("Hoje as aulas são:"'\n',a21, '\n', a22)
#     elif dia_sem == 3:
#         print ("Hoje as aulas são:"'\n',a31, '\n', a32)
#     elif dia_sem == 4:
#         print ("Hoje as aulas são:"'\n',a41, '\n', a42)
#     else:
#         print ("Hoje não tem aula!! :D", '\n')
    
#     while running == 1:
#         running = input("Deseja encerrar? (S ou N): ")

#         if running == "S":
#             running = 0
    
#         elif running =="N":
#             running = 1    
        
#         else: 
#             print("Valor inválido!")

#     print(running) 