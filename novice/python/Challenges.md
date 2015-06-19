---
layout: page
title: Building programs with Python
subtitle: Challenges
---

>## Python basics: Variables, Arrays, Lists etc

> #### What's inside the box? {.challenge}
>
> Draw diagrams showing what variables refer to what values after each statement in the following program:
>
> ~~~ {.python}
> weight = 70.5
> age = 35
> # Take a trip to the planet Neptune
> weight = weight * 1.14
> age = age + 20
> ~~~

> #### Sorting out references {.challenge}
>
> What does the following program print out?
>
> ~~~ {.python}
> first, second = 'Grace', 'Hopper'
> third, fourth = second, first
> print third, fourth
> ~~~

> #### Slicing strings {.challenge}
>
> A section of an array is called a [slice](../../reference.html#slice).
> We can take slices of character strings as well:
>
> ~~~ {.python}
> element = 'oxygen'
> print 'first three characters:', element[0:3]
> print 'last three characters:', element[3:6]
> ~~~

> What is the value of `element[:4]`?
> What about `element[4:]`?
> Or `element[:]`?
>
> What is `element[-1]`?
> What is `element[-2]`?
> Given those answers,
> explain what `element[1:-1]` does.

>## Using libraries

> #### Thin slices {.challenge}
>
> From our previous topic challenges, the expression `element[3:3]` produces an [empty string](../../reference.html#empty-string),
> i.e., a string that contains no characters.
> If `data` holds our array of patient data,
> what does `data[3:3, 4:4]` produce?
> What about `data[3:3, :]`?

>## Visualising data using libraries

> #### Make your own plot {.challenge}
>
> Create a plot showing the standard deviation of the inflammation data for each day across all patients.
> Hint: `data.std(axis=0)` gives you standard deviation.

>## Loops

> #### From 1 to N {.challenge}
>
> Python has a built-in function called `range` that creates a list of numbers:
> `range(3)` produces `[0, 1, 2]`, `range(2, 5)` produces `[2, 3, 4]`.
> Using `range`,
> write a loop that uses `range` to print the first 3 natural numbers:
>
> ~~~ {.python}
> 1
> 2
> 3
> ~~~

>## Making choices

> #### How many paths? {.challenge}
> 
> Which of the following would be printed if you were to run this code? Why did you pick this answer?
>
> A
> B
> C
> B and C
> 
> ~~~ {.python}
> if 4 > 5:
>     print 'A'
> elif 4 =< 5:
>     print 'B'
> elif 4 < 5:
>     print 'C'
> ~~~

> #### What is truth? {.challenge}
>
> `True` and `False` aren't the only values in Python that are true and false.
> In fact, *any* value can be used in an `if` or `elif`.
> After reading and running the code below,
> explain what the rule is for which values are considered true and which are considered false.
> (Note that if the body of a conditional is a single statement, we can write it on the same line as the `if`.)
>
> ~~~ {.python}
> if '': print 'empty string is true'
> if 'word': print 'word is true'
> if []: print 'empty list is true'
> if [1, 2, 3]: print 'non-empty list is true'
> if 0: print 'zero is true'
> if 1: print 'one is true'
> ~~~


