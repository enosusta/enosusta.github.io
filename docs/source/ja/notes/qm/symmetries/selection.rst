回転対称性に関する選択則
=============================

量子力学における回転に関する選択則の最も一般的な記述は Wigner--Eckart の定理によって与えられる。ここでは定理を一般的な形で証明する代わりに，スカラー演算子とベクトル演算子に対する選択則を導出することにする。

スカラー演算子に対する選択則
-----------------------------------

スカラー演算子 `\hat{f}` は定義より，

.. math::
    \begin{aligned}
        [\hat{L}_z,\hat{f}] &= 0
        \\
        [\hat{L}_\pm,\hat{f}] &= 0
        \\
        [\hat{L}^2,\hat{f}] &= 0
    \end{aligned}
    
である。これらの交換子を角運動量が定まった2つの状態 `\ket{nlm},\ket{n'l'm'}` で挟むことによって `\hat{f}` に対する選択則を導く。これらの状態は水素原子型軌道であってもよいが，そうである必要はない。必要なのは， `\ket{nlm}` は `\hat{L}^2` と `\hat{L}_z` の固有状態であるということである。

まず，

.. math::
    \braket{n'l'm'|[\hat{L}_z,\hat{f}]|nlm} = \braket{n'l'm'|\hat{L}_z\hat{f}-\hat{f}\hat{L}_z|nlm} = 0

したがって， `\hat{L}_z` のエルミート性を用いれば，

.. math::
    (m'-m)\braket{n'l'm'|\hat{f}|nlm} = 0

となる。よって， `m'-m \eqqcolon \Delta m = 0` でない限り行列要素はゼロである。同様に，

