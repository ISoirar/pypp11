#include "libconfig.h"
#include <stdio.h>

typedef int do_smth_fun_t(int);

struct EXPORT_SYMBOL info {
   do_smth_fun_t* do_smth_fun;
};

EXPORT_SYMBOL int execute_callback(struct info* info, int);

