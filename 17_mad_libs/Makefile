.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

clean:
	yapf mad.py --in-place --style google

rate:
	-flake8 mad.py
	-pylint mad.py
