# Sphinx 入門・実用メモ

最終確認：2026-08-07  
対象：Sphinx 9.1 系（このディレクトリの環境は 9.1.0）

Sphinx は，reStructuredText（reST）や Markdown で書いた原稿を，HTML，PDF，EPUB，man ページなどへ変換する文書作成ツールです。特に，複数ページの目次，ページ間の参照，索引，数式，ソースコードからの API 文書生成を得意とします。

まずは次の関係だけ覚えれば使い始められます。

```text
docs/source/*.rst  -- Sphinx でビルド -->  docs/build/html/*.html
       原稿             設定 conf.py              閲覧する成果物
```

## 1. このディレクトリですぐ試す

すでに仮想環境と Sphinx プロジェクトが作成済みです。

```bash
cd /home/sone/stacks/sphinx
source .venv/bin/activate
sphinx-build --version

cd docs
make html
```

生成された `docs/build/html/index.html` をブラウザで開きます。Linux で GUI が使えるなら `xdg-open build/html/index.html` でも開けます。

原稿を修正した後は，もう一度 `make html` を実行してください。Sphinx は通常，変更されたファイルだけを再ビルドします。設定や依存関係を変えて表示がおかしくなったときは，次のように一度消して作り直します。

```bash
make clean
make html
```

警告も失敗として扱い，可能な箇所を最後まで検査するには次を使います。公開前や CI ではこの形がおすすめです。

```bash
sphinx-build -M html source build --fail-on-warning --keep-going
```

仮想環境を抜けるときは `deactivate` を実行します。

## 2. ファイル構成

このプロジェクトの主要部分は次のとおりです。

```text
sphinx/
├── .venv/                 Sphinx を入れた Python 仮想環境
└── docs/
    ├── Makefile           Linux・macOS 用の簡易コマンド
    ├── make.bat           Windows 用の簡易コマンド
    ├── source/
    │   ├── conf.py        プロジェクト全体の設定
    │   ├── index.rst      文書全体の入口
    │   ├── _static/       CSS・画像など（必要な場合）
    │   └── _templates/    HTML テンプレート（必要な場合）
    └── build/             ビルド成果物（Git には入れない）
```

重要なのは次の 3 点です。

1. 本文は `docs/source/` 以下に書く。
2. 新しいページは `toctree` に登録する。
3. 全体設定は `docs/source/conf.py` に書く。

## 3. reStructuredText の最小限の書き方

Sphinx の標準原稿形式は reStructuredText，拡張子は `.rst` です。

### 見出しと本文

```rst
量子力学
========

これは普通の段落です。段落同士の間には空行を入れます。

状態ベクトル
------------

``状態ベクトル`` は等幅表示，*斜体*，**太字** も使えます。
```

見出しの下線は見出し以上の長さにします。同じ階層では同じ記号を使ってください。このメモでは，第 1 階層に `=`，第 2 階層に `-`，第 3 階層に `~` を使っています。

### 箇条書きと番号付きリスト

```rst
* 項目 A
* 項目 B

  * 入れ子の項目

1. 最初
2. 次
```

リストの前後には空行が必要です。インデントのずれは reST のエラーで最もよくある原因の一つです。

### コード

```rst
.. code-block:: python
   :caption: hello.py

   def hello(name: str) -> str:
       return f"Hello, {name}!"
```

`.. code-block::` の後に空行を置き，内容を同じ幅だけインデントします。

短いコマンドなら，段落末尾の `::` でも書けます。

```rst
実行します::

   python main.py
```

### 数式

インライン数式は次のように書きます。

```rst
:math:`E = mc^2`
```

独立した数式は次のように書きます。

```rst
.. math::

   i\hbar \frac{\partial}{\partial t}\lvert\psi\rangle
   = H\lvert\psi\rangle
```

HTML 出力では標準で MathJax が利用されます。

### 注記と警告

```rst
.. note::

   補足情報です。

.. warning::

   特に注意が必要な内容です。
```

`note` や `code-block` のような，行頭が `..` で始まるブロックを「ディレクティブ」と呼びます。`:ref:` や `:doc:` のように行内で意味を付ける記法は「ロール」と呼びます。

### 表

手書きでは `list-table` が修正しやすい形式です。

```rst
.. list-table:: 出力形式
   :header-rows: 1

   * - コマンド
     - 出力
   * - ``make html``
     - 複数の HTML
   * - ``make singlehtml``
     - 単一の HTML
```

## 4. ページを追加して目次につなぐ

例として `docs/source/notes/gr.rst` を作ります。

