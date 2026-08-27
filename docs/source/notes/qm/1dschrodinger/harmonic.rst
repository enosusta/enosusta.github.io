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

.. dropdown:: 証明

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

これで時間に依存しない Schrödinger 方程式を解く方法が得られる。ある解が分かっていれば， `\hat{a}_+` を繰り返し作用させることで，より高いエネルギーを持つ解の「はしご」を作ることができる。しかし， `\hat{a}_-` を繰り返し作用させれば，やがて `E<0` の状態に到達してしまうが，これは不可能である。したがって，ある段階で `\hat{a}_-` を作用させるとゼロにならなければならない。つまり，ある解 `\psi_0` が存在して，

.. math::
    \hat{a}_-\psi_0 = 0

とならなければならない。この条件から基底状態を求めることができる。この条件は，

.. math::
    \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\dv{}{x} + m\omega x\right)\psi_0 = 0

すなわち，

.. math::
    \dv{\psi_0}{x} = -\frac{m\omega}{\hbar}x\psi_0

となる。両辺を積分すると，

.. math::
    \int \frac{\dd \psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\,\dd x

よって，

.. math::
    \ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + \text{const.}

すなわち，

.. math::
    \psi_0 = Ae^{-m\omega x^2/2\hbar}

となる。規格化条件は，

.. math::
    1 = |A|^2 \int_{-\infty}^{\infty} e^{-m\omega x^2/\hbar}\,\dd x = |A|^2 \sqrt{\frac{\pi\hbar}{m\omega}}

となるので， `A = (m\omega/\pi\hbar)^{1/4}` と選べる。したがって，基底状態は

.. math::
    \boxed{\psi_0 = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-m\omega x^2/2\hbar}}

となる。基底状態のエネルギーは，

.. math::
    E_0\psi_0 = \hbar\omega\left(\hat{a}_+\hat{a}_-+\frac{1}{2}\right)\psi_0 = \frac{1}{2}\hbar\omega\psi_0

となる。励起状態は基底状態に上昇演算子を繰り返し作用させれば得られる：

.. math::
    \boxed{\psi_n(x) = A_n (\hat{a}_+)^n \psi_0(x),\quad E_n = \hbar\omega\left(n+\frac{1}{2}\right)}

ここで `A_n` は規格化定数である。この手続きによって，全ての規格化可能な解が得られる [#]_ 。

規格化定数 `A_n` も代数的に求めることができる。まず，規格化された解 `\{\psi_n\}` について

.. math::
    \hat{a}_+\psi_n = c_n\psi_{n+1},\quad \hat{a}_-\psi_n = d_n\psi_{n-1}

と置く。ここで，任意の関数 `f,g` について，

.. math::
    \begin{aligned}
        \int f^*(\hat{a}_+ g)\,\dd x &= \frac{1}{\sqrt{2\hbar m\omega}}\int f^*\left(-\hbar\dv{g}{x} + m\omega x g\right)\,\dd x
        \\
        &= \frac{1}{\sqrt{2\hbar m\omega}}\int \left(\hbar\dv{f^*}{x} + m\omega x f^*\right)g\,\dd x
        \\
        &= \int (\hat{a}_- f)^* g\,\dd x
    \end{aligned}

となる。ここで部分積分を使った。同様に，

.. math::
    \int f^*(\hat{a}_- g)\,\dd x = \int (\hat{a}_+ f)^* g\,\dd x

となる。すなわち， `\hat{a}_\mp` は `\hat{a}_\pm` のエルミート共役である。また，

.. math::
    \begin{aligned}
        \hat{a}_+\hat{a}_-\psi_n &= (\hat{a}_-\hat{a}_+ - 1)\psi_n
        \\
        &= \left[\left(\frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}\right) - 1\right]\psi_n
        \\
        &= \left[\left(\frac{1}{\hbar\omega}E_n + \frac{1}{2}\right) - 1\right]\psi_n
        \\
        &= \left[\left(n+\frac{1}{2}\right) - \frac{1}{2}\right]\psi_n = n\psi_n
        \\
        \hat{a}_-\hat{a}_+\psi_n &= (\hat{a}_+\hat{a}_- + 1)\psi_n
        \\
        &= \left[\left(\frac{1}{\hbar\omega}E_n + \frac{1}{2}\right) + 1\right]\psi_n
        \\
        &= \left[\left(n+\frac{1}{2}\right) + \frac{1}{2}\right]\psi_n = (n+1)\psi_n
    \end{aligned}

となる。以上より，

.. math::
    \begin{aligned}
        |c_n|^2 &= \int (\hat{a}_+\psi_n)^*(\hat{a}_+\psi_n)\,\dd x
        \\
        &= \int \psi_n^*\hat{a}_-\hat{a}_+\psi_n\,\dd x = n+1
        \\
        |d_n|^2 &= \int (\hat{a}_-\psi_n)^*(\hat{a}_-\psi_n)\,\dd x
        \\
        &= \int \psi_n^*\hat{a}_+\hat{a}_-\psi_n\,\dd x = n
    \end{aligned}

となる。よって，位相を適当に選べば，

.. math::
    \boxed{\hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1},\quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1}}

となる。したがって，規格化された励起状態は，

.. math::
    \begin{aligned}
        \psi_1 &= \hat{a}_+\psi_0
        \\
        \psi_2 &= \frac{1}{\sqrt{2}}\hat{a}_+\psi_1 = \frac{1}{\sqrt{2!}}(\hat{a}_+)^2\psi_0
        \\
        \psi_3 &= \frac{1}{\sqrt{3}}\hat{a}_+\psi_2 = \frac{1}{\sqrt{3!}}(\hat{a}_+)^3\psi_0
        \\
        \psi_4 &= \frac{1}{\sqrt{4}}\hat{a}_+\psi_3 = \frac{1}{\sqrt{4!}}(\hat{a}_+)^4\psi_0
    \end{aligned}

となり，一般に

.. math::
    \boxed{\psi_n = \frac{1}{\sqrt{n!}}(\hat{a}_+)^n\psi_0}

となる。すなわち規格化定数 `A_n` は `1/\sqrt{n!}` である。

調和振動子型ポテンシャルの場合も，無限井戸型ポテンシャルの場合と同様に，解は正規直交していて完全である。

.. [#] もし別の解があると仮定すると，別のはしごが得られると思われるかもしれないが，最下段は `\hat{a}_-\psi_0=0` を必ず満たさなければならないので，結局はしごは同じでなければならない。
