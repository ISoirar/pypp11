// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __ft_output_static_matrix_to_be_exported_hpp__
#define __ft_output_static_matrix_to_be_exported_hpp__

#include <cmath>
#include <string>
#include <iostream>

namespace ft{
    
void filler( int m[2][3], int value ){
    for( int r = 0; r < 2; ++r ){
    	for( int c = 0; c < 3; ++c ){
    		m[r][c] = value;
    	}
    }
}

}

#endif//__ft_output_static_matrix_to_be_exported_hpp__
