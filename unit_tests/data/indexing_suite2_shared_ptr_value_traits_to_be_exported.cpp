// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#include "indexing_suite2_shared_ptr_value_traits_to_be_exported.hpp"


namespace samples
{

boost::shared_ptr<A> func()
{
    return boost::shared_ptr<A>(new A());
}

std::vector<A> funcVector()
{
    std::vector<A> items;
    items.push_back(A());
    items.push_back(A());
    return items;
}

std::vector<boost::shared_ptr<A> > funcVectorShared()
{
    std::vector<boost::shared_ptr<A> > items;
    items.push_back(boost::shared_ptr<A>(new A()));
    items.push_back(boost::shared_ptr<A>(new A()));
    return items;
}

}

