一般化された確率解釈
==============================

第一章では，粒子がある特定の位置で見出される確率を計算する方法と，任意の可観測量の期待値を求める方法を示した。第二章では，エネルギー測定で得られ得る結果と，それらの確率を求める方法を示した。ここで，これらの結果をすべて含む一般化された確率解釈を示す。これは波動関数の連続的な時間発展を記述する Schrödinger 方程式とともに量子力学の基礎をなす。

.. important::
    状態 `\Psi(x,t)` にある粒子について可観測量 `Q(x,p)` を測定すると，エルミート演算子

    .. math::
        \hat{Q}\left(x,-i\hbar\dv{}{x}\right)

    の固有値のいずれかひとつが必ず得られる [#]_ 。 `\hat{Q}` のスペクトルが離散的なら，正規直交化された固有関数 `f_n(x)` に対応する特定の固有値 `q_n` が得られる確率は，

    .. math::
        |c_n|^2,\quad c_n = \braket{f_n|\Psi}

    である。スペクトルが連続的で，実固有値 `z` とそれに対応する Dirac 正規直交化された固有関数 `f_z(x)` を持つなら，範囲 `\dd z` 内の結果が得られる確率は，

    .. math::
        |c(z)|^2\dd z,\quad c(z) = \braket{f_z|\Psi}

    である。測定が行われると，波動関数は対応する固有状態へ「収縮（collapse）」する [#]_ 。

もちろん，すべての可能な結果について足し合わせた全確率は `1` でなければならない：

.. math::
    \sum_n |c_n|^2 = 1

これは確かに波動関数の規格化から従う：

.. math::
    \begin{aligned}
        1 &= \braket{\Psi|\Psi} = \braket{\left(\sum_{n'}c_{n'}f_{n'}\right) \middle| \left(\sum_n c_n f_n\right)}
        \\
        &= \sum_{n'}\sum_{n}c_{n'}^*c_n\braket{f_{n'}|f_n} = \sum_{n'}\sum_{n}c_{n'}^*c_n\delta_{n'n}
        \\
        &= \sum_n c_n^*c_n = \sum_n |c_n|^2
    \end{aligned}

同様に `Q` の期待値は，考えられるすべての結果について，固有値とその固有値が得られる確率との積を足し合わせたものでなければならない：

.. math::
    \braket{Q} = \sum_n q_n |c_n|^2

実際，

.. math::
    \begin{aligned}
        \braket{Q} &= \braket{\Psi|\hat{Q}\Psi}
        \\
        &= \braket{\left(\sum_{n'}c_{n'}f_{n'}\right) \middle| \hat{Q} \left(\sum_n c_n f_n\right)}
    \end{aligned}

で `\hat{Q}f_n = q_nf_n` であることから，

.. math::
    \begin{aligned}
        \braket{Q} &= \sum_{n'}\sum_{n}c_{n'}^*c_n q_n\braket{f_{n'}|f_n}
        \\
        &= \sum_{n'}\sum_{n}c_{n'}^*c_n q_n\delta_{n'n} = \sum_n q_n |c_n|^2
    \end{aligned}

となる。

ここでもともとの位置測定に対する確率解釈が再現されることを示そう。位置演算子 `\hat{x}` の固有値は任意の実数 `y` であり，対応する固有関数は `g_y(x) =\delta(x-y)` である。明らかに，

.. math::
    c(y) = \braket{g_y|\Psi} = \int_{-\infty}^{\infty}\delta(x-y)\Psi(x,t)\,\dd x = \Psi(y,t)

となる。したがって範囲 `\dd y` 内の結果が得られる確率は `|\Psi(y,t)|^2\,\dd y` であり，これはまさにもとの確率解釈である。

.. [#] `Q(x,p)` が `xp` のような積を含む場合，この扱い方には曖昧さがある。古典的には `x` と `p` は交換するので， `\hat{x}\hat{p}` と書くべきか `\hat{p}\hat{x}` と書くべきかは定かではない。幸いなことに，このような可観測量は稀だが，実際に現れるときには曖昧さを解消するために何か別の処方箋を用意しなければならない。

.. [#] 連続スペクトルの場合は，測定装置の精度に応じて，測定値のまわりの狭い範囲へ収縮する。
