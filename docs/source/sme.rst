.. Copyright (C) 2022, Giorgio Comitini

.. This is part of the PySmeQcd Documentation.

.. See the file index.rst for copying conditions.


.. role:: python(code)
  :language: python
  :class: highlight

.. role:: console(code)
  :language: console
  :class: highlight

Set-up of the S.M.E.
--------------------

The Screened Massive Expansion of pure Yang-Mill theory is defined by a simple
shift of the kinetic :math:`\mathcal{L}_{0}` and interaction :math:`\mathcal{L}_{\text{int}}`
terms of the gauge-fixed, renormalized Faddeev-Popov Lagrangian:

.. math::

  \mathcal{L}_{0}\to \mathcal{L}_{0}+\delta\mathcal{L}\ ,\qquad \mathcal{L}_{\text{int}}\to \mathcal{L}_{\text{int}}-\delta\mathcal{L}\ ,

where :math:`\delta\mathcal{L}` is chosen so that the zero-order transverse gluon
propagator :math:`\Delta_{0}^{\mu\nu}(p)` is massive rather than massless:

.. math::

  \delta\mathcal{L}=\frac{m^{2}}{2}\,A_{\mu}^{a}\,t^{\mu\nu}(p)A_{\nu}^{a} \qquad\Longrightarrow\qquad\Delta_{0}^{\mu\nu}(p)=\frac{1}{p^{2}+m^{2}}\ t^{\mu\nu}(p)+\xi \frac{1}{p^{2}}\ \ell^{\mu\nu}(p)\ .

The shift gives rise to a new two-point gluon vertex :math:`\delta\Gamma^{\mu\nu}(p)`,

.. math::

  \delta\Gamma^{\mu\nu}(p)=m^{2}t^{\mu\nu}(p)\ ,

which must be included in the Feynman rules of perturbation theory.

In full QCD, in addition to the shift of the gluon sector, a shift is also performed
in the quark sector. Namely, the kinetic :math:`\mathcal{L}_{q,0}` and interaction
:math:`\mathcal{L}_{q,\text{int}}` terms of the quark Lagrangian are redefined
so that the light quarks propagate with a mass :math:`M` which is much larger than
their bare (UV) mass :math:`M_{B}`, and not related to the latter by perturbative
corrections:

.. math::

  \mathcal{L}_{q,0}\to \mathcal{L}_{q,0}+\delta\mathcal{L}_{q}\ ,\qquad \mathcal{L}_{q,\text{int}}\to \mathcal{L}_{q,\text{int}}-\delta\mathcal{L}_{q}\ ,

where

.. math::

  \delta\mathcal{L}_{q}=(M-M_{B}Z_{\psi})\overline{\psi}\psi \qquad\Longrightarrow\qquad S_{0}(p)=\frac{1}{-i\slashed{p}+M}\ ,

:math:`S_{0}(p)` being the zero-order quark propagator. The two-point quark vertex
:math:`\delta\Gamma_{q}(p)`,

.. math::

  \delta\Gamma_{q}(p)=-(M-M_{B}Z_{\psi})\ ,

is then also included in the Feynman rules of the theory.

--------------------------------------------------------------------------------

Features of the S.M.E.
----------------------

The Screened Massive Expansion of QCD:

- reduces to ordinary perturbation theory in the UV limit (in particular, it is renormalizable),
- yields propagators which are in very good agreement with the lattice data in Euclidean space,
- can be extended to the whole complex Minkowski space to study features such as the complex-conjugate poles of the gluon and quark propagators,
- can be made self-contained when optimized by principles of gauge invariance,
- yields a strong running coupling which is finite (no Landau poles) and small enough to allow the use of perturbation theory.

--------------------------------------------------------------------------------

The gluon propagator
--------------------

In a general covariant gauge, the one-loop gluon polarization :math:`\Pi(p^{2})`
can be expressed in terms of three functions, :math:`F(s)`, :math:`F_{\xi}(s)`
and :math:`F_{Q}(s)`,

.. math::

  \Pi(p^{2})=-\alpha p^{2} \left(F(s)+\xi F_{\xi}(s)+N_{f} F_{Q}(s)+\text{const.}\right)\ ,

or four, if the contribution :math:`F_{Q}^{(cr)}(s)` due to the *crossed* quark
loop is also included in the polarization,

.. math::

  \Pi(p^{2})=-\alpha p^{2} \left(F(s)+\xi F_{\xi}(s)+N_{f} F_{Q}(s)+N_{f} F_{Q}^{(cr)}(s)+\text{const.}\right)\ .

In this documentation, we refer to the first choice as the **uncrossed** (:python:`type='uc'`)
variant of the gluon propagator, and to the second choice as the **crossed** (:python:`type='cr'`)
variant of the gluon propagator. In pure Yang-Mills theory (no quarks, i.e., :math:`N_{f}=0`),
this distinction is irrelevant, since there are no quark loops in the gluon polarization.

The function :math:`F_{Q}^{(cr)}(s)` can be obtained by differentiating :math:`F_{Q}(s)`
with respect to the quark chiral mass,

