#Intervals -- a programming language for describing music

##What is it?
Intervals is programming language for describing music written in Python that builds on the Mingus library and (optionally) FluidSynth and LilyPond. Intervals gives the composer access to native musical data types, means of combing these datatypes, and a sound and sheet music capable REPL, so as to provide a programming enviro made for music.

A diagram describes the evaluation process:
Intervals composition -> Mingus Python objects -> Midi -> Sound (FluidSynth)
                                                    |
                                                    v
                                              Sheet music (LilyPond)

Note that FluidSynth and/or LilyPond can be replaced with other components that perform similar functions. Imagine controlling Logic Pro with the midi output of an Intervals composition.

This is very much a work in progress right now. More complete documentation to come when the code is further along.

##Copyright
Copyright (c) 2013 Josh Imhoff. See LICENSE for details.
