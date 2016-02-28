// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __ft_inout_static_array_to_be_exported_hpp__
#define __ft_inout_static_array_to_be_exported_hpp__

#include <cmath>
#include <string>
#include <iostream>


int sum_and_fill( int v[3], int value ){
    int result = v[0] + v[1] + v[2];
    v[0] = value;
    v[1] = value;
    v[2] = value;
    return result;
}

struct point3d_t{
    
    point3d_t()
    : x( 0 ), y(0), z(0)
    {}
        
    int initialize( int v[3] ){
        x = v[0];
        y = v[1];
        z = v[2];
        return x*y*z;
    }
    
    virtual void position( int v[3] ){
        v[0] = x;
        v[1] = y;
        v[2] = z;        
    }        

    void swap( int v[3] ){
        std::swap( x, v[0] );
        std::swap( y, v[1] );
        std::swap( z, v[2] );
    }

    virtual void swap_derived( int v[3] ){
        this->swap( v );
    }
    
    int x, y, z;
};


#endif//__ft_inout_static_array_to_be_exported_hpp__
