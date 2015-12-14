=============
this & sizeof
=============

-----------
The purpose
-----------

:doc:`Py++ <../../pyplusplus>` can expose a class ``sizeof`` and ``this`` pointer value to `Python`_.
I created this functionality without special purpose in mind.

-------
Example
-------

  .. code-block:: python

    mb = module_builder_t( ... )
    cls = mb.class_( <<<your class>>> )
    cls.expose_this = True
    cls.expose_sizeof = True

The `Python`_ class will contain two properties ``this`` and ``sizeof``. The usage
is pretty simple:

  .. code-block:: python

    import ctypes
    from <<<your module>>> import <<<your class>>> as data_t

    d = data_t()
    print d.this
    print d.sizeof


Warning: I hope you know what you are doing, otherwise don't blame me :-)

.. _`ctypes` : http://docs.python.org/lib/module-ctypes.html
.. _`from_address` : http://docs.python.org/lib/ctypes-data-types.html
.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

