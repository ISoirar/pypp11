#include "libconfig.h"

struct EXPORT_SYMBOL data_t{
    int i;
    unsigned int j : 3;
};

EXPORT_SYMBOL int j;
EXPORT_SYMBOL data_t data;
EXPORT_SYMBOL data_t* data_ptr;

EXPORT_SYMBOL void init();
EXPORT_SYMBOL int get_value_j();
EXPORT_SYMBOL int get_value_data();
EXPORT_SYMBOL int get_value_data_p();
EXPORT_SYMBOL int get_value_data_j();


