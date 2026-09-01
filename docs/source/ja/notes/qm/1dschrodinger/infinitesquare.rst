無限井戸型ポテンシャル
=========================

次のポテンシャルを考える：

.. math::
    V(x) = \begin{cases}
        0 & (0 \le x \le a) \\
        \infty & (\text{otherwise})
    \end{cases}

このポテンシャルは人工的なものだが，その単純さにもかかわらず，いや単純であるがゆえに，後に登場するさまざま機構に対して基礎的な理解を与えてくれる。

井戸の外側で粒子を見出すことはないはずなので `\psi(x)=0` であり，井戸の内側では，時間に依存しない Schrödinger 方程式は，

.. math::
    -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi

すなわち，

.. math::
    \frac{d^2\psi}{dx^2} = -k^2\psi, \quad k \coloneqq \frac{\sqrt{2mE}}{\hbar}

となる。ここで暗黙的に `E\ge 0` とした。実は `E<0` の場合は上手くいかない。この方程式は良く知られた単振動の方程式であり，一般解は，

.. math::
    \psi(x) = A\sin(kx) + B\cos(kx)

である。ここで `A,B` は任意定数で通常これらは問題の境界条件で決まる。通常は， `\psi` と `\dv{\psi}{x}` の両方が連続であるが，今回の場合にようにポテンシャルが無限大になるところでは， `\psi` のみが連続である [#]_ 。

`\psi(x)` の連続性から，井戸の内側と外側の解は，

.. math::
    \psi(0) = \psi(a) = 0

で接続されていなければならない。そうすると，まず，

.. math::
    \psi(0) = A\sin(0) + B\cos(0) = B = 0

であり，したがって，

.. math::
    \psi(x) = A\sin(kx)

となる。次に， `\psi(a)=A\sin(ka)=0` なので， `A=0` であるか， `\sin(ka)=0` である。前者の場合は，自明な解しか残らないため捨てられる。後者の場合は，

.. math::
    ka = 0,\,\pm\pi\,\pm2\pi\,\pm3\pi,\ldots

を意味する。この内， `k=0` はまた自明な解しか残らないため捨てられる。また， `\sin(-\theta)=-\sin(\theta)` であり，負符号は定数 `A` に吸収できるので，負の `k` から新しいものは得られない。したがって，互いに異なる解として，

.. math::
    k_n = \frac{n\pi}{a},\quad n=1,2,3,\ldots

が残る。このように， `x=a` における境界条件によって決定されるのは `A` ではなく `k` である。したがって， `E` の値が制限される：

.. math::
    \boxed{E_n = \frac{\hbar^2k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}}

定数 `A` を求めるには， `\psi` を規格化する：

.. math::
    \int_0^a |A|^2\sin^2(kx)\,\dd x = |A|^2\frac{a}{2} = 1 \implies |A| = \sqrt{\frac{2}{a}}

これで決まるのは `A` の大きさだけだが， `A` の位相は物理的な意味を持たないため， `A=\sqrt{2/a}` としてよい。したがって，緯度の内側での解は，

.. math::
    \boxed{\psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)}

となる。

前節での述べた通り，時間に依存しない Schrödinger 方程式から，離散的なエネルギーを持つ解が得られた。最も低いエネルギーを持つ `\psi_1` は **基底状態** と呼ばれ，それ以外の解は **励起状態** と呼ばれる。 

得られた関数の集合 `\{\psi_n\}` はいくつかの重要な性質を持つ：

1.  井戸の中心について偶関数か奇関数である。 

2.  エネルギーを挙げていくと節がひとつずつ増えていく。

