==============
Tutorials
==============

-------------
What is Py++?
-------------

.. include:: ./../../../definition.irest

--------
Preamble
--------

I guess you decided to try :doc:`Py++ <../../../pyplusplus>` API. Good! Lets start. First of all,
please take a look on two files:


* :doc:`hello_world.hpp <hello_world.hpp>` - C++ source code, that we want to export to Python


* :doc:`generate_code.py <generate_code.py>` - Python code, that uses :doc:`Py++ <../../../pyplusplus>` to export
  declarations from the source file

----------------
module_builder_t
----------------

:doc:`Py++ <../../../pyplusplus>` is built from a few packages, but there is only one package, you
should really to be familiar with - ``module_builder``. This package is some kind
of facade to low level API. It provides simple and intuitive API. The main
class within this package is ``module_builder_t``. The instance of this class will
guide you through the whole process.

-------------------------
module_builder_t.__init__
-------------------------

First of all, what is needed in order to create an instance of the class?

``module_builder_t.__init__`` methods take few arguments:

1. ``files`` - list of all C++ source files, that declarations from them, you want
   to expose. This is the only required parameter.

2. ``gccxml_path`` - path to `GCC-XML`_ binary. If you don't supply this argument
   :doc:`pygccxml <../../../../pygccxml/pygccxml>` will look for it using ``PATH`` environment variable.

There are some other arguments:

* additional include directories
* [un]defined symbols ( macros )
* intermediate results cache strategy configuration
* ...

Parsing of source files is done within this method. Post condition of this
method is that all declarations has been successfully extracted from the sources
files and you can start work on them.

--------------------------
Declarations customization
--------------------------
There are always declarations, which should not be exported or could not be
exported without human invocation. As you already saw from example, :doc:`Py++ <../../../pyplusplus>` provides
simple and powerful declarations query interface. By default, only the declarations
that belongs to the files, you have asked to parse, and to the files, that lies
in the same directories as parsed files, will be exported:
::

  project_root/
      details/
          impl_a.h
          impl_b.h
    include/
        a.h   //includes impl_a.h
        b.h   //includes impl_b.h
        all.h //includes a.h and b.h
  mb = module_builder( [ 'all.h' ] )

All declarations that belongs to ``include`` directory will be signed as included
to exporting. All other declarations will be ignored.

You can change the set of exported declarations by calling ``exclude`` or
``include`` methods, on declarations.

Basically, this is a second step of code generation process. During this step
you could/should/may change :doc:`Py++ <../../../pyplusplus>` defaults:

* to rename exposed declarations
* to include/exclude declarations
* to set call policies
* ...

I think it is critical for beginners to see what is going on, right?
``module_builder_t`` class has ``print_declarations`` method. You can print whole
declarations tree or some specific declaration. You will find a lot of useful
information there:

* whether the declaration is include\\excluded
* call policies
* warnings, :doc:`Py++ <../../../pyplusplus>` warns you about the declarations that have some "problems"
* ...

Very convenient, very useful.

-----------------------------------
module_builder_t.build_code_creator
-----------------------------------

Now it is a time to create module code creator. Do you remember, in introduction
to :doc:`Py++ <../../../pyplusplus>`, I told you that before writing code to disc, :doc:`Py++ <../../../pyplusplus>` will create some
kind of `AST`_. Well calling module_builder_t.build_code_creator function does this.
Right now, the only important argument to the function is ``module_name``.
Self explained, is it?


What is the main value of code creators? Code creators allow you to modify
code before it has been written to disk. For example one common requirement for
open source projects it to have license text within every source file. You can
do it with one line of code only:

.. code-block:: python

  mb.code_creator.license = <<<your license text>>>

After you call this function, I recommend you not to change declarations
configuration. In most cases the change will take effect, in some cases it will
not!

This tutorial is not cover code creators and how you should work with them.
I will write another tutorial.

.. _`AST`: http://en.wikipedia.org/wiki/Abstract_syntax_tree

-----------------------------
module_builder_t.write_module
-----------------------------

You have almost created your module. The last things left is to write module
code to file(s). You can do it with

* ``module_builder_t.write_module`` - you should provide file name, the code
  will be written in.

* ``module_builder_t.split_module`` - you should provide directory name.
  For big projects it is a must to minimize compilation time. So :doc:`Py++ <../../../pyplusplus>`
  splits your module source code to different files within the directory.

-----
Files
-----

.. toctree::

   hello_world.hpp.rest
   generate_code.py.rest
   generated.cpp.rest

That's all. I hope you enjoyed.

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`SourceForge`: http://sourceforge.net/index.php
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org

