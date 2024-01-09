import random

couleurs = ("bleu", "rouge", "jaune", "vert")
sequence = []

def ajout(f):
    indice = random.randint(0, len(couleurs) - 1)
    couleur = couleurs[indice]
    f.append(couleur)
    return f

def afficher_sequence(f):
    print("Séquence à reproduire :")
    for i in range(len(f)):
        print(f"{i + 1}. {f[i]}")

def test_sequence(f):
    sequence_joueur = input("Entrez la séquence (entrez 'annuler' pour annuler la partie) : ").split()
    if sequence_joueur == ['annuler']:
        return False
    for i in range(len(f)):
        if f[i] != sequence_joueur[i]:
            return False
    return True

def main():
    print("Bienvenue dans le jeu Simon !")
    while True:
        ajout(sequence)
        afficher_sequence(sequence)
        if not test_sequence(sequence):
            print("Désolé, vous vous êtes trompé !")
            sequence = []
        else:
            print("Félicitations, vous avez réussi !")
            ajout(sequence)
            sequence = []

if __name__ == "__main__":
    main()