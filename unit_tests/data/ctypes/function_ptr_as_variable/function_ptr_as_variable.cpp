#include "function_ptr_as_variable.h"

EXPORT_SYMBOL int execute_callback(struct info* info, int v) {
    return info->do_smth_fun(v);
}
