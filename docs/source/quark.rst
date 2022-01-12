.. Copyright (C) 2022, Giorgio Comitini

.. This is part of the PySmeQcd Documentation.

.. See the file index.rst for copying conditions.


.. role:: python(code)
  :language: python
  :class: highlight

.. role:: console(code)
  :language: console
  :class: highlight

The oneloop.quark module
========================

.. automodule:: PySmeQcd.oneloop.quark

**Contents:**

  - :ref:`quark_bb`
  - :ref:`quark_se`
  - :ref:`quark_prop`
  - :ref:`quark_par`
  - :ref:`quark_pr`
  - :ref:`quark_gf`

.. note::

  1. Where not otherwise specified:

    - :python:`s` is the adimensional Euclidean momentum squared :math:`s=p^{2}/m^{2}`,
    - :python:`p02` is the adimensional gluon pole :math:`-p_{0}^{2}/m^{2}` in Minkowski space.

  2. Most functions are defined modulo factors of the coupling constant. If the :python:`ren` parameter is available, such factors become irrelevant when renormalization is enabled using :python:`ren=True`.

--------------------------------------------------------------

.. _quark_bb:

Building blocks for the one-loop quark propagator and related functions
-----------------------------------------------------------------------

.. autofunction:: PySmeQcd.oneloop.quark.quark_t

.. autofunction:: PySmeQcd.oneloop.quark.quark_R

.. autofunction:: PySmeQcd.oneloop.quark.quark_CR

.. autofunction:: PySmeQcd.oneloop.quark.quark_Cx

.. autofunction:: PySmeQcd.oneloop.quark.quark_Cxs

.. autofunction:: PySmeQcd.oneloop.quark.quark_C0

.. autofunction:: PySmeQcd.oneloop.quark.dquark_t

.. autofunction:: PySmeQcd.oneloop.quark.dquark_tdx

.. autofunction:: PySmeQcd.oneloop.quark.dquark_R

.. autofunction:: PySmeQcd.oneloop.quark.dquark_Rdx

.. autofunction:: PySmeQcd.oneloop.quark.dquark_CR

.. autofunction:: PySmeQcd.oneloop.quark.dquark_CRdx

.. autofunction:: PySmeQcd.oneloop.quark.dquark_Cx

.. autofunction:: PySmeQcd.oneloop.quark.dquark_Cxdx

.. autofunction:: PySmeQcd.oneloop.quark.dquark_Cxs

.. autofunction:: PySmeQcd.oneloop.quark.dquark_Cxsdx

.. autofunction:: PySmeQcd.oneloop.quark.dquark_C0

.. autofunction:: PySmeQcd.oneloop.quark.dquark_C0dx

--------------------------------------------------------------

.. _quark_se:

The one-loop quark self-energy
------------------------------

.. autofunction:: PySmeQcd.oneloop.quark.quark_SigV1

.. autofunction:: PySmeQcd.oneloop.quark.quark_SigS1

.. autofunction:: PySmeQcd.oneloop.quark.quark_SigV2

.. autofunction:: PySmeQcd.oneloop.quark.quark_SigS2

.. autofunction:: PySmeQcd.oneloop.quark.quark_SigVgl

.. autofunction:: PySmeQcd.oneloop.quark.quark_SigSgl

.. autofunction:: PySmeQcd.oneloop.quark.quark_SigV

.. autofunction:: PySmeQcd.oneloop.quark.quark_SigS

.. autofunction:: PySmeQcd.oneloop.quark.dquark_SigV1

.. autofunction:: PySmeQcd.oneloop.quark.dquark_SigV1dx

.. autofunction:: PySmeQcd.oneloop.quark.dquark_SigS1

.. autofunction:: PySmeQcd.oneloop.quark.dquark_SigS1dx

.. autofunction:: PySmeQcd.oneloop.quark.dquark_SigV

.. autofunction:: PySmeQcd.oneloop.quark.dquark_SigS

--------------------------------------------------------------

.. _quark_prop:

The one-loop quark propagator
-----------------------------

.. autofunction:: PySmeQcd.oneloop.quark.quark_A

.. autofunction:: PySmeQcd.oneloop.quark.quark_B

.. autofunction:: PySmeQcd.oneloop.quark.quark_Z

.. autofunction:: PySmeQcd.oneloop.quark.quark_M

.. autofunction:: PySmeQcd.oneloop.quark.quark_Q

.. autofunction:: PySmeQcd.oneloop.quark.quark_propV

.. autofunction:: PySmeQcd.oneloop.quark.quark_propS

.. autofunction:: PySmeQcd.oneloop.quark.quark_spectralV

.. note::

  :python:`s` is the adimensional Minkowski momentum squared :math:`p_{M}^{2}/m^{2}`,
  or the dimensionful Minkowski momentum squared :math:`p_{M}^{2}` if
  :python:`dimensionful=True`.

.. autofunction:: PySmeQcd.oneloop.quark.quark_spectralS

.. note::

  :python:`s` is the adimensional Minkowski momentum squared :math:`p_{M}^{2}/m^{2}`,
  or the dimensionful Minkowski momentum squared :math:`p_{M}^{2}` if
  :python:`dimensionful=True`.

.. autofunction:: PySmeQcd.oneloop.quark.dquark_A

.. autofunction:: PySmeQcd.oneloop.quark.dquark_B

.. autofunction:: PySmeQcd.oneloop.quark.dquark_M

.. autofunction:: PySmeQcd.oneloop.quark.dquark_Q

--------------------------------------------------------------

.. _quark_par:

Parameter conversion
--------------------

.. autofunction:: PySmeQcd.oneloop.quark.quark_MB

.. note::

  The dimensions of the return value are determined by the dimensions of the
  parameter :python:`K0`. The default value of :python:`K0` is adimensionalized
  by the quark chiral mass :math:`M`.

.. autofunction:: PySmeQcd.oneloop.quark.quark_H0

.. autofunction:: PySmeQcd.oneloop.quark.quark_K0

.. note::

  The dimensions of the return value are determined by the dimensions of the
  parameter :python:`MB`.

--------------------------------------------------------------

.. _quark_pr:

Poles and residues
------------------

.. autofunction:: PySmeQcd.oneloop.quark.quark_pole

.. autofunction:: PySmeQcd.oneloop.quark.quark_residue

--------------------------------------------------------------

.. _quark_gf:

Plots
-----

.. autofunction:: PySmeQcd.oneloop.quark.quark_Z_plot

.. autofunction:: PySmeQcd.oneloop.quark.quark_M_plot

.. autofunction:: PySmeQcd.oneloop.quark.quark_propV_plot

.. autofunction:: PySmeQcd.oneloop.quark.quark_propS_plot

.. autofunction:: PySmeQcd.oneloop.quark.quark_spectralV_plot

.. note::

  :python:`s` is the adimensional Minkowski momentum squared :math:`p_{M}^{2}/m^{2}`,
  or the dimensionful Minkowski momentum squared :math:`p_{M}^{2}` if
  :python:`dimensionful=True`.

.. autofunction:: PySmeQcd.oneloop.quark.quark_spectralS_plot

.. note::

  :python:`s` is the adimensional Minkowski momentum squared :math:`p_{M}^{2}/m^{2}`,
  or the dimensionful Minkowski momentum squared :math:`p_{M}^{2}` if
  :python:`dimensionful=True`.
