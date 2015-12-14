===========================
How to deal with templates?
===========================

------------
Introduction
------------

I would like to introduce the following piece of code. I am going to use it for most exlanations.

.. code-block:: c++

   // file point.h
   template< class T>
   struct point_t{
       T x, y;
   };

   template <class T>
   double distance( const point_t<T>& point ){
       return sqrt( point.x * point.x + point.y*point.y );
   }

   struct environment_t{
      ...
      template< class T>
      T get_value(const std::string& name);
      ...
   };

----------------------
Template instantiation
----------------------

First of all you should understand, that you can not export template itself, but
only its instantiations.

You can instantiate template class using operator ``sizeof``:

.. code-block:: c++

   sizeof( point_t<int> );


In order to instantiate a function you have to call it:

.. code-block:: c++

   void instantiate(){
       double x = distance( point_t<t>() );

       environment_t env;
       std::string path = env.get_value< std::string >( "PATH" );
       int version = env.get_value< int >( "VERSION" );
   }

You should put that code in some header file, parsed by GCC-XML.

"Dynamic" instantiation
-----------------------
If you have a template class, which should be instantiated with many types, you
can create a small code generator, which will "instantiate the class". It is
pretty easy to blend together the generated code and the existing one:

.. code-block:: python

   from module_builder import module_builder_t, create_text_fc

   def generate_instantiations_string( ... ):
      ...

   code = generate_instantiations_string( ... )

   mb = module_builder_t( [ create_text_fc( code ), <<<other file names>>> ], ... )
   ...

Function ``create_text_fc`` allows you to extract declarations from the string,
which contains valid C++ code. It creates temporal header file and compiles it.

----------------------------------
Functions templated on return type
----------------------------------

.. code-block:: c++

   environment_t env;
   std::string path = env.get_value< std::string >( "PATH" );
   int version = env.get_value< int >( "VERSION" );


`GCC-XML`_ provides information for both instantiations:

    * ``get_value<int>``

    * ``get_value< std::string >``

But, in this case there is a catch: the name of both functions is "**get_value**".
The only difference is "return type".

In this situation, :doc:`Py++ <../../pyplusplus>` will generate code that contains errors. If your are
lucky, it depends on the compiler you use, the generated code will not compile.
Otherwise, you will discover the errors while testing the bindings.

Generated code:

.. code-block:: c++

  bp::class_< environment_t >( "environment_t" )
      ...
      .def( "get_value"
            , (int ( ::environment_t::* )( ::std::string const & ) )( &::environment_t::get_value ) )
      .def( "get_value"
            , (::std::string ( ::environment_t::* )( ::std::string const & ) )( &::environment_t::get_value ) );

The correct code:

.. code-block:: c++

  bp::class_< environment_t >( "environment_t" )
      .def( "get_value"
            , (int ( ::environment_t::* )( ::std::string const & ) )( &::environment_t::get_value< int > ) )
            //--------------------------------------------------------------------------^^^^^^^^^^^^^^^^
      .def( "get_value"
            , (::std::string ( ::environment_t::* )( ::std::string const & ) )( &::environment_t::get_value< std::string > ) );
            //------------------------------------------------------------------------------------^^^^^^^^^^^^^^^^^^^^^^^^

The perfect one:

.. code-block:: c++

  bp::class_< environment_t >( "environment_t" )
      ...
      .def( "get_value", &::environment_t::get_value< int > )
      .def( "get_value", &::environment_t::get_value< std::string > );


Work-around
-----------

:doc:`Py++ <../../pyplusplus>` contains a work-around to the problem:

.. code-block:: python

   mb = module_builder_t( ..., optimize_queries=False, ... )
   environment = mb.class_( "environment_t" )
   for f in environment.member_functions( "get_value" ):
       #set the function alias
       f.alias = f.name + "_" + f.return_type.decl_string
       #correct function name
       f.name = f.demangled_name
   #you still want the queries to run fast
   mb.run_query_optimizer()

Before you read the rest of the solution, you should understand what is
"name mangling" means. If you don't, consider reading about it on `Wikipedia`__ .

.. __ : http://en.wikipedia.org/wiki/Name_mangling

The solution is pretty simple. `GCC-XML`_ reports mangled and demangled function
names. The demangled function name contains "real" function name:
``get_value< used type >``. You only have to instruct :doc:`Py++ <../../pyplusplus>` to use it.

:doc:`Py++ <../../pyplusplus>` does not use by default demangled function name for mainly one reason.
Demangled function name is a string that contains a lot of information. :doc:`Py++ <../../pyplusplus>`
implements a parser, which extracts the only relevant one. The parser
implementation is a little bit complex and was not heavily tested. By "heavily" I
mean that I tested it on a lot of crazy use cases and on a real project, but
there is always some new use case out there. I am almost sure it will work for
you. The problem, we deal with, is rare, so by default "demangled_name"
feature is turned off.

By the way, almost the same problem exists for template classes. But, in the
classes use case :doc:`Py++ <../../pyplusplus>` uses demangled name by default.

-----------
Help wanted
-----------
I understand that the provided solutions are not perfect and that something
better and simpler should be done. Unfortunatelly the priority of this task is
low.

Allen Bierbaum has few suggestion that could improve :doc:`Py++ <../../pyplusplus>`. He created a
`wiki page`_, that discuss possible solutions. Your contribution is welcome too!

.. _`wiki page` : https://realityforge.vrsource.org/view/PyppApi/TemplateSupport



.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org
