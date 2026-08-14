一般化された不確定性原理
=============================

以前に不確定性原理を `\sigma_{x}\sigma_{p}\geq \frac{\hbar}{2}` の形で紹介したが証明は述べなかった。ここでは不確定性原理をより一般的な形で証明し，そこから生じる結果について述べる。

.. important::
    任意の可観測量 `A,B` に対して，

    .. math::
        \sigma_A^2\sigma_B^2 \ge \left(\frac{1}{2i}\braket{[\hat{A},\hat{B}]}\right)^2

    が成り立つ。

.. admonition:: 証明 [hide/show]
    :collapsible: closed

    任意の可観測量 `A` について，

    .. math::
        \sigma_A^2 = \braket{(\hat{A}-\braket{A})\Psi|(\hat{A}-\braket{A})\Psi} = \braket{f|f}

    ここで，

    .. math::
        f \coloneqq (\hat{A}-\braket{A})\Psi

    と定義した。同様に，任意の可観測量 `B` について，

    .. math::
        \sigma_B^2 = \braket{g|g},\quad g \coloneqq (\hat{B}-\braket{B})\Psi

    である。Schwarz の不等式より，

    .. math::
        \sigma_A^2\sigma_B^2 = \braket{f|f}\braket{g|g} \ge |\braket{f|g}|^2

    となる。ここで任意の複素数 `z` に対して，

    .. math::
        |z|^2 = [\mathrm{Re}(z)]^2 + [\mathrm{Im}(z)]^2 \ge [\mathrm{Im}(z)]^2 = \left[\frac{1}{2i}(z-z^*)\right]^2

    となるので， `z=\braket{f|g}` とおくと，

    .. math::
        \sigma_A^2\sigma_B^2 \ge \left[\frac{1}{2i}(\braket{f|g}-\braket{g|f})\right]^2

    となる。しかし，

    .. math::
        \begin{aligned}
            \braket{f|g} &= \braket{(\hat{A}-\braket{A})\Psi|(\hat{B}-\braket{B})\Psi}
            \\
            &= \braket{\Psi|(\hat{A}-\braket{A})(\hat{B}-\braket{B})\Psi}
            \\
            &= \braket{\Psi|(\hat{A}\hat{B}-\hat{A}\braket{B}-\hat{B}\braket{A}+\braket{A}\braket{B})\Psi}
            \\
            &= \braket{\Psi|\hat{A}\hat{B}\Psi}-\braket{B}\braket{\Psi|\hat{A}\Psi}-\braket{A}\braket{\Psi|\hat{B}\Psi}+\braket{A}\braket{B}\braket{\Psi|\Psi}
            \\
            &= \braket{\hat{A}\hat{B}}-\braket{A}\braket{B}-\braket{A}\braket{B}+\braket{A}\braket{B}
            \\
            &= \braket{\hat{A}\hat{B}}-\braket{A}\braket{B}
        \end{aligned}

    であり，同様に，

    .. math::
        \braket{g|f} = \braket{\hat{B}\hat{A}}-\braket{B}\braket{A}

    であるから，

    .. math::
        \braket{f|g}-\braket{g|f} = \braket{\hat{A}\hat{B}}-\braket{\hat{B}\hat{A}} = \braket{[\hat{A},\hat{B}]}

    となる。ここで，

    .. math::
        [\hat{A},\hat{B}] \coloneqq \hat{A}\hat{B}-\hat{B}\hat{A}

    は2つの演算子の交換子である。以上より，

    .. math::
        \sigma_A^2\sigma_B^2 \ge \left(\frac{1}{2i}\braket{[\hat{A},\hat{B}]}\right)^2

    が成り立つ。

たとえば `A=x,B=p` とすると，

.. math::
    [\hat{x},\hat{p}] = i\hbar

より，

.. math::
    \sigma_x^2\sigma_p^2 \ge \left(\frac{1}{2i}i\hbar\right)^2 = \left(\frac{\hbar}{2}\right)^2

標準偏差は正なので，

.. math::
    \boxed{\sigma_x\sigma_p \ge \frac{\hbar}{2}}

となる。これはもとの Heisenberg の不確定性原理にほかならない。

