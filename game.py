from binascii import Error
"""
  Un script python pour apprend le black Jack et le comptage Hi-Lo

  La méthode Hi-Lo est une technique de comptage de cartes utilisée au blackjack
  pour aider les joueurs à déterminer si le jeu est favorable pour eux ou pour 
  le croupier.
  Le comptage des cartes consiste à attribuer une valeur à chaque carte selon le
  groupe auquel elle appartient. Les cartes à haute valeur (10, J, Q, K, A) ont 
  une valeur de -1, les cartes à faible valeur (2, 3, 4, 5, 6) ont une valeur 
  de +1 et les cartes à valeur moyenne (7, 8, 9) n'ont pas de valeur. Le joueur 
  tient un compte courant en ajoutant les valeurs des cartes qui ont été 
  distribuées au cours du jeu.

  Le joueur commence le compte courant à 0 au début du jeu et ajoute ou soustrait 
  la valeur de chaque carte qui est distribuée au cours de la partie. Par exemple, 
  si une carte de 5 est distribuée, le joueur ajoute 1 au compte courant, tandis 
  qu'une carte de K soustrait 1 au compte courant.

  Plus le compte courant est élevé, plus il y a de cartes à faible valeur qui ont 
  été distribuées, ce qui signifie qu'il reste plus de cartes à haute valeur dans 
  le sabot. Dans ce cas, le joueur a un avantage et peut augmenter sa mise. 
  À l'inverse, plus le compte courant est faible, plus il y a de cartes à haute 
  valeur dans le sabot, ce qui augmente l'avantage du croupier et le joueur 
  devrait diminuer sa mise.

  La méthode Hi-Lo est l'une des techniques de comptage de cartes les plus 
  populaires au blackjack en raison de sa simplicité et de son efficacité. 
  Cependant, il est important de noter que le comptage de cartes est illégal dans 
  de nombreux casinos et peut entraîner l'expulsion du joueur ou l'interdiction de 
  jouer. Il est donc important de comprendre les risques associés à cette méthode 
  avant de l'utiliser.

"""

import random

def space():
  """
    Cette fonction ajoute un séparateur lors des affichages texte 
    en console
  """
  print('')
  print('-'*50)
  print()



def proba(shoe, k_card):
  """
    Cette fonction calcul et affiche la probabilité de chaque carte en
    fonction du nobre restant dans le sabot
  """
  nb_rest = len(shoe)
  print(f"Le sabot contient {len(shoe)} cartes")
  for i in range(len(k_card)):
    nb_val = shoe.count(k_card[i])
    r = round((nb_rest/nb_val),2)
    print(f"---- {k_card[i]}  = {r} % de chance")



def read_count(count):
  """
    Cette fonction renvoit le compte du sabot en cours.
    Si le compte est proche de zéro : neutre
    Si le compte et positif le sabot est en votre faveur
    Si le compte est négatif le sabot est en faveur du croupier
  """
  if count >= 2:
    r = "Le total courant est de ",count,". C'est bénéfique pour vous. Vous devriez peut-être parier plus gros et prendre des risques supplémentaires."
  elif count >= 1:
    r = "Le total courant est de ",count,". C'est légèrement bénéfique pour vous. Vous pouvez peut-être parier un peu plus gros."
  elif count == 0:
    r="Le total courant est de ",count,". Il n'y a pas d'avantage pour l'un ou l'autre. Vous pouvez parier normalement."
  elif count <= -2:
    r="Le total courant est de ",count,". C'est fortement en faveur du croupier. Vous devriez peut-être parier moins et jouer de manière plus conservatrice."
  elif count <= -1:
    r="Le total courant est de ",count,". C'est légèrement en faveur du croupier. Vous devriez peut-être parier moins et jouer de manière plus conservatrice."
  print(r)


"""
  Création des dict pour les valeurs de la méthode Hi-Lo et création
  des cartes et de leurs valeurs.
  car_values = compte Hi-Lo
  card_game = valeur des cartes
  k_card = pour parcourir les cartes dans le script
"""

card_values = {
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1,
    "6": 1,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": -1,
    "J": -1,
    "Q": -1,
    "K": -1,
    "A": -1,
}

card_game = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}
k_card = {
    0: "2",
    1: "3",
    2: "4",
    3: "5",
    4: "6",
    5: "7",
    6: "8",
    7: "9",
    8: "10",
    9: "J",
    10: "Q",
    11: "K",
    12: "A"
}



"""
  Initialisation des variables de départ
  game_online = True/False ( demarrage du jeu)
  capital_depart
  mise = valeur de la somme engagé lors d'un tour
  step = compte le nombre de tour
  shoe = creation du sabot vide
  print = affiche la valeur du wallet de depard

"""
game_online = False
capital_depart = 100
mise = 0
step = 0
shoe = []
print(f"ton capital est de : {capital_depart} $")

"""
  Si le jeu n'a pas démarré, on demande la mise de depard du joueur
  Si input renvoit un entier inférieur ou égal à la valeur du wallet on commence
"""
while game_online == False: 
  try:
    mise = int(input("Combien voulez vous miser ? "))
    if (type(mise) == int) and (mise <= capital_depart) and (mise > 0):
      game_online = True
      break
    else:
      print(f"{mise} est supérieur a ton capital ( ou inf a 0)")
      mise = 0
  except ValueError:
    print("Désolé la valeur saisie n'est pas un nombre.")


"""
  la variable game_online renvoit TRUE, on rentre dans la boucle
  Si la mise est a 0 c'est un nouveau tour, on demande la mise
"""

