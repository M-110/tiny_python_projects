.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

clean:
	yapf ransom.py --in-place --style google

rate:
	-flake8 ransom.py
	-pylint ransom.py
