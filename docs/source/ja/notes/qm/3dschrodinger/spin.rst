スピン
==============

古典力学では剛体は2種類の角運動量を持つ。すなわち，重心の運動に伴う軌道角運動量と，重心のまわりの運動に伴うスピン角運動量である。古典的な文脈では，この区別は便宜上の問題である。結局，スピン角運動量は剛体を形作る質点が重心まわりを回るときの軌道角運動量の和にほかならない。

しかし量子力学では，この区別が絶対的に基本的なものとなる。水素原子の場合，電子が原子核のまわりを運動することに伴う軌道角運動量に加えて，電子にはもうひとつの形の角運動量を持つ。それは空間内の運動とは何の関係もないが，どことなく古典的なスピンに似ているものである。電子は知る限り内部構造を持たない素粒子であり，そのスピン角運動量を構成要素の軌道角運動量に分解することはできない。

スピンの代数的な理論は交換関係

.. math::
    [S_x,S_y] = i\hbar S_z,\quad [S_y,S_z] = i\hbar S_x,\quad [S_z,S_x] = i\hbar S_y

から始まる。 `S^2` と `S_z` の固有ベクトルは

.. math::
    S^2\ket{sm} = \hbar^2 s(s+1)\ket{sm},\quad S_z\ket{sm} = \hbar m\ket{sm}

および，

.. math::
    S_{\pm}\ket{sm} = \hbar\sqrt{s(s+1)-m(m\pm 1)}\ket{s,m\pm 1}

を満たす。ここで `S_\pm \coloneqq S_x\pm iS_y` である。しかし今回は固有ベクトルは球面調和関数でなく（そもそも関数ではない） `s,m` の半整数値を除外する理由はない：

.. math::
    s = 0,\frac{1}{2},1,\frac{3}{2},\dots;\quad m = -s,-s+1,\dots,s-1,s

あらゆる素粒子はたまたま特定の不変な `s` の値を持っており，これをその粒子種の **スピン** と呼ぶ。例えば， `\pi` 中間子のスピンは `0` ，電子のスピンは `1/2` ，光子のスピンは `1` [#]_ ， `\Delta` バリオンのスピンは `3/2` である。

特に重要なのは `s=1/2` の場合である。これは通常の物質を構成する粒子のスピンであり，またすべてのクォークとすべてのレプトンのスピンでもある。さらにスピン `1/2` を理解すれば，それより大きい任意のスピンに対する形式論を導くのは簡単である。

この場合，固有状態は2つだけである： `\ket{\frac{1}{2},\frac{1}{2}}` はスピン上向き（ `\ket{\uparrow}` と略記）， `\ket{\frac{1}{2},-\frac{1}{2}}` はスピン下向き（ `\ket{\downarrow}` と略記）である。これらを基底ベクトルに用いると，スピン `1/2` 粒子の一般的な状態は [#]_ ，2成分の列ベクトルで表せる：

.. math::
    \chi = \begin{pmatrix} a \\ b \end{pmatrix} = a\chi_+ + b\chi_-

ここで

.. math::
    \chi_+ = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\quad \chi_- = \begin{pmatrix} 0 \\ 1 \end{pmatrix}

はスピン上向きと下向きの状態を表す。

この基底に関してスピン演算子は `2\times 2` 行列となり，その `\chi_+` と `\chi_-` への作用に注目すれば行列要素を求められる：

.. math::
    S^2\chi_+ = \frac{3}{4}\hbar^2\chi_+,\quad S^2\chi_- = \frac{3}{4}\hbar^2\chi_-

ここで `S^2` を行列

.. math::
    S^2 = \begin{pmatrix} c & d \\ e & f \end{pmatrix}

と置くと，第一式は

.. math::
    \begin{pmatrix} c & d \\ e & f \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{3}{4}\hbar^2\begin{pmatrix} 1 \\ 0 \end{pmatrix} \implies \begin{pmatrix} c \\ e \end{pmatrix} = \begin{pmatrix} 3/4\hbar^2 \\ 0 \end{pmatrix}

第二式は

.. math::
    \begin{pmatrix} c & d \\ e & f \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{3}{4}\hbar^2\begin{pmatrix} 0 \\ 1 \end{pmatrix} \implies \begin{pmatrix} d \\ f \end{pmatrix} = \begin{pmatrix} 0 \\ 3/4\hbar^2 \end{pmatrix}

したがって，

.. math::
    S^2 = \frac{3}{4}\hbar^2\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}

となる。同様に

.. math::
    S_z\chi_+ = \frac{\hbar}{2}\chi_+,\quad S_z\chi_- = -\frac{\hbar}{2}\chi_-

から

.. math::
    S_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}

