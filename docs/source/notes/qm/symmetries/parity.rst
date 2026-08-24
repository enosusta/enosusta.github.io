パリティ
=============

空間反転はパリティ演算子 `\hat{\Pi}` によって表される。1次元では，

.. math::
    \hat{\Pi}\psi(x) = \psi'(x) = \psi(-x)

である。明らかに，パリティ演算子はそれ自身の逆演算子である：

.. math::
    \hat{\Pi}^{-1} = \hat{\Pi}

また，これはエルミートである：

.. math::
    \hat{\Pi}^{\dagger} = \hat{\Pi}

これらを合わせると，パリティ演算子はユニタリーでもあることが分かる：

.. math::
    \hat{\Pi}^{-1} = \hat{\Pi} = \hat{\Pi}^{\dagger}

任意の演算子は空間反転の下で

.. math::
    \hat{Q}' = \hat{\Pi}^\dagger \hat{Q} \hat{\Pi}

と変換される。位置演算子と運動量演算子はparityの下で

.. math::
    \begin{aligned}
        \hat{x}' &= \hat{\Pi}^\dagger \hat{x} \hat{\Pi} = -\hat{x}
        \\
        \hat{p}' &= \hat{\Pi}^\dagger \hat{p} \hat{\Pi} = -\hat{p}
    \end{aligned}

と変換される。これによって任意の演算子がどのように変換されるかが分かる：

.. math::
    \hat{Q}'(\hat{x},\hat{p}) = \hat{\Pi}^\dagger \hat{Q}(\hat{x},\hat{p}) \hat{\Pi} = \hat{Q}(-\hat{x},-\hat{p})

このようなパリティ変換によってハミルトニアンが変わらないなら系は反転対称性を持つという：

.. math::
    \hat{H}' = \hat{\Pi}^\dagger \hat{H} \hat{\Pi} = \hat{H}

あるいはユニタリー性より

.. math::
    [\hat{H},\hat{\Pi}] = 0

ハミルトニアンが1次元ポテンシャル `V(x)` 中の質量 `m` の粒子を記述するなら，反転対称性は，単にポテンシャルが位置についての偶関数であることを意味する：

.. math::
    V(x) = V(-x)

反転対称性の重要な結果は2つある。まず， `\hat{\Pi}` と `\hat{H}` の同時固有状態の完全系を `\psi_n` と書くと

.. math::
    \hat{\Pi}\psi_n(x) = \psi_n(-x) = \pm \psi_n(x)

を満たすので，パリティ演算子の固有値は `\pm 1` に限られる。したがって，位置の偶関数であるポテンシャルの定常状態は偶関数か奇関数である [#]_ 。この性質は，調和振動子型ポテンシャルの場合や無限井戸型ポテンシャル，デルタ関数型ポテンシャルの場合で既に示した。

次に，一般化された Ehrenfest の定理によれば，ハミルトニアンが反転対称性を持つならば，

.. math::
    \dv{}{t}\braket{\Pi} = \frac{i}{\hbar}\braket{[\hat{H},\hat{\Pi}]} = 0

なので，対称なポテンシャル中を運動する粒子についてパリティは保存する。しかも前節の定理によれば，期待値だけでなく，測定で任意の特定の結果が得られる確率も時刻に依存しない。

3次元においてパリティ演算子が生成する空間反転は

.. math::
    \hat{\Pi}\psi(\bm{r}) = \psi'(\bm{r}) = \psi(-\bm{r})

である。位置演算子と運動量演算子はパリティの下で

.. math::
    \begin{aligned}
        \hat{\bm{r}}' &= \hat{\Pi}^\dagger \hat{\bm{r}} \hat{\Pi} = -\hat{\bm{r}}
        \\
        \hat{\bm{p}}' &= \hat{\Pi}^\dagger \hat{\bm{p}} \hat{\Pi} = -\hat{\bm{p}}
    \end{aligned}

と変換される。よって任意の演算子は，

.. math::
    \hat{Q}'(\hat{\bm{r}},\hat{\bm{p}}) = \hat{\Pi}^\dagger \hat{Q}(\hat{\bm{r}},\hat{\bm{p}}) \hat{\Pi} = \hat{Q}(-\hat{\bm{r}},-\hat{\bm{p}})

と変換される。パリティが偶であるベクトルやスカラーは擬ベクトルや擬スカラーと呼ばれる。

3次元では，ポテンシャル `V(\bm{r})` 中を運動する質量 `m` の粒子のハミルトニアンは

.. math::
    V(-\bm{r}) = V(\bm{r})

ならば反転対称性を持つ。特に全ての中心力ポテンシャルはこの条件を満たす。例えば水素原子の電子を表す波動関数

.. math::
    \psi_{nlm}(\bm{r}) = R_{nl}(r)Y_l^m(\theta,\phi)

はパリティの固有状態

.. math::
    \hat{\Pi}\psi_{nlm}(\bm{r}) = (-1)^l\psi_{nlm}(\bm{r})

である。

さて，選択則というものは，系の対称性に基づいて，行列要素がいつゼロになるかを教えるものである。ここで行列要素とは

.. math::
    \braket{b|\hat{Q}|a}

という形の任意の量であり，期待値とは `a=b=\psi` の特別な場合である。選択則が物理的に重要な演算子のひとつとして，電気双極子モーメント演算子

.. math::
    \hat{\bm{p}}_e = q\hat{\bm{r}}

がある。この演算子の選択則は，どの原子遷移が許され，どれが禁止されるかを決定する（詳しくは後で説明する）。位置ベクトルは奇なので，これもパリティの下で奇である：

.. math::
    \hat{\Pi}^\dagger\hat{\bm{p}}_e\hat{\Pi} = -\hat{\bm{p}}_e

ここで，2つの状態 `\psi_{nlm}` と `\psi_{n'l'm'}` の間の電気双極子モーメント演算子の行列要素を考える：

.. math::
    \begin{aligned}
        \braket{n'l'm'|\hat{\bm{p}}_e|nlm} &= -\braket{n'l'm'|\hat{\Pi}^\dagger\hat{\bm{p}}_e\hat{\Pi}|nlm}
        \\
        &= -\braket{n'l'm'|(-1)^{l'}\hat{\bm{p}}_e(-1)^l|nlm}
        \\
        &= (-1)^{l+l'+1}\braket{n'l'm'|\hat{\bm{p}}_e|nlm}
    \end{aligned}

したがって，

.. math::
    \braket{n'l'm'|\hat{\bm{p}}_e|nlm} = 0 \quad \text{if } l+l' \text{ is even}

となる。これは Laporte 則と呼ばれ，パリティが同じ状態の間では，双極子モーメント演算子の行列式がゼロになることを意味する。より一般に Laporte 則はパリティが奇である任意の演算子に適用される。

.. [#] 縮退がある場合は，そのように選ぶことができる。
