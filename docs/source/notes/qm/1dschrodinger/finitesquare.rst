有限井戸型ポテンシャル
===========================

次のポテンシャルを考える：

.. math::
    V(x) = \begin{cases}
        -V_0 & -a \le x \le a
        \\
        0 & |x| > a
    \end{cases}

ここで `V_0` は正の定数である。この場合もデルタ関数型ポテンシャルの場合と同様に，束縛状態 (`E<0`) と散乱状態 (`E>0`) の両方が存在する。

束縛状態
----------------

まず束縛状態を調べる。領域 `x<-a` では `V(x)=0` なので，時間に依存しない Schrödinger 方程式は

.. math::
    -\frac{\hbar^2}{2m}\dv{^2\psi}{x^2} = E\psi

すなわち，

.. math::
    \dv{^2\psi}{x^2} = \kappa^2\psi,\quad \kappa \coloneqq \frac{\sqrt{-2mE}}{\hbar}

となる。ここで `\kappa` は正の実数である。一般解は， `\psi(x)=Ae^{-\kappa x}+Be^{\kappa x}` だが，第一項は `x\to-\infty` で発散するので，物理的に許される解は，

.. math::
    \psi(x) = Be^{\kappa x},\quad x<-a

である。領域 `-a < x < a` では `V(x)=-V_0` であり，時間に依存しない Schrödinger 方程式は

.. math::
    -\frac{\hbar^2}{2m}\dv{^2\psi}{x^2} - V_0\psi = E\psi

すなわち，

.. math::
    \dv{^2\psi}{x^2} = -l^2\psi,\quad l \coloneqq \frac{\sqrt{2m(E+V_0)}}{\hbar}

となる。束縛状態では `E` は負であるが， `E>V_\text{min}=-V_0` でなければならない。したがって， `l` も正の実数である。一般解は，

.. math::
    \psi(x) = C\sin(l x) + D\cos(l x),\quad -a<x<a

である。ここで `C,D` は任意定数である。領域 `x>a` では `V(x)=0` なので，領域 `x<-a` の場合と同様に，一般解は `\psi(x)=Fe^{-\kappa x}+Ge^{\kappa x}` であるが，第二項は `x\to\infty` で発散するので，物理的に許される解は，

.. math::
    \psi(x) = Fe^{-\kappa x},\quad x>a

である。

次に境界条件を課す。すなわち， `-a` と `+a` で `\psi` と `\dv{\psi}{x}` は連続でなければならない。しかし，このポテンシャルが偶関数であることに注目すれば，少し計算の手間が省ける。一般性を失うことなく，解は偶関数か奇関数であると仮定できる。したがって，片側でだけ境界条件を課せばよい。ここでは偶関数解のみを求めることにする。奇関数解の場合も同様の議論で求められる。つまり，次の形の解を探す：

.. math::
    \psi(x) = \begin{cases}
        Fe^{-\kappa x} & x>a
        \\
        D\cos(l x) & 0 < x < a
        \\
        \psi(-x) & x<0
    \end{cases}

`x=0` における `\psi(x)` の連続性は，

.. math::
    Fe^{-\kappa a} = D\cos(l a)

を与え， `\dv{\psi}{x}` の連続性は，

.. math::
    -\kappa Fe^{-\kappa a} = -l D\sin(l a)

を与える。これらの式から， `D` を消去すると，

.. math::
    \kappa = l\tan(l a)

となる。 `\kappa` と `l` はともに `E` の関数なので，これは許されるエネルギーを与える条件である。そこで `E` について解くために，より扱いやすい記号

.. math::
    z \coloneqq l a,\quad z_0 \coloneqq \frac{a}{\hbar}\sqrt{2mV_0}

を導入する。定義より `\kappa^2+l^2=2mV_0/\hbar^2` なので， `\kappa a=\sqrt{z_0^2-z^2}` となり，条件式は

.. math::
    \tan(z) = \sqrt{\left(\frac{z_0}{z}\right)^2-1}

