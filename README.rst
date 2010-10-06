What's This
===========
This is Graphing extension for Sphinx_ .
using Gruffy_ module.

.. _Sphinx: http://sphinx.pocoo.org/
.. _Gruffy: http://pypi.python.org/pypi/gruffy/


Install
=======
used to easy_install::

  $ easy_install sphinxcontrib-gruffygen


Require
=======
Require Sphinx_ and Gruffy_

install::

    $ easy_install sphinx
    $ easy_install gruffy


Usage
=====
basic usage in sphinx documentation::

    .. gruffy::
       :type: SideBar
       :title: test graph

        data("foo", [1, 4, 3])
        data("bar", [8, 2, 5])

set to following types,

* Area
* Bar
* Dot
* Line
* Pie
* SideBar
* StackedArea
* StackedBar
* StackedSideBar