となる。また，

.. math::
    S_+\chi_- = \hbar\chi_+,\quad S_-\chi_+ = \hbar\chi_-,\quad S_+\chi_+ = 0,\quad S_-\chi_- = 0

から

.. math::
    S_+ = \hbar\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix},\quad S_- = \hbar\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}

となる。さて， `S_{\pm} = S_x\pm iS_y` であるから， `S_x = (1/2)(S_+ + S_-)` および `S_y = (1/2i)(S_+ - S_-)` であり，したがって，

.. math::
    S_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\quad S_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}

となる。 `S_x,S_y,S_z` はすべて因子 `\hbar/2` を含むので， `\bm{S}=(\hbar/2)\bm{\sigma}` と書くとすっきりする。ここで

.. math::
    \boxed{\sigma_x \coloneqq \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\quad \sigma_y \coloneqq \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\quad \sigma_z \coloneqq \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}}

は Pauli 行列と呼ばれる。 `S_x,S_y,S_z,S^2` はすべてエルミート行列だが， `S_+,S_-` はエルミートではない。 

`S_z` の固有ベクトルは固有値 `\pm \hbar/2` に対応する `\chi_\pm` である。一般的な状態 `\chi` にある粒子について `S_z` を測定すると，確率 `|a|^2` で `+\hbar/2` ，確率 `|b|^2` で `-\hbar/2` の値が得られる。この2つの可能性しかないので，

.. math::
    |a|^2 + |b|^2 = 1

である。すなわち `\chi^\dagger\chi = 1` でなければならない。

ここで `S_x` を測定するとどうなるだろう。一般化された確率解釈によれば， `S_x` の固有値と固有ベクトルを知る必要がある。その特性方程式は

.. math::
    \mathrm{det}\begin{pmatrix} -\lambda & \hbar/2 \\ \hbar/2 & -\lambda \end{pmatrix} = 0 \implies \lambda^2 = \left(\frac{\hbar^2}{2}\right)^2 \implies \lambda = \pm \frac{\hbar}{2}

となる。 `S_x` の可能な値は `S_z` と同じである。固有ベクトルは

.. math::
    \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \pm\frac{\hbar}{2}\begin{pmatrix} \alpha \\ \beta \end{pmatrix} \implies \begin{pmatrix} \beta \\ \alpha \end{pmatrix} = \pm\begin{pmatrix} \alpha \\ \beta \end{pmatrix}

よって `S_x` の規格化された固有ベクトルは

.. math::
    \chi_+^{(x)} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix},\quad \chi_-^{(x)} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}

でそれぞれ固有値 `+\hbar/2` と `-\hbar/2` に対応する。一般的な状態 `\chi` はこれらの線形結合として

.. math::
    \chi = \left(\frac{a+b}{\sqrt{2}}\right)\chi_+^{(x)} + \left(\frac{a-b}{\sqrt{2}}\right)\chi_-^{(x)}

と書ける。したがって， `S_x` を測定すると，確率 `|(a+b)/\sqrt{2}|^2` で `+\hbar/2` ，確率 `|(a-b)/\sqrt{2}|^2` で `-\hbar/2` の値が得られる。

より非自明な問題として，2粒子系のスピン状態について考えよう。第一の粒子は状態 `\ket{s_1m_1}` ，第二の粒子は状態 `\ket{s_2m_2}` にあるとする。合成状態を `\ket{s_1s_2m_1m_2}` と表す：

.. math::
    \begin{aligned}
        (S^{(1)})^2\ket{s_1s_2m_1m_2} &= s_1(s_1+1)\hbar^2\ket{s_1s_2m_1m_2}
        \\
        (S^{(2)})^2\ket{s_1s_2m_1m_2} &= s_2(s_2+1)\hbar^2\ket{s_1s_2m_1m_2}
        \\
        S_z^{(1)}\ket{s_1s_2m_1m2} &= m_1\hbar\ket{s_1s_2m_1m_2}
        \\
        S_z^{(2)}\ket{s_1s_2m_1m2} &= m_2\hbar\ket{s_1s_2m_1m_2}
    \end{aligned}

