---
layout: page
title: Writing Robust Code and Unit Testing
subtitle: Defensive Programming
minutes: 15
---

We made several mistakes while writing the programs in our first few lessons:

-   Are there still errors lurking in the code we have?
-   How can we guard against introducing new errors in code as we modify it?

<!-- include mention of research into searching for bugs in same place -->

The first step is to use *defensive programming*, i.e., to assume that mistakes *will* happen and to guard against them.

One way to do this is to add *assertions* to our code so that it checks itself as it runs. An assertion is simply a statement that something must be true at a certain point in a program. When Python sees one, it checks that the assertion's condition:

-   If it's true, Python does nothing
-   If it's false, Python halts the program immediately and prints the error message provided

For example, this piece of code halts as soon as the loop encounters a value that isn't positive:

~~~ {.python}
numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    assert n >= 0.0, 'Data should only contain positive values'
    total += n
print 'total is:', total
~~~

~~~ {.output}
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-1-33d87ea29ae4> in <module>()
      2 total = 0.0
      3 for n in numbers:
----> 4     assert n >= 0.0, 'Data should only contain positive values'
      5     total += n
      6 print 'total is:', total

AssertionError: Data should only contain positive values
~~~

Programs like the Firefox browser are littered with assertions: 10-20% of the code they contain are there to check that the other 80-90% are working correctly.

Broadly speaking, assertions fall into three categories:

-   A **precondition** is something that must be true at the start of a function in order for it to work correctly.
-   A **postcondition** is something that the function guarantees is true when it finishes.
-   An **invariant** something that is always true at a particular point inside a piece of code.

For example, suppose we are representing rectangles using a tuple of four coordinates `(x0, y0, x1, y1)`. In order to do some calculations, we need to normalize the rectangle so that it is at the origin and 1.0 units long on its longest axis. This function does that, but checks that its input is correctly formatted and that its result makes sense:

~~~ {.python}
def normalize_rectangle(rect):
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates'
    assert y0 < y1, 'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)
~~~

The preconditions on lines 2, 4, and 5 catch invalid inputs:

~~~ {.python}
print normalize_rectangle( (0.0, 1.0, 2.0) ) # missing the fourth coordinate
~~~

~~~ {.output}
--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-22-3a97b1dcab70> in <module>()
----> 1 print normalize_rectangle( (0.0, 1.0, 2.0) ) # missing the fourth coordinate

<ipython-input-21-fdb49ef456c2> in normalize_rectangle(rect)
      1 def normalize_rectangle(rect):
----> 2     assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
      3     x0, y0, x1, y1 = rect
      4     assert x0 < x1, 'Invalid X coordinates'
      5     assert y0 < y1, 'Invalid Y coordinates'

AssertionError: Rectangles must contain 4 coordinates
~~~

~~~ {.python}
print normalize_rectangle( (4.0, 2.0, 1.0, 5.0) ) # X axis inverted
~~~

~~~ {.output}
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-23-f05ae7878a45> in <module>()
----> 1 print normalize_rectangle( (4.0, 2.0, 1.0, 5.0) ) # X axis inverted

<ipython-input-21-fdb49ef456c2> in normalize_rectangle(rect)
      2     assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
      3     x0, y0, x1, y1 = rect
----> 4     assert x0 < x1, 'Invalid X coordinates'
      5     assert y0 < y1, 'Invalid Y coordinates'
      6 

AssertionError: Invalid X coordinates
~~~

The post-conditions help us catch bugs by telling us when our calculations cannot have been correct. For example, if we normalize a rectangle that is taller than it is wide everything seems OK:

~~~ {.python}
print normalize_rectangle( (0.0, 0.0, 1.0, 5.0) )
~~~

~~~ {.output}
(0, 0, 0.2, 1.0)

~~~

but if we normalize one that's wider than it is tall,
the assertion is triggered:

~~~ {.python}
print normalize_rectangle( (0.0, 0.0, 5.0, 1.0) )
~~~

~~~ {.output}
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-27-5f0ef7954aeb> in <module>()
----> 1 print normalize_rectangle( (0.0, 0.0, 5.0, 1.0) )

<ipython-input-21-fdb49ef456c2> in normalize_rectangle(rect)
     15 
     16     assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
---> 17     assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'
     18 
     19     return (0, 0, upper_x, upper_y)

AssertionError: Calculated upper Y coordinate invalid
~~~

Re-reading our function, we realize that line 10 should divide `dy` by `dx` rather than `dx` by `dy`. (You can display line numbers by typing Ctrl-M, then L.) If we had left out the assertion at the end of the function, we would have created and returned something that looked like a valid answer, but wasn't; detecting and debugging that would almost certainly have taken more time in the long run than writing the assertion.

But assertions aren't just about catching errors: they also help people understand programs. Each assertion gives the person reading the program a chance to check (consciously or otherwise) that their understanding matches what the code is doing.

Most good programmers follow two rules when adding assertions to their code.

- The first is, "**fail early, fail often**". The greater the distance between when and where an error occurs and when it's noticed, the harder the error will be to debug, so good code catches mistakes as early as possible.

- The second rule is, "**turns bugs into assertions or tests**". If you made a mistake in a piece of code, the odds are good that you have made other mistakes nearby, or will make the same mistake (or a related one) the next time you change it. Writing assertions to check that you haven't *regressed* (i.e., haven't re-introduced an old problem) can save a lot of time in the long run,
and helps to warn people who are reading the code (including your future self)
that this bit is tricky.

> ## Challenges {.challenge}
> 
> 1.  Suppose you are writing a function called `average` that calculates the average of the numbers in a list.
>     What pre-conditions and post-conditions would you write for it?
>     Compare your answer to your neighbor's:
>     can you think of a function that will pass your tests but not hers or vice versa?
> 
> 2.  Explain in words what the assertions in this code check,
>     and for each one,
>     give an example of input that will make that assertion fail.
>     
>     ```
>     def running(values):
>         assert len(values) > 0
>         result = [values[0]]
>         for v in values[1:]:
>             assert result[-1] >= 0
>             result.append(result[-1] + v)
>         assert result[-1] >= result[0]
>         return result
>     ```
