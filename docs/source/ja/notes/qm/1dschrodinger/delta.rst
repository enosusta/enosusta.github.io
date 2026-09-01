デルタ関数型ポテンシャル
===============================

これまで時間に依存しない Schrödinger 方程式に対する2つの非常に異なる解に出会った：

1. 解は規格化可能で離散的な添え字 `n` で指定される。
2. 解は規格化不可能で連続的な添え字 `k` で指定される。

この違いの物理的な意味は何だろう。

古典力学では，一次元の時間に依存しないポテンシャルは2つの非常に異なる種類の運動を生じさせる。

1. 粒子の全エネルギー `E` よりも `V(x)` が両側で高くなるなら，粒子はポテンシャルの井戸に「閉じ込められる」。粒子は転回点の間を行き来するが，井戸の外に逃げ出すことはない。このような状態を **束縛状態** と呼ぶ。

2. 粒子の全エネルギー `E` よりも `V(x)` が片側で低くなるなら，粒子は「無限遠」からやってきて，ポテンシャル影響の下で減速あるいは加速し，再び無限遠へ戻っていく。このような状態を **散乱状態** と呼ぶ。

`V(x)` によっては，束縛状態だけを許す場合もあれば，散乱状態だけを許す場合もある。さらに，粒子のエネルギーに応じて束縛状態と散乱状態の両方を許す場合もある。

時間に依存しない Schrödinger 方程式の2種類の解は，この束縛状態と散乱状態に対応している。むしろ量子力学ではその区別はよりいっそう明確である。というのも，トンネル効果（後で説明する）によって，粒子は有限なポテンシャル障壁を通り抜けることができるので，2種類の状態を区別するのは無限遠におけるポテンシャルだけだからである：

1. `E < V(-\infty) \text{ and } V(+\infty)` ：束縛状態
2. `E > V(-\infty) \text{ or } V(+\infty)` ：散乱状態

実際のほとんどのポテンシャルは無限遠でゼロに近づくため，判定条件はさらに単純になる：

1. `E < 0` ：束縛状態
2. `E > 0` ：散乱状態

無限井戸型ポテンシャルと調和振動子型ポテンシャルの場合は， `x\to\pm\infty` で `V(x)\to\infty` なので，束縛状態しか許さない。一方で自由粒子の場合は，いたるところで `V(x)=0` なので，散乱状態しか許さない。この節と次節では，両方の状態を持つポテンシャルを与える。

次の形のポテンシャルを考える：

.. math::
    V(x) = -\alpha\delta(x),\quad \alpha>0

これも人工的なポテンシャルだが，簡単に扱える。時間に依存しない Schrödinger 方程式は

.. math::
    -\frac{\hbar^2}{2m}\dv{^2\psi}{x^2} - \alpha\delta(x)\psi = E\psi

であり，束縛状態（ `E<0` ）と散乱状態（ `E>0` ）の両方を生じる。

束縛状態
----------------

まず束縛状態を調べる。領域 `x<0` では `V(x)=0` なので，

.. math::
    \dv{^2\psi}{x^2} = -\frac{2mE}{\hbar^2}\psi = \kappa^2\psi,\quad \kappa \coloneqq \frac{\sqrt{-2mE}}{\hbar}

となる。仮定より `E<0` なので `\kappa>0` である。一般解は，

.. math::
    \psi(x) = Ae^{-\kappa x} + Be^{\kappa x}

である。しかし，第一項は `x\to-\infty` で発散するので， `A=0` としなければならない。したがって，

.. math::
    \psi(x) = Be^{\kappa x},\quad x<0

一方で，領域 `x>0` でも `V(x)=0` であり，一般解は `Fe^{-\kappa x} + Ge^{\kappa x}` である。しかし，第二項は `x\to+\infty` で発散するので， `G=0` としなければならない。したがって，

.. math::
    \psi(x) = Fe^{-\kappa x},\quad x>0

となる。あとは `x=0` における適切な境界条件を用いて，この2つをつなぎ合わせる：

1. `\psi` は連続である。
2. `\dv{\psi}{x}` はポテンシャルが無限大となる点を除いて連続である。

第一の条件から `F=B` となるので，

.. math::
    \psi(x) = \begin{cases}
        Be^{\kappa x}, & x\le 0 \\
        Be^{-\kappa x}, & x\ge 0
    \end{cases}

