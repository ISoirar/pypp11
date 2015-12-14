#include "char_ptr_as_binary_data.h"

EXPORT_SYMBOL data_t* get_empty(){
    data_t* x = new data_t();
    x->size = 0;
    x->bytes = 0;
    return x;
}

EXPORT_SYMBOL data_t* get_hello_world(){
    data_t* x = new data_t();
    x->size = 11;
    x->bytes = "hello\0world";
    return x;
}