これに限らず，演算子が交換しない可観測量のあらゆるペアに対して不確定性原理がある。そのような可観測量を両立しない可観測量と呼ぶことがある。これらは共通の固有関数を持たない。これに対して，両立する（交換する）可観測量は，同時固有関数（両方の可観測量について値が確定している状態）を持つ [#]_ 。例えば次章で扱う水素原子系では，ハミルトニアン，角運動量の大きさ，角運動量の `z` 成分は互いに両立する可観測量であり，それぞれの固有値によってラベル付けされた，3つすべての同時固有関数を構成する。

位置と運動量の不確定性の限界 `\sigma_x\sigma_p = \hbar/2` に達する波動関数には，実は2回出会っている。それは調和振動子型ポテンシャルの基底状態と，自由粒子の Gauss 波束である。実はもっとも一般的な最小不確定波束は Gaussian であることが証明できる（証明は不確定性原理の証明で不等号を等号に置き換えて，その必要十分条件を解けばよい）。

位置と運動量の不確定原理は，しばしば

.. math::
    \Delta x\Delta p \ge \frac{\hbar}{2}

という形で書かれる。そしてこの式はしばしばエネルギーと時間の不確定性原理

.. math::
    \Delta t\Delta E \ge \frac{\hbar}{2}

と一緒に語られる。特殊相対論の文脈では，これは位置と運動量の不確定性原理の帰結と思われるかもしれない。しかし，ここで扱っているのは非相対論的な量子力学である。最後に示したいのは，この関係が実際には位置と運動量の不確定性原理とはまったく別種の代物であり，その表面的な類似が誤解を招くということである。

そもそも，ここでは時刻そのものは力学変数ではない。時刻は独立変数であり，力学的な量はその関数である。特に，エネルギーと時間の不確定性原理における `\Delta t` は，時間を何度も測定して得られる値の標準偏差ではない。ざっくり言えば，これは以下で示すように系が大きく変化するのに要する時間である。

系がどれほど速く変化しているかの尺度として，ある可観測量 `Q(x,p,t)` の期待値の時間微分を計算する：

.. math::
    \dv{}{t}\braket{Q} = \dv{}{t}\braket{\Psi|\hat{Q}\Psi} = \braket{\dv{\Psi}{t}\middle|\hat{Q}\Psi} + \braket{\Psi\middle|\dv{\hat{Q}}{t}\Psi} + \braket{\Psi\middle|\hat{Q}\dv{\Psi}{t}}

時間に依存する Schrödinger 方程式

.. math::
    i\hbar\dv{\Psi}{t} = \hat{H}\Psi

より，

.. math::
    \dv{}{t}\braket{Q} = -\frac{1}{i\hbar}\braket{\hat{H}\Psi\middle|\hat{Q}\Psi} + \frac{1}{i\hbar}\braket{\Psi\middle|\hat{Q}\hat{H}\Psi} + \braket{\pdv{\Psi}{t}}

となる。ここで `\hat{H}` はエルミートなので，

.. math::
    \boxed{\dv{}{t}\braket{Q} = \frac{1}{\hbar}\braket{[\hat{H},\hat{Q}]} + \braket{\pdv{\Psi}{t}}}

となる。これはそれ自体，興味深い結果なので， **一般化された Ehrenfest の定理** と呼ぶことにする。演算子が時刻に陽に依存しない場合，期待値の変化率は，その演算子とハミルトニアンとの交換子によって決まる。特に `\hat{Q}` が `\hat{H}` と可換なら， `\braket{Q}` は一定であり，この意味で `Q` は保存量である。

さて，一般化された不確定性原理において `A=H,B=Q(x,p)` とすると，

.. math::
    \sigma_H^2\sigma_Q^2 \ge \left(\frac{1}{2i}\braket{[\hat{H},\hat{Q}]}\right)^2 = \left(\frac{1}{2i}\frac{\hbar}{i}\dv{\braket{Q}}{t}\right)^2 = \left(\frac{\hbar}{2}\right)^2\left(\dv{\braket{Q}}{t}\right)^2

すなわち，

.. math::
    \sigma_H\sigma_Q \ge \frac{\hbar}{2}\left|\dv{\braket{Q}}{t}\right|

となる。ここで， `\Delta E\coloneqq \sigma_H` と定義し，

.. math::
    \Delta t \coloneqq \frac{\sigma_Q}{|\dd\braket{Q}/\dd t|}

と定義すると，

.. math::
    \boxed{\Delta E\Delta t \ge \frac{\hbar}{2}}

となる。これがエネルギーと時間の不確定性原理である。ここで定義した `\Delta t` は，

.. math::
    \sigma_Q = \left|\dv{\braket{Q}}{t}\right|\Delta t

なので， `Q` の期待値が標準偏差ひとつ分変化するのに要する時間を表す [#]_ 。特に `\Delta t` はどの可観測量 `Q` に注目するかに依存する。しかし `\Delta E` が小さければ，すべての可観測量の変化率は非常に緩やかでなければならない。逆に，いずれかの可観測量が急速に変化するなら，エネルギーの「不確定さ」は大きくならなければならない。

.. [#] これは非可換な行列は同時対角化できないのに対し，可換なエルミート行列は同時対角化できるという事実に対応する。

.. [#] これはエネルギーと時間の不確定性原理の Mandelstam-Tamm の定式化と呼ばれることがある。
