#include <iostream>
#include <string>
#include <cstdlib>

#include "hash.h"


using namespace std;


hashtable::hashtable()
{

    for(int i= 0; i < tableSize; i++) {
        HashTable[i] = new item;
        HashTable[i]->name = "empty";
        HashTable[i]->drink = "empty";
        HashTable[i]->next = NULL;

    }
}

void hashtable::AddItem(string name, string drink) {
    
    int index = Hash(name);
    if(HashTable[index]->name == "empty") {
        HashTable[index]->name = name; 
        HashTable[index]->drink = drink;
    } else {
        item* Ptr= HashTable[index];

        item* n = new item;

        n->name = name;
        n->drink = drink;
        n->next = NULL;

        while(Ptr->next != NULL)
        {
            Ptr = Ptr->next;
        }
        Ptr->next = n;
    }

}

int hashtable::NumberOfItemsInIndex(int index)
{
    int count = 0;

    if(HashTable[index]->name == "empty") {
        return count;
    } else {

        count++;
        item* Ptr = HashTable[index];
        while(Ptr->next != NULL) {

            count++;
            Ptr = Ptr->next;
        }


        
    }

    return count;
}


void hashtable::PrintTable() {
    int number;

    for(int i=0; i < tableSize; i++){

        number =NumberOfItemsInIndex(i);
        cout << "----------------\n";
        cout << "index = " << i << endl;
        cout << HashTable[i]->name << endl;
        cout << HashTable[i]->drink << endl;
        cout << "# of items = " << number << endl;
        cout << "------------------\n";
    }

}


void hashtable::PrintItemsInIndex(int index) {

    item* Ptr = HashTable[index];

    if(Ptr->name == "empty") {
        cout << "index = " << index << " is empty";
    }
    else {
        cout << "index " << index << " contains the following items\n";

        while(Ptr != NULL) {

            cout << "-----------------\n";
            cout << Ptr->name << endl;
            cout << Ptr->drink << endl;
            cout << "----------------\n";
            Ptr = Ptr->next;
        }
    }
}

void hashtable::FindDrink(string name)
{
    int index = Hash(name);

    bool foundName = false;
    string drink;

    item* Ptr = HashTable[index];

    while(Ptr != NULL){

        if(Ptr->name == name) {

            foundName = true;
            drink = Ptr->drink;

        }

        Ptr = Ptr->next;
    }

    if(foundName == true)
    {
        cout << "Favaorite drink = " << drink << endl;
    } else {

        cout << name << "'s info was not found int the HasH Table\n";
    }
}



void hashtable::RemoveItem(string name)
{

    int index = Hash(name);

    item* delPtr;
    item* P1;
    item* P2;

    // case 0 - bucket is empty
    if(HashTable[index]->name == "empty" && HashTable[index]->drink == "empty") {

        cout << name << " was not found in the Hast Table\n";

    }

    // Case 1  - only 1 item contained in bucket and that item hash matching name
    else if(HashTable[index]->name == name && HashTable[index]->next == NULL) {

        HashTable[index]->name = "empty";
        HashTable[index]->drink = "empty";
        cout << name << " was removed from the Hash Table\n";
    }

    // Case 2 - mathc is located in the first item in the bucket but there are
    // more items in the bucket
    else if(HashTable[index]->name == name) {

        delPtr = HashTable[index];
        HashTable[index] = HashTable[index]->next;
        delete delPtr;

        cout << name << " was removed from the Hash Table\n";

    }

    // Case 3 - bucket contains items but first item is not a match
    else {

        P1 = HashTable[index]->next;
        P2 = HashTable[index];

        while(P1 != NULL && P1->name != name) {

            P2 = P1;
            P1 = P1->next;
        }

        // case 3.1 - no match
        if(P1 == NULL) {
            cout << name << " was not found in the Hast Table\n";
        }

        // Case 3.2 - match is found
        else {

            delPtr = P1;
            P1 = P1->next;
            P2->next = P1;

            delete delPtr;
            cout << name << " was removed from the Hash Table\n";
        }
    }


}

int hashtable::Hash(string key) {

    int hash = 0;
    int index;

    index = key.length();

    for(int i=0; i < key.length(); i++)
    {
        //hash = hash + (int)key[i];
        //hash = (hash + (int)key[i]) * 17;
        hash = hash + (int)key[i];
        //cout << "hash = " << hash << endl;
    }

    index = hash % tableSize;

    return index;
}

