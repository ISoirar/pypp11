===============================
Generated file name is too long
===============================

**Generated file name is too long**

There are use cases, when :doc:`Py++ <../../pyplusplus>` generated file name is too long. In some cases
the code generation process even fails because of this.

This is just a symptom of the problem. This happens when you expose template
instantiated classes and you did not specify the class alias. :doc:`Py++ <../../pyplusplus>` uses a class
alias as a basis for the file name.

Let me explain.

.. code-block:: c++

  template < class T>
  struct holder{ ... };

As you know, a class name in `Python`_ has few `constraints`_ and :doc:`Py++ <../../pyplusplus>` is aware
of them. "holder< int >" is illegal class name, so :doc:`Py++ <../../pyplusplus>` will generate another
one - "holder_less_int_greater\_". Pretty ugly and even long, but at least it is
legal one.

.. _`constraints` : http://www.python.org/doc/2.5.2/ref/identifiers.html

It is pretty simple to change the alias of the class, or any other declaration:

.. code-block:: python

  from pyplusplus import module_builder

  mb = module_builder_t( ... )
  holder = mb.class_( 'holder< int >' )
  holder.alias = 'IntHolder'
  #the following line has same effect as the previous one:
  holder.rename( 'IntHolder' )

Another solution to the problem, is to use different strategy to split the generated
code to files. You can read more about splitting files :doc:`here <../split_module>`.

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org
