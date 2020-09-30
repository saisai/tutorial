#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;



#ifndef HASH_H
#define HASH_H

class hashtable {

private:
    //static const int tableSize = 40;
    static const int tableSize = 4;

    struct item {
        string name;
        string drink;
        item* next;
    };

    item* HashTable[tableSize];

    public:
        hashtable();

        int Hash(string key);
        void AddItem(string name, string drink);

        int NumberOfItemsInIndex(int index);
        void PrintTable();

        void PrintItemsInIndex(int index);
        void FindDrink(string name);

        void RemoveItem(string name);

        


};




#endif /* HASH_H */
