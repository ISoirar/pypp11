// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __indexing_suite_v1__to_be_exported_hpp__
#define __indexing_suite_v1__to_be_exported_hpp__

#include <vector>
#include "boost/shared_ptr.hpp"

typedef std::vector< boost::shared_ptr< unsigned short* > > ushort_sptr_ptr_t;

inline ushort_sptr_ptr_t get_empty(){
    ushort_sptr_ptr_t x;    
    typedef unsigned short ushort;
    ushort * y = new ushort(5);
    ushort ** yy = new ushort*( y ); 
    x.push_back( boost::shared_ptr< unsigned short* >( yy ) );
    return x;
}

#endif//__indexing_suite_v1__to_be_exported_hpp__
