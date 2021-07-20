.PHONY: test, clean, rate

WORDS = "../inputs/words.txt"

test: #words
	python3 -m pytest -xv test.py
#
#words:
#	[[ -f $(WORDS) ]] || (cd ../inputs && unzip words.txt.zip)

clean:
	yapf password.py --in-place --style google

rate:
	-flake8 password.py
	-pylint password.py
