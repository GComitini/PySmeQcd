.. Copyright (C) 2022, Giorgio Comitini

.. This is part of the PySmeQcd Documentation.

.. See the file index.rst for copying conditions.


.. role:: python(code)
  :language: python
  :class: highlight

The settings modules
====================

The default values for the functions and routines contained in the :python:`PySmeQcd` package
and -- more specifically -- in the :python:`PySmeQcd.oneloop` module are stored, respectively, in
the :python:`PySmeQcd.settings` and :python:`PySmeQcd.oneloop.oneloop_settings` modules.

In what follows, we describe each of these settings. Please have a look at the :doc:`Symbol table <symbols>`
for reference on the symbols used below.

**Contents:**

  - :ref:`sets`
  - :ref:`ol_sets`

----------------------------------------

.. _sets:

The PySmeQcd.settings module
----------------------------

.. automodule:: PySmeQcd.settings

Theory settings
```````````````

.. autodata:: PySmeQcd.settings.N
.. autodata:: PySmeQcd.settings.Nf
.. autodata:: PySmeQcd.settings.xi

Renormalization settings
````````````````````````

.. autodata:: PySmeQcd.settings.mu0

Numerical settings
``````````````````

.. autodata:: PySmeQcd.settings.step_h
.. autodata:: PySmeQcd.settings.stp

----------------------------------------

.. _ol_sets:

The PySmeQcd.oneloop.oneloop_settings module
--------------------------------------------

.. automodule:: PySmeQcd.oneloop.oneloop_settings

Diagrams settings
`````````````````

.. autodata:: PySmeQcd.oneloop.oneloop_settings.gluetype
.. autodata:: PySmeQcd.oneloop.oneloop_settings.quarktype

Mass settings
`````````````

.. autodata:: PySmeQcd.oneloop.oneloop_settings.m
.. autodata:: PySmeQcd.oneloop.oneloop_settings.x
.. autodata:: PySmeQcd.oneloop.oneloop_settings.K0

Renormalization settings
````````````````````````

.. autodata:: PySmeQcd.oneloop.oneloop_settings.F0
.. autodata:: PySmeQcd.oneloop.oneloop_settings.G0
.. autodata:: PySmeQcd.oneloop.oneloop_settings.H0
.. autodata:: PySmeQcd.oneloop.oneloop_settings.Zglue

Poles and residues
``````````````````

.. autodata:: PySmeQcd.oneloop.oneloop_settings.p02
.. autodata:: PySmeQcd.oneloop.oneloop_settings.p0
.. autodata:: PySmeQcd.oneloop.oneloop_settings.res_im_re
.. autodata:: PySmeQcd.oneloop.oneloop_settings.phi
