#include <iostream>
#include <string>
#include <cstdlib>

#include "hash.h"

using namespace std;

int main(int argc, char** argv) {


    hashtable Hashy;

    string name;
    //Hashy.PrintTable();

    Hashy.AddItem("Jack", "Balvenie");
    Hashy.AddItem("Dan", "McCallan");
    Hashy.AddItem("Randy", "Soju");
    Hashy.AddItem("Hugh", "Heineken");
    Hashy.AddItem("Rose", "Chardonnay");
    Hashy.AddItem("Kay", "Merlot");
    Hashy.AddItem("Sophia", "POG");
    Hashy.AddItem("Isabelle", "Water");
    Hashy.AddItem("Oreo", "Milk");
    Hashy.AddItem("Mother", "Ginger Ale");
   
    //Hashy.PrintTable();
    //
    /*
    while(name != "exit") {

        cout << "Search for ";
        cin >> name;
        if(name != "exit") {
            Hashy.FindDrink(name);
        }
    }
    */

    Hashy.PrintTable();
    while(name != "exit") {


        cout << "Remove ";
        cin >> name;
        if(name != "exit") {

            Hashy.RemoveItem(name);
        }
    }
    
    Hashy.PrintTable();
    //Hashy.PrintItemsInIndex(0);
    /*
    int index;

    hashtable hashObj;

    index = hashObj.Hash("Paula");

    cout << "index = " << index << endl;
    */
    return 0;
}