今の場合，第二の条件からは何もわからない。ここでデルタ関数を使う。まず，時間に依存しない Schrödinger 方程式を `-\epsilon` から `+\epsilon` まで積分する：

.. math::
    -\frac{\hbar^2}{2m}\int_{-\epsilon}^{+\epsilon}\dv{^2\psi}{x^2}\,\dd x + \int_{-\epsilon}^{+\epsilon}V(x)\psi(x)\,\dd x = E\int_{-\epsilon}^{+\epsilon}\psi(x)\,\dd x

左辺の第一項は，2つの端点で評価された `\dv{\psi}{x}` である。右辺は `\epsilon\to 0` の極限でゼロになる。したがって，

.. math::
    \Delta\left(\dv{\psi}{x}\right) \coloneqq \lim_{\epsilon\to0}\left(\left.\dv{\psi}{x}\right|_{+\epsilon} - \left.\dv{\psi}{x}\right|_{-\epsilon}\right) = \frac{2m}{\hbar^2}\lim_{\epsilon\to0}\int_{-\epsilon}^{+\epsilon}V(x)\psi(x)\,\dd x

通常は右辺の極限もゼロであり， `\dv{\psi}{x}` は連続である。しかし，境界で `V(x)` が無限大となる場合は，右辺の極限はゼロでない。特にデルタ関数型ポテンシャル `V(x) = -\alpha\delta(x)` の場合，

.. math::
    \Delta\left(\dv{\psi}{x}\right) = -\frac{2m\alpha}{\hbar^2}\psi(0)

となる。今の場合，

.. math::
    \begin{aligned}
        \dv{\psi}{x} = -B\kappa e^{-\kappa x},\quad x>0 &\implies \left.\dv{\psi}{x}\right|_{+} = -B\kappa
        \\
        \dv{\psi}{x} = +B\kappa e^{\kappa x},\quad x<0 &\implies \left.\dv{\psi}{x}\right|_{-} = +B\kappa
    \end{aligned}

となるので， `\Delta(\dv{\psi}{x}) = -2B\kappa` で `\psi(0)=B` である。したがって，

.. math::
    \kappa = \frac{m\alpha}{\hbar^2}

となり，許されるエネルギーは，

.. math::
    E = -\frac{\hbar^2\kappa^2}{2m} = -\frac{m\alpha^2}{2\hbar^2}

となる。最後に規格化条件より，

.. math::
    1 = \int_{-\infty}^{+\infty}|\psi(x)|^2\,\dd x = 2|B|^2\int_0^{\infty}e^{-2\kappa x}\,\dd x = \frac{|B|^2}{\kappa}

となるので，

.. math::
    B = \sqrt{\kappa} = \frac{\sqrt{m\alpha}}{\hbar}

と選べる。したがってデルタ関数井戸内には，その「強さ」 `\alpha` によらず束縛状態がちょうどひとつだけ存在する：

.. math::
    \boxed{\psi(x) = \frac{\sqrt{m\alpha}}{\hbar}e^{-m\alpha|x|/\hbar^2},\quad E = -\frac{m\alpha^2}{2\hbar^2}}

散乱状態
----------------

次に `E>0` の散乱状態を調べる。 `x<0` に対して時間に依存しない Schrödinger 方程式は

.. math::
    \dv{^2\psi}{x^2} = -\frac{2mE}{\hbar^2}\psi = -k^2\psi,\quad k \coloneqq \frac{\sqrt{2mE}}{\hbar}

となる。一般解は

.. math::
    \psi(x) = Ae^{ikx} + Be^{-ikx}

である。今回はどちらの項も発散しない。同様に `x>0` では，

.. math::
    \psi(x) = Fe^{ikx} + Ge^{-ikx}

となる。 `x=0` における `\psi(x)` の連続性より

.. math::
    :label: eq:delta-boundary1

    F+G = A+B

となる。導関数については，

.. math::
    \begin{aligned}
        \dv{\psi}{x} = ik(Fe^{ikx}-Ge^{-ikx}),\quad x>0 &\implies \left.\dv{\psi}{x}\right|_{+} = ik(F-G)
        \\
        \dv{\psi}{x} = ik(Ae^{ikx}-Be^{-ikx}),\quad x<0 &\implies \left.\dv{\psi}{x}\right|_{-} = ik(A-B)
    \end{aligned}

