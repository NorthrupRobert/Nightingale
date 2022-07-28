// PUBLIC FUNCITONS



// PROTECTED FUNCTIONS



// PRIVATE FUNCTIONS
#include "dataset.h"
#include <iostream>

int main() {
    int myArray[] = {1, 2, 3, 4, 5, 6};

    std::cout << "ABOUT TO CONSTRUCT\n";
    dataset myDataset;
    std::cout << myDataset.mean << "\n";
    std::cout << "CONSTRUCTED\n";

    for (int i = 0; i < 6; i++)
        std::cout << myArray[i] << " ";

    return 0;
}

dataset::dataset() {
    std::cout << "\tDATASET DEFAULT CONSTRUCTOR\n";
    mean = 10.0f;
}