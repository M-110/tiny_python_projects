.PHONY: test, rate, clean

test:
	python3 -m pytest -xvv test.py 

rate:
	-flake8 rhymer.py
	-pylint rhymer.py

clean:
	yapf rhymer.py --in-place --style google
