Schrödinger 方程式
=========================

1次元の場合から3次元の場合への一般化は簡単である。時間に依存する Schrödinger 方程式は

.. math::
    i\hbar\pdv{\Psi}{t} = \hat{H}\Psi

ここでハミルトニアン演算子 `\hat{H}` は古典的なエネルギー

.. math::
    \frac{1}{2}mv^2 + V = \frac{1}{2m}(p_x^2+p_y^2+p_z^2) + V

から標準的な処方

.. math::
    p_x \to -i\hbar\pdv{}{x},\quad p_y \to -i\hbar\pdv{}{x},\quad p_z \to -i\hbar\pdv{}{z}

すなわち，

.. math::
    \boxed{\bm{p} \to -i\hbar\nabla}

によって得られる。したがって，

.. math::
    \boxed{i\hbar\pdv{\Psi}{t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi}

となる。ここで

.. math::
    \nabla^2 \coloneqq \pdv{^2}{x^2} + \pdv{^2}{y^2} + \pdv{^2}{z^2}

はラプラシアンである。ポテンシャル `V` と波動関数 `\Psi` は `\bm{r}=(x,y,z)` と `t` の関数である。無限小体積 `\dd^3 r = \dd x \dd y \dd z` の中に粒子を見出す確率は `|\Psi(\bm{r},t)|^2\,\dd^3 r` であり，規格化条件は

.. math::
    \int |\Psi|^2\,\dd^3 r = 1

となる。積分は全空間に渡る。 `V` が時刻に依存しないならば，定常状態

.. math::
    \Psi_n(\bm{r},t) = \psi_n(\bm{r})e^{-iE_nt/\hbar}

が存在し，波動関数 `\psi_n` は時間に依存しない Schrödinger 方程式

.. math::
    \boxed{-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi}

を満たす。時間に依存する Schrödinger 方程式の一般解は，

.. math::
    \Psi(\bm{r},t) = \sum_n c_n\psi_n(\bm{r})e^{-iE_nt/\hbar}

であり，係数 `c_n` は通常通り初期波動関数 `\Psi(\bm{r},0)` によって決まる。ポテンシャルが連続状態を許すならこれらの和は積分に置き換わる。

これから扱う系は中心力ポテンシャル，すなわち `V` が原点からの距離だけの関数である場合， `V(\bm{r}) \to V(r)` を扱う。この場合には，球座標 `(r,\theta,\phi)` を採用するのが自然である。球座標におけるラプラシアンは，

.. math::
    \nabla^2 = \frac{1}{r^2}\pdv{}{r}\left(r^2\pdv{}{r}\right) + \frac{1}{r^2\sin\theta}\pdv{}{\theta}\left(\sin\theta\pdv{}{\theta}\right) + \frac{1}{r^2\sin^2\theta}\pdv{^2}{\phi^2}

となる。したがって，球座標では時間に依存しない Schrödinger 方程式は，

.. math::
    -\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\pdv{}{r}\left(r^2\pdv{\psi}{r}\right) + \frac{1}{r^2\sin\theta}\pdv{}{\theta}\left(\sin\theta\pdv{\psi}{\theta}\right) + \frac{1}{r^2\sin^2\theta}\pdv{^2\psi}{\phi^2}\right] + V\psi = E\psi

と書ける。今回もまず分離された解

.. math::
    \psi(r,\theta,\phi) = R(r)Y(\theta,\phi)

を探す。これを時間に依存しない Schrödinger 方程式に代入すると，

.. math::
    -\frac{\hbar^2}{2m}\left[\frac{Y}{r^2}\dv{}{r}\left(r^2\dv{R}{r}\right) + \frac{R}{r^2\sin\theta}\pdv{}{\theta}\left(\sin\theta\pdv{Y}{\theta}\right) + \frac{R}{r^2\sin^2\theta}\pdv{^2Y}{\phi^2}\right] + VRY = ERY

となる。両辺を `YR` で割り， `-2mr^2/\hbar^2` を掛けると，

.. math::
    \left\{\frac{1}{R}\dv{}{r}\left(\dv{R}{r}\right)-\frac{2mr^2}{\hbar^2}[V(r)-E]\right\} + \frac{1}{Y}\left\{\frac{1}{\sin\theta}\pdv{}{\theta}\left(\sin\theta\pdv{Y}{\theta}\right)+\frac{1}{\sin^2\theta}\pdv{^2Y}{\phi^2}\right\} = 0

となる。第一項は `r` だけに依存し，残りは `\theta,\phi` だけに依存するから，それらはそれぞれが定数でなければならない。この定数を後の為に `l(l+1)` を書くことにすると，

