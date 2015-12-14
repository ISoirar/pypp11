#include "opaque.h"

user_data_t* create(){
    user_data_t *x = new user_data_t();
    x->i = 1977;
    return x;
};

int read_user_data(user_data_t* y){
    return y->i;
}

void destroy(user_data_t* x){
    delete x;
}

