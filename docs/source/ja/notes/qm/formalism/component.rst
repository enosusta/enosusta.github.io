状態と演算子の成分
==========================

量子力学における系の状態は Hilbert 空間のベクトル `\ket{S(t)}` によって表されるが，任意の数の異なる基底に関して表すことができる。波動関数 `\Psi(x,t)` は実際には，位置固有関数の基底で `\ket{S(t)}` を展開した時の `x` 成分である：

.. math::
    \boxed{\Psi(x,t) = \braket{x|S(t)}}

ここで `\ket{x}` は固有値 `x` をもつ `\hat{x}` の固有関数を表す。運動量空間の波動関数は，運動量固有関数の基底で `\ket{S(t)}` を展開した時の `p` 成分である：

.. math::
    \Phi(p,t) = \braket{p|S(t)}

ここで `\ket{p}` は固有値 `p` をもつ `\hat{p}` の固有関数を表す。あるいは， `\ket{S(t)}` をエネルギー固有関数の基底で展開することもできる（簡単のためスペクトルは離散的だとする）：

.. math::
    c_n(t) = \braket{n|S(t)}

ここで `\ket{n}` は `\hat{H}` の第 `n` 固有関数を表す。しかし，これらはどれも同じ状態である。関数 `\Psi,\Phi,\{c_n\}` は全く同じ情報を含んでいる。これらは同じベクトルを特定する3つの異なる方法にすぎない。

可観測量を表す演算子は Hilbert 空間上の線形変換であり，1つのベクトルを別のベクトルへ変換する：

.. math::
    :label: eq:operator

    \ket{\beta} = \hat{Q}\ket{\alpha}

ベクトルが正規直交基底 `\{\ket{e_n}\}` に関する成分によって

.. math::
    \begin{aligned}
        \ket{\alpha} &= \sum_n a_n\ket{e_n},\quad a_n = \braket{e_n|\alpha}
        \\
        \ket{\beta} &= \sum_n b_n\ket{e_n},\quad b_n = \braket{e_n|\beta}
    \end{aligned}

と表されるのと同様に，演算子は特定の基底に関する行列要素によって表される：

.. math::
    Q_{mn} \coloneqq \braket{e_m|\hat{Q}|e_n}
    
この記法では :eq:`eq:operator` は次のように書き換えられる：

.. math::
    \sum_n b_n\ket{e_n} = \sum_n a_n\hat{Q}\ket{e_n}

あるいは `\bra{e_m}` との内積をとれば，

.. math::
    \sum_n b_n\braket{e_m|e_n} = \sum_n a_n\braket{e_m|\hat{Q}|e_n}

したがって，正規直交性 `\braket{e_m|e_n} = \delta_{mn}` を用いれば，

.. math::
    b_m = \sum_n Q_{mn}a_n

となる。このように， `\hat{Q}` の行列成分は線形変換に対して成分がどのように変換されるかを与える。後で，線形独立な状態を有限個 `N` 個しか許さない系に出会う。その場合， `\ket{S(t)}` は `N` 次元ベクトル空間に存在し，ある基底に関する `N` 個の成分の列として表すことができ，演算子は通常の `N\times N` 行列の形で表すことができる。これらはもっとも単純な量子系であり，無限次元ベクトル空間に伴う微妙な問題は何も生じない。

ベクトルが異なる基底で表されると異なって見えるのと同様に，演算子も異なって見える。たとえば，

.. math::
    \begin{aligned}
        \hat{x} &\to \begin{cases}
            x & \text{in position space}
            \\
            i\hbar\pdv{}{p} & \text{in momentum space}
        \end{cases}
        \\
        \hat{p} &\to \begin{cases}
            -i\hbar\pdv{}{x} & \text{in position space}
            \\
            p & \text{in momentum space}
        \end{cases}
    \end{aligned}

とはいえ，実際にはほとんどの場合には位置空間で作業するので，波動関数を「系の状態」と呼んでもよい。

