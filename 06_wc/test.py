#!/usr/bin/env python3
"""tests for wc.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './wc.py'
empty = './inputs/empty.txt'
one_line = './inputs/one.txt'
two_lines = './inputs/two.txt'
fox = '../inputs/fox.txt'
sonnet = '../inputs/sonnet-29.txt'


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
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_bad_file():
    """bad_file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} count {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_empty():
    """Test on empty"""

    rv, out = getstatusoutput(f'{prg} count {empty}')
    assert rv == 0
    assert out.rstrip() == '       0       0       0 ./inputs/empty.txt'


# --------------------------------------------------
def test_one():
    """Test on one"""

    rv, out = getstatusoutput(f'{prg} count {one_line}')
    assert rv == 0
    assert out.rstrip() == '       1       1       2 ./inputs/one.txt'


# --------------------------------------------------
def test_two():
    """Test on two"""

    rv, out = getstatusoutput(f'{prg} count {two_lines}')
    assert rv == 0
    assert out.rstrip() == '       2       2       4 ./inputs/two.txt'


# --------------------------------------------------
def test_fox():
    """Test on fox"""

    rv, out = getstatusoutput(f'{prg} count {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_more():
    """Test on more than one file"""

    rv, out = getstatusoutput(f'{prg} count {fox} {sonnet}')
    expected = ('       1       9      45 ../inputs/fox.txt\n'
                '      17     118     661 ../inputs/sonnet-29.txt\n'
                '      18     127     706 total')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_stdin():
    """Test on stdin"""

    rv, out = getstatusoutput(f'{prg} count < {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      46 <stdin>'


# --------------------------------------------------
def test_b_flag():
    """Test b flag"""

    rv, out = getstatusoutput(f'{prg} count {fox} -b')
    assert rv == 0
    assert out.rstrip() == '      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_c_flag():
    """Test c flag"""

    rv, out = getstatusoutput(f'{prg} count {fox} -w')
    assert rv == 0
    assert out.rstrip() == '       9 ../inputs/fox.txt'


# --------------------------------------------------
def test_l_flag():
    """Test l flag"""

    rv, out = getstatusoutput(f'{prg} count {fox} -l')
    assert rv == 0
    assert out.rstrip() == '       1 ../inputs/fox.txt'


# --------------------------------------------------
def test_bl_flag():
    """Test bl flag"""

    rv, out = getstatusoutput(f'{prg} count {fox} -bl')
    assert rv == 0
    assert out.rstrip() == '       1      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_cat_command():
    """Test cat command"""

    rv, out = getstatusoutput(f'{prg} cat {fox}')
    assert rv == 0
    assert out.rstrip() == 'The quick brown fox jumps over the lazy dog.'


# --------------------------------------------------
def test_head_command():
    """Test head command"""

    rv, out = getstatusoutput(f'{prg} head {fox} -c 6 ')
    assert rv == 0
    assert out.rstrip() == 'The qu'
    
    
# --------------------------------------------------
def test_tail_command():
    """Test tail command"""

    rv, out = getstatusoutput(f'{prg} tail {fox} -c 6')
    assert rv == 0
    assert out.rstrip() == 'dog.'
    
    
# --------------------------------------------------
def test_tac_command():
    """Test tail command"""

    rv, out = getstatusoutput(f'{prg} tac {sonnet}')
    assert rv == 0
    assert out.rstrip() == """That then I scorn to change my state with kings.
For thy sweet love remembered such wealth brings
From sullen earth) sings hymns at heaven’s gate;
(Like to the lark at break of day arising
Haply I think on thee, and then my state,
Yet in these thoughts myself almost despising,
With what I most enjoy contented least;
Desiring this man’s art and that man’s scope,
Featured like him, like him with friends possessed,
Wishing me like to one more rich in hope,
And look upon myself and curse my fate,
And trouble deaf heaven with my bootless cries,
I all alone beweep my outcast state,
When, in disgrace with fortune and men’s eyes,

William Shakespeare
Sonnet 29"""

