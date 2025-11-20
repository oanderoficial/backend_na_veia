nome = "Anderson"
print(f"Olá, {nome}!")

# 1) Inserindo variáveis
nome = "Anderson"
idade = 25
print(f"Meu nome é {nome} e tenho {idade} anos.")

# 2) Operações dentro das chaves
a = 5
b = 3
print(f"A soma é {a + b}")

# 3) Formatando números (ex.: 1 casa decimal)
media = 6.8333
print(f"Média final: {media:.1f}")  # 6.8

# 4) Alinhamento e largura
print(f"{'Python':^20}")  # centraliza em 20 espaços
print(f"{'Python':>20}")  # alinha à direita
print(f"{'Python':<20}")  # alinha à esquerda
