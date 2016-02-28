# Contributing

The quality and capability of Py++11 depends upon a community contributing to
its code base, porting existing Py++ code, writing documentation and tutorials
and so forth. In order to make contributing to Py++11 easier for everyone,
contributors should follow a few guidelines that help along the way.

Remember, valuable contributions aren't limited to just code you write. Every
issue explaining a bug or problem, every piece of documentation, every tutorial
you provide will help Py++11 becoming a useful tool in generating Python
packages interfacing C++ libraries!

## Getting Started

* Make sure you have a [GitHub account][github_account].
* If you haven't already, find a part of the project you'd like to contribute
  to, for example:
	* Check out the [development stage plan][development_stages] to find
	  something that still needs to be worked on.
	* [Port Py++ internals][port_pypp] to generate [pybind11] code, instead of
	  [Boost.Python][boost_python].
	* Provide an [issue][issues] explaining a bug or problem you found, or even
	  a feature you'd like Py++11 to have.
	* Help out on existing [issues][issues].
	* Document parts of the code that have no or very little documentation.
	* Write a tutorial explaining how to complete a certain task using Py++11.
* [Fork][fork_help] the repository on GitHub, then clone it using:

	```
	git clone git@github.com:YOUR_USERNAME/pypp11.git
	```

## Making Changes

* Create a topic branch from where you want to base your work (usually
  `master`).
	* To quickly create a topic branch based on `master`:

	```
	git checkout -b topic_branch master
	```

	Please **avoid** working directly on the `master` branch!
* Make commits of logical units.
* Add notable changes to the [changelog].
* Check for unnecessary white space with `git diff --check` before committing.
* Make sure your commit messages are in a [proper format][commit_message], for
  example:

	```
	Add summary in imperative language (max. 50 chars)

	After a blank line, provide a more detailed description of the changes
	you introduced. Keep it under about 72 characters in width. Explain the
	problems you fixed, the features you added and so forth. The first line
	should give a quick heads-up on what the commit did and the description
	should help to follow the development of the code base as a whole.

	Further paragraphs come after blank lines:

	* If need be, add bullet points

	* Usually using a hyphen or an asterisk
	```

## Submitting Changes

* Push your changes to a topic branch in your fork of the repository.
* Submit a [pull request][pull_request] to the [Py++11 repository][pypp11].
* The pull request will be reviewed and feedback may be given.
* After feedback, if any, is incorporated, the change will be added to Py++11.

<!-- References -->
[boost_python]: http://www.boost.org/doc/libs/1_60_0/libs/python/doc/html/index.html "Boost.Python"
[changelog]: https://github.com/IAmRarios/pypp11/blob/master/CHANGELOG.md "Py++11 Changelog"
[commit_message]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html "Proper Commit Messages"
[development_stages]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/development_stages.md "Development Stages"
[fork_help]: https://help.github.com/articles/fork-a-repo/ "Fork a Repository"
[github_account]: https://github.com/signup/free "GitHub Sign Up"
[issues]: https://github.com/IAmRarios/pypp11/issues "Py++11 issues"
[port_pypp]: https://github.com/IAmRarios/pypp11/blob/master/dev_tools/port_to_pybind11.md "Port Py++ to pybind11"
[pull_request]: https://help.github.com/articles/creating-a-pull-request/ "Creating a Pull Request"
[pybind11]: http://pybind11.readthedocs.org/en/latest/index.html "pybind11"
[pypp11]: https://github.com/IAmRarios/pypp11 "Py++11 Repository"
