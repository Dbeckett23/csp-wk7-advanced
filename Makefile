test:
	python3 -m unittest --pep8 coveralls -v --cov coveralls --cov-report term-missing
core:
	python3 rpn.py
.PHONY: test
