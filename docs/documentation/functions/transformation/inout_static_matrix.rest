====================================
``inout_static_matrix`` transformer
====================================

----------
Definition
----------

``inout_static_matrix`` transformer is a combination of :doc:`input <input_static_matrix>`
and :doc:`output <output_static_matrix>` transformers.
It allows to call a C++ function, which takes 2D array using Python ``list`` class

"input_static_matrix" transformer takes as first argument name or index of the
original function argument. The argument should have "array" or "pointer" type.
The second and the third arguments specify rows and columns sizes.

-----------
Limitations
-----------

This transformer could not be applied on virtual functions. 

-------
Example
-------

.. code-block:: c++

  int sum_and_fill( int m[2][3], int value ){
      int result = 0;
      for( int r = 0; r < 2; ++r ){
          for( int c = 0; c < 3; ++c ){
              result += m[r][c];
              m[r][c] *= value;
          }
      }
      return result;
  }

In order to expose ``sum_and_fill`` function we need to create a small wrapper.
The following :doc:`Py++ <../../../pyplusplus>` code does it for you:

  .. code-block:: python

     from pyplusplus import module_builder
     from pyplusplus import function_transformers as FT

     mb = module_builder.module_builder_t( ... )
     sum_and_fill = mb.free_fun( 'sum_and_fill' )
     sum_and_fill.add_transformation( ft.inout_static_matrix('m', rows=2, columns=3) )

What you see below is the relevant pieces of generated code:

  .. code-block:: c++

     static boost::python::tuple sum_and_fill_ec4892ec81f672fe151a0a2caa3215f4( boost::python::object m, int value ){
         int native_m[2][3];
         boost::python::list py_m;
         pyplus_conv::ensure_uniform_sequence< boost::python::list >( m, 2 );
         for( size_t row = 0; row < 2; ++row ){
             pyplus_conv::ensure_uniform_sequence< int >( m[row], 3 );
             pyplus_conv::copy_sequence( m[row], pyplus_conv::array_inserter( native_m[row], 3 ) );
         }
         int result = ::ft::sum_and_fill(native_m, value);
         for (int row2 = 0; row2 < 2; ++row2 ){
             boost::python::list pyrow;
             pyplus_conv::copy_container( native_m[row2]
                                          , native_m[row2] + 3
                                          , pyplus_conv::list_inserter( pyrow ) );
             py_m.append( pyrow ); 
         }
         return bp::make_tuple( result, py_m );
     }
     
     BOOST_PYTHON_MODULE(ft_inout_static_matrix){
         { //::ft::sum_and_fill
         
             typedef boost::python::tuple ( *sum_and_fill_function_type )( boost::python::object,int );
             
             bp::def( 
                 "sum_and_fill"
                 , sum_and_fill_function_type( &sum_and_fill_ec4892ec81f672fe151a0a2caa3215f4 )
                 , ( bp::arg("m"), bp::arg("value") ) );
         
         }
     }

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