```rst
一般相対論
==========

ここに本文を書きます。
```

次に `docs/source/notes/index.rst` の `toctree` へ，拡張子を付けずに追加します。

```rst
.. toctree::
   :maxdepth: 2

   qm
   qft
   gr
```

`toctree` は単なる表示用目次ではありません。ページの親子関係，並び順，「前へ」「次へ」のリンクも決めます。原則として，全 `.rst` ファイルをどこかの `toctree` へ入れてください。入っていないページは `document isn't included in any toctree` という警告になります。

また，各ページの先頭には見出しを付けてください。見出しがないページを登録すると `doesn't have a title` という警告になります。

## 5. リンクと相互参照

### 同じ文書内・別ページの節へリンクする

リンク先に，プロジェクト内で一意なラベルを置きます。

```rst
.. _install-guide:

インストール
============
```

別の場所から次のように参照します。

```rst
:ref:`install-guide` を参照してください。
:ref:`インストール手順 <install-guide>` を参照してください。
```

ラベルは見出しの直前に置き，ラベルと見出しの間に空行を入れます。見出し名を変えてもリンクが壊れないため，通常の URL を直接書くより安全です。

### ページへリンクする

```rst
:doc:`notes/qm`
:doc:`量子力学のノート <notes/qm>`
```

### 外部サイトへリンクする

```rst
`Sphinx 公式サイト <https://www.sphinx-doc.org/>`_
```

リンク切れの検査は次のコマンドで行います。インターネットへの接続が必要です。

```bash
make linkcheck
```

## 6. 画像を入れる

たとえば `docs/source/_static/figures/setup.png` を置いた場合は次のようにします。

```rst
.. figure:: /_static/figures/setup.png
   :alt: Sphinx の構成図
   :width: 80%
   :align: center

   Sphinx の構成
```

先頭の `/` は OS のルートではなく，Sphinx のソースディレクトリ `docs/source/` を表します。本文の一部としてキャプションを付けたい場合は `figure`，単に表示するだけなら `image` を使います。

## 7. `conf.py` で設定する

現在の `docs/source/conf.py` には，おおよそ次の設定があります。

```python
project = "PIP"
author = "Enos"
release = "1.0.0"
language = "ja"

extensions = []
html_theme = "alabaster"
```

よく変更する項目は次のとおりです。

| 設定 | 意味 |
| --- | --- |
| `project` | 文書・プロジェクト名 |
| `author` | 著者名 |
| `release` | 公開バージョン |
| `language` | Sphinx が生成する UI の言語。日本語は `"ja"` |
| `extensions` | 使用する拡張機能の Python モジュール名 |
| `html_theme` | HTML のテーマ |
| `exclude_patterns` | ビルド対象外にするパターン |

`conf.py` は設定ファイルですが，中身は Python コードです。文字列の引用符，リスト末尾のコンマ，インデントに注意してください。

静的ファイルやテンプレート用ディレクトリをまだ作らない場合，対応する設定を空にしても構いません。

```python
templates_path = []
html_static_path = []
```

## 8. 新しい Sphinx プロジェクトを作る

別の場所で最初から作る場合は，プロジェクトごとに仮想環境を用意します。Sphinx 9.1 は Python 3.12 以上が必要です。

```bash
mkdir my-project
cd my-project
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install "sphinx~=9.1.0"
sphinx-quickstart docs
```

`sphinx-quickstart` の質問には，最初は次のように答えれば十分です。

```text
Separate source and build directories (y/n) [n]: y
Project name: プロジェクト名
Author name(s): 著者名
Project release []: 0.1.0
Project language [en]: ja
```

その後，次を実行します。

```bash
cd docs
make html
```

依存バージョンを共有・再現したい場合は，プロジェクトの方針に合わせて `requirements.txt` や `pyproject.toml` に Sphinx と拡張機能を記録します。`.venv/` と `docs/build/` は生成し直せるので Git には入れません。

## 9. Markdown を使う

Sphinx の標準は reST です。Markdown を使いたい場合は，公式が案内している MyST-Parser を追加します。

```bash
python -m pip install --upgrade myst-parser
```

`conf.py` に追加します。

```python
extensions = [
    "myst_parser",
]
```

これで `.md` を `toctree` に登録できます。CommonMark に加えて Sphinx のディレクティブやロール相当の記法を使えますが，通常の GitHub Flavored Markdown と完全に同じではありません。ひとつのプロジェクト内で reST と MyST Markdown を混在させることもできます。

## 10. Python の API 文書を docstring から作る

`autodoc` は Python モジュールを import し，関数・クラスのシグネチャと docstring を文書へ取り込みます。Google 形式や NumPy 形式の docstring には `napoleon` が便利です。

`conf.py` の例です。

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
```

