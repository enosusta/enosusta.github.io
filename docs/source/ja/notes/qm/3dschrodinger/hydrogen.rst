水素原子
==============

水素原子は，重く動かない陽子と，電荷 `e` を持つ陽子を回る軽い電子（質量 `m_e` ，電荷 `-e` ）から成り，両者は異符号の電荷の相互引力によって束縛されている。Coulomb の法則より，電子のポテンシャルエネルギーは SI 単位系で

.. math::
    V(r) = -\frac{e^2}{2\pi\epsilon_0}\frac{1}{r}

であり，動径方程式は

.. math::
    -\frac{\hbar^2}{2m_e}\dv{^2u}{r^2} + \left[-\frac{e^2}{4\pi\epsilon_0}\frac{1}{r} + \frac{\hbar^2}{2m_e}\frac{l(l+1)}{r^2}\right]u = Eu

となる。問題は，この方程式を `u(r)` について解き，許されるエネルギーを求めることである。水素原子は重要な場合なので，調和振動子型ポテンシャルのときに使った解析的方法で詳しく導出することにする。また，Coulomb ポテンシャルは水素原子を表す束縛状態（ `E<0` ）だけでなく，電子と陽子の散乱を記述する散乱状態（ `E>0` ）も許すが，ここでは束縛状態だけを扱う。

まずは記法を整えるために，

.. math::
    \kappa \coloneqq \frac{\sqrt{-2m_e E}}{\hbar}

と置く。束縛状態では `\kappa` は正の実数である。動径方程式を `E` で割ると，

.. math::
    \frac{1}{\kappa^2}\dv{^2u}{r^2} = \left[1-\frac{m_ee^2}{2\pi\epsilon_0\hbar^2\kappa}\frac{1}{\kappa r} + \frac{l(l+1)}{(\kappa r)^2}\right]u

となる。ここで，

.. math::
    :label: eq:rho-def

    \rho \coloneqq \kappa r,\quad \rho_0 \coloneqq \frac{m_e e^2}{2\pi\epsilon_0\hbar^2\kappa}

と置くと，動径方程式は

.. math::
    \dv{^2u}{\rho^2} = \left[1-\frac{\rho_0}{\rho} + \frac{l(l+1)}{\rho^2}\right]u

となる。

次に解の漸近形を調べる。 `\rho\to\infty` では，括弧内の定数項が支配的になるので，近似的に

.. math::
    \dv{^2u}{\rho^2} \approx u

となる。一般解は

.. math::
    u(\rho) \approx A e^{-\rho} + B e^{\rho}

だが， `e^\rho` は `\rho\to\infty` で発散するので `B=0` である。したがって，大きな `\rho` に対して

.. math::
    u(\rho) \approx A e^{-\rho}

となる。一方で `\rho\to0` では遠心力項が支配的であり，近似的には

.. math::
    \dv{^2u}{\rho^2} \approx \frac{l(l+1)}{\rho^2}u

となる。一般解は

.. math::
    u(\rho) \approx C\rho^{l+1} + D\rho^{-l}

だが， `\rho^{-l}` は `\rho\to0` で発散するので `D=0` である。したがって，小さな `\rho` に対して

.. math::
    u(\rho) \approx C\rho^{l+1}

となる。

そこで新しい関数 `v(\rho)` を

.. math::
    u(\rho) \eqqcolon \rho^{l+1} e^{-\rho} v(\rho)

で定義する。そうすると一階微分は

.. math::
    \dv{u}{\rho} = \rho^le^{-\rho}\left[(l+1-\rho)v+\rho\dv{v}{\rho}\right]

となり，二階微分は

.. math::
    \dv{^2u}{\rho^2} = \rho^le^{-\rho}\left\{\left[-2l-2+\rho+\frac{l(l+1)}{\rho}\right]v + 2(l+1-\rho)\dv{v}{\rho} + \rho\dv{^2v}{\rho^2}\right\}

となる。したがって動径方程式は

