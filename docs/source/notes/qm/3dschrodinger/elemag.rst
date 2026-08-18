電磁相互作用
==================

古典電磁気学では，電場 `\bm{E}` と磁場 `\bm{B}` の中を速度 `\bm{v}` で運動する電荷 `q` の粒子に作用する力は Lorentz 力

.. math::
    \bm{F} = q(\bm{E} + \bm{v} \times \bm{B})

によって与えらえる。この力はポテンシャルエネルギーの勾配として表せないが，ハミルトニアンは

.. math::
    H = \frac{1}{2m}(\bm{p} - q\bm{A})^2 + q\varphi

と書ける。ここで `\bm{A}` はベクトルポテンシャル， `\varphi` はスカラーポテンシャルである：

.. math::
    \bm{E} = -\nabla\varphi - \pdv{\bm{A}}{t}, \quad \bm{B} = \nabla \times \bm{A}

標準的な置き換え `\bm{p} \to -i\hbar\nabla` を行うと，時間に依存する Schrödinger 方程式は

.. math::
    i\hbar\pdv{\Psi}{t} = \left[\frac{1}{2m}(-i\hbar\nabla - q\bm{A})^2 + q\varphi\right]\Psi

となる。

古典電磁気学では，ポテンシャル `\bm{A}` と `\varphi` は一意に決まらないことに注意する。物理的な量は電磁場 `\bm{E},\bm{B}` であり，任意の関数 `\Lambda(\bm{x},t)` に対してゲージ変換

.. math::
    \bm{A}' = \bm{A} + \nabla\Lambda, \quad \varphi' = \varphi - \pdv{\Lambda}{t}

は `\bm{A}` と `\varphi` と同じ電磁場を与える。

量子力学ではどうか。容易に示せるように

.. math::
    \Psi' \coloneqq e^{iq\Lambda/\hbar}\Psi

はゲージ変換されたポテンシャル `\bm{A}'` と `\varphi'` に対する時間に依存する Schrödinger 方程式の解である。 `\Psi'` と `\Psi` は位相因子しか違わないので，同じ物理状態を表し，その意味では理論はゲージ不変である。長い間，古典論と同じく，電磁場がゼロの領域には電磁気的な影響はないと考えられていた。しかし，1959年に Aharonov と Bohm は，粒子が電磁場そのものはゼロである領域に閉じ込めている場合でさえ，ベクトルポテンシャルが荷電粒子の量子的振る舞いに影響を与えることを示した。

一般に，粒子が `\bm{B}=0` だが `\bm{A}` そのものはゼロでない領域を運動しているとする。時間に依存する Schrödinger 方程式は

.. math::
    \Psi = e^{ig}\Psi',\quad g(\bm{r}) \coloneqq \frac{q}{\hbar}\int_{\mathcal{O}}^{\bm{r}}\bm{A}(\bm{r}')\cdot \dd\bm{r}'

と書くことで簡単にできる。ここで `\mathcal{O}` は任意の基準点である。この定義は考えている領域で `\bm{B} = \nabla \times \bm{A} = 0` のときだけ意味を持つことに注意する [#]_ 。もしそうでなければ線積分は経路に依存し `\bm{r}` の関数として定義されない。実際，

.. math::
    \nabla\Psi = e^{ig}(i\nabla g)\Psi' + e^{ig}\nabla\Psi'

で， `\nabla g=(q/\hbar)\bm{A}` なので，

.. math::
    (-i\hbar\nabla-q\bm{A})\Psi = -i\hbar e^{ig}\nabla\Psi'

となり，

.. math::
    (-i\hbar\nabla-q\bm{A})^2\Psi = -\hbar^2 e^{ig}\nabla^2\Psi'

となる。したがって，時間に依存する Schrödinger 方程式は

.. math::
    -\frac{\hbar^2}{2m}\nabla^2\Psi' = i\hbar\pdv{\Psi'}{t}

となる。これは通常の時間に依存する Schrödinger 方程式である。これが解けるなら，回転がゼロのベクトルポテンシャルの存在に対する補正は依存因子 `e^{ig}` を付け加えるだけである。

Aharonov と Bohm は，電子ビームを2つに分けて，再び合流させる前に長いソレノイドの両側を通す実験を提案した。ビームはソレノイドそのものから十分遠く話しておくので `\bm{B}=0` の領域しか通らない。しかし `\bm{A}` はゼロではなく，2つのビームは異なる位相因子を持つ：

.. math::
    g = \frac{q}{\hbar}\int\bm{A}\cdot\dd\bm{r} = \frac{q\Phi}{2\pi\hbar}\int\left(\frac{1}{r}\bm{e}_\phi\right)\cdot\left(r\bm{e}_\phi\,\dd\phi\right) = \pm\frac{q\Phi}{2\hbar}

ここで `\Phi` はソレノイドの中を通る磁束であり，符号は `\bm{A}` と同じ方向，すなわちソレノイドの電流と同じ方向へ進む電子に対して正である。これらの2つの電子ビームは，その経路が囲む磁束 `\Phi` に比例する量だけ位相がずれる：

.. math::
    \text{phase difference} = \frac{q\Phi}{\hbar}

この位相のずれは測定可能な干渉を生み，Chambers らによって実験的に確認された。したがって，電磁場がゼロの領域でも電磁気的な影響は存在しうる。ただい `\bm{A}` そのものが測定可能になるわけではない。最終的な結果に残るのは囲まれた磁束だけであり，理論はゲージ不変のままである。

.. [#] さらに，考えている領域は単連結でもなければならない。よくある状況としてソレノイドを領域に置くことがあるが，この場合はソレノイドそのものを除外しなければならない。これを回避するには，ソレノイドの両側を別々の単連結領域として扱えばよい。Aharonov と Bohm はその点も抜かりなく確認していたそうだ。
