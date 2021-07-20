.PHONY: test, clean, rate

test:
	python3 -m pytest -xv test.py

unit:
	python3 -m pytest -xv unit.py

clean:
	yapf tictactoe.py --in-place --style google

rate:
	-flake8 tictactoe.py
	-pylint tictactoe.py