.. math::
    \begin{aligned}
        \frac{1}{R}\dv{}{r}\left(r^2\dv{R}{r}\right) - \frac{2mr^2}{\hbar^2}[V(r)-E] &= l(l + 1)
        \\
        \frac{1}{Y}\left\{\frac{1}{\sin\theta}\left(\sin\theta\pdv{Y}{\theta}\right) + \frac{1}{\sin^2\theta}\pdv{^2Y}{\phi^2}\right\} &= -l(l + 1)
    \end{aligned}

となる。これらをそれぞれ動径方程式と角度方程式と呼ぶことにして解を求める。

角度方程式
-------------------

角度方程式に `Y\sin^2\theta` を掛けると，

.. math::
    \sin\theta\pdv{}{\theta}\left(\sin\theta\pdv{Y}{\theta}\right) + \pdv{^2Y}{\phi^2} = - l(l+1)\sin^2\theta Y

となる。これも分離された解

.. math::
    Y(\theta,\phi) = \Theta(\theta)\Phi(\phi)

を探す。これを代入して `\Theta\Phi` で割ると，

.. math::
    \left\{\frac{1}{\Theta}\left[\sin\theta\dv{}{\theta}\left(\sin\theta\dv{\Theta}{\theta}\right)\right] + l(l+1)\sin^2\theta\right\} + \frac{1}{\Phi}\dv{^2\Phi}{\phi^2} = 0

となる。第一項は `\theta` だけに依存し，第二項は `\phi` だけに依存するから，それぞれが定数でなければならない。この定数を後の為に `m^2` と書くことにすると，

.. math::
    \begin{aligned}
        \frac{1}{\Theta}\left[\sin\theta\dv{}{\theta}\left(\sin\theta\dv{\Theta}{\theta}\right)\right] + l(l+1)\sin^2\theta &= m^2
        \\
        \frac{1}{\Phi}\dv{^2\Phi}{\phi^2} &= -m^2
    \end{aligned}

となる。 `\Phi` の方程式は簡単である：

.. math::
    \dv{^2\Phi}{\phi^2} = -m^2\Phi \implies \Phi(\phi) = e^{im\phi}

実際には `e^{im\phi}` と `e^{-im\phi}` という2つの解があるが， `m` に負の値を許すことで後者も含める。また定数因子を付けることもできるが，それは `\Theta` の方に押し付けてしまってよい。さて， `\phi` が `2\pi` だけ進むと，空間内の同じ点へ戻るので，

.. math::
    \Phi(\phi+2\pi) = \Phi(\phi)

でなければならない。つまり， `e^{im(\phi+2\pi)}=e^{im\phi}` ，すなわち `e^{2\pi im} = 1` である。したがって， `m` は整数でなければならない：

.. math::
    m = 0,\pm 1,\pm 2,\dots

一方で， `\Theta` の方程式

.. math::
    :label: eq:theta

    \sin\theta\dv{}{\theta}\left(\sin\theta\dv{\Theta}{\theta}\right) + \left[l(l+1)\sin^2\theta - m^2\right]\Theta = 0

の解は

.. math::
    \Theta(\theta) = AP_l^m(\cos\theta)

となる。ここで `P_l^m` は Legendre 陪関数であり，

.. math::
    P_l^m(x) \coloneqq (-1)^m(1-x^2)^{m/2}\left(\dv{}{x}\right)^m P_l(x)

で定義される。また， `P_l` は Legendre 多項式であり，Rodrigues の公式

.. math::
    P_l(x) \coloneqq \frac{1}{2^l l!}\left(\dv{}{x}\right)^l(x^2-1)^l

で定義される。たとえば，

.. math::
    \begin{aligned}
        P_0(x) &= 1
        \\
        P_1(x) &= x
        \\
        P_2(x) &= \frac{1}{2}(3x^2-1)
        \\
        P_3(x) &= \frac{1}{2}(5x^3-3x)
    \end{aligned}

