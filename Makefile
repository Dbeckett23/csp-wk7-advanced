test:
	coverage run --source unittest test_rpn.py test | coveralls
core:
	python3 rpn.py
.PHONY: test
