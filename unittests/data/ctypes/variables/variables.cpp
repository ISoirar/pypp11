#include "variables.h"

EXPORT_SYMBOL void init(){
    data.i = 1900;
    data.j = 7;
    data_ptr = new data_t();
    data_ptr->i = 11;
    j = 87;
}

EXPORT_SYMBOL int get_value_j(){
    return j;
}

EXPORT_SYMBOL int get_value_data(){
    return data.i;
}

EXPORT_SYMBOL int get_value_data_p(){
    return data_ptr->i;
}

EXPORT_SYMBOL int get_value_data_j(){
    return data.j;
}


