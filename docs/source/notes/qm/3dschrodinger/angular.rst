角運動量
===============

古典的には，粒子の角運動量は

.. math::
    \bm{L} = \bm{r} \times \bm{p}

という公式で与えられる。すなわち，

.. math::
    L_x = yp_z - zp_y,\quad L_y = zp_x - xp_z,\quad L_z = xp_y - yp_x

対応する量子力学的な演算子は，標準的な処方

.. math::
    p_x \to -i\hbar\pdv{}{x},\quad p_y \to -i\hbar\pdv{}{y},\quad p_z \to -i\hbar\pdv{}{z}

で得られる [#]_ 。ここでは純粋に代数的な方法によって角運動量演算子の固有値を求める。これは交換関係を巧妙に利用することに基づいている。その後で固有関数を求める。

演算子 `L_x` と `L_y` は可換ではない。実際，

.. math::
    \begin{aligned}
        [L_x,L_y] &= [yp_z - zp_y, zp_x - xp_z]
        \\
        &= [yp_z, zp_x] - [yp_z, xp_z] - [zp_y, zp_x] + [zp_y, xp_z]
    \end{aligned}

となる。正準交換関係から，ここに現れる演算子のうち可換でないのは， `x` と `p_x` ， `y` と `p_y` ， `z` と `p_z` だけだと分かる。したがって，中央の2つの項は消え，

.. math::
    [L_x,L_y] = yp_x[p_z,z] + xp_y[z,p_z] = i\hbar(xp_y-yp_x) = i\hbar L_z

となる。もちろん， `[L_y,L_z]` または `[L_z,L_x]` から出発してもできたが，これらを別々に計算する必要はない。添え字を `x\to y,y\to z,z\to x` と巡回置換すれば，

.. math::
    \boxed{[L_x,L_y] = i\hbar L_z,\quad [L_y,L_z] = i\hbar L_x,\quad [L_z,L_x] = i\hbar L_y}

を得る。これらが角運動量の基本交換関係であり，すべてはここから導かれる。

`L_x,L_y,L_z` は両立しない可観測量であることに注意する。一般化された不確定性原理によれば，

.. math::
    \sigma_{L_x}^2\sigma_{L_y}^2 \ge \left(\frac{1}{2i}\braket{i\hbar L_z}\right)^2 = \frac{\hbar^2}{4}\braket{L_z}^2

すなわち，

.. math::
    \sigma_{L_x}\sigma_{L_y} \ge \frac{\hbar}{2}|\braket{L_z}|

したがって，これらの同時固有関数を探しても無駄である。しかし，全角運動量の二乗

.. math::
    L^2 = L_x^2 + L_y^2 + L_z^2

は `L_x` と可換である：

.. math::
    \begin{aligned}
        [L^2,L_x] &= [L_x^2,L_x] + [L_y^2,L_x] + [L_z^2,L_x]
        \\
        &= L_y[L_y,L_x] + [L_y,L_x]L_y + L_z[L_z,L_x] + [L_z,L_x]L_z
        \\
        &= L_y(-i\hbar L_z) + (-i\hbar L_z)L_y + L_z(i\hbar L_y) + (i\hbar L_y)L_z
        \\
        &= 0
    \end{aligned}

同様に `L^2` は `L_y,L_z` とも可換であり，簡潔に

.. math::
    [L^2,\bm{L}] = 0

である。したがって， `L^2` と例えば `L_z` の同時固有状態

.. math::
    L^2f = \lambda f,\quad L_zf = \mu f

を見出せる。

ここで調和振動子型ポテンシャルの場合に定義したものとよく似た昇降演算子を導入する：

.. math::
    L_\pm \coloneqq L_x \pm iL_y

これと `L_z` との交換子は

.. math::
    [L_z,L_{\pm}] = [L_z,L_x] \pm i[L_z,L_y] = i\hbar L_y \pm i(-i\hbar L_x) = \pm\hbar(L_x \pm iL_y)

なので，

.. math::
    [L_z,L_{\pm}] = \pm\hbar L_{\pm}

また，

.. math::
    [L^2,L_{\pm}] = 0

となる。よって，

.. math::
    L^2(L_{\pm}f) = L_{\pm}(L^2f) = L_{\pm}(\lambda f) = \lambda(L_{\pm}f)

となるので， `L_{\pm}f` は同じ固有値 `\lambda` を持つ `L^2` の固有関数である。また，

.. math::
    \begin{aligned}
        L_z(L_{\pm}f) &= (L_zL_{\pm}-L_{\pm}L_z)f + L_{\pm}L_zf
        \\
        &= \pm\hbar L_{\pm}f + L_{\pm}(\mu f) = (\mu \pm \hbar)(L_{\pm}f)
    \end{aligned}

となるので， `L_{\pm}f` は新しい固有値 `\mu\pm\hbar` を持つ `L_z` の固有関数である。 `L_+` は `L_z` の固有値を `\hbar` だけ増加させる上昇演算子， `L_-` は `L_z` の固有値を `\hbar` だけ減少させる下降演算子と呼ぶ。

したがって， `\lambda` の値をひとつ固定すると，状態のはしごが得られ，各段には `L_z` の固有値において隣の段から `\hbar` ずつ隔たっている。はしごを上るには上昇演算子を，下るには下降演算子を作用させる。しかし，この過程を延々に続けることはできない。やがて `z` 成分が全角運動量を上回る状態に達してしまうが，それは不可能である [#]_ 。したがって，ある最上段 `f_t` が存在して

.. math::
    L_+f_t = 0

となるはずである。最上段における `L_z` の固有値を `\hbar l` とすると，

.. math::
    L_zf_t = \hbar l f_t,\quad L^2f_t = \lambda f_t

ここで，

.. math::
    \begin{aligned}
        L_{\pm}L_{\mp} &= (L_x \pm iL_y)(L_x \mp iL_y)
        \\
        &= L_x^2 + L_y^2 \mp i(L_xL_y-L_yL_x)
        \\
        &= L_x^2 + L_y^2 \mp i[L_x,L_y]
    \end{aligned}

である。したがって，

.. math::
    L^2f_t = (L_-L_+ L_z^2 + \hbar L_z)f_t = (0 + \hbar^2l^2 + \hbar^2l)f_t = \hbar^2l(l+1)f_t

よって，

.. math::
    \lambda = \hbar^2l(l+1)

である。これは `L_z` の最大固有値によって `L^2` の固有値が決まることを意味する。

同様に最下段 `f_b` が存在して

.. math::
    L_-f_b = 0

となる。最下段における `L_z` の固有値を `\hbar \bar{l}` とすると，

.. math::
    L_zf_b = \hbar \bar{l} f_b,\quad L^2f_b = \lambda f_b

で，

.. math::
    L^2f_b = (L_+L_- + L_z^2 - \hbar L_z)f_b = (0 + \hbar^2\bar{l}^2 - \hbar^2\bar{l})f_b = \hbar^2\bar{l}(\bar{l}-1)f_b

よって，

.. math::
    \lambda = \hbar^2\bar{l}(\bar{l}-1)

である。したがって， `l(l+1) = \bar{l}(\bar{l}-1)` となるので， `\bar{l}=l+1` か `\bar{l}=-l` であるが，前者は最下段が最上段より高いことになってしまうから不可能で，

.. math::
    \bar{l} = -l

となる。したがって， `L_z` の固有値は `m\hbar` であり， `m` は `-l` から `+l` まで `N` 回の整数刻みで変化する。特に `l=-l+N` ，したがって， `l = N/2` であるから， `l` は整数または半整数でなければならない。固有関数はこのような `l,m` によって特徴づけられる：

.. math::
    L^2f_l^m = \hbar^2l(l+1)f_l^m,\quad L_zf_l^m = m\hbar f_l^m

ここで，

.. math::
    l = 0,\frac{1}{2},1,\frac{3}{2},\ldots;\quad m = -l,-l+1,\ldots,l-1,l

である。 `l` の値をひとつ固定すると `m` には `2l+1` 個の異なる値がある。

我々はこれまでで角運動量の交換関係から出発し，純粋に代数的な方法で固有関数そのものを一度も見ることなく， `L^2` と `L_z` の固有値を求めることができた。次に固有関数を求めるが，これははるかに厄介である。結論を先に言うと， `f_l^m=Y_l^m` は球面調和関数になる。球面調和関数の直交性はエルミート演算子 `L^2` と `L_z` の相異なる固有値に属する固有関数の直交性によって保証される。

まずは `L_x,L_y,L_z` を球座標で書き直す。 `\bm{L}=-i\hbar(\bm{r}\times\bm{\nabla})` であり，球座標における勾配は

.. math::
    \bm{\nabla} = \bm{e}_r\pdv{}{r} + \bm{e}_\theta\frac{1}{r}\pdv{}{\theta} + \bm{e}_\phi\frac{1}{r\sin\theta}\pdv{}{\phi}

である。一方で `\bm{r} = r\bm{e}_r` なので，

.. math::
    \begin{aligned}
        \bm{L} &= -i\hbar\left[r(\bm{e}_r\times\bm{e}_r)\pdv{}{r} + (\bm{e}_r \times \bm{e}_\theta)\pdv{}{\theta} + (\bm{e}_r \times \bm{e}_\phi)\frac{1}{\sin\theta}\pdv{}{\phi}\right]
        \\
        &= -i\hbar\left(\bm{e}_\phi\pdv{}{\theta}-\bm{e}_\theta\frac{1}{\sin\theta}\pdv{}{\phi}\right)
    \end{aligned}

となる。ここで，球座標における単位ベクトルは

.. math::
    \bm{e}_\theta &= (\cos\theta\cos\phi)\bm{e}_x + (\cos\theta\sin\phi)\bm{e}_y - (\sin\theta)\bm{e}_z
    \\
    \bm{e}_\phi &= -(\sin\phi)\bm{e}_x + (\cos\phi)\bm{e}_y

であるから，

.. math::
    \bm{L} = -i\hbar\left[(-\sin\phi\bm{e}_x + \cos\phi\bm{e}_y)\pdv{}{\theta} - (\cos\theta\cos\phi\bm{e}_x + \cos\theta\sin\phi\bm{e}_y - \sin\theta\bm{e}_z)\frac{1}{\sin\theta}\pdv{}{\phi}\right]

したがって，

.. math::
    \begin{aligned}
        L_x &= -i\hbar\left(-\sin\phi\pdv{}{\theta} - \cos\phi\cot\theta\pdv{}{\phi}\right)
        \\
        L_y &= -i\hbar\left(\cos\phi\pdv{}{\theta} - \sin\phi\cot\theta\pdv{}{\phi}\right)
    \end{aligned}

および，

.. math::
    \boxed{L_z = -i\hbar\pdv{}{\phi}}

となる。上昇・下降演算子は

.. math::
    L_\pm = L_x \pm iL_y = -i\hbar\left[(-\sin\phi\pm i\cos\phi)\pdv{}{\theta}-(\cos\phi\pm i\sin\phi)\cot\theta\pdv{}{\phi}\right]

しかし `\cos\phi\pm i\sin\phi = e^{\pm i\phi}` なので，

.. math::
    L_\pm = \pm\hbar e^{\pm i\phi}\left(\pdv{\theta}\pm i\cot\theta\pdv{}{\phi}\right)

となる。特に，

.. math::
    L_+L_- = -\hbar^2\left(\pdv{^2}{\theta^2} + \cot\theta\pdv{}{\theta} + \cot^2\theta\pdv{^2}{\phi^2} + i\pdv{}{\phi}\right)

よって，

.. math::
    \boxed{L^2 = -\hbar^2\left[\frac{1}{\sin\theta}\pdv{}{\theta}\left(\sin\theta\pdv{}{\theta}\right) + \frac{1}{\sin^2\theta}\pdv{^2}{\phi^2}\right]}

となる。これで `f_l^m(\theta,\phi)` を求められる。これは固有値 `\hbar^2l(l+1)` の `L^2` の固有関数である：

.. math::
    L^2 f_l^m = -\hbar^2\left[\frac{1}{\sin\theta}\pdv{}{\theta}\left(\sin\theta\pdv{}{\theta}\right) + \frac{1}{\sin^2\theta}\pdv{^2}{\phi^2}\right]f_l^m = \hbar^2l(l+1)f_l^m

これはまさに角度方程式である。また固有値 `m\hbar` の `L_z` の固有関数でもある：

.. math::
    L_z f_l^m = -i\hbar\pdv{}{\phi}f_l^m = m\hbar f_l^m

これはまさに `\phi` 依存性を決定した方程式である。この連立方程式は既に解いた。その結果は適切に規格化すれば球面調和関数である。つまり，変数分離によって時間に依存しない Schrödinger 方程式を解いたとき，知らず知らずのうちに，可換な3つの演算子 `H,L^2,L_z` の同時固有関数を求めていたことになる。

しかし全く同じではない。角運動量の代数からは `l` や `m` は半整数値も許される。変数分離から得られた固有関数は整数値に対してのみであった。この新しい半整数の解は次節で述べるように非常に重要である。

.. [#] 記述を簡潔にするために演算子から `\hat{}` を省略する。

.. [#] 形式的には `\braket{L^2} = \braket{L_x^2} + \braket{L_y^2} + \braket{L_z^2}` であるが， `\braket{L_x^2} = \braket{f|L_x^2f} = \braket{L_xf|L_xf} \ge 0` （ `L_y` についても同様）なので `\lambda = \braket{L^2} = \braket{L_x^2} + \braket{L_y^2} + \mu^2 \ge \mu^2` である。
