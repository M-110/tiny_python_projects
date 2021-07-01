.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

rate: 
	-flake8 abuse.py
	-pylint abuse.py

clean:
	yapf abuse.py --in-place --style google