などとなる。その名の通り `P_l(x)` は `x` の `l` 次多項式であり， `l` の偶奇に応じて偶関数か奇関数である。しかし一般に `P_l^m(x)` は多項式ではない [#]_ 。たとえば，

.. math::
    \begin{aligned}
        P_2^0(x) &= \frac{1}{2}(3x^2-1)
        \\
        P_2^1(x) &= -3x\sqrt{1-x^2}
        \\
        P_2^2(x) &= 3(1-x^2)
    \end{aligned}

などとなる。我々が必要とするのは `P_l^m(\cos\theta)` であり， `\sqrt{1-\cos^2\theta} = \sin\theta` であるから， `P_l^m(\cos\theta)` は `\cos\theta` か `\sin\theta` の多項式である。

Rodrigues の公式が意味を持つためには `l` が非負整数でなければならない。さらに， `m>l` なら `P_l^m=0` である。したがって，指定された `l` に対して， `m` には `2l+1` 個の値が許される：

.. math::
    l = 0,1,2,\ldots ; \quad m=-l,-l+1,\ldots,-1,0,1,\ldots,l-1,l

しかし，方程式 :eq:`eq:theta` は二階微分方程式であるから，どんな `l,m` の値に対しても線形独立な解を2つ持つはずである。ほかの解はどうなったか。もちろん数学的にはもうひとつ解が存在する。しかし，それは `\theta=0` か `\theta=\pi` で発散するため物理的には許されない。

さて，球座標における体積要素は

.. math::
    \dd^3 r = r^2\sin\theta\,\dd r\dd\theta\dd\phi = r^2\,\dd r\dd\Omega,\quad \dd\Omega \coloneqq \sin\theta\,\dd\theta\dd\phi

なので，規格化条件は

.. math::
    \int |\psi|^2r^2\sin\theta\,\dd r\dd\theta\dd\phi = \int |R|^2r^2\,\dd r \int |Y|^2\,\dd\Omega = 1

となる。そこで `R` と `Y` を別々に規格化すると便利である：

.. math::
    \int_0^\infty |R|^2r^2\,\dd r = 1,\quad \int_0^\pi \int_0^{2\pi} |Y|^2\sin\theta\,\dd\theta\dd\phi = 1

規格化された角度波動関数は球面調和関数と呼ばれる：

.. math::
    Y_l^m(\theta,\phi) = \sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}}e^{im\phi}P_l^m(\cos\theta)

これらは正規直交化されている：

.. math::
    \int_0^\pi\int_0^{2\pi} [Y_l^m(\theta,\phi)]^*[Y_{l'}^{m'}(\theta,\phi)]\sin\theta\,\dd\theta\dd\phi = \delta_{ll'}\delta_{mm'}

たとえば，

.. math::
    \begin{aligned}
        Y_0^0 &= \left(\frac{1}{4\pi}\right)^{1/2}
        \\
        Y_1^0 &= \left(\frac{3}{4\pi}\right)^{1/2}\cos\theta
        \\
        Y_1^{\pm 1} &= \mp\left(\frac{3}{8\pi}\right)^{1/2}\sin\theta e^{\pm i\phi}
        \\
        Y_2^0 &= \left(\frac{5}{16\pi}\right)^{1/2}(3\cos^2\theta-1)
        \\
        Y_2^{\pm 1} &= \mp\left(\frac{15}{8\pi}\right)^{1/2}\sin\theta\cos\theta e^{\pm i\phi}
        \\
        Y_2^{\pm 2} &= \left(\frac{15}{32\pi}\right)^{1/2}\sin^2\theta e^{\pm 2i\phi}
    \end{aligned}

などとなる。

動径方程式
-------------------

波動関数の角度部分 `Y(\theta,\phi)` はすべての球対称ポテンシャルについて同じである。ポテンシャルの形 `V(r)` は波動関数の動径部分 `R(r)` にのみ影響し，それは動径方程式

.. math::
    \dv{}{r}\left(r^2\dv{R}{r}\right) - \frac{2mr^2}{\hbar^2}[V(r)-E]R = l(l+1)R

によって決まる。より簡単な形に書き直すために

.. math::
    u(r) \coloneqq rR(r)

と置く。そうすると，

.. math::
    R = \frac{u}{r},\quad \dv{R}{r} = \frac{r(\dd u/\dd r)-u}{r^2},\quad \dv{}{r}\left(r^2\dv{R}{r}\right) = r\dv{^2u}{r^2}

となるので，動径方程式は

.. math::
    \boxed{-\frac{\hbar^2}{2m}\dv{^2u}{r^2} + \left[V+\frac{\hbar^2}{2m}\frac{l(l+1)}{r^2}\right]u = Eu}

となる。これは1次元 Schrödinger 方程式と形が同じだが，有効ポテンシャル

.. math::
    V_\text{eff}(r) = V + \frac{\hbar^2}{2m}\frac{l(l+1)}{r^2}

が遠心力項と呼ばれる余分な部分 `(\hbar^2/2m)[l(l+1)/r^2]` を持つ点が異なる。これは古典力学の遠心力とまったく同じように，粒子を外向きへ投げ出そうとする。また，規格化条件は

.. math::
    \int_0^\infty |u|^2\,\dd r = 1

となる。特定のポテンシャル `V(r)` が与えられるまでは，これ以上先へは進めない。

.. [#] 紛らわしいことに一部の文献では `P_l^m` は Legendre 陪多項式と呼ばれることがある。
