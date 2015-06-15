---
layout: page
title: Building programs with Python
subtitle: Creating Functions
minutes: 20
---
> ## Learning Objectives {.objectives}
>
> *   Define a function that takes parameters.
> *   Return a value from a function.
> *   Test and debug a function.
> *   Set default values for function parameters.
> *   Explain why we should divide programs into small, single-purpose functions.

At this point,
we've written code to draw some interesting features in our inflammation data,
loop over all our data files to quickly draw these plots for each of them,
and have Python make decisions based on what it sees in our data.
But, our code is getting pretty long and complicated;
what if we had thousands of datasets,
and didn't want to generate a figure for every single one?
Commenting out the figure-drawing code is a nuisance.
Also, what if we want to use that code again,
on a different dataset or at a different point in our program?
Cutting and pasting it is going to make our code get very long and very repetetive,
very quickly.
We'd like a way to package our code so that it is easier to reuse,
and Python provides for this by letting us define things called 'functions' -
a shorthand way of re-executing longer pieces of code.

Let's start by defining a function `fahr_to_kelvin` that converts temperatures from Fahrenheit to Kelvin:

~~~ {.python}
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15
~~~

The definition opens with the word `def`,
which is followed by the name of the function
and a parenthesized list of parameter names.
The [body](../../reference.html#function-body) of the function --- the
statements that are executed when it runs --- is indented below the definition line,
typically by four spaces.

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a [return statement](../../reference.html#return-statement) to send a result back to whoever asked for it.

Let's try running our function.
Calling our own function is no different from calling any other function:

~~~ {.python}
print 'freezing point of water:', fahr_to_kelvin(32)
print 'boiling point of water:', fahr_to_kelvin(212)
~~~
~~~ {.output}
freezing point of water: 273.15
boiling point of water: 273.15
~~~

We've successfully called the function that we defined,
and we have access to the value that we returned.
Unfortunately, the value returned doesn't look right.
What went wrong?

### Debugging a Function

*Debugging* is when we fix a piece of code
that we know is working incorrectly.
In this case, we know that `fahr_to_kelvin`
is giving us the wrong answer,
so let's find out why.

For big pieces of code,
there are tools called *debuggers* that aid in this process.
Since we just have a short function,
we'll debug by choosing some parameter value,
breaking our function into small parts,
and printing out the value of each part.

~~~ {.python}
# We'll use temp = 212, the boiling point of water, which was incorrect
print "212 - 32:", 212 - 32
~~~
~~~ {.output}
212 - 32: 180
~~~

~~~ {.python}
print "(212 - 32) * (5/9):", (212 - 32) * (5/9)
~~~
~~~ {.output}
(212 - 32) * (5/9): 0
~~~

Aha! The problem comes when we multiply by `5/9`.
This is because `5/9` is actually 0.

~~~ {.python}
5/9
~~~
~~~ {.output}
0
~~~

Computers store numbers in one of two ways:
as [integers](../../reference.html#integer)
or as [floating-point numbers](../../reference.html#floating-point-number) (or floats).
The first are the numbers we usually count with;
the second have fractional parts.
Addition, subtraction and multiplication work on both as we'd expect,
but division works differently.
If we divide one integer by another,
we get the quotient without the remainder:

~~~ {.python}
print '10/3 is:', 10/3
~~~
~~~ {.output}
10/3 is: 3
~~~

If either part of the division is a float,
on the other hand,
the computer creates a floating-point answer:

~~~ {.python}
print '10.0/3 is:', 10.0/3
~~~
~~~ {.output}
10.0/3 is: 3.33333333333
~~~

The computer does this for historical reasons:
integer operations were much faster on early machines,
and this behavior is actually useful in a lot of situations.
It's still confusing,
though,
so Python 3 produces a floating-point answer when dividing integers if it needs to.
We're still using Python 2.7 in this class,
though,
so if we want `5/9` to give us the right answer,
we have to write it as `5.0/9`, `5/9.0`, or some other variation.

Another way to create a floating-point answer
is to explicitly tell the computer that you desire one.
This is achieved by [casting](../../reference.html#typecast) one of the numbers:

~~~ {.python}
print 'float(10)/3 is:', float(10)/3
~~~
~~~ {.output}
float(10)/3 is: 3.33333333333
~~~

The advantage to this method is it can be used with existing variables.
Let's take a look:

~~~ {.python}
a = 10
b = 3
print 'a/b is:', a/b
print 'float(a)/b is:', float(a)/b
~~~
~~~ {.output}
a/b is: 3
float(a)/b is: 3.33333333333
~~~

Let's fix our `fahr_to_kelvin` function with this new knowledge:

~~~ {.python}
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5.0/9.0)) + 273.15

print 'freezing point of water:', fahr_to_kelvin(32)
print 'boiling point of water:', fahr_to_kelvin(212)
~~~
~~~ {.output}
freezing point of water: 273.15
boiling point of water: 373.15
~~~

### Composing Functions

Now that we've seen how to turn Fahrenheit into Kelvin,
it's easy to turn Kelvin into Celsius:

~~~ {.python}
def kelvin_to_celsius(temp):
    return temp - 273.15

print 'absolute zero in Celsius:', kelvin_to_celsius(0.0)
~~~
~~~ {.output}
absolute zero in Celsius: -273.15
~~~

What about converting Fahrenheit to Celsius?
We could write out the formula,
but we don't need to.
Instead,
we can [compose](../../reference.html#function-composition) the two functions we have already created:

~~~ {.python}
def fahr_to_celsius(temp):
    temp_k = fahr_to_kelvin(temp)
    result = kelvin_to_celsius(temp_k)
    return result

print 'freezing point of water in Celsius:', fahr_to_celsius(32.0)
~~~
~~~ {.output}
freezing point of water in Celsius: 0.0
~~~

This is our first taste of how larger programs are built:
we define basic operations,
then combine them in ever-large chunks to get the effect we want.
Real-life functions will usually be larger than the ones shown here --- typically half a dozen to a few dozen lines --- but
they shouldn't ever be much longer than that,
or the next person who reads it won't be able to understand what's going on.
