#include "varargs.h"
#include <stdio.h>
#include <stdarg.h>

EXPORT_SYMBOL unsigned long sum_ints( int count, ... ){
    va_list vl;
    unsigned long result = 0;
    va_start( vl, count );
    // Step through the list.
    for( int i = 0; i < count; ++i ){
        result += va_arg( vl, int );
    }
    va_end( vl );
    return result;
}