.. math::
    \rho\dv{^2v}{\rho^2} + 2(l+1-\rho)\dv{v}{\rho} + [\rho_0-2(l+1)]v = 0

と書ける。

そして解 `v(\rho)` が `\rho` の冪級数として表せると仮定する：

.. math::
    v(\rho) = \sum_{j=0}^\infty c_j \rho^j

項別微分をすると，

.. math::
    \dv{v}{\rho} = \sum_{j=0}^\infty jc_j\rho^{j-1} = \sum_{j=0}^\infty (j+1)c_{j+1}\rho^j

となり，もう一度微分すると，

.. math::
    \dv{^2v}{\rho^2} = \sum_{j=0}^\infty j(j+1)c_{j+1}\rho^{j-1}

となる。これを動径方程式に代入すると，

.. math::
    \sum_{j=0}^\infty\{j(j+1)c_{j+1}+2(l+1)(j+1)c_{j+1}-2jc_j+[\rho_0-2(l+1)]c_j\}\rho^j = 0

となる。各係数がゼロでなければならないので，

.. math::
    (j+1)(j+2l+2)c_{j+1} = [2(j+l+1)-\rho_0]c_j

すなわち，漸化式

.. math::
    c_{j+1} = \frac{2(j+l+1)-\rho_0}{(j+1)(j+2l+2)}c_j

