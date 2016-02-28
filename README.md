# Py++11 - [pybind11] code generator

Py++11, successor of Py++, is a code generator for [pybind11] that simplifies
writing Python bindings of a C/C++ library. The tool is implemented as a Python
module and is controlled by a user script.

Check out the [pybind11 documentation][pybind11doc] for more information on 
[pybind11]!

## Requirements

In order to use Py++11 you need the following additional components:

- Python v2.6 (or higher)
- [pygccxml]
- [CastXML][castxml]

## Installing

Py++11 uses Python's distutils, so you can apply the usual procedure by placing
yourself in the root of the project's directory and entering the following
command:

	```
	python setup.py install
	```

## Contributing

Please check out the instructions on [how to contribute][contribute] to Py++11
if you would like to help the Py++11 project!

This repository currently hosts the original Py++ code, exposing C/C++
libraries as Boost.Python code. This should change in future, so we will make
it a community effort to port Py++ to pybind11, making it Py++11.

Please feel free to help reaching the goal and create an awesome code generator
for an awesome library! :grin:

## Documentation

The documentation is yet to be added.

## Special Thanks

* [Wenzel Jakob][wjakob] - For creating the awesome [pybind11] library :heart:

---

Distributed under the [Boost Software License, Version 1.0][boost_license].

<!-- References -->
[boost_license]: http://www.boost.org/LICENSE_1_0.txt "Boost Software License, v1.0"
[castxml]: https://github.com/CastXML/CastXML
[contribute]: https://github.com/IAmRarios/pypp11/blob/master/CONTRIBUTING.md "Contributing to Py++11"
[pybind11]: https://github.com/wjakob/pybind11 "pybind11"
[pybind11doc]: http://pybind11.readthedocs.org/en/latest/ "pybind11 documentation @ Read the Docs"
[pygccxml]: http://pygccxml.readthedocs.org/en/develop/ "pygccxml"
[wjakob]: https://github.com/wjakob "Wenzel Jakob"
