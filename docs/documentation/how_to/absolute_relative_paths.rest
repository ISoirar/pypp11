=========================
Absolute\\relative paths
=========================

**Absolute\\relative paths**

Consider the following layout:
::

  boost/
    date_time/
      ptime.hpp
      time_duration.hpp
      date_time.hpp

``date_time.hpp`` is the main header file, which should be parsed.

:doc:`Py++ <../../pyplusplus>` does not handle relative paths, as input, well. It tries, but there are uses
cases it fails. In these cases it generates empty module - nothing is exposed:

.. code-block:: python

   mb = module_builder( [ 'date_time/date_time.hpp' ], ... )
   mb.split_module( ... )

I recommend you to use absolute paths instead of relative ones:

.. code-block:: python

   import os
   mb = module_builder( [ os.path.abspath('date_time/date_time.hpp') ], ... )
   mb.split_module( ... )

and :doc:`Py++ <../../pyplusplus>` will expose all declarations found in the ``date_time.hpp`` file and
other files from the same directory.

.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html
.. _`Python`: http://www.python.org
.. _`GCC-XML`: http://www.gccxml.org
