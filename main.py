# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from collections import defaultdict
import re

def read_file_content(filename):
    with open(filename) as chris:
        now_reading = chris.read()    
    return now_reading


def count_words():
    text = read_file_content("./story.txt")
    counts = defaultdict(int)
    for a_text in re.findall('\w+', text):
        counts[a_text] += 1
    return counts


file_is = 'story.txt'
about_to_open_and_read_file = read_file_content(file_is)
print(count_words())
