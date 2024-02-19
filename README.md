# Melodic language
Translate english to music.

## Here is a sound [sample](https://soundcloud.com/overdance/melodic-language-sample)

### To use it, have python installed and import mido:

```
pip install mido
```

Then run midilang.py file. You can do it in terminal `C:\path\to\files python midilang.py`

# Language chart.

__Eariot__ - [English letter frequency.](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html)

__Tuxvy__ - Letters sorted by shuffling english letter frequency to match [pleasant intervals](https://www.reddit.com/r/musictheory/comments/p9lrbh/i_rank_all_intervals_from_most_to_least_consonant/)

| Number | Semitones | Eariot | Tuxvy |
| -------- | ------- | -------- | ------- |
| 1 | 0 | E | O |
| 2 | 1 up | A | K |
| 3 | 1 down | R | W |
| 4 | 2 up | I | B |
| 5 | 2 down | O | G |
| 6 | 3 up | T | P |
| 7 | 3 down | N | D |
| 8 | 4 up | S | S |
| 9 | 4 down | L | N |
| 10 | 5 up | C | E |
| 11 | 5 down | U | A |
| 12 | 6 up | D | J |
| 13 | 6 down | P | Z |
| 14 | 7 up | M | I |
| 15 | 7 down | H | R |
| 16 | 8 up | G | L |
| 17 | 8 down | B | C |
| 18 | 9 up | F | M |
| 19 | 9 down | Y | H |
| 20 | 10 up | W | F |
| 21 | 10 down | K | Y |
| 22 | 11 up | V | V |
| 23 | 11 down | X | X |
| 24 | 12 up | Z | U |
| 25 | 12 down | J | T |

If you want to extend it, follow the semitone sequence for accurate translation 
example:
| 26 | 13 up | Ę | 
| -------- | ------- | -------- |
| 27 | 13 down | Ą |


## Fun facts
Author hasn't found any existing musical language. So he decided to make one, on his own based on english.
it can be categorized as a Conlang. (language, constructed artificially)
It was created for artistic purposes (for a fantasy world). So subcategory is an Artlang.
It is a Relex -  The constructed language using word for word translation from existing language.

Code made specifically for people to create, and easily translate to music their own languages. Without coding knowledge - You just need to add your conlang dictionary to a [settings](settings.py) file. But first I would recommend to make it in excel.

The list of letters itself can be extended up to 49 Without bugs. Up to 97 with small fixes. 
(So it is possible to literally translate both hiragana and katakana alphabets "Japanese" to sounds with just one dictionary. !Not possible for humans to sing it!)

English has 26 letters, the languages below have 25 because Q and K got merged. Look at [dictionaries](settings.py) To perfectly fit a scale of two octaves (12 semitones up and down). !It is possible to sing it!


