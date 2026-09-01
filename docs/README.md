# Documentation

Language-specific reStructuredText files live in `source/<language>/`. Shared
Sphinx configuration and theme assets live directly under this directory.

The default `make html` command builds every language that has an
`index.rst`. Japanese is currently available; English will be picked up
automatically after `source/en/index.rst` and its referenced pages are added.
Until then, `make site` publishes the static English placeholder from `site/`.

```console
make html
make html-ja
make html-en
make site
```

The generated GitHub Pages tree is written to `build/html/`.
