==============================================================
Fatal error C1204: compiler limit: internal structure overflow
==============================================================

**Fatal error C1204: compiler limit: internal structure overflow**

If you get this error, than the generated file is too big. You will have to split
it to few files. Well, not you but :doc:`Py++ <../../pyplusplus>`, you will only have to tell it to do
that.

If you are using ``module_builder_t.write_module`` method, consider to switch
to ``module_builder_t.split_module``.

If you are using ``split_module``, but still the generated code for some class
could not be compiled, because of the error, you can ask :doc:`Py++ <../../pyplusplus>` to split the
code generated for class to be split to few source files.

For more information, considre to read the :doc:`splitting generated code to files <../split_module>`
document.

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org
