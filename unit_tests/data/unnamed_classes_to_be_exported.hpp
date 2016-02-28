// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __unnamed_enums_to_be_exported_hpp__
#define __unnamed_enums_to_be_exported_hpp__

#include "libconfig.h"

namespace unnamed_enums{

struct EXPORT_SYMBOL color{
    union{
        struct {
            float r,g,b,a;
        };
        float val[4];
    };
};

struct {
    int x;
} unnamed_struct_with_mem_var_x;

void EXPORT_SYMBOL do_smth( color ){}

}

#endif//__unnamed_enums_to_be_exported_hpp__
