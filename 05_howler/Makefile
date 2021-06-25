.PHONY: test, rate, clean

test:
	python3 -m pytest -xv test.py

rate:
	flake8 howler.py
	-pylint howler.py

clean:
	yapf howler.py --in-place --style google
