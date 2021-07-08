#!/usr/bin/env python
"""
Purpose: Find all unique stems in the dictionary and save them as a file.
"""

import re
        
    
def main():
    """Parse dictionary for unique stems and save them as a file."""
    unique_stems = set()

    pattern = '([^aeiou]*?)([aeoiu].*)'
    with open('../inputs/words.txt') as file:
        for word in file:
            stems = re.findall(pattern, word.lower().rstrip())
            if stems:
                unique_stems.add(stems[0][0])
    
    with open('../inputs/stems.txt', 'w') as file:
        for word in list(sorted(list(unique_stems)))[1:]:
            file.writelines(word+'\n')
    print('Saved words to ../inputs/stems.txt')
    

if __name__ == '__main__':
    main()
