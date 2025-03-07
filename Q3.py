# Nom(s) étudiant(s) / Name(s) of student(s):
# Trung Nguyen 20238006

import sys
import statistics

# Espace pour fonctions auxillaires :
# Space for auxilary functions :




# Fonction à compléter / function to complete:
def solve(numbers):
    listLength = len(numbers)

    # Si la liste contient moins de 2 nombres, aucun couple ne peut être formé
    if listLength < 2:
        return []

        # Calculer la médiane de la liste
    median = int(statistics.median(numbers))

    # Initialiser deux pointeurs et une liste vide pour stocker les paires valides
    left, right = 0, listLength - 1
    pairs = []

    # Utiliser une approche à deux pointeurs pour trouver les paires qui ont une somme égale à la médiane
    while left < right:
        pairSum = numbers[left] + numbers[right]

        if pairSum < median:
            left += 1  # Déplacer le pointeur gauche pour augmenter la somme
        elif pairSum > median:
            right -= 1  # Déplacer le pointeur droit pour diminuer la somme
        else:
            # Ajouter la paire valide à la liste des résultats
            pairs.append((numbers[left], numbers[right]))

            # Éviter les doublons en sautant les valeurs répétées
            leftVal, rightVal = numbers[left], numbers[right]
            while left < right and numbers[left] == leftVal:
                left += 1
            while left < right and numbers[right] == rightVal:
                right -= 1

    return pairs  # Retourner la liste des paires valides

# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            content = f.read()
        
        # Convert content into a list of integers
        numbers = list(map(int, content.split()))

        pairs = solve(numbers)

        return(len(pairs))

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q3.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()