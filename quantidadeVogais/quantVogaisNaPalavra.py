# programa que le uma palavra e diz quantas vogais tem
from utils import contar_vogais  

palavra = str(input('digite uma palavra: '))
palavra = ' '.join(palavra.split())  
quantidade_vogais = contar_vogais(palavra)
print(f"A palavra '{palavra}' contém {quantidade_vogais} vogais.")
