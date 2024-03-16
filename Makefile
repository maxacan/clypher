.DEFAULT_GOAL := help

.PHONY: install
.PHONY: test
.PHONY: uninstall
.PHONY: help

uninstall:
	pip uninstall -y clypher

install: uninstall
	pip install .

help:
	@echo "Commands: "
	@echo "  test       : Run tests"
	@echo "  install    : Installs the latest build"
	@echo "  uninstall  : Removes the installation."




