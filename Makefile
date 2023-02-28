SHELL := /bin/bash
.PHONY: all clean deps dist docs upgrade lint test integration help

RUN=poetry run

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all: clean lint test

lint:
	@${RUN} ruff check .

test_only:
	@${RUN} pytest -m "not integration" -v --cov-config .coveragerc --cov=i18web -l --tb=short --maxfail=1 tests/
	@${RUN} coverage xml

test: test_only

integration:
	@${RUN} behave

upgrade:
	@poetry update

build: clean
	@poetry build

deps:
	@poetry export -f requirements.txt > requirements.txt
	@poetry export --with dev -f requirements.txt > requirements_dev.txt

dist: build
#	@poetry run python setup.py sdist bdist_wheel

docs:
	cd docs
	@${RUN} mkdocs build
	cd ..

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf docs/build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
