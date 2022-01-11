.. Copyright (C) 2022, Giorgio Comitini

.. This is part of the PySmeQcd Documentation.

.. Permission is granted to copy, distribute and/or modify this document under
   the terms of the GNU Free Documentation License, Version 1.3 or any later
   version published by the Free Software Foundation; with no Invariant
   Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the
   license is included in the section entitled "GNU Free Documentation License".


.. PySmeQcd documentation master file, created by
   sphinx-quickstart on Fri Jan  7 13:18:22 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. role:: python(code)
 :language: python
 :class: highlight

Welcome to PySmeQcd's documentation!
====================================

Release v\ |release|. (:ref:`Installation <install>`)

**PySmeQcd** is a Python library for making calculations within the framework of
the Screened Massive Expansion of Quantum Chromodynamics.

Currently, PySmeQcd contains :ref:`functions and routines <pkgcontents>`
related to the one-loop gluon, ghost and quark propagators in any covariant gauge,
both in pure Yang-Mills theory and in full QCD.

.. note::
  Since the number of colors :math:`N` and number of quarks :math:`N_{f}` are
  controlled either by modifiable global settings (see the API reference for the
  :doc:`settings submodules <settings>`) or by function parameters, PySmeQcd
  can actually be used for calculations in 4-dimensional :math:`SU(N)` Yang-Mills
  theory, coupled to an arbitrary number of fermions in the fundamental
  representation.

------------------------------------------------------------------------------

.. toctree::
  :hidden:

  symbols

The Screened Massive Expansion: an introduction
-----------------------------------------------

The **Screened Massive Expansion** (**S.M.E.**) is a perturbative framework for
the study of the low-energy limit of Quantum Chromodynamics. It was first
introduced in the context of pure :math:`SU(N)` Yang-Mills theory in
`F. Siringo, Nucl. Phys. B 907, 572 (2016) <https://doi.org/10.1016/j.nuclphysb.2016.04.028>`_
with the aim of describing the dynamical generation of a gluon infrared mass in
the Landau gauge, and then extended to arbitrary covariant gauges and to full QCD.

The S.M.E. allows to derive gluon, ghost and quark propagators which are in
excellent agreement with the lattice data, down to the deep infrared. It is
defined by a shift of the expansion point of the QCD perturbative series,
performed in such a way as to treat the transverse gluons as massive already at
tree-level and enhance the quark masses with respect to their bare (UV) masses,
while leaving the QCD Lagrangian unchanged.

Read more about the Screened Massive Expansion :doc:`here <sme>`.

.. toctree::
  :hidden:

  sme

------------------------------------------------------------------

.. _pkgcontents:

Structure and contents of this package
--------------------------------------

At present (release v\ |release|), in line with the current status of research,
the PySmeQcd library only supports one-loop calculations in the two-point gluon,
ghost and quark sectors. For forward compatibility, the functions and routines
related to each of these sectors can be accessed via submodules of the
:python:`PySmeQcd.oneloop` module:

- the :python:`PySmeQcd.oneloop.gluon` module contains functions and routines related to the gluon propagator,
- the :python:`PySmeQcd.oneloop.ghost` module contains functions and routines related to the ghost propagator,
- the :python:`PySmeQcd.oneloop.quark` module contains functions and routines related to the quark propagator.

In order to improve access to the library, these submodules are linked to the
main :python:`PySmeQcd` module as follows:

- :python:`PySmeQcd.gluon` :math:`\hookrightarrow` :python:`PySmeQcd.oneloop.gluon`
- :python:`PySmeQcd.ghost` :math:`\hookrightarrow` :python:`PySmeQcd.oneloop.ghost`
- :python:`PySmeQcd.quark` :math:`\hookrightarrow` :python:`PySmeQcd.oneloop.quark`

The gluon module
````````````````

The gluon module contains functions and routines related to the gluon propagator.

In it, functions are defined for computing the gluon dressing function, propagator
and spectral function in an arbitrary covariant gauge and with an arbitrary number
of quarks of equal masses.

Due to the non-perturbative nature of the S.M.E. (as opposed to the method itself,
which is perturbative), when making loop calculations, one is free to include any
number of *crossed* diagrams in the gluon polarization. Release v\ |release| of
PySmeQcd supports the calculation of two variants of the full-QCD one-loop gluon
propagator:

- the **uncrossed** (:python:`type='uc'`) variant, which only includes the ordinary quark loop as the full quark contribution to the propagator,
- the **crossed** (:python:`type='cr'`) variant, which also includes the *crossed* quark loop in the quark contribution to the propagator.

For pure Yang-Mills theory (:math:`N_{f}=0`, i.e., no quarks), these are equivalent,
since there are no quark loops.

The gluon module also contains routines for computing the poles and residues of
the gluon propagator, and for plotting the gluon dressing function, the propagator,
the spectral function, and more.

