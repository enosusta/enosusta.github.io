規格化
==================

`|\Psi(\bm{x},t)|^2` は時刻 `t` に点 `\bm{x}` で粒子を見出す確率密度であるから，すべての `x` に渡る `|\Psi(\bm{x},t)|^2` の積分は `1` でなければならない：

.. math::
    \int_{\mathbb{R}^3} |\Psi(\bm{x},t)|^2\,\dd^3x = 1

ここで Schrödinger 方程式

.. math::
    i\hbar\pdv{}{t}\Psi(\bm{x},t) = -\frac{\hbar^2}{2m}\nabla^2\Psi(\bm{x}, t) + V(\bm{x})\Psi(\bm{x}, t)

を見ると，もし `\Psi(\bm{x},t)` が解ならば， `A` を任意の複素定数として `A\Psi(\bm{x},t)` も解であることが分かる。これを使って規格化条件を満たすように `A` を選ぶことができる。この手続きを **規格化** と呼ぶ [#]_ 。しかし，積分が発散する場合や，解が自明 `\Psi(\bm{x},t) = 0` である場合には規格化できないため，捨てなければならない。したがって，物理的に実現可能な状態は，Schrödinger 方程式の **二乗可積分** な解に対応する。

しかし，波動関数は Schrödinger 方程式によって決定されるはずなので，両者が同時に成り立たなければならない。つまり，時刻 `t=0` に波動関数を規格化したとして，時間が経った後に規格化されていなければならない。そうでなければ， `A` が時刻 `t` の関数となり， `A\Psi(\bm{x},t)` はもはや Schrödinger 方程式の解ではなくなる。幸いなことに，Schrödinger 方程式は規格化を自動的に保つことが証明できる。

これを証明するには，

.. math::
    \dv{}{t}\int_{\mathbb{R}^3} |\Psi(\bm{x},t)|^2\,\dd^3x = \int_{\mathbb{R}^3} \pdv{}{t}|\Psi(\bm{x},t)|^2\,\dd^3x

がゼロになることを示せば良い。ここで左辺の積分は `t` の関数なので，全微分の記号を用いるが，右辺の被積分関数は `x` と `t` の関数なので，偏微分の記号を用いている。微分の Leibniz 則より，

.. math::
    \pdv{}{t}|\Psi|^2 = \pdv{}{t}(\Psi^*\Psi) = \Psi\pdv{\Psi^*}{t} + \Psi^*\pdv{\Psi}{t}

となる。一方で，Schrödinger 方程式より，

.. math::
    \pdv{\Psi}{t} = \frac{i\hbar}{2m}\nabla^2\Psi - \frac{i}{\hbar}V\Psi

であり，その複素共役を取ると

.. math::
    \pdv{\Psi^*}{t} = -\frac{i\hbar}{2m}\nabla^2\Psi^* + \frac{i}{\hbar}V\Psi^*

となる。したがって，

.. math::
    \begin{aligned}
        \pdv{}{t}|\Psi|^2 &= \frac{i\hbar}{2m}\left(\Psi^*\nabla^2\Psi - \Psi\nabla^2\Psi^*\right)
        \\
        &= \nabla \left[\frac{i\hbar}{2m}\left(\Psi^*\nabla\Psi - \Psi\nabla\Psi^*\right)\right]
    \end{aligned}

となる。これで積分は，

.. math::
    \dv{}{t}\int_{\R^3}|\Psi(\bm{x},t)|^2\ \dd^3{x} = \left.\frac{i\hbar}{2m}\left(\Psi^*\nabla\Psi-\Psi\nabla\Psi^*\right)\right|_{\partial\R^3}

となる。ここで `\partial\R^3` は `\R^3` の無限遠の境界であり，もし `\Psi(\bm{x},t)` が無限遠でゼロになるならば，右辺はゼロになる。そうでなければ，波動関数は規格化できない [#]_ 。したがって， `\Psi(\bm{x},t)` は時刻 `t=0` で規格化されていれば，以降の全ての時刻に渡って規格化されたままである。

.. [#] 規格化によって定まるのは `A` の絶対値だけであり，その位相は決まらない。しかし，位相はいずれにせよ物理的な意味を持たない。

.. [#] 数学者なら反例を示すかもしれないが，そのような病的な解は物理的に現れないと思うことにする。
