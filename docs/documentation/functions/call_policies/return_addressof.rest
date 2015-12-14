================
return_addressof
================

----------
Definition
----------

Class ``return_addressof`` is a model of `ResultConverterGenerator`_  which
can be used to wrap C++ functions returning any pointer, such that the pointer
value is converted to ``unsigned int`` and it is copied into a new Python object.

This call policy was created to be used with ``ctypes`` package and provide access
to some raw\\low level data, without creating wrappers.

Pay attention: you have to manage the memory by your own.

-------
Example
-------

.. code-block:: c++

  int* get_value(){
      static int buffer[] = { 0,1,2,3,4 };
      return buffer;
  }

  namespace bpl = boost::python;
  BOOST_PYTHON_MODULE(my_module){
    def( "get_value"
         , bpl::return_value_policy< pyplusplus::call_policies::return_addressof<> >() );
  }

The :doc:`Py++ <../../../pyplusplus>` code is not that different from what you already know:

.. code-block:: python

  from pyplusplus import module_builder
  from pyplusplus.module_builder import call_policies

  mb = module_builder.module_builder_t( ... )
  mb.free_function( return_type='float *' ).call_policies \
      = call_policies.return_value_policy( call_policies.return_addressof )

Python code:

.. code-block:: python

  import ctypes
  import my_module

  buffer_type = ctypes.c_int * 5
  buffer = buffer_type.from_address( my_module.get_value() )
  assert [0,1,2,3,4] == list( buffer )

.. _`ResultConverterGenerator` : http://boost.org/libs/python/doc/v2/ResultConverter.html#ResultConverterGenerator-concept

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

