// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __return_ref_to_ptr_to_be_exported_hpp__
#define __return_ref_to_ptr_to_be_exported_hpp__

struct number_t{
    int m_value;
};


struct numbers_t{
    numbers_t()
    : m_number( new number_t() )
    {}

    typedef number_t * value_type;
    const value_type& operator[]( int index ) const {
        return m_number;
    }
    number_t* m_number;
};


#endif//__return_ref_to_ptr_to_be_exported_hpp__
