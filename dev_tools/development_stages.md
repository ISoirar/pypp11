# Py++11 development stages

The development of Py++11 will be divided into 3 stages. Each stage has its own 
goals and required tasks towards completion. Note that the specific subprojects
for every stage might be subject to change as the project further develops.

## Stage I

### Goals

* Fully ported Py++ code, generating valid [pybind11] code, instead of 
[Boost.Python][boost_python] code. 
* The interface stays intact, so legacy Py++ scripts can be used with Py++11. 
* Support for Python 3.

### Subprojects towards completion

* [ ] [Port general][port_general] [Boost.Python][boost_python] code generation 
	   to [pybind11].
* [ ] [Port class][port_classes] exposing code generation.
* [ ] [Port function][port_functions] exposing code generation.
* [ ] [Port constructor][port_functions_constructors] exposing code generation.
* [ ] [Port overloaded operator][port_functions_operators] exposing code 
	  generation.
* [ ] [Port return-value-policy][port_functions_rvp] generation.
* [ ] [Port virtual function][port_functions_virtuality] exposing code 
	  generation.
* [ ] Write a style guide (naming conventions, code layout, etc.) to make it
	  easier for contributors to keep the code and interface uniform.
* [ ] Fix non-working unit tests.
* [ ] Switch Py++11 and dependencies from Python 2 to Python 3.

## Stage II

### Goals

* Move away from deprecated dependencies towards modern approaches. 
* Improve code documentation and tutorials. 
* Add goodies such as [documentation extractors][doc_extractors] to main code 
base.

### Subprojects towards completion

* [ ] Assess [libclang] as alternative to [pygccxml].
* [ ] Make it easier and faster to get and run Py++11.
* [ ] Properly document Py++11 classes and functions.
* [ ] Provide an online documentation, for example through 
	  [Read the Docs][readthedocs].
* [ ] Update/Write tutorials on Py++11 features and most common tasks.
* [ ] Include the
[contributed Doxygen documentation extractor][doxygen_doc_extractor] into the
main codebase.

## Stage III

### Goals

* Project maintenance.
* Adding requested features.

### Subprojects towards completion

Strictly speaking, there is no "completion" for this stage. It will be an
on-going effort to keep the project up-to-date and add requested functionality.

<!-- References -->
[boost_python]: http://www.boost.org/doc/libs/1_60_0/libs/python/doc/html/index.html "Boost.Python"
[doc_extractors]: https://github.com/IAmRarios/pypp11/tree/master/contrib/doc_extractors "Documentation Extractor Example"
[doxygen_doc_extractor]: https://github.com/IAmRarios/pypp11/blob/master/contrib/doc_extractors/doxygen.py "doxygen.py"
[libclang]: http://clang.llvm.org/doxygen/group__CINDEX.html "libclang"
[port_classes]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/port_to_pybind11.md#classes-and-enumerations "Class Port"
[port_functions]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/port_to_pybind11.md#functions "Function Port"
[port_functions_constructors]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/port_to_pybind11.md#constructors "Function Port - Constructors"
[port_functions_operators]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/port_to_pybind11.md#operator-overloading "Function Port - Operator Overloading"
[port_functions_rvp]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/port_to_pybind11.md#return-value-policies "Function Port - Return-Value-Policies"
[port_functions_virtuality]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/port_to_pybind11.md#virtuality "Function Port - Virtuality"
[port_general]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/port_to_pybind11.md#general "General Code Port"
[pybind11]: http://pybind11.readthedocs.org/en/latest/index.html "pybind11"
[pygccxml]: http://pygccxml.readthedocs.org/en/develop/ "pygccxml"
[readthedocs]: https://readthedocs.org/ "Read the Docs"
