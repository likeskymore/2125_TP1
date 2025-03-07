# Nom(s) étudiant(s) / Name(s) of student(s):

import sys

# Espace pour fonctions auxillaires :
# Space for auxilary functions :




# Fonction à compléter / function to complete:
def solve(nums1, nums2):
    # S'assurer que nums1 est le plus petit des deux tableaux
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)  # Tailles des deux listes
    low, high = 0, x  # Définition des bornes de recherche

    while low <= high:
        # Trouver la position de partition dans nums1 et nums2
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # Trouver les valeurs adjacentes à la partition
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        # Vérifier si la partition est correcte
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # Si le total est pair, la médiane est la moyenne des deux valeurs centrales
            if (x + y) % 2 == 0:
                return int((max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2)
            else:  # Si impair, la médiane est le plus grand des maxLeft
                return int(max(maxLeftX, maxLeftY))
        elif maxLeftX > minRightY:
            high = partitionX - 1  # Réduire la partitionX
        else:
            low = partitionX + 1  # Augmenter la partitionX

# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

# Ne pas modifier le code ci-dessous :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            lines = f.readlines() 
            l0 = list(map(int, lines[0].split()))    
            l1 = list(map(int, lines[1].split()))    

        return solve(l0,l1)
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q6.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()