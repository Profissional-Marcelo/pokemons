class Pokemon:
    def __init__(self, hp, dano, ataques, nivel, tipo):
        self.hp = hp
        self.dano = dano
        self.ataques = ataques
        self.nivel = nivel
        self.tipo = tipo

    def ganharXp(self, quantidade):
        self.nivel += quantidade
    
    def perderHP(self, quantidade):
        self.hp -= quantidade

# charmander = Pokemon(hp=100, dano=20, ataques=['Brasas', 'Garra'], nivel=5, tipo='Fogo')




# Usando métodos da classe Pokemon
# charmander.perderHP(10)
# charmander.ganharXp(2)

# print(f"Nível do Charmander: {charmander.nivel}")
# print(f"HP restante do Charmander: {charmander.hp}")