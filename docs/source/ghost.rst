.. Copyright (C) 2022, Giorgio Comitini

.. This is part of the PySmeQcd Documentation.

.. See the file index.rst for copying conditions.


.. role:: python(code)
  :language: python
  :class: highlight

The oneloop.ghost module
========================

.. automodule:: PySmeQcd.oneloop.ghost

**Contents:**

  - :ref:`ghost_bb`
  - :ref:`ghost_prop`
  - :ref:`ghost_gf`

.. note::

  1. Where not otherwise specified, :python:`s` is the adimensional Euclidean momentum squared :math:`s=p^{2}/m^{2}`.

  2. Most functions are defined modulo factors of the coupling constant. If the :python:`ren` parameter is available, such factors become irrelevant when renormalization is enabled using :python:`ren=True`.

--------------------------------------------------------------

.. _ghost_bb:

Building blocks for the one-loop ghost propagator and related functions
-----------------------------------------------------------------------

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_G

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_G_xi

.. autofunction:: PySmeQcd.oneloop.ghost.dghost_G

.. autofunction:: PySmeQcd.oneloop.ghost.dghost_G_xi

--------------------------------------------------------------

.. _ghost_prop:

The one-loop ghost dressing function, propagator and spectral function
----------------------------------------------------------------------

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_chi_inv

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_chi

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_prop

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_spectral

.. note::

  :python:`s` is the adimensional Minkowski momentum squared :math:`p_{M}^{2}/m^{2}`,
  or the dimensionful Minkowski momentum squared :math:`p_{M}^{2}` if
  :python:`dimensionful=True`.

.. autofunction:: PySmeQcd.oneloop.ghost.dghost_chi_inv

--------------------------------------------------------------

.. _ghost_gf:

Plots
-----

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_chi_plot

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_prop_plot

.. autofunction:: PySmeQcd.oneloop.ghost.ghost_spectral_plot

.. note::

  :python:`s` is the adimensional Minkowski momentum squared :math:`p_{M}^{2}/m^{2}`,
  or the dimensionful Minkowski momentum squared :math:`p_{M}^{2}` if
  :python:`dimensionful=True`.
