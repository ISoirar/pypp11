// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __refee_refer_to_be_exported_hpp__
#define __refee_refer_to_be_exported_hpp__

#include <memory>

struct refee_t{
    int i;
};

struct refer_t{
    refee_t& refee;
};

inline std::auto_ptr<refer_t> make_refer(refee_t* refee){
    refer_t tmp = { *refee };
    return std::auto_ptr<refer_t>(new refer_t(tmp));
}

#endif//__refee_refer_to_be_exported_hpp__
