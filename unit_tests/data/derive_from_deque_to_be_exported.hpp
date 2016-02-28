// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __derive_from_deque_to_be_exported_hpp__
#define __derive_from_deque_to_be_exported_hpp__

#include <iostream>
#include <vector>
#include <deque>


struct A{
    A(int a, int b)
    : a_(a),b_(b)
    {}

    int a_;
    int b_;

    int compute(){return a_ + b_;}
};

struct C : A{

    C(int a, int b)
    : A(a,b)
    {}
};

namespace pyplusplus{ namespace aliases{

    typedef std::deque< C > CDeque;
    void instantiate( std::deque<C> d){
    }
} }

struct F : public std::deque<C>
{
    F(){}
    int dlugosc() {return this->size();}
};

#endif//__derive_from_deque_to_be_exported_hpp__
