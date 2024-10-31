.PHONY: build install-local install-editable clean

build:
	python -m build

install-local: build
	pip install dist/*.whl --force-reinstall

install-editable:
	pip install -e .

clean:
	rm -rf dist/ build/ *.egg-info