====================================
``inout_static_array`` transformer
====================================

----------
Definition
----------

``inout_static_array`` transformer is a combination of :doc:`input <input_static_array>`
and :doc:`output <output_static_array>` transformers.
It allows to call a C++ function, which takes an array using Python ``list`` class

"inout_static_array" transformer takes as first argument name or index of the
original function argument. The argument should have "array" or "pointer" type.
The second argument specifies the array size.

-------
Example
-------

.. code-block:: c++

   int sum_and_fill( int v[3], int value ){
       int result = v[0] + v[1] + v[2];
       v[0] = value;
       v[1] = value;
       v[2] = value;
       return result;
   }

In order to expose ``sum_and_fill`` function we need to create a small wrapper.
The following :doc:`Py++ <../../../pyplusplus>` code does it for you:

  .. code-block:: python

     from pyplusplus import module_builder
     from pyplusplus import function_transformers as FT

     mb = module_builder.module_builder_t( ... )
     sum_and_fill = mb.free_fun( 'sum_and_fill' )
     sum_and_fill.add_transformation( ft.inout_static_array('v', 3) )

What you see below is the relevant pieces of generated code:

  .. code-block:: c++

     static boost::python::tuple sum_and_fill_2dd285a3344dbf7d71ffb7c78dd614c5( boost::python::object v, int value ){
         int native_v[3];
         boost::python::list py_v;
         pyplus_conv::ensure_uniform_sequence< int >( v, 3 );
         pyplus_conv::copy_sequence( v, pyplus_conv::array_inserter( native_v, 3 ) );
         int result = ::sum_and_fill(native_v, value);
         pyplus_conv::copy_container( native_v, native_v + 3, pyplus_conv::list_inserter( py_v ) );
         return bp::make_tuple( result, py_v );
     }
     
     BOOST_PYTHON_MODULE(ft_inout_static_array){
         { //::ft::sum_and_fill
         
             typedef boost::python::tuple ( *sum_and_fill_function_type )( boost::python::object,int );
        
             bp::def( 
                      "sum_and_fill"
                      , sum_and_fill_function_type( &sum_and_fill_2dd285a3344dbf7d71ffb7c78dd614c5 )
                      , ( bp::arg("v"), bp::arg("value") ) );
         }
     }

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

