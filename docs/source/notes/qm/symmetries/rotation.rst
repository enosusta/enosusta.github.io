回転対称性
=================

関数を `z` 軸のまわりに角度 `\varphi` だけ回転させる演算子は

.. math::
    \hat{R}_z(\varphi)\psi(r,\theta,\phi) = \psi'(r,\theta,\phi) = \psi(r,\theta,\phi-\varphi)

であり，前々節の議論と同様にして，

.. math::
    \hat{R}_z(\varphi) = \exp\left(-\frac{i\varphi}{\hbar}\hat{L}_z\right)

となる。そこで `\hat{L}_z` は `z` 軸のまわりの回転の生成子であるという。

実際には演算子の無限小形

.. math::
    \hat{R}_z(\delta) \approx 1 - \frac{i\delta}{\hbar}\hat{L}_z

を用いるのが便利である。そうすると位置演算子は

.. math::
    \begin{aligned}
        \hat{x}' &= \hat{R}_z^\dagger\hat{x}\hat{R}_z \approx \left(1 + \frac{i\delta}{\hbar}\hat{L}_z\right)\hat{x}\left(1 - \frac{i\delta}{\hbar}\hat{L}_z\right)
        \\
        &\approx \hat{x} + \frac{i\delta}{\hbar}\left[\hat{L}_z,\hat{x}\right] = \hat{x} - \delta\hat{y}
    \end{aligned}

と変換される。同様に，

.. math::
    \hat{y}' \approx \hat{y} + \delta\hat{x},\quad
    \hat{z}' = \hat{z}

と変換される。これらの結果は

.. math::
    \begin{pmatrix}
        \hat{x}' \\ \hat{y}' \\ \hat{z}'
    \end{pmatrix}
    \approx
    \begin{pmatrix}
        1 & -\delta & 0 \\
        \delta & 1 & 0 \\
        0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
        \hat{x} \\ \hat{y} \\ \hat{z}
    \end{pmatrix}

とまとめることができる。これは回転

.. math::
    \begin{pmatrix}
        x' \\ y' \\ z'
    \end{pmatrix}
    =
    \begin{pmatrix}
        \cos\varphi & -\sin\varphi & 0 \\
        \sin\varphi & \cos\varphi & 0 \\
        0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
        x \\ y \\ z
    \end{pmatrix}

において `\varphi \to \delta` の極限をとったものに一致する。

これまでの議論は，単位ベクトル `\bm{n}` に沿う軸のまわりの回転へ一般化できる：

.. math::
    \hat{R}_{\bm{n}}(\varphi) = \exp\left(-\frac{i\varphi}{\hbar}\bm{n}\cdot\hat{\bm{L}}\right)

回転の下で位置演算子と同じように変換される任意の演算子を **ベクトル演算子** と呼ぶ。「同じように変換される」とは，

.. math::
    \hat{\bm{V}}' = \bm{D}\hat{\bm{V}}

であり， `\bm{D}` が

.. math::
    \bm{r}' = \bm{D}\bm{r}

に現れるものと同じであるという意味である。特に `z` 軸のまわりの回転については，

.. math::
    \begin{pmatrix}
        \hat{V}_x' \\ \hat{V}_y' \\ \hat{V}_z'
    \end{pmatrix}
    =
    \begin{pmatrix}
        \cos\varphi & -\sin\varphi & 0 \\
        \sin\varphi & \cos\varphi & 0 \\
        0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
        \hat{V}_x \\ \hat{V}_y \\ \hat{V}_z
    \end{pmatrix}

となる。この変換則は交換関係

.. math::
    \boxed{[\hat{L}_i,\hat{V}_j] = i\hbar\epsilon_{ijk}\hat{V}_k}

から従う。あるいはこれをベクトル演算子の定義としてもよい。これまでに，そのような演算子として `\hat{\bm{r}}` と `\hat{\bm{p}}` と `\hat{\bm{L}}` に出会っている。

また， **スカラー演算子** とは回転によって変化しない演算子 `\hat{f}` のことである。これは，

.. math::
    \boxed{[\hat{\bm{L}},\hat{f}] = 0}

と同値である。これで演算子を `\hat{\bm{L}}` との交換関係に基づいてスカラーまたはベクトルに，また `\hat{\Pi}` との交換関係に基づいて真の量または擬の量に分類できる [#]_ 。

ポテンシャル `V(\bm{r})` 中を運動する質量 `m` の粒子について，ハミルトニアンは

.. math::
    \hat{H} = \frac{\hat{\bm{p}}^2}{2m} + V(\hat{\bm{r}})

である。ここで `V(\bm{r})=V(r)` ならば，これは回転不変である。この場合，ハミルトニアンは任意の軸のまわりの任意の角度の回転と可換である：

.. math::
    [\hat{H},\hat{R}_{\bm{n}}(\varphi)] = 0

特に，これは無限小回転

.. math::
    \hat{R}_{\bm{n}}(\delta) \approx 1 - \frac{i\delta}{\hbar}\bm{n}\cdot\hat{\bm{L}}

についても成り立たなければならないので，

.. math::
    [\hat{H},\hat{\bm{L}}] = 0

である。一般化された Ehrenfest の定理より，

.. math::
    \dv{}{t}\braket{\bm{L}} = \frac{i}{\hbar}\braket{[\hat{H},\hat{\bm{L}}]} = 0

となる。したがって，角運動量保存則は回転不変性の結果である。ここでも，角運動量保存則は，角運動量の各成分についての確率分布も時刻に依存しないことを意味する。

.. [#] すべての演算子がこれらの範疇に収まるわけではない。より一般にテンソル演算子と呼ばれるものが定義される。