を得る。この漸化式が係数を決め，したがって関数 `v(\rho)` を決定する [#]_ 。

さて，大きな `j` に対して係数がどのようになるか調べる。これは高次の冪が支配的になる `\rho` が大きい場合に対応する。この領域では漸化式は

.. math::
    c_{j+1} \approx \frac{2j}{j(j+1)}c_j = \frac{2}{j+1}c_j

となるので，

.. math::
    c_j \approx \frac{2^j}{j!}c_0

となる。そうすると，

.. math::
    v(\rho) = c_0\sum_{j=0}^{\infty}\frac{(2\rho)^j}{j!} = c_0e^{2\rho}

であり，したがって，

.. math::
    u(\rho) \approx c_0\rho^{l+1}e^{\rho}

となって，大きな `\rho` で発散する。この指数関数は望まれなかった漸近的振る舞いそのものである。

この問題を逃れるには級数は打ち切られなければならない。すなわち，ある整数 `N` が存在して，

.. math::
    c_{N-1} \neq 0,\quad c_N = 0

とならなければならない。この場合，漸化式から

.. math::
    2(N+l) - \rho_0 = 0

となる。ここで，

.. math::
    n \coloneqq N + l

と定義すれば，

.. math::
    \rho_0 = 2n

となる。この `\rho_0` は式 :eq:`eq:rho-def` より `E` を決定し，

.. math::
    E = -\frac{\hbar^2\kappa^2}{2m_e} = -\frac{m_e e^4}{8\pi^2\epsilon_0^2\hbar^2\rho_0^2}

となる。したがって許されるエネルギーは

.. math::
    \boxed{E_n = -\left[\frac{m_e}{2\hbar^2}\left(\frac{e^2}{4\pi\epsilon_0}\right)\right]\frac{1}{n^2} = \frac{E_1}{n^2},\quad n=1,2,3,\dots}

となる。これは有名な Bohr の公式である。驚くべきことに，Bohr は 1913 年に古典力学と時期尚早の量子力学とを混ぜ合わせることでこの公式を得た。

また，

.. math::
    \kappa = \left(\frac{m_ee^2}{4\pi\epsilon_0\hbar^2}\right)\frac{1}{n} = \frac{1}{an}

となる。ここで，

.. math::
    \boxed{a \coloneqq \frac{4\pi\epsilon_0\hbar^2}{m_ee^2} \approx 0.529 \times 10^{-10}\,\mathrm{m}}

は Bohr 半径と呼ばれる。さらに，

.. math::
    \rho = \frac{r}{an}

となる。

以上より波動関数は3個の量子数 `n,l,m` によってラベル付けされる：

.. math::
    \psi_{nlm}(r,\theta,\phi) = R_{nl}(r)Y_l^m(\theta,\phi)

ここで

.. math::
    R_{nl}(r) = \frac{1}{r}\rho^{l+1}e^{-\rho}v(\rho)

であり， `v(\rho)` は `\rho` の `n-l-1` 次多項式である。その係数は全体の規格化因子を除いて，漸化式

.. math::
    c_{j+1} = \frac{2(j+l+1-n)}{(j+1)(j+2l+2)}c_j

によって決まる。基底状態は `n=1` の場合で，

.. math::
    \boxed{E_1 = -\left[\frac{m_e}{2\hbar^2}\left(\frac{e^2}{4\pi\epsilon_0}\right)^2\right] =  -13.6\,\mathrm{eV}}

となる。つまり，水素の束縛エネルギー（基底状態の電子を原子から電離させるために必要なエネルギー）は `13.6` eV である。このとき， `l=0` で `m=0` なので，波動関数は

.. math::
    \psi_{100}(r,\theta,\phi) = R_{10}(r)Y_0^0(\theta,\phi)

となる。漸化式は第一項のあとですぐに打ち切られるので， `v(\rho)` は定数 `c_0` であり，

.. math::
    R_{10}(r) = \frac{c_0}{a}e^{-r/a}

となる。これを規格化すると，

.. math::
    \int_0^\infty|R_{10}|^2r^2\,\dd r = \frac{|c_0|^2}{a^2}\int_0^\infty e^{-2r/a}r^2\,\dd r = |c_0|^2\frac{a}{4} = 1

となるので， `c_0 = 2/\sqrt{a}` と選べる。一方で `Y_0^0=1/\sqrt{4\pi}` なので，基底状態の波動関数は

.. math::
    \boxed{\psi_{100}(r,\theta,\phi) = \frac{1}{\sqrt{\pi a^3}}e^{-r/a}}

となる。

`n=2` ならエネルギーは

.. math::
    E_2 = \frac{-13.6\,\mathrm{eV}}{4} = -3.40\,\mathrm{eV}

である。このとき `l=0` か `l=1` が可能であり，それぞれ `m=0` と `m=-1,0,1` が可能である。これら4つの異なる状態が第一励起状態である。 `l=0` のとき漸化式より

.. math::
    c_1 = -c_0,\quad c_2 = 0

となるので `v(\rho) = c_0(1-\rho)` であり，したがって

.. math::
    R_{20}(r) = \frac{c_0}{2a}\left(1-\frac{r}{2a}\right)e^{-r/2a}

となる。 `l=1` のとき漸化式は第一項のあとですぐに打ち切られるので， `v(\rho)` は定数 `c_0` であり，

.. math::
    R_{21}(r) = \frac{c_0}{4a^2}re^{-r/2a}

となる。

任意の `n` に対して可能な `l` の値は，

.. math::
    l = 0,1,2,\dots,n-1

であり，各 `l` について `m` の可能な値が `2l+1` 個あるので，エネルギー準位 `E_n` の全縮退度は

.. math::
    d(n) = \sum_{l=0}^{n-1}(2l+1) = n^2

となる。異なる `l` の値が同じエネルギーを持つことに注意する。球対称だけから期待される縮退度（ `2l+1 = 1,3,5,7,\ldots` ）と比べて Coulomb ポテンシャルに余分な縮退度（ `n^2 = 1,4,9,16,\ldots` ）が生じるのはこのためである。

実は多項式 `v(\rho)` は応用数学的によく知られた関数であり，規格化を除けば

.. math::
    v(\rho) = L_{n-l-1}^{2l+1}(2\rho)

と書ける。ここで

.. math::
    L_q^p(x) \coloneqq (-1)^p\left(\dv{}{x}\right)^p L_{q+p}(x)

は Laguerre 陪多項式と呼ばれ，

.. math::
    L_q(x) \coloneqq \frac{e^x}{q!}\left(\dv{}{x}\right)^q(e^{-x}x^q)

は `q` 次 Laguerre 多項式と呼ばれる。たとえば，

.. math::
    \begin{aligned}
        L_0(x) &= 1
        \\
        L_1(x) &= -x + 1
        \\
        L_2(x) &= \frac{1}{2}x^2 - 2x + 1
        \\
        L_3(x) &= -\frac{1}{6}x^3 + \frac{3}{2}x^2 - 3x + 1
    \end{aligned}

などとなり，

.. math::
    \begin{aligned}
        L_0^1(x) &= 1
        \\
        L_1^0(x) &= -x + 1
        \\
        L_2^0(x) &= \frac{1}{2}x^2 - 2x + 1
        \\
        L_0^1(x) &= 1
        \\
        L_1^1(x) &= -x + 2
        \\
        L_2^1(x) &= \frac{1}{2}x^2 - 3x + 3
    \end{aligned}

などとなる。したがって（規格化の詳細は述べないが）規格化された水素の波動関数は

.. math::
    \boxed{\psi_{nlm}(r,\theta,\phi) = \sqrt{\left(\frac{2}{na}\right)^3\frac{(n-l-1)!}{2n(n+l)!}}e^{-r/na}\left(\frac{2r}{na}\right)^l L_{n-l-1}^{2l+1}\left(\frac{2r}{na}\right)Y_l^m(\theta,\phi)}

となる。少し複雑だが文句は言ってはいけない。このように厳密に閉じた形で解けるような現実的な系のそうそうない。波動関数は次のように直交規格化されている：

.. math::
    \int \psi_{nlm}^*\psi_{n'l'm'}\,\dd^3r = \delta_{nn'}\delta_{ll'}\delta_{mm'}

これは球面調和関数の規格直交性と，異なる固有値をもつエルミート演算子 `\hat{H}` の固有関数であることから従う。水素の波動関数を視覚化するのは容易ではないが，電子雲の明るさを `|\psi|^2` に比例させた密度プロットがよく使われている。

原理的には水素原子をある定常状態 `\Psi_{nlm}` に置けば，永久にそこに留まるはずである。しかし，原子をわずかに刺激すると，原子は別の定常状態に遷移することがある。エネルギーを吸収してより高いエネルギー状態へ上がるか，あるいはエネルギーを放出して下へ移る。実際に，このような遷移は絶えず起こっており，その結果，水素を入れた容器は光を放つ。そのエネルギーは始状態と終状態のエネルギー差に対応する：

.. math::
    E_\gamma = E_i-E_f  = -13.6\,\mathrm{eV}\left(\frac{1}{n_i^2} - \frac{1}{n_f^2}\right)

Planck の公式によれば，光子のエネルギーはその振動数に比例する：

.. math::
    E_\gamma = h\nu

一方で波長は `\lambda =c/\nu` なので，

.. math::
    \frac{1}{\lambda} = \mathcal{R}\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right)

となる。ここで，

.. math::
    \mathcal{R} \coloneqq \frac{m_e}{4\pi c\hbar^3}\left(\frac{e^2}{4\pi\epsilon_0}\right)^2 \approx 1.097\times10^7\,\mathrm{m^{-1}}

は Rydberg 定数として知られている。この結果は19世紀に経験的に発見され，その説明を与えたのは Bohr であった。基底状態（ `n_f=1` ）への遷移は紫外域にあり Lyman 系列として知られている。第一励起状態（ `n_f=2` ）への遷移は可視域にあり Balmer 系列として知られている。第二励起状態（ `n_f=3` ）への遷移は赤外域にあり Paschen 系列として知られている。室温では水素原子の大部分が基底状態にあるため，実際に発光スペクトルを見るには，まず種々の励起状態を占有させなければならない。典型的には気体中に放電すればよい。

.. [#] `u(\rho)` を冪級数にするのではなく，漸近的な振る舞いをくくり出したのは技術的な理由である。もしそうしなければ，三項漸化式が得られ途方に暮れることになる。
