.PHONY: test, clean, rate

test:
	pytest -xv unit.py

rate:
	-flake8 itictactoe.py
	-pylint itictactoe.py

clean:
	yapf itictactoe.py --in-place --style google
