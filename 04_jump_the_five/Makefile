.PHONY: test, rate, clean

test:
	python -m pytest -xv test.py

rate:
	@flake8 jump.py
	@-pylint jump.py

clean:
	yapf jump.py --in-place --style google