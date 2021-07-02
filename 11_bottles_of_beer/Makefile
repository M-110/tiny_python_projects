.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

sums:
	./mk-sums.sh > sums.txt

clean:
	yapf bottles.py --in-place --style google

rate:
	-flake8 bottles.py
	-pylint bottles.py
