===================================================
How to register ``shared_ptr<const T>`` conversion?
===================================================

------------
Introduction
------------

.. include:: ./definition.irest

---------
Solutions
---------

There are two possible solutions to the problem. The first one is to fix
Boost.Python library: `pointer_holder.hpp.patch` . The patch was contributed
to the library ( 8-December-2006 ) and some day it will be committed to the CVS.

It is also possible to solve the problem, without changing Boost.Python library:

  .. code-block:: c++

     namespace boost{

         template<class T>
         inline T* get_pointer( boost::shared_ptr<const T> const& p ){
             return const_cast< T* >( p.get() );
         }

     }

     namespace boost{ namespace python{

         template<class T>
         struct pointee< boost::shared_ptr<T const> >{
             typedef T type;
         };

     } } //boost::python

     namespace utils{

         template< class T >
         register_shared_ptrs_to_python(){
             namespace bpl = boost::python;
             bpl::register_ptr_to_python< boost::shared_ptr< T > >();
             bpl::register_ptr_to_python< boost::shared_ptr< const T > >();
             bpl::implicitly_convertible< boost::shared_ptr< T >, boost::shared_ptr< const T > >();
         }

     }

     BOOST_PYTHON_MODULE(...){
        class_< YourClass >( "YourClass" )
            ...;
        utils::register_shared_ptrs_to_python< YourClass >();
     }

The second approach is a little bit "evil" because it redefines ``get_pointer``
function for all shared pointer class instantiations. So you should be careful.

Files
-----

.. toctree::

  `solution.cpp` - C++ source file <solution.cpp.rest>
  Build script (SCons) <sconstruct.rest>
  Usage example/tester <test.py.rest>
  `pointer_holder.hpp.patch` Boost.Python library patch <pointer_holder.hpp.patch.rest>

--------
Download
--------

:download:`shared_ptr.zip`

