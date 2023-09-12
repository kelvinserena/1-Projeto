from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)

#Criar uma data
lancamento_do_app = datetime(2024, 6, 17)
print(lancamento_do_app)
print(type(lancamento_do_app))

data_atual = datetime.now()
data_de_aniversario = datetime.strptime(input('Qual é a data do seu aniversário? '),'%d/%m/%Y')
dias_ate_aniversario = data_de_aniversario - data_atual
dias_ate_aniversario = str(dias_ate_aniversario)

print(f'Faltam {dias_ate_aniversario[:3]} dias')