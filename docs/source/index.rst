==============
`Py++11` package
==============

----------------
What is `Py++11`?
----------------
Definition:
  .. include:: ./definition.irest

`Py++11` uses a few different programming paradigms to help you expose C++
declarations in Python. This code generator will guide you through the whole 
process, raising warnings in the case you are doing something wrong, with a link
to the explanation. And the most importantly: it
will save you time. You will not have to update the code generator script every
time the source code is changed.

-----------------------
Code generation process
-----------------------

The code generation process consists of a few steps. The following paragraphs 
will tell you more about each step.

*"read declarations"*
---------------------

`Py++11` does not reinvent the wheel. It uses `GCC C++ compiler`_ to parse C++
source files. To be more precise, the tool chain looks like this:

1. Source code is passed to `GCC-XML`_

2. `GCC-XML`_ passes it to `GCC C++ compiler`_

3. `GCC-XML`_ generates an XML description of the C++ program from GCC's 
internal representation.

4. `Py++11` uses :doc:`pygccxml <http://pygccxml.readthedocs.org/en/develop/>` 
package to read the `GCC-XML`_ generated file.

The bottom line - you can be sure that all your declarations are read correctly.

.. _`GCC C++ compiler` : http://www.gnu.org/software/gcc

*"build module"*
-----------------

Only very small and simple projects can be exported as is. Most of the projects
still require human invocation. Basically there are 2 questions that you should
answer:

    1. Which declarations should be exported?
    2. How this specific declaration should be exported? Or, if I change the
       question a little, what code should be written in order for me to get 
       access from Python to that functionality?

Of course, `Py++11` cannot answer those question, but it provides as much help
as it can.

How can `Py++11` help you with the first question? `Py++11` provides very a
powerful and simple query interface. For example, in one line of code you can 
select all free functions that have two arguments, where the first argument has 
type ``int &`` and the type of the second argument is of any type:

.. code-block:: python

  mb = module_builder_t( ... ) # module_builder_t is the main class that
                               # will help you with code generation process
  mb.free_functions( arg_types=[ 'int &', None ] )

Another example - the developer wants to exclude all protected functions from
being exported:

.. code-block:: python

  mb = module_builder_t( ... )
  mb.calldefs( access_type_matcher_t( 'protected' ) ).exclude()

The developer can create custom criteria, for example exclude all declarations
with an 'impl' ( implementation ) string within the name:

.. code-block:: python

  mb = module_builder_t( ... )
  mb.decls( lambda decl: 'impl' in decl.name ).exclude()

Note the way the queries were built. You can think about those queries as
the rules, which will continue to work even after exported C++ code was changed.
It means that you don't have to change the code generator source code every 
time.

So far, so good. What about the second question? Well, by default `Py++11` 
generates code that will satisfy almost all developers. `Py++11` could be 
configured in many ways to satisfy your needs. But sometimes this is still not 
enough. There are use cases when you need full control over the generated code. 
One of the biggest problems with code generators in general is modifying 
generated code and preserving changes. How many code generators did you use or 
know that allow you to put your code anywhere or to reorder generated code as 
you wish? `Py++11` allows you to do that.

`Py++11` introduces new concepts: code creator and code creator tree. You can 
think about the code creator tree as some kind of `AST`_. The only difference is
that code creator trees provide more specific functionality. For example 
``include_t`` code creator is responsible to create C++ ``include`` directive 
code. You have full control over the code creator tree, before it is written to
disc. Here is an UML diagram of almost all code creators: `class diagram`_.

.. _`AST`: http://en.wikipedia.org/wiki/Abstract_syntax_tree
.. _`class diagram`: code_creators_uml.png

At the end of this step you have the code creator tree, which is ready to be 
written to disc.

*"write code to files"*
-----------------------
During this step `Py++11` reads the code creator tree and writes the code to
disc. The code generation process result should not be different from the one a
human would have created. For small projects, writing all code into single file 
is a good approach, however, for big ones the code should be splitted into
multiple files. `Py++11` implements both strategies.

-------------
Features list
-------------

* `Py++11` will supports almost all features found in `pybind11`_ library. It
  currently generates `Boost.Python` code.

* You can develop extension modules simultaneously using `Py++11`, especially
  when they share code.

* `Py++11` generates code, which will help you:

   * understand compiler generated error messages

   * minimize project built time

* `Py++11` has a couple of modes of writing code into files:

  * single file

  * multiple files

  * fixed set of multiple files

  * multiple files, where single class code is split to few files

* You have full control over generated code. Your code could be inserted almost
  anywhere.

* Your license is written at the top of every generated file.

* `Py++11` will check the "completeness" of the bindings. It will check for you
  that the exposed declarations don't have references to unexposed ones.

* `Py++11` provides enough functionality to extract source code documentation
  and write it as Python documentation string.

* `Py++11` provides a simple and powerful framework to create a wrapper for
  functions, which could not be exposed "as is" to `Python`_.

* ...

-------
License
-------

`Boost Software License`_.

---------------------------
Documentation contents
---------------------------

.. toctree::
   :maxdepth: 1

   documentation/tutorials/tutorials.rst
   quotes.rst
   download.rst
   documentation/index.rst
   examples/examples.rst
   links.rst
   comparisons/compare_to.rst
   peps/peps_index.rst
   troubleshooting_guide/lessons_learned.rst
   history/history.rst

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org
.. _`Boost Software License`: http://boost.org/more/license_info.html
