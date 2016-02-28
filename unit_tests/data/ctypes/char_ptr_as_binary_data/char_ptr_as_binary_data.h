#include "libconfig.h"

struct EXPORT_SYMBOL data_t{
    unsigned int size;
    char const * bytes;
};

EXPORT_SYMBOL data_t* get_empty();
EXPORT_SYMBOL data_t* get_hello_world();


