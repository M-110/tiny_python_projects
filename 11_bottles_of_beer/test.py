#!/usr/bin/env python3
"""tests for bottles.py"""

import hashlib
import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './bottles.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_int():
    """Bad integer value"""

    bad = random.randint(-10, 1)
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv != 0
    assert re.search(f'--num "{bad}" must be greater than 0', out)


# --------------------------------------------------
def test_float():
    """float value"""

    bad = round(random.random() * 10, 2)
    rv, out = getstatusoutput(f'{prg} --num {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_str():
    """str value"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_one():
    """One bottle of beer"""

    expected = ('1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} --num 1')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_two():
    """Two bottles of beer"""

    expected = ('2 bottles of beer on the wall,\n'
                '2 bottles of beer,\n'
                'Take one down, pass it around,\n'
                '1 bottle of beer on the wall!\n\n'
                '1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} -n 2')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_random():
    """Random number"""

    sums = dict(
        map(lambda x: x.split('\t'),
            open('sums.txt').read().splitlines()))

    for n in random.choices(list(sums.keys()), k=10):
        flag = '-n' if random.choice([0, 1]) == 1 else '--num'
        rv, out = getstatusoutput(f'{prg} {flag} {n}')
        out += '\n'  # because the last newline is removed
        assert rv == 0
        assert hashlib.md5(out.encode('utf-8')).hexdigest() == sums[n]
        
        
# --------------------------------------------------
def test_text():
    """Numbers as text."""

    expected = ('Two bottles of beer on the wall,\n'
                'Two bottles of beer,\n'
                'Take one down, pass it around,\n'
                'One bottle of beer on the wall!\n\n'
                'One bottle of beer on the wall,\n'
                'One bottle of beer,\n'
                'Take one down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} -n 2 -t')
    assert rv == 0
    assert out == expected
        
        
# --------------------------------------------------
def test_steps():
    """Numbers as text."""

    expected = ('15 bottles of beer on the wall,\n'
                '15 bottles of beer,\n'
                'Take five down, pass them around,\n'
                '10 bottles of beer on the wall!\n\n'
                '10 bottles of beer on the wall,\n'
                '10 bottles of beer,\n'
                'Take five down, pass them around,\n'
                '5 bottles of beer on the wall!\n\n'
                '5 bottles of beer on the wall,\n'
                '5 bottles of beer,\n'
                'Take five down, pass them around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} -n 15 -s 5')
    assert rv == 0
    assert out == expected
        
        
# --------------------------------------------------
def test_steps_uneven():
    """Numbers as text."""

    expected = ('15 bottles of beer on the wall,\n'
                '15 bottles of beer,\n'
                'Take seven down, pass them around,\n'
                '8 bottles of beer on the wall!\n\n'
                '8 bottles of beer on the wall,\n'
                '8 bottles of beer,\n'
                'Take seven down, pass them around,\n'
                '1 bottle of beer on the wall!\n\n'
                '1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} -n 15 -s 7')
    assert rv == 0
    assert out == expected
    
    
# --------------------------------------------------
def test_reverse():
    """Two bottles of beer"""

    expected = ('0 bottles of beer on the wall,\n'
                '0 bottles of beer,\n'
                'Take one down, pass it around,\n'
                '1 bottle of beer on the wall!\n\n'
                '1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                '2 bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} -n 2 -r')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
