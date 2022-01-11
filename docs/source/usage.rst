.. Copyright (C) 2022, Giorgio Comitini

.. This is part of the PySmeQcd Documentation.

.. See the file index.rst for copying conditions.


.. role:: python(code)
  :language: python
  :class: highlight

.. role:: console(code)
  :language: console
  :class: highlight

.. _install:

Installing the library
----------------------

Using :python:`pip`
```````````````````

PySmeQcd is available on PyPI. To install it, run

.. code-block:: console

  $ pip install PySmeQcd

From source
```````````

To use PySmeQcd from the source code:

1. Download the source code from `GitHub <https://github.com/GComitini/PySmeQcd/releases/download/v1.0.0-alpha/PySmeQcd-1.0.0a0.tar.gz>`_.

  .. code-block:: console

    $ wget https://github.com/GComitini/PySmeQcd/releases/download/v1.0.0-alpha/PySmeQcd-1.0.0a0.tar.gz

2. Unpack the archive and :console:`cd` into the :file:`PySmeQcd-1.0.0a0/src` directory.

  .. code-block:: console

    $ tar -xzvf PySmeQcd-1.0.0a0.tar.gz
    $ cd PySmeQcd-1.0.0a0/src

3. Copy the :file:`PySmeQcd` directory to the main directory of your project.

  .. code-block:: console

    $ cp PySmeQcd <MY_PROJECT>

.. note::

  PySmeQcd depends on:

  - matplotlib
  - numpy
  - scipy

  When using PySmeQcd from source, make sure that you have these dependencies installed.

----------------------------------------------------------------------------------------

.. _use:

Using the library
-----------------

To use the PySmeQcd library:

1. :python:`import` the :python:`PySmeQcd` package into an interactive Python session or into a Python script:

  .. code-block:: python

    >>> import PySmeQcd

2. The functions and routines contained in the :python:`PySmeQcd` package can be accessed by using the point notation:

  .. code-block:: python

    >>> PySmeQcd.<module_name>.<function_name>()

3. Alternatively, you can import the submodules you need using :python:`from .. import ..`. For example,

  .. code-block:: python

    >>> from PySmeQcd import gluon

  will make the functions and routines contained in the :python:`PySmeQcd.gluon` submodule accessible by using the dot notation on :python:`gluon`:

  .. code-block:: python

    >>> gluon.<function_name>()

See the :ref:`examples <examples>` for practical use-cases or the :ref:`API Reference <api>` for an in-depth description of the available functions.
