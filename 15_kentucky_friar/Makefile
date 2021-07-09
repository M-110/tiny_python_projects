.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

clean:
	yapf friar.py --in-place --style google

rate:
	-flake8 friar.py
	-pylint friar.py