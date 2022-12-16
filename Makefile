# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS		= "-W"
SPHINXBUILD		= sphinx-build
SOURCEDIR		= src
BUILDDIR		= _build
RUNNER			= cwl-runner

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from https://sphinx-doc.org/)
endif

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

watch: clean
	@echo
	@echo "Building and watching for changes in the documentation."
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" \
			--ignore='**venv' \
			--ignore='**.github' \
			--ignore='*.egg-info' \
			--ignore='**_includes/**/*.txt' \
			--watch='cwl'

## unittest-examples	:
unittest-examples:
	cd src/_includes/cwl; cwltest --test=cwl_tests.yml --tool=${RUNNER}

## check-json			:
check-json:
	python -m json.tool < src/.zenodo.json >> /dev/null && exit 0 || echo "NOT valid JSON"; exit 1

container-pull:
	for container in $$(git grep dockerPull $$(git ls-files *.cwl) | awk '-F: ' '{print $$3}'); do docker pull $${container}; done

.PHONY: help clean watch unittest-examples check-json Makefile

# Catch-all target		: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

