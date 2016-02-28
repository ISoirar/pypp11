// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __indexing_suites2_to_be_exported_hpp__
#define __indexing_suites2_to_be_exported_hpp__

#include <vector>

struct foo{
    int bar;
};

typedef std::vector< foo > foo_vector;

foo_vector get_foos(){    
    return foo_vector();
}

#endif//__indexing_suites2_to_be_exported_hpp__
