==================================
``input_static_matrix`` transformer
==================================

----------
Definition
----------

"input_static_matrix" transformer works on native static 2D arrays. It
handles the translation between `Python`_ object, passed as argument
that represent a sequence of sequences, and the matrix. The number of rows
and columns should be known in advance.

"input_static_matrix" transformer takes as first argument name or index of the
original function argument. The argument should have "array" or "pointer" type.
The second and the third arguments specify rows and columns size.

-----------
Limitations
-----------

This transformer could not be applied on virtual functions. 

-------
Example
-------

.. code-block:: c++

   template< int rows, int columns >
   int sum_impl( const int m[rows][columns] ){
       int result = 0;
       for( int r = 0; r < rows; ++r ){
           for( int c = 0; c < columns; ++c ){
               result += m[r][c];
           }
       }
       return result;
   }
   
   int sum( int m[2][3]){
       return sum_impl<2, 3>( m );
   }


In order to expose ``sum`` function we need to create a small wrapper:
The following :doc:`Py++ <../../../pyplusplus>` code does it for you:

  .. code-block:: python

     from pyplusplus import module_builder
     from pyplusplus import function_transformers as FT

     mb = module_builder.module_builder_t( ... )
     sum = mb.free_fun( 'sum' )
     sum.add_transformation( FT.input_static_matrix('m', rows=2, columns=3) )

What you see below is the relevant pieces of generated code:

  .. code-block:: c++

     #include "__convenience.pypp.hpp" //Py++ header file, which contains few convenience function

     namespace bp = boost::python;

     static boost::python::object sum_d4475c1b6a0ff117f0754ec5ecacdda3( boost::python::object m ){
         int native_m[2][3];
         pyplus_conv::ensure_uniform_sequence< boost::python::list >( m, 2 );
         for( size_t row = 0; row < 2; ++row ){
             pyplus_conv::ensure_uniform_sequence< int >( m[row], 3 );
             pyplus_conv::copy_sequence( m[row], pyplus_conv::array_inserter( native_m[row], 3 ) );
         }
         int result = ::ft::sum(native_m);
         return bp::object( result );
     }

     BOOST_PYTHON_MODULE(...){
         ...
        typedef boost::python::object ( *sum_function_type )( boost::python::object );
        
        bp::def( 
            "sum"
            , sum_function_type( &sum_d4475c1b6a0ff117f0754ec5ecacdda3 )
            , ( bp::arg("m") ) );
     }

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