.. math::

    F_{Q}^{(cr)}(s)=-M\frac{\partial}{\partial M}\,F_{Q}(s)\ .

The inverse gluon dressing function :math:`J^{-1}(s)` is then given by

.. math::

    J^{-1}(s)&=1+\alpha \left(F(s) + \xi F_{\xi}(s)+N_{f} F_{Q}(s)\right)+ \text{const.}=\\
             &=\alpha \left(F(s) + \xi F_{\xi}(s)+N_{f} F_{Q}(s)+F_{0}\right)

for the uncrossed variant of the propagator, or

.. math::

    J^{-1}(s)=\alpha \left(F(s) + \xi F_{\xi}(s)+N_{f} F_{Q}(s)+N_{f}F_{Q}^{(cr)}(s)+F_{0}\right)

for its crossed variant. In the above equations, :math:`F_{0}` is an additive
renormalization constant.

The functions :math:`F(s)`, :math:`F_{\xi}(s)`, :math:`F_{Q}(s)` and :math:`F_{Q}^{(cr)}(s)`
are defined in the :python:`SmeQcd.oneloop.gluon` module, together with the gluon
propagator :math:`\Delta(p^{2})`, dressing function :math:`J(s)`,

.. math::

  J(s)=p^{2}\Delta(p^{2})\ ,

and spectral function (in Minkowski space) :math:`\rho_{\Delta}(p^{2}_{M})`,

.. math::

  \rho_{\Delta}(p^{2}_{M})=2\, \mathrm{Im} \{\Delta(-p_{M}^{2}-i\varepsilon)\}\ .

--------------------------------------------------------------------------------

The ghost propagator
--------------------

In a general covariant gauge, the one-loop ghost self-energy :math:`\Sigma_{\text{gh}}(p^{2})`
can be expressed in terms of two functions, :math:`G(s)` and :math:`G_{\xi}(s)`:

.. math::

  \Sigma_{\text{gh}}(p^{2})=-\alpha p^{2} \left(G(s)+\xi G_{\xi}(s)+\text{const.}\right)\ .

The inverse ghost dressing function :math:`\chi^{-1}(s)` is then given by

.. math::

    \chi^{-1}(s)=1+\alpha \left(G(s) + \xi G_{\xi}(s)\right)+ \text{const.}=\alpha \left(G(s) + \xi G_{\xi}(s)+G_{0}\right)\ ,

where :math:`G_{0}` is an additive renormalization constant.

The functions :math:`G(s)` and :math:`G_{\xi}(s)` are defined in the :python:`SmeQcd.oneloop.ghost`
module together with the ghost propagator :math:`\mathcal{G}(p^{2})`, dressing function :math:`\chi(s)`,

.. math::

  \chi(s)=p^{2}\mathcal{G}(p^{2})\ ,

and spectral function (in Minkowski space) :math:`\rho_{\mathcal{G}}(p^{2}_{M})`,

.. math::

  \rho_{\mathcal{G}}(p^{2}_{M})=2\, \mathrm{Im} \{\mathcal{G}(-p_{M}^{2}-i\varepsilon)\}\ .

--------------------------------------------------------------------------------

The quark propagator
--------------------

The quark self-energy :math:`\Sigma(p^{2})` can be expressed as

.. math::

  \Sigma(p^{2})=i\slashed{p}\,\Sigma_{V}(p^{2})+\Sigma_{S}(p^{2})\ ,

where :math:`\Sigma_{V}(p^{2})` and :math:`\Sigma_{S}(p^{2})` are scalar functions. To
one loop, if only the ordinary quark loop and *quark-crossed* quark loop are included
in the quark self-energy, we say that the quark propagator is computed in the
**minimalistic scheme** (:python:`type='ms'`). If, on the other hand,
the *gluon-crossed* quark loop is also included in the self-energy, we say that
the propagator is computed in the **vertex-wise scheme** (:python:`type='vw'`).
Finally, we refer to a scheme in which the internal gluon line is replaced by
the principal part of the dressed gluon propagator as the **complex-conjugate
scheme** (:python:`type='cc'`).

In the minimalistic scheme, the quark self-energy is given by the sum :math:`\Sigma^{(2)}(p^{2})`
of the ordinary quark loop :math:`\Sigma^{(2)}(p^{1})` and of the quark-crossed loop:

.. math::

  \Sigma(p^{2})=\Sigma^{(2)}(p^{2})\ .

In the vertex-wise scheme, the gluon-crossed :math:`\Sigma^{(gl)}(p^{2})` loop is
also added to the self-energy:

.. math::

  \Sigma(p^{2})=\Sigma^{(2)}(p^{2})+\Sigma^{(gl)}(p^{2})\ .

In the complex-conjugate scheme, the quark-self energy is given by two terms, each
of which is obtained by replacing :math:`m^{2}\to p_{0}^{2}` -- where :math:`p_{0}^{2}`
is the Minkowski gluon pole -- in :math:`\Sigma^{(2)}(p^{2})`, and multiplying the term
by the corresponding residue :math:`R`:

