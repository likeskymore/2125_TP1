#include "CareerCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe CareerCalculator
// this file contains the definitions of the methods of the CareerCalculator class

using namespace std;

CareerCalculator::CareerCalculator()
{
}

bool CareerCalculator::CalculateMaxCareer(const vector<int>& Steps) {
    int maxReach = 0;  // Indique la position maximale atteignable
    int numSteps = Steps.size();  // Nombre total d'étapes

    // Parcours de chaque étape
    for (int i = 0; i < numSteps; i++) {
        if (i > maxReach) return false;  // Si on ne peut pas avancer, on retourne false

        // Mettre à jour la portée maximale atteignable
        maxReach = max(maxReach, i + Steps[i]);

        // Si on atteint ou dépasse la dernière étape, on retourne true
        if (maxReach >= numSteps - 1) return true;
    }

    return false;  // Si on ne peut pas atteindre la fin, on retourne false
}
