#!/usr/bin/env python3
"""tests for crowsnest_further.py"""

import os
from subprocess import getstatusoutput, getoutput


prg = './crowsnest_further.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'
template_side = 'Ahoy, Captain, {} {} off the {} bow!'


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
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)
        
        
# --------------------------------------------------
def test_vowel_title():
    """Octopus -> An Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('An', word.title())
        
        
# --------------------------------------------------
def test_consonant_title():
    """Brigantine -> A Brigantine"""
    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title())
        
        
# --------------------------------------------------
def test_larboard():
    """Tests --side argument"""
    word = 'narwhal'
    for side in ['starboard', 'back', 'front']:
        out = getoutput(f'{prg} {word} --side {side}')
        assert out.strip() == template_side.format('a', word, side)
        

# --------------------------------------------------
def test_invalid_names():
    """Tests that invalid words raise a value error"""
    words = ['4dog', '%cat', '.bat', '0mat']
    for word in words:
        out = getoutput(f'{prg} {word}')
        assert 'ValueError' in out
