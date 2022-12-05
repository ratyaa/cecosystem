# Makefile for python code
# 
# > make help
#
# The following commands can be used.
#
# init:  sets up environment and installs requirements
# install:  Installs development requirments
# format:  Formats the code with autopep8
# lint:  Runs flake8 on src, exit if critical rules are broken
# clean:  Remove build and cache files
# env:  Source venv and environment files for testing
# leave:  Cleanup and deactivate venv
# test:  Run pytest
# run:  Executes the logic

nixos :=			false
SHELL :=			bash
ENV :=				env
WHICH :=			which
PYTHON :=			python3
CREATE_VENV := 			$(PYTHON) -m venv $(ENV)
ACTIVATE_VENV :=		source $(ENV)/bin/activate
INSTALL_PACKAGES :=		$(PYTHON) -m pip install -r requirements.txt
CLEAN :=			rm -rf $(ENV) src/__pycache__

.DEFAULT_GOAL :=		help
.PHONY: help init --osconfig

.ONESHELL:
--osconfig:
ifeq ($(nixos), true)
	@$(eval CREATE_VENV :=)
	@$(eval ACTIVATE_VENV :=)
	@$(eval INSTALL_PACKAGES :=)
	@$(eval ENV :=)
endif
ifeq ($(OS), Windows_NT)
	@$(eval ACTIVATE_VENV := $(ENV)\Scripts\activate)
	@$(eval CLEAN := if (test-path env, src/pycache) {rm -r -Force env, src/__pycache__})
endif

help: --osconfig
ifeq ($(OS), Windows_NT)
	@type help.txt
else
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2 > "help.txt"}'
	@cat help.txt
endif


init: ## Initialize virtual environment and install packages.
init: --osconfig
	@$(CREATE_VENV)
	@$(ACTIVATE_VENV)
	@$(INSTALL_PACKAGES)

run: ## Run the program.
run: --osconfig
	@$(ACTIVATE_VENV)
	$(PYTHON) src/main.py

clean: ## Remove created directories.
clean: --osconfig
	@$(CLEAN)
