// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __ft_inout_static_matrix_to_be_exported_hpp__
#define __ft_inout_static_matrix_to_be_exported_hpp__

#include <cmath>
#include <string>
#include <iostream>

namespace ft{
    
int sum_and_fill( int m[2][3], int value ){
    int result = 0;
    for( int r = 0; r < 2; ++r ){
        for( int c = 0; c < 3; ++c ){
            result += m[r][c];
            m[r][c] *= value;
        }
    }
    return result;
}

}

#endif//__ft_inout_static_matrix_to_be_exported_hpp__
