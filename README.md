#Intervals -- a language for describing music

##What is it?
Intervals is written in Python, builing on the Mingus library and (optionally)
FluidSynth and LilyPond, that gives the composer access to native musical data
types, means of combing these datatypes, and a sound and sheet music capable
REPL, so as to provide a programming enviro made for music.

A diagram describes the evaluation process:
Intervals composition -> Python program w/ Mingus -> Midi -> Sound (FluidSynth)
                                                      |
                                                      v
                                                    Sheet music (LilyPond)

Note that FluidSynth and/or LilyPond can be replaced with other components that
perform similar functions. Imagine controlling Logic Pro with the midi output
of an Intervals composition.

I intentionally use the word "composition" to describe an Intervals program,
and the word "program" to describe translated Mingus code. Mingus is a
wonderful library; lots of amount of work has been put into building a correct,
expansive "sense" of music theory into Mingus. Regardless of this, Mingus is 
a pain to use! It is too constrained by Python's syntax to allow a person 
to compose music naturally.

If I want to hear an E5, I should be able to type:
    E5
Not:
    fluidsynth.play_Note(Note("E-5"))

If I want to write a series of notes to MIDI, I should be able to type:
    A C E
Not: 
    nc = NoteContainer(["A", "C", "E"])
    MidiFileOut.write_NoteContainer("test.mid", nc)"
Intervals abstracts away the details.

Intervals compositions are a superset of traditional musical scores. They are 
machine-parsable, human-readable versions of sheet music that evaluate to midi, 
synthesized (or sampled) sound, and standard sheet music.

##Why the hell would I want a text-based Finale?
You wouldn't. Intervals is more than a text-based Finale. One of the main ideas
behind Intervals is to bring the most important Computer Science ideas to the 
field of musical composition.

Intervals implements four key CS ideas:
1. Abstraction
2. Introspection
3. Statistics and AI
4. Turing-complete
5. Non-determinism

##God's greatest gift: abstraction
Rather than writing a composition and then transcribing from key to key, the
Intervals way to do this would be to write your composition *in terms of* a 
tonic (or a set of important notes). The rest of the compostion can be written
in terms of intervalic distances rather than specific notes. In this way, your 
composition can take as input a key and give as ouput some particular version 
of the composition.

Rather than writing a chorus and then copying that chorus to a later part of 
the song, the Intervals way of doing this would be to abstract away the chorus
as a function (possibly with parameters) and call it again later. Copy and 
paste is evil!

Intervals calls functions "themes" and even support higher-order themes.

##If its based on Python, it better support introspection!
Agreed. Introspection is especially important in the case of a musical
programming language because we want to be able to analysize existing music's 
chord structures, intervalic distances, and more.

##Statical tables and models built in?
Based on introspection queries, Intervals can calculate descriptive statistics 
about a composition. What is cooler is that Intervals can even create 
statistical models (via Pandas) of compositions or sets of compositions. 
Imagine a Markov process or neural network that guesses what note you are 
about to choose based on your past compositions!

##Is it Turing-complete?
Of course. Because the Intervals interpreter is coded in Python, I have given 
an Intervals composer full access to the power of the Python language at all 
times. In-line Python is the most important features because it keeps 
Intervals from being limited from what the language designer can think of!

Imagine the possibilities: 
1. A composer can "non-deterministically" choose notes based on the output of 
the random module.
2. He can select the appropriate key based on a http request to weather.com
3. He can create music that

##Sweet Jesus, what do you mean Intervals is non-deterministic?
It is not as scary as it sounds. Intervals allows the composer to describe
a set of possible choices for a pitch, note, or even meter, rather than one
determinstic choice. An Intervals composer would never actually implement 1 
from the previous section via in-line Python because this functionality is 
built into Intervals.

Intervals will try all possible musical paths, but it will stop composing if
one of the paths results in a composition that doesn't make musical-sense. 
Intervals has a very liberal defintion of musical sense -- it is not some kind
of theory-Nazi -- but if a compostion's meter is 4/4 and a path of computation
chooses a bar with five whole notes in it, Intervals will backtrack as it 
should.

##Let's see some examples

##Copyright
Copyright (c) 2013 Josh Imhoff. See LICENSE for details.