Read the complete API reference for the gluon module :doc:`here <gluon>`.

The ghost module
````````````````

The ghost module contains functions and routines related to the ghost propagator.

In it, functions are defined for computing the ghost dressing function, propagator
and spectral function in an arbitrary covariant gauge.

The ghost module also contains routines for plotting the inverse gluon dressing
function, propagator and spectral function.

Read the complete API reference for the ghost module :doc:`here <ghost>`.


The quark module
````````````````

The quark module contains functions and routines related to the quark propagator.

In it, functions are defined for computing the quark :math:`Z`-function, the mass
function, the vector and scalar components of the quark propagator, and the
vector and scalar components of the spectral function, in an arbitrary covariant
gauge.

Release v\ |release| of PySmeQcd supports the calculation of three variants of
the one-loop quark propagator:

- the **minimalistic scheme** (:python:`type='ms'`) variant, which only includes the ordinary and quark-crossed loops as the full contribution to the propagator,
- the **vertex-wise scheme** (:python:`type='vw'`) variant, which also includes the gluon-crossed loop in the contribution to the propagator,
- the **complex-conjugate scheme** (:python:`type='cc'`) variant, in which the internal gluon line is replaced by the principal part of the dressed gluon propagator.

The quark module also contains routines for computing the poles and residues of
the quark propagator, and for plotting :math:`Z` and mass function, the components
of the quark propagator, and components of the spectral function.

Read the complete API reference for the quark module :doc:`here <quark>`.

.. note::

  This library is under development. Future releases will include features
  such as the optimization of the S.M.E. from principles of gauge invariance
  and the Renormalization Group analysis of the S.M.E..

------------------------------------------------------------------

Installation and usage
----------------------

Follow the guides for :ref:`installing <install>` and :ref:`using <use>`
PySmeQcd.

.. toctree::
  :hidden:

  usage

------------------------------------------------------------------

.. _examples:

Examples
----------

Compute the unrenormalized gluon propagator at a specified adimensional momentum
````````````````````````````````````````````````````````````````````````````````

Compute the unrenormalized gluon propagator at :math:`p^{2}=m^{2}` by importing
the :python:`gluon` module from the :python:`PySmeQcd` package and calling the
:python:`gluon_prop()` function:

.. code-block:: python

  >>> from PySmeQcd import gluon
  >>> gluon.gluon_prop(1)
  0.798347501002427

Compute the renormalized gluon propagator at a specified dimensionful momentum
``````````````````````````````````````````````````````````````````````````````

Compute the renormalized gluon propagator at :math:`p^{2}=4` GeV\ :sup:`2` by
importing the :python:`gluon` module from the :python:`PySmeQcd` package and
calling the :python:`gluon_prop()` function with the :python:`ren=True` and
:python:`dimensionful=True` options:

.. code-block:: python

  >>> from PySmeQcd import gluon
  >>> gluon.gluon_prop(4,dimensionful=True)
  0.3766047017129976

Plot the renormalized ghost dressing function
`````````````````````````````````````````````

Plot the renormalized ghost dressing function by importing the :python:`ghost`
module from the :python:`PySmeQcd` package and calling the :python:`ghost_chi_plot()`
function:

.. code-block:: python

  >>> from PySmeQcd import ghost
  >>> ghost.ghost_prop_plot()

Find the adimensional Euclidean poles of the gluon propagator
`````````````````````````````````````````````````````````````

Find the adimensional Euclidean poles of the gluon propagator by importing the
:python:`gluon` module and calling the :python:`gluon_pole()` function:

.. code-block:: python

  >>> from PySmeQcd import ghost
  >>> gluon.gluon_pole()
  (-0.4575251454672443-1.0129799082521271j)

Find the renormalized residues of the quark propagator at its poles
```````````````````````````````````````````````````````````````````

Find the renormalized residues of the quark propagator at its poles by importing
the :python:`quark` module and calling the :python:`quark_residue()` function:

.. code-block:: python

  >>> from PySmeQcd import quark
  >>> quark.quark_residue()
  (0.9719642868071728+0.5240628262206164j)

------------------------------------------------------------------

.. _api:

API Reference
-------------

Read the full documentation of the functions, routines and settings contained
in the :python:`PySmeQcd` package in what follows.

.. toctree::
   :maxdepth: 1

   ghost
   gluon
   quark
   settings

------------------------------------------------------------------

Licensing
---------

PySmeQcd is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

PySmeQcd is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
PySmeQcd. If not, see https://www.gnu.org/licenses/.

Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU Free Documentation License, Version 1.3 or any later
version published by the Free Software Foundation; with no Invariant
Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the
license is included in the section entitled :doc:`"GNU Free Documentation License" <license>`.

.. toctree::
  :hidden:

  license

------------------------------------------------------------------

Indices and tables
------------------

* :ref:`Index <genindex>`
* :ref:`Module index <modindex>`
* :ref:`Search <search>`
