.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

clean:
	yapf scrambler.py --in-place --style google

rate:
	-flake8 scrambler.py
	-pylint scrambler.py
