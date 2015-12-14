#include <stdexcept>
#include <iostream>

namespace tests{

class listener {
    public:
        virtual void listen(int id, const std::string& name, int& skip) { 
            throw std::runtime_error ( std::string ("Virtual function listener::listen called!") ); 
        }
        virtual void listenPV(int id, const std::string& name, int& skip) = 0;
};

bool callListener ( listener* myListener) {
    int skip = 10;
    std::cout << "C++: Calling myListener->listen\n";
    myListener->listen(100, "test", skip);
    if (skip == 10)   
        throw std::runtime_error( "PROBLEM in C++: Called Returned with same value " );
    else 
        std::cout << "C++: Called OK " << skip <<"\n";

    return skip;
}


bool callListenerPV ( listener* myListener) {
    int skip = 10;
    std::cout << "C++: Calling myListener->listen\n";
    myListener->listenPV(100, "test", skip);
    if (skip == 10){   
        throw std::runtime_error( "PROBLEM in C++: Called Returned with same value " );
    }
    else 
        std::cout << "C++: Called OK " << skip <<"\n";
    return skip;
}


}
