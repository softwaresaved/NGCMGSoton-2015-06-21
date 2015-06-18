---
layout: slides
title: Writing Robust Code and Unit Testing
subtitle: Why do it?
---

## So far...

- Have introduced the basic tools of programming
- But how do we know a program gives the right answer?

- We need to
    + write programs that check their own operation
    + write tests to catch the mistakes those self-checks miss


## Confess!

Why don't you write tests?

- "I don't write buggy code"
- "It's too hard"
- "It's not interesting"
- "It takes too much time and I've research to do"


## Ariane 5

- Ariane 5 used Ariane 4 code
- Ariane 5’s faster engines caused buffer overflow
- Buffer overflow caused Ariane 5 to explode!
- Unfortunately, code wasn't properly tested

Millions of pounds down the drain, some very red faces


## Consider Geoffrey Chang...

- Dept. of Molecular Biology, Scripps Institute
- 5th Annual Presidential Early Career Awards, 2000
- Beckerman Foundation Young Investigator Award, 2001 

Three pharma publications in *Science*, 2001-2005

Letters – Retraction, Science 22 December 2006


## And he's not alone...

- “A Test of Corrections for Extraneous Signals in Gridded Surface Temperature Data”, R. McKitrick et al, Climate Research, 2004
    + “McKitrick screws up yet again”, T. Lambert’s blog
    + “McKitrick mucks it up”, J. Quiggin’s blog

“ERRATUM”, Climate Research, 2004

- “formula for computing cosine of absolute latitude … takes the angle in *radians*, but our data were entered in *degrees*”


## What testing gives you

- Confidence that your code does what it is supposed to
    + That your research is built on a solid foundation
- Ability to detect, and fix, bugs more quickly
- Confidence to refactor or fix bugs without creating new bugs
- Examples of how to use your code
- “if it’s not tested, it’s broken”
    + bittermanandy, 10/09/2010

## Learning Objectives

> * how to write code defensively to guard against making errors;
> * how to use a unit testing framework;
> * when it's useful to write tests *before* writing code.
> * how Python reports and handles errors;