Dirac は内積に対するブラケット記号 `\braket{\alpha|\beta}` を2つに切り分け，それぞれを「ブラ」 `\bra{\alpha}` と「ケット」 `\ket{\beta}` と呼んだ（ `c` はどこかへ消えた）。後者はベクトルだが，前者はベクトルの線形関数であり，ベクトルに作用して1つの複素数（内積）を与えるものである。関数空間では，ブラは積分

.. math::
    \bra{f} = \int f^*[\cdots]\,\dd x

とみなせる。ここで `[\cdots]` はブラが作用する関数を表す。有限次元ベクトル空間でケットをある基底に関する成分の列として表すとすれば，ブラは行である：

.. math::
    \bra{\beta} = \begin{pmatrix}
        b_1^* & b_2^* & \cdots & b_n^*
    \end{pmatrix}

そして内積 `\braket{\beta|\alpha}=b_1^*a_1+b_2^*a_2+\cdots+b_n^*a_n` は行列の積である。すべてのブラの集まりは，もうひとつのベクトル空間を成し，双対空間を呼ばれる。

ブラをそれ自体独立した存在として扱うと，より簡潔な記述が可能になる。たとえば， `\ket{\alpha}` が規格化されたベクトルなら，演算子

.. math::
    \hat{P} = \ket{\alpha}\bra{\alpha}

は，他の任意のベクトル `\ket{\beta}` から `\ket{\alpha}` に「沿った」部分を抜き出す：

.. math::
    \hat{P}\ket{\beta} = \braket{\alpha|\beta}\ket{\alpha}

そこでこれを `\ket{\alpha}` が張る1次元部分空間への射影演算子と呼ぶ。 `\{\ket{e_n}\}` が離散的な正規直交基底ならば，

.. math::
    \boxed{\sum_n \ket{e_n}\bra{e_n} = \hat{1}}

となる。ここで `\hat{1}` は恒等演算子である。実際，この演算子を任意のベクトル `\ket{\alpha}` に作用させると基底 `\{\ket{e_n}\}` における `\ket{\alpha}` の展開が得られる：

.. math::
    \sum_n \braket{e_n|\alpha}\ket{e_n} = \ket{\alpha}

同様に， `\{\ket{e_n}\}` が Dirac 正規直交化された連続基底ならば，

.. math::
    \boxed{\int \ket{e_z}\bra{e_z}\,\dd z = \hat{1}}

となる。これらは完全性を表すもっとも簡潔な方法である。

とくには演算子の関数にも出会う。通常それらは Taylor 級数展開によって定義される。たとえば，

.. math::
    \begin{aligned}
        e^{\hat{Q}} &\coloneqq \hat{1} + \hat{Q} + \frac{1}{2}\hat{Q}^2 + \frac{1}{3!}\hat{Q}^3 + \cdots
        \\
        \frac{1}{\hat{1}-\hat{Q}} &\coloneqq \hat{1} + \hat{Q} + \hat{Q}^2 + \hat{Q}^3 + \cdots
        \\
        \ln(\hat{1}+\hat{Q}) &\coloneqq \hat{Q} - \frac{1}{2}\hat{Q}^2 + \frac{1}{3}\hat{Q}^3 - \cdots
    \end{aligned}

などである。右辺には和と積しかなく，それらの扱い方は既に分かっている。

演算子はケットに作用し，その作用の結果は，適切な基底ベクトルとの内積をとることで任意の基底において表現できる。たとえば，

.. math::
    \braket{x|\hat{x}|S(t)} = \text{action of position operator in $x$ basis} = x\Psi(x,t)

あるいは，

.. math::
    \braket{p|\hat{x}|S(t)} = \text{action of position operator in $p$ basis} = i\hbar\pdv{\Phi(p,t)}{p}

となる。この記法では，演算子を基底間で変換するのが簡単になる。
