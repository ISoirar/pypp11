// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __indexing_suite2_shared_ptr_value_traits_to_be_exported_hpp__
#define __indexing_suite2_shared_ptr_value_traits_to_be_exported_hpp__

#include <vector>
#include <boost/shared_ptr.hpp>

namespace samples
{

class A
{};

boost::shared_ptr<A> func();

std::vector<A> funcVector();

std::vector<boost::shared_ptr<A> > funcVectorShared();

}

#endif//__indexing_suite2_shared_ptr_value_traits_to_be_exported_hpp__
