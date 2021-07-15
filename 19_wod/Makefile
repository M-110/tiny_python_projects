.PHONY: test, clean, rate

test:
	python3 -m pytest test.py -v

clean:
	yapf wod.py --in-place --style google

rate:
	-flake8 wod.py
	-pylint wod.py