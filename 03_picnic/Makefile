.PHONY: all test rate clean

test: test.py
	python3 -m pytest -xv test.py

rate: picnic.py
	@-python3 -m pylint picnic.py -rn
	@flake8 picnic.py

clean: picnic.py
	@echo "Cleaning code..."
	@yapf picnic.py --in-place --style google