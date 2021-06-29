.PHONY: test, rate, clean

test:
	python3 -m pytest -xv test.py

rate:
	-flake8 wc.py
	-pylint wc.py

clean:
	yapf wc.py --in-place --style google
