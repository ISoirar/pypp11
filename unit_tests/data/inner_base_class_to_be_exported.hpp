// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __inner_base_class_to_be_exported_hpp__
#define __inner_base_class_to_be_exported_hpp__

struct foo1_t{
    struct foo2_t;
};

struct foo3_t : public foo1_t
{};

struct foo1_t::foo2_t : public foo3_t
{};

#endif//__inner_base_class_to_be_exported_hpp__
