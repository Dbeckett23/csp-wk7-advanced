test:
	coverage run test_rpn.py test | coveralls
core:
	python3 rpn.py
.PHONY: test