この系の全角運動量の `z` 成分は

.. math::
    \begin{aligned}
        S_z\ket{s_1s_2m_1m_2} &= (S_z^{(1)} + S_z^{(2)})\ket{s_1s_2m_1m_2}
        \\
        &= (m_1 + m_2)\hbar\ket{s_1s_2m_1m_2}
    \end{aligned}

したがって，

.. math::
    m = m_1 + m_2

という単純な和になる。しかしスピン `s` の値ははるかに微妙である。そこで最も単純な例として，2つのスピン `1/2` 粒子の合成状態を考えよう。第一の粒子は状態 `\ket{\up}` または `\ket{\down}` にあり，第二の粒子も同様である。したがって，この系の状態は全部で4つの可能性がある：

.. math::
    \begin{aligned}
        \ket{\up\up} &\coloneqq \ket{\frac{1}{2}\frac{1}{2}\frac{1}{2}\frac{1}{2}} \quad (m=1)
        \\
        \ket{\up\down} &\coloneqq \ket{\frac{1}{2}\frac{1}{2}\frac{1}{2}\left(-\frac{1}{2}\right)} \quad (m=0)
        \\
        \ket{\down\up} &\coloneqq \ket{\frac{1}{2}\frac{1}{2}\left(-\frac{1}{2}\right)\frac{1}{2}} \quad (m=0)
        \\
        \ket{\down\down} &\coloneqq \ket{\frac{1}{2}\frac{1}{2}\left(-\frac{1}{2}\right)\left(-\frac{1}{2}\right)} \quad (m=-1)
    \end{aligned}

これは一見すると `s=1` のように見えるが， `m=0` の余分な状態がひとつある。この問題を理解する一つの方法は，状態 `\ket{\up\up}` に下降演算子 `S_- = S_-^{(1)} + S_-^{(2)}` を作用させることである：

.. math::
    \begin{aligned}
        S_-\ket{\up\up} &= (S_-^{(1)}\ket{\up})\ket{\up} + \ket{\up}(S_-^{(2)}\ket{\up})
        \\
        &= (\hbar\ket{\down})\ket{\up} + \ket{\up}(\hbar\ket{\down}) = \hbar(\ket{\down\up} + \ket{\up\down})
    \end{aligned}

さらに，

.. math::
    S_-(\ket{\down\up} + \ket{\up\down}) = \hbar(\ket{\down\down} + \ket{\down\down}) = 2\hbar\ket{\down\down}

よって `s=1` の3つの状態は

.. math::
    \boxed{
        \begin{aligned}
            \ket{11} &= \ket{\up\up}
            \\
            \ket{10} &= \frac{1}{\sqrt{2}}(\ket{\up\down} + \ket{\down\up})
            \\
            \ket{1-1} &= \ket{\down\down}
        \end{aligned}
    }

となる。これは三重項状態と呼ばれる。一方で `m=0` をもつ直交状態

.. math::
    \boxed{\ket{00} = \frac{1}{\sqrt{2}}(\ket{\up\down} - \ket{\down\up})}

は `s=0` の1つの状態であり，一重項状態と呼ばれる。実際に昇降演算子を作用させるとゼロになる。

したがって，2つのスピン `1/2` 粒子の合成状態は，三重項状態か一重項状態かに応じてスピン `1` か `0` を持つことが期待される。これを確認するには，三重項状態が固有値 `1(1+1)\hbar^2 = 2\hbar^2` を持つ `S^2` の固有状態で，一重項状態が固有値 `0(0+1)\hbar^2 = 0` を持つ `S^2` の固有状態であることを確認すればよい。まず，

.. math::
    S^2 = (\bm{S}^{(1)} + \bm{S}^{(2)})^2 = (S^{(1)})^2 + (S^{(2)})^2 + 2\bm{S}^{(1)}\cdot\bm{S}^{(2)}

で，例えば，