.. math::
    [l'(l'+1)-l(l+1)]\braket{n'l'm'|\hat{f}|nlm} = 0

したがって， `l'-l \eqqcolon \Delta l = 0` でない限り行列要素はゼロである [#]_ 。以上より，スカラー演算子に対する選択則は `\Delta l = 0` および `\Delta m = 0` である。

残る交換関係は，許される行列要素の間の関係を与える。ここでは `\hat{L}_+` の場合を考えると， `(\hat{L}_+)^\dagger = \hat{L}_-` より，

.. math::
    B_{l'}^{m'}\braket{n'l'(m'-1)|\hat{f}|nlm} - A_l^m\braket{n'l'm'|\hat{f}|nl(m+1)} = 0

となる。ここで，

.. math::
    A_l^m \coloneqq \hbar\sqrt{l(l+1)-m(m+1)},\quad B_l^m \coloneqq \hbar\sqrt{l(l+1)-m(m-1)}

とした。この2つの項は `m'=m+1,l'=l` でない限りゼロである。もしその場合， `B_l^{m+1} = A_l^m` であるから，

.. math::
    \braket{n'lm|\hat{f}|nlm} = \braket{n'l(m+1)|\hat{f}|nl(m+1)}

となる。すなわち，行列要素は `m` に依存しない。

以上の結果をまとめると，

.. math::
    \boxed{\braket{n'l'm'|\hat{f}|nlm} = \delta_{ll'}\delta_{mm'}\braket{n'l||\hat{f}||nl}}

となる。ここで `\braket{n'l||\hat{f}||nl}` は **換算行列要素** と呼ばれ， `n,l,n'` には依存するが， `m` には依存しない。

ベクトル演算子に対する選択則
-------------------------------

ベクトル演算子 `\hat{\bm{V}}` の場合はより手間がかかるが，その結果は，原子遷移を扱う後の章にとって重要である。まず，

.. math::
    \hat{V}_\pm \coloneqq \hat{V}_x \pm i\hat{V}_y

と定義する。そうすると，定義より，

.. math::
    \begin{aligned}
        [\hat{L}_z,\hat{V}_z] &= 0
        \\
        [\hat{L}_z,\hat{V}_\pm] &= \pm\hbar\hat{V}_\pm
        \\
        [\hat{L}_\pm,\hat{V}_\pm] &= 0
        \\
        [\hat{L}_\pm,\hat{V}_z] &= \mp\hbar\hat{V}_\pm
        \\
        [\hat{L}_\pm,\hat{V}_\mp] &= \pm2\hbar\hat{V}_z
    \end{aligned}

となる（複合同順）。先ほどと同様に，これらの交換関係を角運動量が定まった2つの状態 `\ket{nlm},\ket{n'l'm'}` で挟むことによって，ベクトル演算子に対する選択則を導く。

そうすると，行列要素が必ずゼロになる条件は，

.. math::
    \begin{aligned}
        \braket{n'l'm'|\hat{V}_+|nlm} &= 0 \quad \text{unless} \quad  m' = m + 1
        \\
        \braket{n'l'm'|\hat{V}_z|nlm} &= 0 \quad \text{unless} \quad  m' = m
        \\
        \braket{n'l'm'|\hat{V}_-|nlm} &= 0 \quad \text{unless} \quad  m' = m - 1
    \end{aligned}

となる。もちろん， `x` および `y` 成分の行列要素は，

.. math::
    \begin{aligned}
        \braket{n'l'm'|\hat{V}_x|nlm} &= \frac{1}{2}[\braket{n'l'm'|\hat{V}_-|nlm} + \braket{n'l'm'|\hat{V}_+|nlm}]
        \\
        \braket{n'l'm'|\hat{V}_y|nlm} &= \frac{i}{2}[\braket{n'l'm'|\hat{V}_-|nlm} - \braket{n'l'm'|\hat{V}_+|nlm}]
    \end{aligned}

から求められる。残りの交換関係は， `l` に関する選択則と，ゼロでない行列要素の間の関係を与える。その結果が，ベクトル演算子 `\hat{\bm{V}}` に対する Wigner--Eckart の定理である：

.. math::
    \boxed{
        \begin{aligned}
            \braket{n'l'm'|\hat{V}_+|nlm} &= -\sqrt{2}C_{m1m}^{l1l'}\braket{n'l'||\hat{\bm{V}}||nl}
            \\
            \braket{n'l'm'|\hat{V}_-|nlm} &= \sqrt{2}C_{m-1m}^{l1l'}\braket{n'l'||\hat{\bm{V}}||nl}
            \\
            \braket{n'l'm'|\hat{V}_z|nlm} &= C_{m0m}^{l1l'}\braket{n'l'||\hat{\bm{V}}||nl}
        \end{aligned}
    }

ここで定数 `C_{m_1m_2M}^{j_1j_2J}` は角運動量の合成で現れた Clebsch--Gordan 係数に他ならない。Clebsh--Gordan 係数は， `M=m_1+m_2` で，かつ `J=j_1+j_2,j_1+j_2-1,\ldots,|j_1-j_2|` のときに限りゼロでない。したがって，ベクトル演算子の任意の成分 `\hat{V}_i` の行列要素がゼロでないのは，特に

.. math::
    \boxed{\Delta l = 0,\pm1,\quad \Delta m = 0,\pm1}

のときである。

ここで Clebsh--Gordan 係数が現れるのは偶然ではない。状態は角運動量を持つが，演算子も角運動量を持つ。スカラー演算子は `l=0` であり，角運動量ゼロの状態が回転によって変化しないのと同様に，回転によって変化しない。ベクトル演算子は `l=1` であり，その成分は，角運動量 `l=1` の三重項のなす状態が回転の下で互いに変換されるのと同様に，互いに変換される。演算子を状態に作用させるとき，状態と演算子の角運動量が加わる。この角運動量の合成こそが，Clebsh--Gordan 係数が現れる理由である。

.. [#] 方程式 `l'(l'+1)-l(l+1) = 0` のもうひとつの解は `l' = -(l+1)` であるが， `l` と `l'` はともに非負であるから，この解は許されない。
