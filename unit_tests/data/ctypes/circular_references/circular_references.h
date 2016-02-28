#include "libconfig.h"

struct foo_t;
struct bar_t;

typedef int (*foo_func_type)( struct foo_t* );
typedef int (*bar_func_type)( struct bar_t* );

struct EXPORT_SYMBOL foo_t{
    foo_func_type* f_foo;
    bar_func_type* f_bar;
};

struct EXPORT_SYMBOL bar_t{
    int a, b;
    struct foo_t foo;
};

void EXPORT_SYMBOL use_bar( bar_t* );
