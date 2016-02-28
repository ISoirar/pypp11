// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __indexing_suites2_to_be_exported_hpp__
#define __indexing_suites2_to_be_exported_hpp__

#if defined( __GNUC__ )
    #include <ext/hash_set>
    #include <ext/hash_map>
    #define HASH_XXX_NS __gnu_cxx
#else
    #include <hash_set>
    #include <hash_map>
	#if defined( __GCCXML__ ) && !defined( __PYGCCXML_MSVC9__ )
		#define HASH_XXX_NS std
	#else
		#define HASH_XXX_NS stdext
	#endif//GCCXML
#endif

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

namespace indexing_suites2 {

typedef std::vector< std::string > strings_t;

inline void do_nothing( const strings_t& ){}

struct item_t{
    item_t() : value( -1 ){}
    explicit item_t( int v) : value( v ){}

    bool operator==(item_t const& item) const {
        return value == item.value;
    }

    bool operator!=(item_t const& item) const {
        return value != item.value;
    }

    int value;
};


typedef std::vector<item_t> items_t;

typedef std::vector<item_t*> items_ptr_t;
inline items_ptr_t create_items_ptr(){
    items_ptr_t items;
    items.push_back( new item_t(0) );
    items.push_back( new item_t(1) );
    items.push_back( new item_t(2) );
    items.push_back( new item_t(3) );
    items.push_back( new item_t(4) );
    return items;
}

inline item_t get_value( const std::vector<item_t>& vec, unsigned int index ){
    return vec.at(index);
}

inline void set_value( std::vector<item_t>& vec, unsigned int index, item_t value ){
    vec.at(index);
    vec[index] = value;
}

typedef std::vector<float> fvector;
fvector empty_fvector(){ return fvector(); }

HASH_XXX_NS::hash_map< int, int > get_int_mapping(){
    HASH_XXX_NS::hash_map< int, int > x;
    x[ 1 ] = 1;
    return x;
}

HASH_XXX_NS::hash_multimap< int, int > get_int_multimapping(){
    HASH_XXX_NS::hash_multimap< int, int > x;
    x.insert( HASH_XXX_NS::hash_multimap< int, int >::value_type( 1,1) );
    return x;
}

typedef std::map< std::string, std::string > name2value_t;
inline std::string get_first_name( name2value_t const * names ){
    if( !names ){
        return "";
    }
    else{
        return names->begin()->first;
    }
}


typedef std::multimap< int, int > multimap_ints_t;
inline multimap_ints_t create_multimap_ints(){
    return multimap_ints_t();
}

typedef std::set< std::string > set_strings_t;
inline set_strings_t create_set_strings(){
    return set_strings_t();
}

struct protected_item_t{
    protected_item_t() : value( -1 ){}
    explicit protected_item_t( int v) : value( v ){}

    int value;
protected:
    bool operator==(protected_item_t const& item) const {
        return value == item.value;
    }

    bool operator!=(protected_item_t const& item) const {
        return value != item.value;
    }
    
};


typedef std::vector<protected_item_t> protected_items_t;

typedef std::vector<protected_item_t> protected_items_ptr_t;
inline protected_items_t create_protected_items(){
    protected_items_t items;
    items.push_back( protected_item_t(0) );
    items.push_back( protected_item_t(1) );
    items.push_back( protected_item_t(2) );
    items.push_back( protected_item_t(3) );
    items.push_back( protected_item_t(4) );
    return items;
}

}

std::ostream& operator<<( std::ostream& o, const indexing_suites2::set_strings_t& x){
    for( indexing_suites2::set_strings_t::const_iterator index = x.begin(); index != x.end(); ++index ){
        o << *index << ',';
    }
    return o;
}

std::set<int> ffff( ) {
    return std::set<int>();
}


namespace pyplusplus{ namespace aliases{
    typedef std::vector<indexing_suites2::item_t*> items_ptr_t;
    typedef std::vector<indexing_suites2::protected_item_t*> protected_items_ptr_t;
}}

#endif//__indexing_suites2_to_be_exported_hpp__