となる。これは `z` （すなわち `E` ）についての超越方程式であり，井戸の「大きさ」 `z_0` の関数である。計算機を使って数値的に解いてもいいし，同じ座標上に `\tan(z)` と `\sqrt{(z_0/z)^2-1}` のグラフを描いて交点を求めてもよい。ここで次の2つの極限の場合が興味深い：

1.  広く深い井戸の場合： `z_0` が非常に大きい場合，交点は `n` が奇数の `z_n=n\pi/2` のすぐ下に現れる。したがって，エネルギーは

    .. math::
        E_n + V_0 \approx \frac{n^2\pi^2\hbar^2}{2m(2a)^2},\quad n=1,3,5,\dots

    となる。 `E+V_0` は井戸の底から測ったエネルギーであり，右辺は幅 `2a` の無限井戸型ポテンシャルのエネルギーに等しい。したがって， `V_0\to\infty` のとき，有限井戸型ポテンシャルは無限井戸型ポテンシャルへ移行する。しかし，任意の有限な `V_0` に対して束縛状態の数は有限個しかない。

2.  浅く狭い井戸の場合： `z_0` が小さくなるにつれて束縛状態の数はますます少なくなり，最終的には `z_0<\pi/2` でひとつだけが残る。しかし，井戸がどれほど「浅く」なっても束縛状態は常にひとつは存在する。

散乱状態
--------------

次に散乱状態（ `E>0` ）を調べる。左側の `V(x)=0` の領域では，

.. math::
    \psi(x) = Ae^{ikx}+Be^{-ikx},\quad x<-a,\quad k \coloneqq \frac{\sqrt{2mE}}{\hbar}

である。井戸の内部 `V(x)=-V_0` では，

.. math::
    \psi(x) = C\sin(l x)+D\cos(l x),\quad -a<x<a,\quad l \coloneqq \frac{\sqrt{2m(E+V_0)}}{\hbar}

である。右側の `V(x)=0` の領域では，右から入射する波がないと仮定すれば，

.. math::
    \psi(x) = Fe^{ikx},\quad x>a

である。ここで `A` は入射波の振幅， `B` は反射波の振幅， `F` は透過波の振幅である。

境界条件は4つある [#]_ 。 `x=-a` における `\psi(x)` の連続性は，

.. math::
    Ae^{-ika}+Be^{ika} = -C\sin(l a)+D\cos(l a)

を与え， `\dv{\psi}{x}` の連続性は，

.. math::
    ik[Ae^{-ika}-Be^{ika}] = l[C\cos(l a)+D\sin(l a)]

を与える。 `x=+a` における `\psi(x)` の連続性は，

.. math::
    C\sin(l a)+D\cos(l a) = Fe^{ika}

を与え， `\dv{\psi}{x}` の連続性は，

.. math::
    l[C\cos(l a)-D\sin(l a)] = ikFe^{ika}

を与える。このうち2つを使って `C,D` を消去し，残り2つを使って `B,F` を求めると，

.. math::
    \begin{aligned}
        B &= i\frac{\sin(2l a)}{2kl}(l^2-k^2)F
        \\
        F &= \frac{e^{-2ika}A}{\cos(2l a)-i\frac{k^2+l^2}{2kl}\sin(2l a)}
    \end{aligned}

となる。したがって，透過係数 `T` は，元の変数で

.. math::
    T^{-1} = 1 + \frac{V_0^2}{4E(E+V_0)}\sin^2\left(\frac{2a}{\hbar}\sqrt{2m(E+V_0)}\right)

となる。ここで，

.. math::
    \frac{2a}{\hbar}\sqrt{2m(E+V_0)} = n\pi,\quad n=1,2,\dots

のとき常に `T=1` となることに注意する。つまり，井戸が「透明」になるエネルギーは

.. math::
    E_n + V_0 = \frac{n^2\pi^2\hbar^2}{2m(2a)^2}

である。これは偶然にも無限井戸型ポテンシャルに対して許されるエネルギーとまったく同じである。

.. [#] もちろん束縛状態の場合と同様に，偶関数か奇関数の解を探すこともできるが，散乱問題では波が片側から入射するので本質的には非対称である。この文脈では，進行波を表す表記の方が自然である。
