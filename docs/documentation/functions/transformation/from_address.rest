============================
``from_address`` transformer
============================

----------
Definition
----------

"from_address" transformer allows integration with :mod:`ctypes` package.
Basically it handles the translation between ``size_t`` value, which
represents a pointer to some data and the exposed code. Thus you can
use :mod:`ctypes` package to create the data and than pass it to the
`Boost.Python`_ exposed function.

    
"from_address" transformer takes as first argument name or index of the
"data" argument. The argument should have "reference" or "pointer" type.

-------
Example
-------

.. code-block:: c++

  unsigned long
  sum_matrix( unsigned int* matrix, unsigned int rows, unsigned int columns ){
      if( !matrix ){
          throw std::runtime_error( "matrix is null" );
      }
      unsigned long result = 0;
      for( unsigned int r = 0; r < rows; ++r ){
          for( unsigned int c = 0; c < columns; ++c ){
              result += *matrix;
              ++matrix;
          }
      }
      return result;
  }

In order to expose ``sum_matrix`` function we need to create a small wrapper.
The following :doc:`Py++ <../../../pyplusplus>` code does it for you:

  .. code-block:: python

     from pyplusplus import module_builder
     from pyplusplus import function_transformers as FT

     mb = module_builder.module_builder_t( ... )
     mb.free_function( 'sum_matrix' ).add_transformation( FT.from_address( 0 ) )

What you see below is the relevant pieces of generated code:

  .. code-block:: c++

     static boost::python::object sum_matrix_515b62fca9176ae4fffaf5fb118855dc( unsigned int matrix, unsigned int rows, unsigned int columns ){
         long unsigned int result = ::sum_matrix(reinterpret_cast< unsigned int * >( matrix ), rows, columns);
         return bp::object( result );
     }

     BOOST_PYTHON_MODULE(...){
         { //::sum_matrix
     
             typedef boost::python::object ( *sum_matrix_function_type )( unsigned int,unsigned int,unsigned int );
        
             bp::def( 
                 "sum_matrix"
                 , sum_matrix_function_type( &sum_matrix_515b62fca9176ae4fffaf5fb118855dc )
                 , ( bp::arg("matrix"), bp::arg("rows"), bp::arg("columns") )
                 , "documentation" );
         }
     }

And now the Python usage example:

  .. code-block:: python

     import ctypes
     import mymodule

     rows = 10
     columns = 7
     matrix_type = ctypes.c_uint * columns * rows
     sum = 0
     counter = 0
     matrix = matrix_type()
     for r in range( rows ):
        for c in range( columns ):
             matrix[r][c] = counter
             sum += counter
             counter += 1
     result = module.sum_matrix( ctypes.addressof( matrix ), rows, columns )


.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

