.PHONY: test build

test:
	@python test/runner.py

build:
	@python setup.py build sdist bdist_wheel

release: build
	@twine upload dist/* --verbose && rm -Rf dist/
