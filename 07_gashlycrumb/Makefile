.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

rate:
	-flake8 gashlycrumb.py
	-pylint gashlycrumb.py

clean:
	yapf gashlycrumb.py --in-place --style google
