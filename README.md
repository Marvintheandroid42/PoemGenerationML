# PoemGenerationML

**_About: Using ML to discern the styles of poets through corpus datasets and using sentiment analysis along with syllable and rhyme filters to structure generated lines into poetic forms to generate poems_** 

### Initial Rhyme dictionary example:

'lord': ['Wrong me, noble lord?\n'], 'test': ['Yes, in good test!\n'], 'all': ['The other wore, woe and of you all.\n'], 'me': ["The all suffer'd better to by me\n"], 'own': ['here unto me with a tomb you own\n'], 'woo': ['best now to break the wretch and trial, as he knows woo,\n'], 'much': ['Why, how now, good fellow; how much\n'], 'for': ['How more than history, with a cause for all this issue for\n'], 'fair': ['Sit how the doom of her of it fair.\n'], 'come': ['Nor thine own children; I come\n'], 'leck': ['At face of his proud heart a leck.\n'], 'her': ['To fly two duck content against her.\n'], 'mother': ['Since I am I long as you have a quier mother!\n'],


### Initial Syllable parsing:

[[['Y EH1 S'], ['IH1 N'], ['G IH0 D'], ['T EH1 S T']], [['R AO1 NG'], ['M IY1'], ['N OW1 B AH0 L'], ['L AO1 R D']], [['DH AH1'], ['AH1 DH ER0'], ['W AO1 R'], ['W OW1'], ['AE1 N D'], ['AH1 V'], ['Y UW1'], ['AO1 L']], [['S OW1'], ['M AH1 CH'], ['T IH0'], ['D UW1 M'], ['AH1 V'], ['M IY1']],


*****************************************

## Final Generated Shakespeare Sonnet:

But that I speak thee, nor myself, I say.

Your dicipline in war, wisdom in place; 

Whilst you have fed upon my servant may 

No, good sweet sir; no, I beseech your grace 



To draw the brats of Clarence out of sight; 

How, Phility, hould live, or else a pair 

I am the drudge and toil in your delight, 

Show me a mistress that is passing fair, 



That you do speak to them, nor who is now. 

How say you sing at once chafed, he cannot 

I must confess your offer is the bow;

But for my sister, and I think it not


Your father's image is so hit in you, 

He shor holds and friends: he was ever too

*****************************************

## Dickenson Sonnet 6 syllables per line:

Myself would run away 

The Things that Death will buy 

Jowe so fal far -- today -- 

A something in the sky -- 


Lambs for whon time will come 

Ad period of go! 

A Service, like a Drum -- 

Or Bees, at Christmas show -- 


What ailed so smart a ling -- 

The World that thou hast pain -- 

Bright Wednesd -- to blooms Spring 

Your Problem -- of the Brain -- 


Had God will find it bight 

For newness of the night -- 

****************************

## Shakspeare with sentiment analysis (mean and fit into inequality of greater than 0.7 and lower than -0.01)

### Example 1:

And their true sovereign, whom they must obey?

Your dicipline in war, wisdom in place;

Whilst you have fed upon my servant may

No, good sweet sir; no, I beseech your grace


To draw the brats of Clarence out of sight;

How, Phility, hould live, or else a pair

I am the drudge and toil in your delight,

Show me a mistress that is passing fair,


That you do speak to them, nor who is now
.
How say you sing at once chafed, he cannot

I must confess your offer is the bow;

But for my sister, and I think it not


Your father's image is so hit in you,

He shor holds and friends: he was ever too
 
**SENTIMENT SCORE - 0.8474025974025974**

### Example 2

Go, night, thy soul! there's no no stock and prayer.

Your dicipline in war, wisdom in place;

How, Phility, hould live, or else a pair

No, good sweet sir; no, I beseech your grace


To draw the brats of Clarence out of sight;

That you do speak to them, nor who is now.

I am the drudge and toil in your delight,

I must confess your offer is the bow;


How say you sing at once chafed, he cannot

Your father's image is so hit in you,

But for my sister, and I think it not

He shor holds and friends: he was ever too


She's dead, he's dead, he's changed in hearing we

What art thou the angry Maptation 
 
**SENTIMENT SCORE: -0.4025974025974026**

*********************************

## Dickenson Format of Poems

8686 - syllables
2 and 4 rhyme in quartain
short lines

### Example 1:

A Door just opened on a street -- 

The Bird would not arise -- 

But seemed engrossed to Absolute -- 

And estimate its size --

### Example 2:

My tenderer Experiment 

Is cherished of the Crow 

And period every worn -- 

And Mourners to and fro 

### Example 3:

From allooved I a Butterfly -- 

Lambs for whon time will come 

And whatsoever is consumed 

And Ear -- and Heaven -- numb -- 
