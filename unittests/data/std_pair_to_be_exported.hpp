// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __std_pair_to_be_exported_hpp__
#define __std_pair_to_be_exported_hpp__

#include <utility>

struct tester_t{
    tester_t(int a, int b){
       pair_.first = a;
       pair_.second = b;
    }

    int compute(){return pair_.first + pair_.second;}

    std::pair<int, int> pair_;
};
#endif//__std_pair_to_be_exported_hpp__

