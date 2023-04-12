# blackjack-couting

Vous pouvez améliorer le script en ajoutant la possibilité de spliter la premiere main quand celle ci est double.

Dans quelques semaines vous aurez la version devellopé avec dec _class_ et pourquoi pas une interface graphqiue avec PyGame :)

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
  
  
  
  -----------------------------------------
  
  A python script to learn Black Jack and Hi-Lo counting

    The Hi-Lo method is a card counting technique used in blackjack
    to help players determine whether the game is favorable for them or for
    the dealer.
    Card counting consists of assigning a value to each card according to the
    group to which it belongs. High value cards (10, J, Q, K, A) have
    a value of -1, low value cards (2, 3, 4, 5, 6) have a value
    of +1 and medium value cards (7, 8, 9) have no value. The player
    keeps a running count by adding the values of the cards that have been
    distributed during the game.

    The player starts the running count at 0 at the start of the game and adds or subtracts
    the value of each card that is dealt during the game. For example,
    if a 5 card is dealt, the player adds 1 to the running count, while
    that a card of K subtracts 1 from the running count.

    The higher the running count, the more low value cards that have
    been dealt, which means there are more high-value cards left in
    the clog. In this case, the player has an advantage and can increase his bet.
    Conversely, the lower the current count, the more cards with high
    value in the shoe, which increases the advantage of the dealer and the player
    Should reduce his bet.

    The Hi-Lo method is one of the most popular card counting techniques.
    popular in blackjack due to its simplicity and effectiveness.
    However, it is important to note that card counting is illegal in
    many casinos and may result in the player being expelled or banned from
    play. It is therefore important to understand the risks associated with this method.
    before using it.
