test:
	coverage run -m unittest
core:
	python3 rpn.py
.PHONY: test