.. math::
    \begin{aligned}
        \bm{S}^{(1)}\cdot\bm{S}^{(2)}\ket{\up\down} &= (S_x^{(1)}\ket{\up})(S_x^{(2)}\ket{\down}) + (S_y^{(1)}\ket{\up})(S_y^{(2)}\ket{\down}) + (S_z^{(1)}\ket{\up})(S_z^{(2)}\ket{\down})
        \\
        &= \left(\frac{\hbar}{2}\ket{\down}\right)\left(\frac{\hbar}{2}\ket{\up}\right) + \left(\frac{i\hbar}{2}\ket{\down}\right)\left(-\frac{i\hbar}{2}\ket{\up}\right) + \left(\frac{\hbar}{2}\ket{\up}\right)\left(-\frac{\hbar}{2}\ket{\down}\right)
        \\
        &= \frac{\hbar^2}{4}(2\ket{\down\up} - \ket{\up\down})
        \\
        \bm{S}^{(1)}\cdot\bm{S}^{(2)}\ket{\down\up} &= \frac{\hbar^2}{4}(2\ket{\up\down} - \ket{\down\up})
    \end{aligned}

となるので，

.. math::
    \begin{aligned}
        \bm{S}^{(1)}\cdot\bm{S}^{(2)}\ket{10} &= \frac{\hbar^2}{4}\ket{10}
        \\
        \bm{S}^{(1)}\cdot\bm{S}^{(2)}\ket{00} &= -\frac{3\hbar^2}{4}\ket{00}
    \end{aligned}

となり，

.. math::
    \begin{aligned}
        S^2\ket{10} &= \left(\frac{3\hbar^2}{4} + \frac{3\hbar^2}{4} + 2\frac{\hbar^2}{4}\right)= 2\hbar^2\ket{10}
        \\
        S^2\ket{00} &= \left(\frac{3\hbar^2}{4} + \frac{3\hbar^2}{4} - 2\frac{3\hbar^2}{4}\right)= 0
    \end{aligned}

となる。したがって， `\ket{10}` は固有値 `2\hbar^2` を持つ `S^2` の固有状態であり， `\ket{00}` は固有値 `0` を持つ `S^2` の固有状態であることが確認できた。同様に `\ket{11}` と `\ket{1-1}` も固有値 `2\hbar^2` を持つ `S^2` の固有状態であることが確認できる。

いま行ったことは，より大きいスピンを持つ場合でも同様に行える。一般にスピン `s_1` とスピン `s_2` を合成すると，可能なスピンの値は

.. math::
    \boxed{s = (s_1+s_2),(s_1+s_2-1),\dots,|s_1-s_2|}

となる。全スピン `s` ， `z` 成分 `m` を持つ合成状態 `\ket{sm}` は，合成状態 `\ket{s_1s_2m_1m_2}` のある線形結合となる：

.. math::
    \ket{sm} = \sum_{m_1+m_2=m}C_{m_1m_2m}^{s_1s_2s}\ket{s_1s_2m_1m_2}

`z` 成分は単純に足されるので，寄与する合成状態は `m_1+m_2=m` を満たすものだけである。係数 `C_{m_1m_2m}^{s_1s_2s}` は **Clebsch-Gordan 係数** と呼ばれる。例えば，

.. math::
    \ket{30} = \frac{1}{\sqrt{5}}\ket{21}\ket{1(-1)} + \sqrt{\frac{3}{5}}\ket{20}\ket{10} + \frac{1}{\sqrt{5}}\ket{2(-1)}\ket{11}

となる。逆に

.. math::
    \ket{s_1s_2m_1m_2} = \sum_{s}C_{m_1m_2m}^{s_1s_2s}\ket{sm} \quad (m=m_1+m_2)

のようにも書ける。例えば，

.. math::
    \ket{\frac{3}{2}1\frac{1}{2}0} = \sqrt{\frac{3}{5}}\ket{\frac{5}{2}\frac{1}{2}} + \sqrt{\frac{1}{15}}\ket{\frac{3}{2}\frac{1}{2}} - \sqrt{\frac{1}{3}}\ket{\frac{1}{2}\frac{1}{2}}

となる。これらは数学的には回転群の2つの既約表現のテンソル積表現を既約表現へ直和分解することに対応する。計算の方法については群論の教科書を参照されたい。

.. [#] 光子のような質量のない粒子は正確にはスピンではなくヘリシティである。特に `m=0` の状態は存在しない。

.. [#] ここではひとまずスピン状態だけを考える。粒子が運動しているなら位置状態 `\Psi` も扱う必要がある。
