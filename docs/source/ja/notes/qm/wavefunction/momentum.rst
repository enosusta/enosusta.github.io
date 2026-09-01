運動量
==================

状態 `\Psi(\bm{x},t)` にある粒子について，位置 `x` の期待値は

.. math::
    \braket{\bm{x}} = \int_{\R^3} \bm{x} |\Psi(\bm{x},t)|^2\,\dd^3x

と書ける。これはひとつの粒子の位置を何度も繰り返し測定するときに得られる値の平均 **ではない** 。これまでに学んだことは，最初の測定によって，波動関数は実際の値に局在化（collapse）し，その直後の測定は単に同じ値が得られるということである。したがって， `\braket{\bm{x}}` は **すべて同じ状態** `\Psi(\bm{x},t)` **にある** 粒子について行われた測定結果の平均である。これは例えば，各々が同じ状態 `\Psi(\bm{x},t)` にある粒子のアンサンブル全体を用意し，その全ての位置を測定して得られる値の平均である。

波動関数 `\Psi(\bm{x},t)` は時間に依存するので，位置の期待値 `\braket{\bm{x}}` も時間発展する。その速度は，

.. math::
    \begin{aligned}
        \dv{\braket{\bm{x}}}{t} &= \int_{\R^3} \bm{x} \dv{}{t} |\Psi(\bm{x},t)|^2\,\dd^3x
        \\
        &= \frac{i\hbar}{2m}\int_{\R^3}\bm{x}\nabla\left(\Psi^*\nabla\Psi-\Psi\nabla\Psi^*\right)\,\dd^3x
        \\
        &= -\frac{i\hbar}{2m}\int_{\R^3}\left(\Psi^*\nabla\Psi-\Psi\nabla\Psi^*\right)\,\dd^3x
    \end{aligned}

となる。ここで，積分の部分積分を行い，境界条件として `\Psi(\bm{x},t)\to 0` （`|\bm{x}|\to\infty`）を用いた。さらに右辺の第二項について部分積分を行うと，

.. math::
    :label: eq:velocity-expectation-value

    \dv{\braket{\bm{x}}}{t} = -\frac{i\hbar}{m}\int_{\R^3}\Psi^*\nabla\Psi\,\dd^3x

となる。これは位置 `x` の期待値の「速度」であって，粒子の速度ではないことに注意する。量子力学において粒子の速度が何を意味するのかさえ明らかでない。粒子は測定以前に定まった位置を持たないので，明確な速度も持たない。波動関数 `\Psi(\bm{x},t)` が与えられたときに速度の確率密度を構成する方法は後で見る。結果だけ先に伝えると，

.. math::
    \braket{\bm{v}} = \dv{\braket{\bm{x}}}{t}

となる。したがって，式 :eq:`eq:velocity-expectation-value` は波動関数 `\Psi(\bm{x},t)` から 速度の期待値 `\braket{\bm{v}}` を計算する方法を与えている。

実際には，速度よりも運動量を扱うのが慣例である：

.. math::
    \braket{\bm{p}} = m\dv{\braket{\bm{x}}}{t} = -i\hbar\int_{\R^3}\Psi^*\nabla\Psi\,\dd^3x

これらの表式をより示唆的な形に書いておこう：

.. math::
    \begin{aligned}
        \braket{\bm{x}} &= \int_{\R^3} \Psi^*[\bm{x}]\Psi\,\dd^3x
        \\
        \braket{\bm{p}} &= \int_{\R^3} \Psi^*[-i\hbar\nabla]\Psi\,\dd^3x
    \end{aligned}

そうすると， `\bm{x}` や `-i\hbar\nabla` という「演算子」が位置や運動量を表し，その期待値を計算するためには，その演算子を `\Psi^*` と `\Psi` の間に挟んで積分すればよいことがわかる。

その他の古典的な力学変数はすべて位置と運動量を用いて表すことができるので，任意の力学変数 `Q(x,p)` の期待値は，単に全ての `\bm{p}` を `-i\hbar\nabla` に置き換え，その結果を `\Psi^*` と `\Psi` の間に挟んで積分すればよい：

.. math::
    \braket{Q(\bm{x},\bm{p})} = \int_{\R^3} \Psi^*[Q(\bm{x},-i\hbar\nabla)]\Psi\,\dd^3x

これは `\braket{\bm{x}}` や `\braket{\bm{p}}` の表式を特別な場合として含む。