while game_online: # si la mise est True on lance le jeu
  step+=1
  """
    Mise en forme des step
  """
  space()
  print(f"!!!!!!!!!!!!!!!!!!  TOUR {step} // ROUND {step} !!!!!!!!!!!!!!!!!!")
  print(f"Votre capital : {capital_depart} $")
  while mise == 0:  # si mise == 0 on demande une mise
    try:
      mise = int(input("Combien voulez vous miser ? "))
      if (type(mise) == int) and (mise <= capital_depart) and (mise > 0):
        break
      else:
        print(f"{mise} est supérieur a ton capital ou inf à zero)")
        mise = 0
    except ValueError:
      print("Désolé la valeur saisie n'est pas un nombre.")


  """
    Si le sabot est egal a zero , il faut lui mettre des cartes
    si il n'est pas egale a zero, la partie est en cours
  """
  if len(shoe) < 50:
    if (len(shoe) < 50) and (len(shoe) > 0):
      print(f"Merci d'avoir patientez. Le croupier vient de recharger le sabot. Faite vos jeux.")
    if (len(shoe) == 0):
      print(f"Le croupier vient de charger le sabot. Faite vos jeux.")
    for i in range(24):
        for card in card_values.keys():
            shoe.append(card)


  print(f"Le sabot contient {len(shoe)} cartes")

  # Mélanger le sabot de cartes
  random.shuffle(shoe)

  # Distribuer deux cartes au joueur et deux cartes au croupier supprimer les cartes de shoe
  player_cards = [shoe.pop(random.randrange(len(shoe))) for _ in range(2)]
  dealer_cards = [shoe.pop(random.randrange(len(shoe))) for _ in range(2)]

  # Initialiser le total courant
  count = 0
  
  space()
  # Afficher les deux cartes du joueur
  print(f"Votre main : {player_cards}") 
  # on affiche que une cartes du croupier (depuis la fin par facility)
  print(f"Main du croupier : {dealer_cards[1:]}")
  space()
  # On affiche les probabilitées des tirages versus le sabot
  proba(shoe, k_card)
  space()

  # Calculer le total courant en utilisant la méthode Hi-Lo

  for card in player_cards + dealer_cards[1:]: 
      count += card_values[card]

  # Demander au joueur de choisir une action
  while True:
      """
        varirable de test blackjack
        player_cards = ['K','A']
      """
      #si main du joueur blackjack
      if sum([card_game[card] for card in player_cards]) == 21:
        print(f"BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK ")
        print(f"BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK ")
        print(f"BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK BLACKJACK ")
        capital_depart += mise*2
        space()
        break
      # Afficher le total courant
      #read_count(count)
      #space()
      
      player_action = input("Voulez-vous tirer une carte (tapez 'h') ou rester (tapez 's') ? ")

      # Si le joueur choisit de tirer une carte
      if player_action == "h":
        space()
        card = shoe.pop(random.randrange(len(shoe)))
        player_cards.append(card)
        count += card_values[card]

        # Afficher les cartes du joueur et du croupier

        print(f"Cartes : {player_cards}")
        print("Main du croupier : {}".format([dealer_cards[0:]]))  # on affiche la carte du croupier deja tiré
        space()

        # Si le joueur dépasse 21, il perd la partie
        if sum([card_game[card] for card in player_cards]) > 21:
          print(f"Vous avez dépassé 21. Vous avez perdu la partie.")
          capital_depart -= mise
          print(f"Votre capital : {capital_depart} $")
          break

        # Afficher le total courant
        read_count(count)
        space()

      # Si le joueur choisit de rester
      elif player_action == "s":
        space()

        # Révéler la carte cachée du croupier et calculer son total
        dealer_total = sum([card_game[card] for card in dealer_cards])
        print("Main du croupier : {}".format([dealer_cards[0:]]))  # on affiche les dates du croupier

        #on a relever la carte du croupier on l'ajoute au count
        count += card_values[dealer_cards[0]] # on ajoute la carte 1 (index 0) au count

        # Tant que le total du croupier est inférieur à 17, il doit tirer une carte
        while dealer_total < 17:
          card = shoe.pop(random.randrange(len(shoe)))
          dealer_cards.append(card)
          if (card == 'A') and (sum([card_game[card] for card in player_cards]) > 21): # si il pioche AS et a un compte sup a 21 il compte 1 et pas 11 
            dealer_total += 1
            count += -1
          else:
            dealer_total += card_game[card]
            count += card_values[card]
      
          # Afficher les cartes du croupier
          print("TIRAGE = Main du croupier : {}".format([dealer_cards[0:]]))  # on affiche les cartes du croupier
          space()

        # Si le croupier dépasse 21, le joueur gagne
        if dealer_total > 21:
          print("Le croupier a dépassé 21. Vous avez gagné la partie.")
          capital_depart += mise*2

        # Si le joueur a un total plus élevé que le croupier, le joueur gagne
        elif sum([card_values[card] for card in player_cards]) > dealer_total:
          print("Votre total est plus élevé que celui du croupier. Vous avez gagné la partie.")
          capital_depart += mise*2
          space()

        # Si le joueur a un total inférieur ou égal à celui du croupier, le joueur perd
        else:
          print("Votre total est inférieur ou égal à celui du croupier. Vous avez perdu la partie.")
          capital_depart -= mise
          space()
        #on met la mise a 0 (partie win or loss)
        mise = 0
        if capital_depart == 0:
          game_online = False
          print(f"Vous avez tenu {step} tour(s) avant de vous faire RETK, bien joué :)")
        break
#CORNELIUS VINCENT - BLACKJACK COUNTING HI-LO !
      