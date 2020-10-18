SHELL := /bin/bash
.PHONY: all clean deps dist docs install test help

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all: clean install test

test_only:
	@poetry run pytest -m "not integration" -v --cov-config .coveragerc --cov=i18web -l --tb=short --maxfail=1 tests/
	@poetry run coverage xml

test: test_only

install:
	@poetry update

build: clean
	@poetry build

deps:
	@poetry export -f requirements.txt > requirements.txt
	@poetry export --dev -f requirements.txt > requirements_dev.txt

dist: clean
	@poetry run python setup.py sdist bdist_wheel

docs:
	cd docs
	@poetry run mkdocs build
	cd ..

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf docs/build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