となる。したがって， `\Delta(\dv{\psi}{x}) = ik(F-G-A+B)` である。一方で `\psi(0) = A+B` なので，境界条件は，

.. math::
    ik(F-G-A+B) = -\frac{2m\alpha}{\hbar^2}(A+B)

となる。これを整理すると，

.. math::
    :label: eq:delta-boundary2

    F-G = A(1+2i\beta)-B(1-2i\beta),\quad \beta \coloneqq \frac{m\alpha}{\hbar^2k}

となる。

2つの境界条件を課した結果，4つの未知数 `A,B,F,G` に対して 2つの方程式 :eq:`eq:delta-boundary1` と :eq:`eq:delta-boundary2` が残った。 `k` まで数えるなら未知数は5つである。規格化条件はそもそもこれは規格化可能な状態ではないので使えない。ここで一旦立ち止まって，さまざまな定数の物理的意味を調べる。

`e^{ikx}` は振動因子 `e^{-iEt/\hbar}` を掛けると，右へ伝わる波動関数を生じ， `e^{-ikx}` は左へ伝わる波を生じる。したがって， `A` は左から入射する波の振幅， `B` は左へ戻っていく波の振幅である。同様に， `F` は右へ去っていく波の振幅， `G` は右から入射する波の振幅である。典型的な散乱実験では，粒子は一方向から，例えば左から入射させる。この場合，右から入射する波の振幅はゼロである：

.. math::
    G = 0

`A` は入射波の振幅， `B` は反射波の振幅， `F` は透過波の振幅である。境界条件 :eq:`eq:delta-boundary1` と :eq:`eq:delta-boundary2` を `B` と `F` について解くと，

.. math::
    B = \frac{i\beta}{1-i\beta}A,\quad F = \frac{1}{1-i\beta}A

となる。さて，指定された位置に粒子を見出す確率は `|\Psi|^2` で与えられるので，入射粒子が反射して戻る「相対的な」確率は [#]_ ，

.. math::
    R \coloneqq \frac{|B|^2}{|A|^2} = \frac{\beta^2}{1+\beta^2}

となる。この `R` を反射係数と呼ぶ。一方で，粒子がそのまま右へ通り抜ける確率は，

.. math::
    T \coloneqq \frac{|F|^2}{|A|^2} = \frac{1}{1+\beta^2}

となる。この `T` を透過係数と呼ぶ。もちろん，これらの確率の和が `1` でなければならず，実際そうなる：

.. math::
    R + T = 1

`R,T` は `\beta` の関数であり，したがって `E` の関数である：

.. math::
    \boxed{R = \frac{1}{1+(2\hbar^2E/m\alpha^2)},\quad T = \frac{1}{1+(m\alpha^2/2\hbar^2E)}}

エネルギーが高いほど透過する確率が大きい。これはもっともな結果である。

しかし，何度も言うがこれらの散乱波動関数は規格化できないので，実際には可能な粒子状態を表していない。真の物理的粒子は波束によって表される。原理上は素直に構成できても，反射係数や透過係数の計算は面倒であり，計算機の任せるのがよい [#]_ 。ここで求めた `R,T` は， `E` に近いエネルギーを持つ粒子に対する近似的な結果と解釈すべきである。

デルタ関数障壁の場合
-------------------------

最後に，デルタ関数障壁の場合について述べておく。形式的には `\alpha` の符号を変えるだけで良い。これにより束縛状態は消滅する。一方で，奇妙なことに `\alpha^2` にのみ依存する反射係数と透過係数は変化しない。もちろん古典的には，エネルギーがいくらあっても無限に高いポテンシャル障壁を越えることはできない。しかし，量子力学では，粒子のエネルギーがいくら高くても，障壁を越える確率はゼロにはならない。この現象を **トンネル効果** と呼ぶ。これは現代の電子工学の多くを可能にしている機構である。逆に `E>V_\text{max}` の場合でも，粒子が跳ね返る可能性がある。

.. [#] これは規格化可能な波動関数ではないので，特定の位置に粒子を見出す絶対的な確率は定義されない。しかし，入射波と反射波の確率の比には意味がある。

.. [#] 1次元ポテンシャルによる波束の散乱を解析する強力なプログラムとして，たとえば，University of Colorado Boulder の PhET Interactive Simulations の "`Quantum Tunneling and Wave Packets <https://phet.colorado.edu/en/simulations/quantum-tunneling>`_" がある。
