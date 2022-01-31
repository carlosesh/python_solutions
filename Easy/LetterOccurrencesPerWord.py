import unittest

"""
Letter Occurrences Per Word

Create a function that takes in a sentence and a character to find.
Return a dictionary of each word in the sentence, with the number
of the specified character as the value.

Examples
find_occurrences("Hello World", "o") ➞ {
  "hello" : 1,
  "world" : 1
}

find_occurrences("Create a nice JUICY function", "c") ➞  {
  "create" : 1,
  "a" : 0,
  "nice" : 1,
  "juicy" : 1,
  "function" : 1
}

find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A") ➞ {
  "an" : 1,
  "apple" : 1,
  "a" : 1,
  "day" : 1,
  "keeps" : 0,
  "archeologist" : 1,
  "away..." : 2
}

Notes
* The function shouldn't be case sensitive.
* Words in the dictionary should be in lowercase.
* You may be required to find punctuation.
* Duplicate words should be ignored (see example #3 for the word "an").
"""

def find_occurrences(txt, ch):
    occurrences = {}

    # populate dictionary
    for i in txt.lower().split():
        if i not in occurrences:
            occurrences[i] = (0)

    for k, v in occurrences.items():
        lower_ch = ch.lower()
        if lower_ch in k:
            occurrences[k] = occurrences.get(k) + k.count(lower_ch)

    return occurrences


class LetterOccurrencesPerWord(unittest.TestCase):
    def test_find_occurrences(self):
        self.assertEqual(find_occurrences("Hello World", "o"), {
        	"hello" : 1,
        	"world" : 1
        })
        self.assertEqual(find_occurrences("Create a nice JUICY function", "c"),  {
        	"create" : 1,
        	"a" : 0,
        	"nice" : 1,
        	"juicy" : 1,
        	"function" : 1
        })
        self.assertEqual(find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "a"), {
        	"an" : 1,
        	"apple" : 1,
        	"a" : 1,
        	"day" : 1,
        	"keeps" : 0,
        	"archeologist" : 1,
        	"away..." : 2
        })
        self.assertEqual(find_occurrences("hello people of the planet Earth", "g"), {"hello": 0, "people": 0, "of": 0, "the": 0, "planet": 0, "earth": 0})
        self.assertEqual(find_occurrences("Reference site about Lorem Ipsum, giving information on its origins, as well as a random Lipsum generator.", "R"), {"reference": 2, "site": 0, "about": 0, "lorem": 1, "ipsum,": 0, "giving": 0, "information": 1, "on": 0, "its": 0, "origins,": 1, "as": 0, "well": 0, "a": 0, "random": 1, "lipsum": 0, "generator.": 2})
        self.assertEqual(find_occurrences("Lift your spirits with funny jokes, trending memes, entertaining gifs, inspiring stories,", "l"), {"lift": 1, "your": 0, "spirits": 0, "with": 0, "funny": 0, "jokes,": 0, "trending": 0, "memes,": 0, "entertaining": 0, "gifs,": 0, "inspiring": 0, "stories,": 0})
        self.assertEqual(find_occurrences("Thats not a camel, thats my wife.", "a"), {"thats": 1, "not": 0, "a": 1, "camel,": 1, "my": 0, "wife.": 0})
        self.assertEqual(find_occurrences("hippopotomonstrosesquippedaliophobia is the fear of long words", "p"), {"hippopotomonstrosesquippedaliophobia": 6, "is": 0, "the": 0, "fear": 0, "of": 0, "long": 0, "words": 0})
        self.assertEqual(find_occurrences("Some writers believe longs sentences are simply made by coupling clauses with the word and. This is called polysyndeton, and yes, it is one of twelve literary devices you can use to take charge of your boring writing. But its a cheap way to get a long sentence.", "s"), {"some": 1, "writers": 1, "believe": 0, "longs": 1, "sentences": 2, "are": 0, "simply": 1, "made": 0, "by": 0, "coupling": 0, "clauses": 2, "with": 0, "the": 0, "word": 0, "and.": 0, "this": 1, "is": 1, "called": 0, "polysyndeton,": 1, "and": 0, "yes,": 1, "it": 0, "one": 0, "of": 0, "twelve": 0, "literary": 0, "devices": 1, "you": 0, "can": 0, "use": 1, "to": 0, "take": 0, "charge": 0, "your": 0, "boring": 0, "writing.": 0, "but": 0, "its": 1, "a": 0, "cheap": 0, "way": 0, "get": 0, "long": 0, "sentence.": 1})
        self.assertEqual(find_occurrences("i wrote code to give me these long long long long long sentences", "l"), {"i": 0, "wrote": 0, "code": 0, "to": 0, "give": 0, "me": 0, "these": 0, "long": 1, "sentences": 0})
        self.assertEqual(find_occurrences("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa a spider", "a"), {"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa": 133, "a": 1, "spider": 0})
        self.assertEqual(find_occurrences("she sell sea shells on the sea shore", "s"), {"she": 1, "sell": 1, "sea": 1, "shells": 2, "on": 0, "the": 0, "shore": 1})
        self.assertEqual(find_occurrences("Woah, I just realised, that I could, use this, to find, punctuation also.", ","), {"woah,": 1, "i": 0, "just": 0, "realised,": 1, "that": 0, "could,": 1, "use": 0, "this,": 1, "to": 0, "find,": 1, "punctuation": 0, "also.": 0})


if __name__ == '__main__':
    unittest.main()
