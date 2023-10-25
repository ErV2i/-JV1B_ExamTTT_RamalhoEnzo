joueurgagnant = "joueur X"
#1.Écrire la fonction permettant d’afficher la grille de jeu

#crée une liste de 9 (3x3) qui contiadera les "X" ou "O" 😎
grille = [" "]*9

#crée la grille en imprimant la fonction grille et en sautant une ligne tout les 3 ligne du tableau
#définir ce tableau en def pour l'apeller chaque tours 
def morpion ():
   for i in range (9):
       if i==2 or i ==5:
        print(" ", (grille[i]))
       else: 
           print(" ", (grille[i]),end = '')


#2.Écrire la fonction permettant de jouer un O ou un X

#change l'endroit de la grille décider par le joueur par un X ou un O
def jouerX (placement):
   placement = int(input("C'est au joueur X de jouer, choisit un chiffre entre 1 et 9\n"))
   grille[placement-1] = "X"

def jouerO (placement):
   placement = int(input("c'est au joueur O de jouer, choisit un chiffre entre 1 et 9\n"))
   grille[placement-1] = "O"

#3.Écrire les fonctions vérifiant si oui ou non l’un des joueurs a réussi à aligner 3

#le joueur gagne si le meme symbole est aligner
def victoir ():
    rempli = [(0,1,2) or (3,4,5) or (6,7,8) or (0,3,6) or (1,4,7) or (2,5,8) or (0,4,8) or (6,4,2)]
    #on rencontrera un probleme car au début la partie est deja remplie d'espace ༼ つ ◕_◕ ༽つ


#4.Écrire la fonction vérifiant si la grille est complète

def complet ():
   
#5.Écrire un programme permettant de jouer à deux au Tic tac toe.

joueur = "X"
#faire un fonction while temps que la partie n'est pas terminer ou un joueur a gagner la partie tournera
partieEnCours = True
while partieEnCours == True:
    print(grille)
   #chaque tours la grille s'imprime pour connaitre l'états de la partie au fille du jeu 
    if victoir == False or complet == False:
    #vérifie chaque tours si la partie est terminer, si c'est pas le cas le joueur joue.
    else:
       partieEnCours = False
print("Bien jouer", joueurgagnant, "a gagner !")


#6 Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de Puissance 4 ?

#Pour transformer ce programme en puissance 4 nous aurons besoin d'abord d'agrandire la grille puis nous devrons faire en sorte 
#qu'il sois impossible de mettre un pion s'il y a rien en dessous ainsi qu'une condision de victoir d'au moins 4 et non de 3.
#pour simplifier le jeu il serais envisageable de faire choisire au joueur un chiffre seulement de 1 a 7 et non chaque case et de faire tomber les pion
#et de finir le programe eventuelement. (¬_¬)
