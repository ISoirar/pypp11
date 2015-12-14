// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __enums_to_be_exported_hpp__
#define __enums_to_be_exported_hpp__

#include "libconfig.h"

enum EXPORT_SYMBOL Chisla{ nol, odin, dva, tri };

namespace enums{

enum EXPORT_SYMBOL color{
    red = 1
    , green = 2
    , blue = 4 };

enum EXPORT_SYMBOL numbers{
    zero = 0
    , noll = 0
};

struct EXPORT_SYMBOL struct_with_enum{
    enum fruits{
        lemon, orange, apple
    };
};

inline int EXPORT_SYMBOL to_int( int x=red ){ return x; }

}


#endif//__enums_to_be_exported_hpp__
