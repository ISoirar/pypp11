// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __ft_input_static_matrix_to_be_exported_hpp__
#define __ft_input_static_matrix_to_be_exported_hpp__

#include <cmath>
#include <string>
#include <iostream>

namespace ft{
    
template< int rows, int columns >
int sum_impl( const int m[rows][columns] ){
    int result = 0;
    for( int r = 0; r < rows; ++r ){
    	for( int c = 0; c < columns; ++c ){
    		result += m[r][c];
    	}
    }
    return result;
}

int sum( int m[2][3]){
	return sum_impl<2, 3>( m );
}

int sum_const( int m[2][3]){
	return sum_impl<2, 3>( m );
}

struct matrix_sum_t{
    virtual int calculate( const int m[3][5] ) const{
    	return sum_impl<3,5>( m );
    }
};

}

#endif//__ft_input_static_matrix_to_be_exported_hpp__
