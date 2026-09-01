# source/ja/conf.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "common"))

from conf_common import *

language = "ja"

html_baseurl = 'https://enosusta.github.io/ja/'
html_context = {
    **html_context,
    "conf_py_path": "/docs/source/ja/",
}
