# Changelog
All notable changes to this project will be documented in this file.

This project follows the practice of [Semantic Versioning][semantic_versioning].

## [Unreleased][unreleased]

### Added

* `.gitignore`
* `CHANGELOG.md`
* `CONTRIBUTING.md`
* `dev_tools/` as folder for development information and scripts.
* Description of planned development in `dev_tools/development_stages.md`
* Description of required changes in Py++ internals in
  `dev_tools/port_to_pybind11.md`
* Sphinx documentation make files `docs/Makefile` and `docs/make.bat`

### Changed

* Added information on requirements, installation, contribution and special
  thanks to `README.md`
* `LICENSE_1_0.txt` -> `LICENSE.md`
* `contri/` -> `contributed/`
* `pyplusplus/`-> `pypp11/`
* `unittests/` -> `unit_tests/`
* Made `setup.py` compatible with Py++11 and the changed directory tree
* Rewritten `pygccxml` revision number check in `pypp11/__init__.py`, so it
  actually does what it should and not just throw `AttributeError`
* `from pygccxml import utils` -> `from pygccxml.utils import utils`
* Moved documentation source root from `docs/` to `docs/source/`. Documentation
  will be generated into `docs/build/`

### Removed

* `README.txt`

---

Based on [keepachangelog.com][keepachangelog].

<!-- References -->
[keepachangelog]: http://keepachangelog.com/ "Keep a Changelog"
[semantic_versioning]: http://semver.org/spec/v2.0.0.html "Semantic Versioning v2.0.0"

<!-- Version links -->
<!-- "unreleased" should always point to the latest release version and "HEAD" -->
[unreleased]: https://github.com/IAmRarios/pypp11/compare/master...HEAD "Unreleased Changes"
