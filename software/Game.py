from pokemon import PokemonCapturado


class Game:


 print(f"Escolha seu pokemon inicial (números 1, 2 ou 3)")
contador = 0
while contador == 0:

    escolha = input()
    if escolha == 1:
       print(f"Seu inicial é o bulbassaur! Quer trocar? 1/Sim 2/Não")
       resposta = input()
       if resposta == 2:
          break
       if resposta == 1:
          
     




# Instanciando a classe Game
jogo = Game()

# Acessando o objeto PokemonCapturado dentro da classe Game
print(f"Pokemon capturado no jogo: HP={jogo.pokemon_capturado.hp}, Dano={jogo.pokemon_capturado.dano}, Nível={jogo.pokemon_capturado.nivel}, Tipo={jogo.pokemon_capturado.tipo}")