3.  それらは **正規直交** している：

    .. math::
        \int_0^a \psi_m^*(x)\psi_n(x)\,\dd x = \delta_{mn}

    `m=n` の場合は規格化条件から `1` となる。 `m\neq n` の場合，

    .. math::
        \begin{aligned}
            \int_0^a \psi_m^*(x)\psi_n(x)\,\dd x &= \frac{2}{a}\int_0^a \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi x}{a}\right)\,\dd x \\
            &= \frac{1}{a}\int_0^a \left[\cos\left(\frac{(m-n)\pi x}{a}\right) - \cos\left(\frac{(m+n)\pi x}{a}\right)\right]\,\dd x \\
            &= \left[\frac{1}{(m-n)\pi}\sin\left(\frac{(m-n)\pi x}{a}\right) - \frac{1}{(m+n)\pi}\sin\left(\frac{(m+n)\pi x}{a}\right)\right]_0^a
            \\
            &= 0
        \end{aligned}

    となる。

4.  それらは **完全** である。すなわち，任意の関数 `f(x)` をそれらの線形結合

    .. math::
        f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty}c_n\sin\left(\frac{n\pi}{a}x\right)

    で表すことができる。このような性質は Dirichlet の定理によって保証されている。これは `f(x)` の Fourier 級数に他ならない。したがって，係数 `c_n` は Fourier の方法に従って求めることができる。両辺に `\psi_m^*` を掛けて積分すると，

    .. math::
        \int_0^a \psi_m(x)^*f(x)\,\dd x = \sum_{n=1}^{\infty}c_n\int_0^a\psi_m(x)^*\psi_n(x)\,\dd x = \sum_{n=1}^{\infty}c_n\delta_{mn} = c_m

    となる。したがって，

    .. math::
        \boxed{c_n = \int_0^a \psi_n(x)^*f(x)\,\dd x}

    である。

これらの性質は，無限井戸型ポテンシャルだけに特有のものではない。性質 1 は，ポテンシャルが対称な場合に成り立つし，性質 2,3 は，ポテンシャルに依らず成り立つ。性質 4 は通常考えるようなポテンシャルに対して成り立つが証明はやや面倒である。

時間に依存する Schrödinger 方程式の一般解は，定常状態の線形結合

.. math::
    \Psi(x,t) = \sum_{n=1}^{\infty}c_n\sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right)e^{-i(n^2\pi^2\hbar/2ma^2)t}

である。係数 `c_n` は初期条件

.. math::
    \Psi(x,0) = \sum_{n=1}^{\infty}c_n\sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right)

を満たすように選ばれ，Fourier の方法によって

.. math::
    c_n = \sqrt{\frac{2}{a}}\int_0^a\sin\left(\frac{n\pi}{a}x\right)\Psi(x,0)\,\dd x

で求められる。

これで終わりである。波動関数が手に入ったので，任意の力学変数の期待値を計算することができる。特に，エネルギーの期待値については，

.. math::
    \begin{aligned}
        \braket{H} &= \int_0^a\Psi^*\hat{H}\Psi\,\dd x = \int_0^a\left(\sum_{m=1}^{\infty}c_m\psi_m\right)^*\hat{H}\left(\sum_{n=1}^{\infty}c_n\psi_n\right)\,\dd x
        \\
        &= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_nE_n\int_0^a\psi_m^*\psi_n\,\dd x = \sum_{n=1}^{\infty}|c_n|^2E_n
    \end{aligned}

と求まる。さらに，性質 3 と規格化条件を用いることで，係数 `c_n` が満たすべき条件を確認することができる：

.. math::
    \begin{aligned}
        1 &= \int_0^a|\Psi(x,0)|^2\,\dd x = \int_0^a\left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)\,\dd x
        \\
        &= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int_0^a\psi_m(x)^*\psi_n(x)\,\dd x = \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\delta_{mn}
        \\
        &= \sum_{n=1}^{\infty}|c_n|^2
    \end{aligned}

以上のような手続きがどのポテンシャルの場合にも適用される。変更されるのは， `\psi` の関数形と許されるエネルギーの値だけである。

.. [#] これらの条件と， `V=\infty` の場合の例外については後で詳しく説明する。
