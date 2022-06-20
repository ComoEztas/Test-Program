#include <iostream>
#include <fstream>
#include <chrono>
#include <string>
 
int main()
{
    std::string line;

    for (int i = 0; i < 1000; i++)
    {
        auto begin = std::chrono::steady_clock::now();

        std::ifstream in ("hello.txt", std::ios_base::in); 
        if (in.is_open())
        {
           
            while (getline(in, line))
        {
            std::cout << line << std::endl;
        }
            
        }
        in.close();

        auto end = std::chrono::steady_clock::now();

        auto elapsed_ms = std::chrono::duration_cast<std::chrono::microseconds>(end - begin);
        if (elapsed_ms.count() >= 1)
        {
            std::cout << "The time: " << elapsed_ms.count() << " micro sec\n";
    
        }
        
    }
    //system ("pause");
    return 0;
}