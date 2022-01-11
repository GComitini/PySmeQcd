.. Copyright (C) 2022, Giorgio Comitini

.. This is part of the PySmeQcd Documentation.

.. See the file index.rst for copying conditions.


.. role:: python(code)
  :language: python
  :class: highlight

.. role:: console(code)
  :language: console
  :class: highlight

The oneloop.gluon module
========================

.. automodule:: PySmeQcd.oneloop.gluon

**Contents:**

  - :ref:`gluon_bb`
  - :ref:`gluon_prop`
  - :ref:`gluon_pr`
  - :ref:`gluon_gf`

.. note::

  1. Where not otherwise specified, :python:`s` is the adimensional Euclidea momentum squared :math:`s=p^{2}/m^{2}`.

  2. Most functions are defined modulo factors of the coupling constant. If the :python:`ren` parameter is available, such factors become irrelevant when renormalization is enabled using :python:`ren=True`.

  3. With the parametrization described below, to one loop, the number of colors only enters the expressions through the quark contribution -- hence is irrelevant in pure Yang-Mills theory (no quarks, i.e., :math:`N_{f}=0`) -- and through the value of the gluon mass parameter :math:`m`.

--------------------------------------------------------------

.. _gluon_bb:

Building blocks for the one-loop gluon propagator and related functions
-----------------------------------------------------------------------

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_F

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_F_xi

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_F_Q

.. autofunction:: PySmeQcd.oneloop.gluon.dgluon_F

.. autofunction:: PySmeQcd.oneloop.gluon.dgluon_F_xi

.. autofunction:: PySmeQcd.oneloop.gluon.dgluon_F_Q

.. autofunction:: PySmeQcd.oneloop.gluon.dgluon_F_Qdx

.. autofunction:: PySmeQcd.oneloop.gluon.dgluon_F_Qdxds

--------------------------------------------------------------

.. _gluon_prop:

The one-loop gluon dressing function, propagator and spectral function
----------------------------------------------------------------------

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_J_inv

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_J

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_prop

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_spectral

.. note::

  :python:`s` is the adimensional Minkowski momentum squared :math:`p_{M}^{2}/m^{2}`,
  or the dimensionful Minkowski momentum squared :math:`p_{M}^{2}` if
  :python:`dimensionful=True`.

.. autofunction:: PySmeQcd.oneloop.gluon.dgluon_J_inv

--------------------------------------------------------------

.. _gluon_pr:

Poles and residues
------------------

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_pole

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_residue

--------------------------------------------------------------

.. _gluon_gf:

Graphical functions
-------------------

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_J_plot

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_J_3D_plot

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_J_inv_contour

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_prop_plot

.. autofunction:: PySmeQcd.oneloop.gluon.gluon_spectral_plot

.. note::

  :python:`s` is the adimensional Minkowski momentum squared :math:`p_{M}^{2}/m^{2}`,
  or the dimensionful Minkowski momentum squared :math:`p_{M}^{2}` if
  :python:`dimensionful=True`.
