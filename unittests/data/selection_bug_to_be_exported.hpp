// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __selection_bug_to_be_exported_hpp__
#define __selection_bug_to_be_exported_hpp__

#include "libconfig.h"
#include <stdio.h>

class A{
public:
   void g() { printf("A::g()\n"); }
   virtual void foo() = 0;
};

class B : public A{
   virtual void foo() { printf("B:foo()\n"); }
};

void free_func(A *a){
   a->foo();
}


#endif//__selection_bug_to_be_exported_hpp__
