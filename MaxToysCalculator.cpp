#include "MaxToysCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe MaxToysCalculator
// this file contains the definitions of the methods of the MaxToysCalculator class

using namespace std;

MaxToysCalculator::MaxToysCalculator()
{
}

int MaxToysCalculator::CalculateMaxToys(const vector<int>& Toys, int S) {
    int numToys = Toys.size();  // Nombre total de jouets
    int left = 0, sum = 0, maxNeighbors = 0;  // Initialisation des variables

    // Parcours des jouets avec une fenêtre glissante
    for (int right = 0; right < numToys; right++) {
        sum += Toys[right];  // Ajouter le prix du jouet actuel à la somme

        // Réduire la fenêtre si la somme dépasse le budget S
        while (sum > S && left <= right) {
            sum -= Toys[left];  // Retirer le jouet le plus à gauche
            left++;  // Déplacer la borne gauche de la fenêtre
        }

        // Mettre à jour la longueur maximale de la séquence valide
        maxNeighbors = max(maxNeighbors, right - left + 1);
    }

    return maxNeighbors;  // Retourner le nombre maximal de jouets consécutifs achetables
}
