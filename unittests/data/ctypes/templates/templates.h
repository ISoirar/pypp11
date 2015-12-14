#include "libconfig.h"

template< class ValueType >
struct value_t{
    ValueType get_value(){ return value;}
    ValueType value;
};

void EXPORT_SYMBOL init( value_t<int>& );

template class EXPORT_SYMBOL value_t<int>;