.. math::

  \Sigma(p^{2})=R\left[\Sigma^{(2)}(p^{2})\right]_{m^{2}\to p_{0}^{2}}+\overline{R}\left[\Sigma^{(2)}(p^{2})\right]_{m^{2}\to \overline{p_{0}^{2}}}\ .

For an in-depth discussion of the minimalistic, vertex-wise and complex-conjugate schemes, see
`G. Comitini, D. Rizzo, M. Battello, and F. Siringo, Phys. Rev. D 104, 074020 (2021) <https://doi.org/10.1103/PhysRevD.104.074020>`_.

In any scheme, the quark propagator :math:`S(p)` can be expressed as

.. math::

  S(p)=\frac{Z(p^{2})}{p^{2}+\mathcal{M}^{2}(p^{2})}\,\left(i\slashed{p}+\mathcal{M}(p^{2})\right)\ ,

where

.. math::

  Z(p^{2})=\frac{1}{A(p^{2})}\ ,\qquad\mathcal{M}(p^{2})=\frac{B(p^{2})}{A(p^{2})}\ ,

and the functions :math:`A(p^{2})` and :math:`B(p^{2})` are obtained from the quark
self-energy as

.. math::

  A(p^{2}) = Z_{\psi}-\Sigma_{V}(p^{2})\ ,\qquad B(p^{2}) = M_{B}Z_{\psi}+\Sigma_{S}(p^{2})\ .

In the above equations, :math:`Z_{\psi}` is the quark field-strength renormalization constant.
To one loop, the following quantities are often used in place of :math:`Z_{\psi}` and
:math:`M_{B}`:

.. math::

  H_{0}=3\pi Z_{\psi}/\alpha_{s}\ ,\qquad K_{0}=\pi M_{B} Z_{\psi}/\alpha_{s}\ .

The vector and scalar components of the functions :math:`\Sigma^{(1)}(p^{2})`,
:math:`\Sigma^{(2)}(p^{2})` and :math:`\Sigma^{(gl)}(p^{2})` are defined
in the module :python:`PySmeQcd.oneloop.quark`, together with the functions
:math:`A(p^{2})`, :math:`B(p^{2})`, :math:`Z(p^{2})`, :math:`\mathcal{M}(p^{2})`,
the vector and scalar components :math:`S_{V/S}(p^{2})` of the quark propagator,

.. math::

  S(p)=i\slashed{p}\,S_{V}(p^{2})+S_{S}(p^{2})\ ,

and the vector and scalar components :math:`\rho_{S_{V/S}}(p^{2}_{M})` of the
quark spectral function in Minkowski space,

.. math::

  \rho_{S_{V/S}}(p^{2}_{M})=2\, \mathrm{Im} \{S_{V/S}(-p_{M}^{2}-i\varepsilon)\}\ .

References
----------

1. `F. Siringo, Nucl. Phys. B 907, 572 (2016) <https://doi.org/10.1016/j.nuclphysb.2016.04.028>`_
2. `F. Siringo, Phys. Rev. D 94, 114036 (2016) <https://doi.org/10.1103/PhysRevD.94.114036>`_
3. `F. Siringo, EPJ Web Conf. 137, 03021 (2017) <https://doi.org/10.1051/epjconf/201713703021>`_
4. `F. Siringo, EPJ Web Conf. 137, 13016 (2017) <https://doi.org/10.1051/epjconf/201713713016>`_
5. `F. Siringo, EPJ Web Conf. 137, 13017 (2017) <https://doi.org/10.1051/epjconf/201713713017>`_
6. `F. Siringo, Phys. Rev. D 96, 114020 (2017) <https://doi.org/10.1103/PhysRevD.96.114020>`_
7. `G. Comitini, arXiv:1803.02335 (2018) <https://arxiv.org/abs/1803.02335>`_
8. `G. Comitini and F. Siringo, Phys. Rev. D 97, 056013 (2018) <https://doi.org/10.1103/PhysRevD.97.056013>`_
9. `F. Siringo and G. Comitini, Phys. Rev. D 98, 034023 (2018) <https://doi.org/10.1103/PhysRevD.98.034023>`_
10. `F. Siringo, Phys. Rev. D 99, 094024 (2019) <https://doi.org/10.1103/PhysRevD.99.094024>`_
11. `G. Comitini, arXiv:1910.13022 (2019) <https://arxiv.org/abs/1910.13022>`_
12. `F. Siringo, Phys. Rev. D 100, 074014 (2019) <https://doi.org/10.1103/PhysRevD.100.074014>`_
13. `G. Comitini and F. Siringo, Phys. Rev. D 102, 094002 (2020) <https://doi.org/10.1103/PhysRevD.102.094002>`_
14. `F. Siringo and G. Comitini, Phys. Rev. D 103, 074014 (2021) <https://doi.org/10.1103/PhysRevD.103.074014>`_
15. `G. Comitini, D. Rizzo, M. Battello, and F. Siringo, Phys. Rev. D 104, 074020 (2021) <https://doi.org/10.1103/PhysRevD.104.074020>`_
