// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __operators_to_be_exported_hpp__
#define __operators_to_be_exported_hpp__

#include "boost/rational.hpp"
#include <iostream>
#include <vector>

namespace pyplusplus{ namespace rational{

typedef boost::rational< long int > pyrational;

struct helper{

    void instantiate(){
        sizeof( pyrational );
        boost::gcd<long int>( 1, 1);
        boost::lcm<long int>( 1, 1);
        std::cout << pyrational( 1,1);
        pyrational x(1,1);
        x = pyrational( 2, 3 );

    }
};

struct XXX{
    friend std::ostream& operator<<(std::ostream& s, XXX const& x);
};

inline std::ostream& operator<<(std::ostream& s, XXX const& x){
    return s << "<XXX instance at " << &x << ">";
}

//Boost.Python does not support member operator<<
struct YYY{
    std::ostream& operator<<(std::ostream& s) const{
        return s;
        //return s << "<YYY instance at " << reinterpret_cast<unsigned long>( this )<< ">";
    }
};

typedef std::vector< pyrational > rationals_t;

inline rationals_t&
operator+=( rationals_t& v, const pyrational& n ){
    for( rationals_t::iterator i = v.begin(); i != v.end(); ++i ){
        *i += n;
    }
    return v;
}

inline rationals_t create_randome_rationals(){
    return rationals_t();
}


} }


namespace Geometry{

    namespace PointsUtils{
        struct VecOfInts{};
    }

    class Class {
        int i;
    };

    //this one should not be generated
    extern PointsUtils::VecOfInts&
    operator += ( PointsUtils::VecOfInts &vec, const Class&){
        return vec;
    }
}

namespace Geometry2{

    namespace PointsUtils2{
        typedef std::vector<int> VecOfInts2;
    }

    class Class2 {
        int i;
    };

    extern PointsUtils2::VecOfInts2&
    operator += ( PointsUtils2::VecOfInts2 &vec, const Class2&){
        return vec;
    }
}

#endif//__operators_to_be_exported_hpp__
