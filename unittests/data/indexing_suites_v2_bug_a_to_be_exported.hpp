// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __indexing_suites_v2_bug_to_be_exported_hpp__
#define __indexing_suites_v2_bug_to_be_exported_hpp__

#include <vector>

namespace indexing_suites2 {

std::vector<double> create_vector(){
    std::vector<double> ret;
    for(size_t i = 0; i < 10; i++)
        ret.push_back(i);
    return ret;
}

}

namespace pyplusplus{ namespace aliases{
    typedef std::vector< double > numbers_t;
}}

#endif//__indexing_suites_v2_bug_to_be_exported_hpp__