まず，文書化するパッケージと Sphinx を同じ仮想環境へインストールしてください。開発中の Python パッケージなら，リポジトリのルートで次の形にするのが扱いやすいです。

```bash
python -m pip install -e .
```

`.rst` 側には次のように書きます。

```rst
API リファレンス
================

.. automodule:: my_package.core
   :members:
   :undoc-members:
   :show-inheritance:
```

大量のモジュール用に `.rst` の雛形を生成する場合は `sphinx-apidoc` も使えます。

```bash
sphinx-apidoc -o docs/source/api src/my_package
```

注意点として，`autodoc` はビルド時に対象モジュールを実際に import します。import だけでファイル削除や通信などを行うコードは避け，スクリプトの実行部分は `if __name__ == "__main__":` で保護してください。依存パッケージが欠けていて import に失敗した場合も文書を生成できません。

## 11. 出力形式を変える

代表的なビルダーは次のとおりです。

```bash
make html          # ページごとの HTML
make dirhtml       # 拡張子の見えない URL 向け HTML
make singlehtml    # 全内容を 1 ファイルにした HTML
make linkcheck     # 外部リンクの検査
make latex         # LaTeX ソース
make latexpdf      # LaTeX を経由して PDF
make epub          # EPUB
```

`latexpdf` には TeX Live，LaTeX エンジン，`latexmk` などが別途必要です。日本語 PDF はフォントと LaTeX の追加設定が必要になることがあるため，まず HTML ビルドを成功させてから設定するのが安全です。

利用可能なビルダーとコマンドは `make help` で確認できます。

## 12. よくあるエラー

### `sphinx-build: command not found`

仮想環境が有効になっていません。

```bash
cd /home/sone/stacks/sphinx
source .venv/bin/activate
```

### `document isn't included in any toctree`

作成した `.rst` または `.md` を `index.rst` などの `toctree` に追加します。意図的に目次へ入れないページなら，そのファイルの先頭に `:orphan:` を付けられます。

### `toctree contains reference to nonexisting document`

`toctree` のパスが間違っています。パスは記述している `.rst` からの相対パスで，通常は拡張子を省略します。ファイル名の大文字・小文字も確認してください。

### `toctree contains reference ... that doesn't have a title`

参照先ファイルに見出しがありません。ファイル冒頭へ，見出し文字列と `====` のような下線を追加します。

### `Unexpected indentation` や `Block quote ends without a blank line`

ディレクティブ，リスト，コードブロックの前後の空行とインデントを確認します。タブではなく空白を使うと問題を避けやすくなります。

### `autodoc: failed to import module`

Sphinx を実行している仮想環境で対象モジュールを import できるか確認します。

```bash
python -c "import my_package"
```

失敗する場合は，対象パッケージ自身と必要な依存パッケージをその環境へインストールします。

### 変更が反映されない

ビルドキャッシュを消して再生成します。

```bash
make clean
make html
```

## 13. 日常的な作業手順

普段はこの流れだけで十分です。

```bash
cd /home/sone/stacks/sphinx
source .venv/bin/activate

# docs/source/ 以下の .rst を編集する

cd docs
sphinx-build -M html source build --fail-on-warning --keep-going
```

1. `docs/source/` に原稿を追加・編集する。
2. 新規ページを親ページの `toctree` に登録する。
3. 警告をエラー扱いにしてビルドする。
4. `docs/build/html/index.html` で表示とリンクを確認する。
5. 原稿と設定だけを Git に記録し，`.venv/` と `build/` は記録しない。

## 公式リファレンス

- [Sphinx 公式ドキュメント](https://www.sphinx-doc.org/en/master/)
- [Getting started](https://www.sphinx-doc.org/en/master/tutorial/getting-started.html)
- [`sphinx-quickstart`](https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [`toctree` などのディレクティブ](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)
- [ビルダー一覧](https://www.sphinx-doc.org/en/master/usage/builders/index.html)
- [Markdown（MyST-Parser）](https://www.sphinx-doc.org/en/master/usage/markdown.html)
- [`autodoc`](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [Sphinx 9.1 の変更履歴](https://www.sphinx-doc.org/en/master/changes/index.html)

バージョンに依存する挙動は，検索結果や古い記事ではなく，使用中のバージョンに対応する公式ドキュメントを優先して確認してください。
