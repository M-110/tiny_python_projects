.PHONY: test, rate, clean

test:
	python3 -m pytest -xv test.py

rate:
	-flake8 telephone.py
	-pylint telephone.py

clean:
	yapf telephone.py --in-place --style google
