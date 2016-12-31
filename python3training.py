"""lab01_review_alt.py

This program reads all of the words defined in the file words.txt and
creates a dictionary using each word as the key with an initial value of
zero.  It then reads in the entire book, "Alice in Wonderland,"
replaces all of the punctuation with either a space or a null character
and then splits on whitespace to isolate each word as an entry in a
list.  Then it proceeds to compare each word to the contents of the
dictionary keeping a count of each occurrence of each word that is used.
If a word isn't found, it is appended to a list of unfound words.  At
the end it calculates and prints the percentage of dictionary words that
were used in the book, the word that was used the most along with the
number of occurrences and finally, it removes the duplicates from the
unfound words list and prints the result.

The differences here are that the newer method of formatting is used,
the highest-used word is found by sorting the unloaded/zipped dictionary
and the number of unused words is found by counting the zeros in the
unloaded values of the dictionary
"""

from string import punctuation

words = {}  # Dictionary for all the words in words.txt
# fin = open('c:/pydata/words.txt', 'r')
fin = open('/home/student/pydata/words.txt', 'r')
for word in fin.read().splitlines():
    words[word] = 0  # initialize all dictionary counters to zero
print('Words in dictionary - {0:,d}'.format(len(words)))
fin.close()

unfound_words = []  # List to keep words not located in dictionary.
# fin = open('c:/pydata/alice_in_wonderland.dat', 'r')
fin = open('/home/student/pydata/alice_in_wonderland.dat', 'r')
bookin = fin.read().lower()  # read in the entire book and lower the case
fin.close()
for i in punctuation:
    if i == "'":  # Replace all puctuation with spaces except
        bookin = bookin.replace(i, '')  # apostrophes
    else:
        bookin = bookin.replace(i, ' ')
wordlist = bookin.split()
print('Words in book - {0:,d}'.format(len(wordlist)))
for word in wordlist:
    if word in words:
        words[word] += 1  # If found, increment counter, otherwise
    else:
        unfound_words.append(word)  # add to list of unfound words
wordlist2 = sorted(zip(words.values(), words.keys()))
max_times, max_word = wordlist2[-1]

# Calculate the percentage of dictionary words used in the book.
unused_words = list(words.values()).count(0)  # number of words with a zero count
print('Percentage of dictionary words used in the book is {0:.2%}'.format(
    float(len(words) - unused_words) / len(words)))
print('The word "{0}" was the most frequently used at {1:,d} times'.format(
    max_word, max_times))
# Remove duplicates from unfound list and sort the result
unique_unfound = sorted(set(unfound_words))
print('Number of book words not found in the dictionary -', len(unique_unfound))
nuline = 0
# Print each word left justified in 13 character spaces, and
# put five words on a line.
print('\n', 'Unfound Words'.center(60), '\n')
for word in unique_unfound:
    print('{0:13s}'.format(word), end=' ')
    nuline += 1
    if nuline >= 5:
        nuline = 0
        print()

print("\n\nWe're done!")


