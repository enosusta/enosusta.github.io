時間並進
================

ここでは時間並進不変性を調べる。時間に依存する Schrödinger 方程式

.. math::
    \hat{H}\Psi(x,t) = i\hbar\pdv{}{t}\Psi(x,t)

の解 `\Psi(x,t)` を考える。波動関数の時刻を発展させる演算子 `\hat{U}(t)` を

.. math::
    \hat{U}(t)\Psi(x,0) = \Psi(x,t)

によって定義できる。右辺を `t=0` の周りで Taylor 展開すると [#]_ ，

.. math::
    \hat{U}(t)\Psi(x,0) = \Psi(x,t) = \sum_{n=0}^{\infty}\frac{1}{n!}\left.\pdv{^n}{t^n}\Psi(x,t)\right|_{t=0}t^n

ハミルトニアンが時刻に陽に依存しなければ，時間に依存する Schrödinger 方程式より，

.. math::
    \hat{U}(t)\Psi(x,0) = \sum_{n=0}^{\infty}\frac{1}{n!}\left(-\frac{i}{\hbar}\hat{H}t\right)^n\Psi(x,0)

となる。したがって，時間発展演算子は

.. math::
    \boxed{\hat{U}(t) = \exp\left[-\frac{it}{\hbar}\hat{H}\right]}

と書ける。そこでハミルトニアンは時間並進の生成子であるという。ここで `\hat{U}(t)` はユニタリー演算子であることに注意する。

これまで述べた他の変換と同様に，時間並進を波動関数だけでなく演算子に適用した効果も調べることができる。変換後の演算子は **Heisenberg 描像** の演算子と呼ばれる：

.. math::
    \boxed{\hat{Q}_H(t) = \hat{U}^{\dagger}(t)\hat{Q}\hat{U}(t)}

これまで用いてきた描像は **Schrödinger 描像** と呼ばれるものである [#]_ 。この描像では，波動関数は時間に依存する Schrödinger 方程式

.. math::
    \hat{H}\Psi(x,t) = i\hbar\pdv{}{t}\Psi(x,t)

に従って時間発展する。演算子 `\hat{x}=x` や `\hat{p}=-i\hbar\partial_x` はそれ自身の時刻依存性を持たず，期待値の時刻依存性は波動関数の時刻依存性に由来する：

.. math::
    \braket{\hat{Q}} = \braket{\Psi(t)|\hat{Q}|\Psi(t)}

一方で Heisenberg 描像では，波動関数は時間的に一定 `\Psi_H(x) = \Psi(x,0)` であり，演算子が `\hat{Q}_H(t)=\hat{U}^{\dagger}(t)\hat{Q}\hat{U}(t)` のように時間発展する。期待値の時刻依存性は演算子の時刻依存性に由来する：

.. math::
    \braket{\hat{Q}} = \braket{\Psi_H|\hat{Q}_H(t)|\Psi_H}

もちろん，

.. math::
    \braket{\Psi(t)|\hat{Q}|\Psi(t)} = \braket{\Psi(0)|\hat{U}^\dagger\hat{Q}\hat{U}|\Psi(0)} = \braket{\Psi_H|\hat{Q}_H(t)|\Psi_H}

なので，この2つの描像は完全に等価である [#]_ 。

ハミルトニアンが時刻に依存する場合にも，時間に依存する Schrödinger 方程式の形式的な解を時間並進演算子 `\hat{U}` を用いて書くことができる：

.. math::
    \Psi(x,t) = \hat{U}(t,t_0)\Psi(x,t_0)

しかし `\hat{U}` はもはや単純な形をとらない。無限小時間 `\delta` に対しては，

.. math::
    \hat{U}(t_0+\delta,t_0) \approx 1 - \frac{i}{\hbar}\hat{H}(t_0)\delta

となる。

さて，時間並進不変性とは，時間発展が，どの時間を考えてるかによらないことを意味する。つまり，任意の `t_1,t_2` に対して，

.. math::
    \hat{U}(t_1+\delta,t_1) = \hat{U}(t_2+\delta,t_2)

である。これが成り立つためには `\hat{H}(t_1) = \hat{H}(t_2)` が成り立つ必要がある。したがって，時間並進不変性が成り立つためには，結局ハミルトニアンが時刻に陽に依存してはならない：

.. math::
    \pdv{\hat{H}}{t} = 0

この場合，一般化された Ehrenfest の定理より，

.. math::
    \dv{}{t}\braket{\hat{H}} = \frac{i}{\hbar}\braket{[\hat{H},\hat{H}]} + \braket{\pdv{\hat{H}}{t}} = 0

となる。したがって，エネルギー保存則は時間並進不変性の結果である。

.. [#] ここでは Schrödinger 方程式の解が Taylor 展開できると仮定しているが，それを保証するものは何もない。実際にそのような展開が存在しない例も存在する。しかし，そのような場合にも指数関数を用いた式は成り立つ。

.. [#] この名称は，Schrödinger 自身が考えていた描像であったため，Dirac によって命名された。

.. [#] このような他の描像の内，最も重要なものに相互作用描像（ Dirac 描像）がある。これは時刻に依存する摂動論でしばしば用いられる。
