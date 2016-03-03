=====
Hints 
=====

----------------------------------
Class template instantiation alias
----------------------------------

:doc:`Py++ <../../pyplusplus>` has nice feature. If you define ``typedef`` for instantiated class 
template, than :doc:`Py++ <../../pyplusplus>` will use it as a `Python`_ class name.

For example:

.. code-block:: c++

  #include <vector>
  typedef std::vector< int > numbers;
  numbers generate_n(){
      ...
  }

:doc:`Py++ <../../pyplusplus>` will use "numbers" as Python class name:

.. code-block:: c++

  using boost::python;
  class_< std::vector< int > >( "numbers" )
      ...
  ;

:doc:`Py++ <../../pyplusplus>` will pick up the alias, only in case the class has single "typedef". 

``pyplusplus::aliases`` namespace
---------------------------------

The previous approach is "implicit" - :doc:`Py++ <../../pyplusplus>` does something behind the scene. 
Recently (version 0.8.6 ), another approach was introduced:

.. code-block:: c++

  #include <vector>
  
  namespace pyplusplus{ namespace aliases{
  //^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      typedef std::vector< int > numbers;
    
  } } //pyplusplus::aliases

The idea is that you create namespace with a special name - ``pyplusplus::aliases``
and :doc:`Py++ <../../pyplusplus>` automatically picks the class aliases from it. In case you accidentally 
introduced two or more different aliases to the same class, it will pick the 
longest one and print a warning. Other advantages of the approach:

* you are not forced to learn new API

* you continue to use your favorite editor and familiar language

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

