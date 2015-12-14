=========
Tutorials
=========

.. toctree::

  module_builder/module_builder.rest
  pyplusplus_gui.rest

-------------
What is Py++?
-------------

.. include:: ./../../definition.irest

-------------------
Graphical interface
-------------------
:doc:`Py++ <../../pyplusplus>` includes a :doc:`graphical interface <pyplusplus_gui>`. :doc:`Graphical interface <pyplusplus_gui>` is invoked
with the ``pyplusplus_gui`` command, or with ``pyplusplus_gui.pyw`` from the
``scripts`` subdirectory, of the `Python`_ installation directory.

My advise to you - start with :doc:`graphical interface <pyplusplus_gui>`, because:

  * you don't have to learn new API

  * few clicks with mouse and you have `Boost.Python`_ code for your file(s)

  * it is very easy to evaluate :doc:`Py++ <../../pyplusplus>` using it

  * you can check whether `GCC-XML`_ is able to compile your code or not

  * you can use it as a guide to `Boost.Python`_ library

  * it is able to generate :doc:`Py++ <../../pyplusplus>` code for you

---------------
Getting started
---------------

I suppose you decided to do some coding with :doc:`Py++ <../../pyplusplus>`. 
:doc:`Module builder <module_builder/module_builder>` tutorials will help you.

--------
Advanced
--------

To be written. I think I should cover here the usage of code creators and code
creators tree. Meanwhile you can take a look on the content of
``examples/custom_code_creator`` directory. It contains example, which shows how
to create your own code creator. To be more specific, it exposes ``get*`` and
``set*`` methods as a single property.


.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`SourceForge`: http://sourceforge.net/index.php
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

