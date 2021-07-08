.PHONY: test, rate, clean

test:
	python3 -m pytest -xvv test.py 

rate:
	-flake8 twelve_days.py
	-pylint twelve_days.py

clean:
	yapf twelve_days.py --in-place --style google
