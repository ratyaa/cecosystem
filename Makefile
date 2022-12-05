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
	WHICH := where.exe
	VENV_ACTIVATION_CMD := $(ENV)\Scripts\activate
endif

help: --osconfig
ifeq (, @$(WHICH) awk sort)
	$(error "no awk and sort found")
else
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
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
	@rm -rf $(ENV) src/__pycache__
