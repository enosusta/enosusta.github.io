# Minimal makefile for Sphinx documentation

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
JA_SOURCEDIR     = source/ja
EN_SOURCEDIR     = source/en
JA_BUILDDIR      = build/ja
EN_BUILDDIR      = build/en

help:
	@echo "make html    Build all"
	@echo "make html-ja Build Japanese"
	@echo "make html-en Build English"
	@echo "make clean   Remove build files"

.PHONY: help html html-ja html-en clean

html: html-ja html-en

html-ja:
	@$(SPHINXBUILD) -M html "$(JA_SOURCEDIR)" "$(JA_BUILDDIR)" $(SPHINXOPTS)

html-en:
	@$(SPHINXBUILD) -M html "$(EN_SOURCEDIR)" "$(EN_BUILDDIR)" $(SPHINXOPTS)

clean:
	rm -rf build
