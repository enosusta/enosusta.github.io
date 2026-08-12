調和振動子型ポテンシャル：代数的方法
=====================================

次のポテンシャルを考える：

.. math::
    V(x) = \frac{1}{2} m \omega^2 x^2

ここで， `m` と `\omega` はそれぞれ質量と角振動数である。これはほとんどどんなポテンシャルでも局所的な極小点の近くでは近似的に調和振動子型ポテンシャルが現れるので重要である。

時間に依存しない Schrödinger 方程式は，

.. math::
    -\frac{\hbar^2}{2m} \dv{^2\psi}{x^2} + \frac{1}{2} m \omega^2 x^2 \psi = E \psi

となる。この解法には異なる2つの方法がある。

1. 冪級数を用いた解析的な方法
2. 昇降演算子を用いた代数的な方法

方法 1 は多くの他のポテンシャルに対してできるが比較的複雑である。方法 2 は使用できる場合は限られるが比較的単純である。ここでは方法 2 を用いて解く。次節では方法 1 を用いて解く。

まず時間に依存しない Schrödinger 方程式を

.. math::
    \hat{H} \psi = E \psi,\quad \hat{H} = \frac{1}{2m}[\hat{p}^2 + (m \omega x)^2]

と書き直す。ここで `\hat{p} = -i \hbar \dv{}{x}` は運動量演算子である。普通の数なら， `u^2+v^2=(iu+v)(-iu+v)` のように因数分解できるが，演算子 `\hat{p}` と `x` は可換ではないので単純に因数分解できない。そこで演算子

.. math::
    \hat{a}_{\pm} \coloneqq \frac{1}{\sqrt{2\hbar m\omega}}(\mp i \hat{p} + m \omega x)

を定義する。ここで係数は最終的な結果の見栄えをよくするために付けた。そうすると，

.. math::
    \begin{aligned}
        \hat{a}_{-}\hat{a}_{+} &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega x)(-i\hat{p}+m\omega x)
        \\
        &= \frac{1}{2\hbar m\omega}(\hat{p}^2 + (m\omega x)^2 - i m \omega(x\hat{p}-\hat{p}x))
    \end{aligned}

となる。演算子の非可換性により余分な項 `x\hat{p}-\hat{p}x` が現れた。これは `x` と `\hat{p}` の **交換関係** と呼ばれ，両者の可換性の度合いを表す。一般に，2つの演算子の交換子は

.. math::
    [\hat{A},\hat{B}] \coloneqq \hat{A}\hat{B}-\hat{B}\hat{A}
    
と定義される。この記法を用いると，

.. math::
    \hat{a}_{-}\hat{a}_{+} = \frac{1}{2\hbar m\omega}[\hat{p}^2 + (m\omega x)^2] - \frac{i}{2\hbar}[x,\hat{p}]

となる。交換子 `[\hat{x},\hat{p}]` を求めるには，作用するテスト関数 `f(x)` を与えて，最後のテスト関数を捨てて演算子だけの式を残す，というようにすると間違いが少ない。つまり，

.. math::
    \begin{aligned}
        [x,\hat{p}]f(x) &= \left[x(-i\hbar)\dv{}{x}-(-i\hbar)\dv{}{x}x\right]f(x)
        \\
        &= -i\hbar\left(x\dv{f}{x}-x\dv{f}{x}-f\right) = i\hbar f(x)
    \end{aligned}

となるので，

.. math::
    \boxed{[x,\hat{p}] = i\hbar}

である。これは **正準交換関係** と呼ばれる。この結果を用いると，

.. math::
    \hat{a}_{-}\hat{a}_{+} = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}

すなわち，

.. math::
    \hat{H} = \hbar\omega\left(\hat{a}_{-}\hat{a}_{+} - \frac{1}{2}\right)

となる。ここで演算子 `\hat{a}_+` と `\hat{a}_-` の順番が重要である。もし `\hat{a}_+` を左側において同様の議論をしたならば，

.. math::
    \hat{a}_{+}\hat{a}_{-} = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}

となり，

.. math::
    [\hat{a}_{-},\hat{a}_{+}] = 1

という交換関係が得られる。これらをまとめると結局，時間に依存しない Schrödinger 方程式は

.. math::
    \hbar\omega\left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2}\right)\psi = E\psi

となる。

ここで演算子 `\hat{a}_{\pm}` を特徴づける重要な性質を述べる：

.. important::
    `\psi` がエネルギー `E` を持つ Schrödinger 方程式の解であるとする。このとき， `\hat{a}_{\pm}\psi` はエネルギー `E \pm \hbar\omega` を持つ Schrödinger 方程式の解である。

.. admonition:: 証明 [hide/show]
    :collapsible: closed

    まず， `\hat{a}_{+}` の場合を考える：
    
    .. math::
        \begin{aligned}
            \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega\left(\hat{a}_{+}\hat{a}_{-} + \frac{1}{2}\right)(\hat{a}_{+}\psi)
            \\
            &= \hbar\omega\left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+}\right)\psi
            \\
            &= \hbar\omega\hat{a}_{+}\left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\right)\psi
            \\
            &= \hat{a}_{+}\left[\hbar\omega\left(\hat{a}_{+}\hat{a}_{-} + 1 + \frac{1}{2}\right)\psi\right]
            \\
            &= \hat{a}_{+}(\hat{H}+\hbar\omega)\psi
            \\
            &= \hat{a}_{+}(E+\hbar\omega)\psi
            \\
            &= (E+\hbar\omega)(\hat{a}_{+}\psi)
        \end{aligned}

    同様に， `\hat{a}_{-}` の場合も考える：

    .. math::
        \begin{aligned}
            \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega\left(\hat{a}_{-}\hat{a}_{+} - \frac{1}{2}\right)(\hat{a}_{-}\psi)
            \\
            &= \hbar\omega\left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-}\right)\psi
            \\
            &= \hbar\omega\hat{a}_{-}\left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\right)\psi
            \\
            &= \hat{a}_{-}\left[\hbar\omega\left(\hat{a}_{+}\hat{a}_{-} - 1 + \frac{1}{2}\right)\psi\right]
            \\
            &= \hat{a}_{-}(\hat{H}-\hbar\omega)\psi
            \\
            &= \hat{a}_{-}(E-\hbar\omega)\psi
            \\
            &= (E-\hbar\omega)(\hat{a}_{-}\psi)
        \end{aligned}

したがって， `\hat{a}_{+}` は時間に依存しない Schrödinger 方程式の解に作用して，それより一段高いエネルギーの解を生み出す。一方で， `\hat{a}_{-}` は時間に依存しない Schrödinger 方程式の解に作用して，それより一段低いエネルギーの解を生み出す。そのため， `\hat{a}_{+}` は **上昇演算子** (raising operator) と呼ばれ， `\hat{a}_{-}` は **下降演算子** (lowering operator) と呼ばれ，両方合わせて **昇降演算子** (ladder operator) と呼ばれる。
