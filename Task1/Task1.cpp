
#include "Task1.h"
#include <iostream>

using namespace std;

int main()
{
   int Result = 0;
    for (int i=1;i<1000;i++)
    {
        if ((i % 3 == 0) or (i % 5 == 0))
        {
            Result += i;
        }
    }
    cout<< Result;
}