#include <stdio.h>
#include <chrono>
#include <iostream>

int main() 
{
    for (int i = 0; i < 1000; i++)
    {
        auto begin = std::chrono::high_resolution_clock::now();

        std::cout << "Hello world!\n";

        //printf ("%s \n", "Hello world!");

        auto end = std::chrono::high_resolution_clock::now();

        auto elapsed_ms = std::chrono::duration_cast<std::chrono::microseconds>(end - begin);
        if (elapsed_ms.count() >= 1)
        {
           std::cout << "The time: " << elapsed_ms.count() << " micro sec\n";
        }
                
    }
    
    
    //printf ("The time: %d  milli sec\n", elapsed_ms.count());

    return 0;
}

