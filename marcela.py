# Exercício Python 30: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
MediaIdade = 0
SomaIdade = 0
HomemMaisvelho = 0
MaiorIdadeHomem = 0
MulheresMenor20 = 0

for item in range(1,5):
    nome = str(input(f'Insira o nome da {item}ª pessoa: '))
    idade = int(input('Insira a sua idade: '))
    sexo = str(input('Insira M para MASCULINO \n F para FEMININO: \n'))
    sexo = sexo.upper()

    SomaIdade += idade
MaiorIdadeHomem = idade
HomemMaisvelho = nome
    
if sexo == 'M' and idade == MaiorIdadeHomem:
    
      if sexo == 'F' and idade < 20:
        MulheresMenor20 += 1


MediaIdade = SomaIdade/4

print(f'A média de idade do grupo é de {MediaIdade} anos.')
print(f'O homem mais velho tem {MaiorIdadeHomem} anos e se chama {HomemMaisvelho}.')
print(f'Ao todo são {MulheresMenor20} mulheres com menos de 20 anos.')
