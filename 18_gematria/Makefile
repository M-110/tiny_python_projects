.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

clean:
	yapf gematria.py --in-place --style google

rate:
	-flake8 gematria.py
	-pylint gematria.py
