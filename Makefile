test:
	coverage run --source unittest test_rpn.py test
core:
	python3 rpn.py
.PHONY: test
