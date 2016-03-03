=====================================
``output_static_matrix`` transformer
=====================================

----------
Definition
----------

"output_static_matrix" transformer works on native 2D static arrays.
It handles the translation between a matrix and `Python`_ list object.
The matrix row and column sizes should be known in advance. 

"output_static_matrix" transformer takes as first argument name or index of the
original function argument. The argument should have "array" or "pointer"
type. The second and the third arguments specify rows and columns size.

-----------
Limitations
-----------

This transformer could not be applied on virtual functions. 


-------
Example
-------

.. code-block:: c++

   void filler( int m[2][3], int value ){
       for( int r = 0; r < 2; ++r ){
           for( int c = 0; c < 3; ++c ){
               m[r][c] = value;
           }
       }
   }

In order to expose ``filler`` function we need to create a small wrapper.
The following :doc:`Py++ <../../../pyplusplus>` code does it for you:

  .. code-block:: python

     from pyplusplus import module_builder
     from pyplusplus import function_transformers as FT

     mb = module_builder.module_builder_t( ... )
     filler = mb.free_fun( 'filler' )
     filler.add_transformation( ft.output_static_matrix('m', rows=2, columns=3) )

What you see below is the relevant pieces of generated code:

  .. code-block:: c++

     #include "__convenience.pypp.hpp" //Py++ header file, which contains few convenience function

     namespace bp = boost::python;

     static boost::python::object filler_7b0a7cb8f4000f0474aa44d21c2e4917( int value ){
         int native_m[2][3];
         boost::python::list py_m;
         ::ft::filler(native_m, value);
         for (int row = 0; row < 2; ++row ){
             boost::python::list pyrow;
             pyplus_conv::copy_container( native_m[row]
                                          , native_m[row] + 3
                                          , pyplus_conv::list_inserter( pyrow ) );
             py_m.append( pyrow ); 
         }
         return bp::object( py_m );
     }

     BOOST_PYTHON_MODULE(...){
         ...
        typedef boost::python::object ( *filler_function_type )( int );
        
        bp::def( 
            "filler"
            , filler_function_type( &filler_7b0a7cb8f4000f0474aa44d21c2e4917 )
            , ( bp::arg("value") ) );
     }

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

