# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as chris:
        now_reading = chris.read()    
    return now_reading


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    return {"as": 10, "would": 20}


file_is = 'story.txt'
about_to_open_and_read_file = read_file_content(file_is)
print(about_to_open_and_read_file)