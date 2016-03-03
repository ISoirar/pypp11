========
Examples
========
-------------------
Graphical interface
-------------------

:doc:`Py++ <../pyplusplus>` has nice, small and simple :doc:`graphical interface <../documentation/tutorials/pyplusplus_gui>`. 
Consider to read :doc:`tutorials <../documentation/tutorials/tutorials>` for more information.

---------
pyeasybmp
---------

:doc:`EasyBMP <easybmp/easybmp>` is a small cross-platform library that provide you functionality
needed to work with Windows bitmap (BMP) image files. I took me only few minutes
to create Python bindings for the library. Read more :doc:`here <easybmp/easybmp>`.

---------------
boost libraries
---------------

Boost provides free peer-reviewed portable C++ source libraries. Using :doc:`Py++ <../pyplusplus>` I
created Python bindings for few libraries:

  * `Boost.Date_Time`_
  * `Boost.CRC`_
  * `Boost.Rational`_
  * `Boost.Random`_

This is not "just another example". I went father and created new package:
:doc:`pyboost <boost/boost>`. This is fully working Python package, with almost all unit test from
the libraries ported to Python. For more information please read :doc:`pyboost <boost/boost>`
package documentation.


.. toctree::

   boost/boost.rest
   easybmp/easybmp.rest

.. _`boost.date_time` : http://boost.org/doc/html/date_time.html
.. _`boost.crc` : http://boost.org/libs/crc/index.html
.. _`boost.rational` : http://boost.org/libs/rational/index.html
.. _`boost.random` : http://boost.org/libs/random/index.html
.. _`Boost.Python`: http://www.boost.org/libs/python/doc/index.html

