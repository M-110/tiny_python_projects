.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

rate:
	-flake8 apples.py
	-pylint apples.py

clean:
	yapf apples.py --in-place --style google
