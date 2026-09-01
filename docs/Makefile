SPHINXOPTS   ?=
SPHINXBUILD  ?= python -m sphinx
SOURCEDIR     = source
BUILDDIR      = build

LANGUAGE_SOURCES = $(wildcard $(SOURCEDIR)/*/index.rst)
LANGUAGES        = $(notdir $(patsubst %/index.rst,%,$(LANGUAGE_SOURCES)))
HTML_TARGETS     = $(addprefix html-,$(LANGUAGES))

help:
	@echo "make html     Build every language that has source/<lang>/index.rst"
	@echo "make html-ja  Build Japanese documentation"
	@echo "make html-en  Build English documentation"
	@echo "make site     Build and assemble the GitHub Pages artifact"
	@echo "make clean    Remove generated files"
	@echo "Detected languages: $(LANGUAGES)"

.PHONY: help html html-ja html-en build-language site clean

html: $(HTML_TARGETS)

html-ja:
	@$(MAKE) --no-print-directory build-language LANGUAGE=ja

html-en:
	@$(MAKE) --no-print-directory build-language LANGUAGE=en

build-language:
	@test -f "$(SOURCEDIR)/$(LANGUAGE)/index.rst" || { \
		echo "Missing $(SOURCEDIR)/$(LANGUAGE)/index.rst" >&2; \
		exit 2; \
	}
	@DOCS_LANGUAGE="$(LANGUAGE)" $(SPHINXBUILD) -b html -c . $(SPHINXOPTS) \
		"$(SOURCEDIR)/$(LANGUAGE)" "$(BUILDDIR)/html/$(LANGUAGE)"

site: html
	@cp site/index.html "$(BUILDDIR)/html/index.html"
	@if test ! -f "$(BUILDDIR)/html/en/index.html"; then \
		mkdir -p "$(BUILDDIR)/html/en"; \
		cp site/en/index.html "$(BUILDDIR)/html/en/index.html"; \
	fi
	@touch "$(BUILDDIR)/html/.nojekyll"

clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)/ja" "$(BUILDDIR)" -c .
