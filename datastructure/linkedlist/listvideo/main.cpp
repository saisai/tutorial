#include <cstdlib>
#include "list.h"


using namespace std;

int main(int argc, char** argv) {

    List Paul;

    Paul.AddNode(3);
    Paul.AddNode(5);
    Paul.AddNode(7);

    Paul.PrintList();
    Paul.DeleteNode(5);
    Paul.PrintList();
    Paul.DeleteNode(1);
    Paul.DeleteNode(3);
    Paul.DeleteNode(7);
    Paul.PrintList();

    return 0;
}
