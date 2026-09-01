Schrödinger 方程式
======================

古典力学の基本的な問題は，任意の時刻における粒子の位置 `\bm{x}(t)` を求めることである。これが求まれば，粒子の速度 `\bm{v}(t)=\dot{\bm{x}}(t)` や運動量 `\bm{p}(t)=m\bm{v}(t)`，その他のどのような力学変数も求めることができる。そのような位置 `\bm{x}(t)` を求めるためには，与えられた力 `\bm{F}` に対して Newton の運動方程式と呼ばれる時刻 `t` についての二階微分方程式 `\bm{F}=m\ddot{\bm{x}}` を適当な初期条件（典型的には時刻 `t=0` における位置 `\bm{x}(0)` と速度 `\bm{v}(0)`）を用いて解けばよい。特に本講義では，保存力 `\bm{F}=-\nabla V(\bm{x})` による運動を考える。ここで `V(\bm{x})` は位置 `\bm{x}` に依存するポテンシャルエネルギーである。実際的に，このような特別な力に制限したところで困ることはほとんどないだろう。

一方で，量子力学の基本的な問題は，任意の位置 `\bm{x}` と時刻 `t` における **波動関数** と呼ばれる複素数値関数 `\Psi(\bm{x}, t)` を求めることである。そのような波動関数 `\Psi(\bm{x}, t)` を求めるためには， **Schrödinger 方程式** と呼ばれる時刻 `t` についての1階微分方程式

.. math::
    i\hbar\pdv{\Psi(\bm{x}, t)}{t} = -\frac{\hbar^2}{2m}\nabla^2\Psi(\bm{x}, t) + V(\bm{x})\Psi(\bm{x}, t)

を適当な初期条件（典型的には時刻 `t=0` における波動関数 `\Psi(\bm{x}, 0)`）を用いて解けばよい。ここで `\hbar` は **Planck 定数** `h` を `2\pi` で割ったもので

.. math::
    \hbar \coloneqq \frac{h}{2\pi} \approx 1.054573\times 10^{-34}\,\mathrm{J\cdot s}

という値を持つ。この講義の大部分はこの問題を解くことに費やされる。その前に，この「波動関数」とはいったい何であり，Schrödinger 方程式を解くことが何の役に立つかを説明しよう [#]_ 。

.. [#]  1925年頃，EZH Zürich のコロキウムで Schrödinger が de Broglie の物質波のアイデアを紹介した際，Debye が「波について語るのであれば，それに対応する波動方程式を持つべきではないか」という趣旨の指摘をした。それが Schrödinger 方程式の発想のきっかけになったそうだ (ref. Felix Bloch, "`Heisenberg and the Early Days of Quantum Mechanics <https://physicstoday.aip.org/features/heisenberg-and-the-early-days-of-quantum-mechanics>`_", Physics Today 29, no. 12, 23--27, December 1976)。
