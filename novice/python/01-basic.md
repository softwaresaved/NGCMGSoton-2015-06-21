---
layout: page
title: Building programs with Python
subtitle: Python Basics- Variables, Arrays, Lists etc
minutes: 20
---
> ## Learning Objectives {.objectives}
>
> *   Introduction to Python variables
> *   Creating and Assigning values to variables.
> *   Lists and Arrays in Python
> *   Indexing and slicing

A variable is just a name for a value,
such as `x`, `current_temperature`, or `subject_id`.
Python's variables must begin with a letter.
A variable in Python is defined through assignment i.e. we can create a new variable simply by assigning a value to it using `=`.
As an illustration,
consider the simplest "collection" of data,
a single value.
The line below assigns a value to a variable:


~~~ {.python}
weight_kg = 55
~~~

Once a variable has a value, we can print it:

~~~ {.python}
print weight_kg
~~~
~~~ {.output}
55
~~~

and do arithmetic with it:

~~~ {.python}
print 'weight in pounds:', 2.2 * weight_kg
~~~
~~~ {.output}
weight in pounds: 121.0
~~~

We can also change a variable's value by assigning it a new one:

~~~ {.python}
weight_kg = 57.5
print 'weight in kilograms is now:', weight_kg
~~~
~~~ {.output}
weight in kilograms is now: 57.5
~~~

As the example above shows,
we can print several things at once by separating them with commas.

If we imagine the variable as a sticky note with a name written on it,
assignment is like putting the sticky note on a particular value:

![Variables as Sticky Notes](img/python-sticky-note-variables-01.svg)

This means that assigning a value to one variable does *not* change the values of other variables.
For example,
let's store the subject's weight in pounds in a variable:

~~~ {.python}
weight_lb = 2.2 * weight_kg
print 'weight in kilograms:', weight_kg, 'and in pounds:', weight_lb
~~~
~~~ {.output}
weight in kilograms: 57.5 and in pounds: 126.5
~~~

![Creating Another Variable](img/python-sticky-note-variables-02.svg)

and then change `weight_kg`:

~~~ {.python}
weight_kg = 100.0
print 'weight in kilograms is now:', weight_kg, 'and weight in pounds is still:', weight_lb
~~~
~~~ {.output}
weight in kilograms is now: 100.0 and weight in pounds is still: 126.5
~~~

![Updating a Variable](img/python-sticky-note-variables-03.svg)

Since `weight_lb` doesn't "remember" where its value came from,
it isn't automatically updated when `weight_kg` changes.
This is different from the way spreadsheets work.

> ## What's inside the box? {.challenge}
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

> ## Sorting out references {.challenge}
>
> What does the following program print out?
>
> ~~~ {.python}
> first, second = 'Grace', 'Hopper'
> third, fourth = second, first
> print third, fourth
> ~~~

>### Arrays in Python

One of the most fundamental data structures in any language is the array. Python doesn't have 
a native array data structure, but it has the list which is much more general and can be used 
as a multidimensional array quite easily.

>#### List basics

A list in python is just an ordered collection of items which can be of any type. By comparison 
an array is an ordered collection of items of a single type - so a list is more flexible than an 
array.

A list is also a dynamic mutable type and this means we can add and delete elements from the list 
at any time. 

To define a list we simply write a comma separated list of items in square brackets:

>~~~{.python}
>myList = [1,2,3,4,5,6]
>~~~

This looks like an array because we can use *slicing* notation to pick out an individual element - 
indexes start from 0.

>~~~{.python}
> print myList[2]
>~~~

will display the third element, i.e. the value 3 in this case. Similarly to change the third element we can 
assign directly to it:

>~~~{.python}
>myList[2] = 100
>~~~

The *Slicing* notation looks like array indexing but it is a lot more flexible. For example:

>~~~{.python}
>myList[2:5]
>~~~

is a sublist from the third element to the fifth i.e. from `myList[2]` to `myList[4]`. Notice that the 
final element specified i.e. `[5]` is not included in the slice.

Also notice that you can leave out either of the start and end indexes and they will be assumed to have their maximum possible value. 
For example:

>~~~{.python}
>myList[5:]
>~~~

is the list from `myList[5]` to the end of the list and

>~~~{.python}
>myList[:5]
>~~~

is the list up to and not including myList[5] and

>~~~{.python}
>myList[:]
>~~~

is the entire list.

List slicing is more or less the same as string slicing except that we can modify a slice. For example:

>~~~{.python}
>myList[0:2]=[0,1]
>~~~

has the same effect as

>~~~{.python}
>myList[0]=0
>myList[1]=1
>~~~

Finally is it worth knowing that the list we assign to a slice doesn't have to be the same size as the slice - 
it simply replaces it even if it is a different size.

> ## Slicing strings {.challenge}
>
> A section of an array is called a [slice](../../reference.html#slice).
> We can take slices of character strings as well:
>
> ~~~ {.python}
> element = 'oxygen'
> print 'first three characters:', element[0:3]
> print 'last three characters:', element[3:6]
> ~~~
>
> ~~~ {.output}
> first three characters: oxy
> last three characters: gen
> ~~~
>
> What is the value of `element[:4]`?
> What about `element[4:]`?
> Or `element[:]`?
>
> What is `element[-1]`?
> What is `element[-2]`?
> Given those answers,
> explain what `element[1:-1]` does.

> ## Thin slices {.challenge}
>
> The expression `element[3:3]` produces an [empty string](../../reference.html#empty-string),
> i.e., a string that contains no characters.

> ### Basic array operations

So far so good, and it looks as if using a list is as easy as using an array.

Where things start to go wrong just a little is when we attempt to push the similarities 
between lists and arrays one step too far. For example, suppose we want to create an array 
initialised to a particular value. Following the general array idiom in most languages we 
might write:

> ~~~ {.python}
>myList=[]
>for i in range(10):
> myList[i]=1
>~~~

only to discover that this doesn't work because we can't assign to a list element that doesn't already exist.
One solution is to use the append method to add elements one by one:

> ~~~ {.python}
>myList=[]
>for i in range(10):
> myList.append(1)
>~~~

This works but it only works if we need to build up the list in this particular order - which most of the time you do. 
When the same situation arises in two- and multi-dimensioned arrays the problem often isn't as easy to solve with append, 
and there is a better way.

After examining such problems working with lists as arrays, we will proceed to discover the power of the NumPy arrays in next lesson.

> ## Check your understanding {.challenge}
>
> Draw diagrams showing what variables refer to what values after each statement in the following program:
>
> ~~~ {.python}
> mass = 47.5
> age = 122
> mass = mass * 2.0
> age = age - 20
> ~~~

> ## Sorting out references {.challenge}
>
> What does the following program print out?
>
> ~~~ {.python}
> first, second = 'Grace', 'Hopper'
> third, fourth = second, first
> print third, fourth
> ~~~

> ## Slicing strings {.challenge}
>
> A section of an array is called a [slice](../../reference.html#slice).
> We can take slices of character strings as well:
>
> ~~~ {.python}
> element = 'oxygen'
> print 'first three characters:', element[0:3]
> print 'last three characters:', element[3:6]
> ~~~
>
> ~~~ {.output}
> first three characters: oxy
> last three characters: gen
> ~~~
>
> What is the value of `element[:4]`?
> What about `element[4:]`?
> Or `element[:]`?
>
> What is `element[-1]`?
> What is `element[-2]`?
> Given those answers,
> explain what `element[1:-1]` does.


