class PokemonCapturado(Pokemon):
    def __init__(self, hp, dano, ataques, nivel, tipo):
        super().__init__(hp, dano, ataques, nivel, tipo)
        self.ataques_capturados = []

    def ganharAtaque(self, novo_ataque):
        self.ataques_capturados.append(novo_ataque)

# Exemplo de utilização:
# Criando um PokemonCapturado
# pikachu = PokemonCapturado(hp=80, dano=25, ataques=['Choque do Trovão', 'Investida'], nivel=7, tipo='Elétrico')

# Usando métodos da classe Pokemon e PokemonCapturado
# print(f"Atributos do Pikachu: HP={pikachu.hp}, Dano={pikachu.dano}, Nível={pikachu.nivel}, Tipo={pikachu.tipo}")
# pikachu.ganharAtaque('Ataque Rápido')
# print(f"Ataques capturados do Pikachu: {pikachu.ataques_capturados}")