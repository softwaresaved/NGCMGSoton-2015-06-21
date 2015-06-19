---
layout: page
title: Building programs with Python
subtitle: Command-Line Programs
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> *   Use the values of command-line arguments in a program.
> *   Handle flags and files separately in a command-line program.
> *   Read data from standard input in a program so that it can be used in a pipeline.

The IPython Notebook and other interactive tools are great for prototyping code and exploring data,
but at some point we will want to use our program in a pipeline
or run it in a shell script to process thousands of data files.
In order to do that,
we need to make our programs work like other Unix command-line tools.
For example,
we may want a program that reads a data set
and prints the average inflammation per patient:

~~~
$ python readings.py --mean ../data/inflammation-01.csv
5.45
5.425
6.1
...
6.4
7.05
5.9
~~~

but we might also want to look at the minimum of the first four lines

~~~
$ head -4 ../data/inflammation-01.csv | python readings.py --min
~~~

or the maximum inflammations in several files one after another:

~~~
$ python readings.py --max ../data/inflammation-*.csv
~~~

Our overall requirements are:

1. If no filename is given on the command line, read data from [standard input](../../reference.html#standard-input).
2. If one or more filenames are given, read data from them and report statistics for each file separately.
3. Use the `--min`, `--mean`, or `--max` flag to determine what statistic to print.

To make this work,
we need to know how to handle command-line arguments in a program,
and how to get at standard input.
We'll tackle these questions in turn below.

### Command-Line Arguments

Using the text editor of your choice,
save the following in a text file called `sys-version.py`:

~~~ {.python}
import sys
print 'version is', sys.version
~~~

The first line imports a library called `sys`,
which is short for "system".
It defines values such as `sys.version`,
which describes which version of Python we are running.

~~~ {.output}
2.7.5 (default, Sep  2 2013, 05:24:04) 
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)]
~~~

Here's another script called `argv-list.py` that does something more interesting:

~~~ {.python}
import sys
print 'sys.argv is', sys.argv
~~~

The strange name `argv` stands for "argument values".
Whenever Python runs a program,
it takes all of the values given on the command line
and puts them in the list `sys.argv`
so that the program can determine what they were.
If we run this program with no arguments:

~~~ 
$ python argv-list.py
~~~

~~~ {.output}
sys.argv is ['argv-list.py']
~~~

the only thing in the list is the full path to our script,
which is always `sys.argv[0]`.
If we run it with a few arguments, however:

~~~ 
$ python argv-list.py first second third
~~~
~~~ {.output}
sys.argv is ['argv-list.py', 'first', 'second', 'third']
~~~

then Python adds each of those arguments to that magic list.

With this in hand,
let's build a version of `readings.py` that always prints the per-patient mean of a single data file.
The first step is to write a function that outlines our implementation,
and a placeholder for the function that does the actual work.
By convention this function is usually called `main`,
though we can call it whatever we want:

~~~
$ cat readings-01.py
~~~

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = np.loadtxt(filename, delimiter=',')
    for m in data.mean(axis=1):
        print m
~~~

This function gets the name of the script from `sys.argv[0]`,
because that's where it's always put,
and the name of the file to process from `sys.argv[1]`.
Here's a simple test:

~~~
$ python readings-01.py ../data/inflammation-01.csv
~~~

There is no output because we have defined a function,
but haven't actually called it.
Let's add a call to `main`:

~~~
$ cat readings-02.py
~~~

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = np.loadtxt(filename, delimiter=',')
    for m in data.mean(axis=1):
        print m

main()
~~~

and run that:

~~~
$ python readings-02.py ../data/inflammation-01.csv
~~~

~~~ {.output}
5.45
5.425
6.1
5.9
5.55
6.225
5.975
6.65
6.625
6.525
6.775
5.8
6.225
5.75
5.225
6.3
6.55
5.7
5.85
6.55
5.775
5.825
6.175
6.1
5.8
6.425
6.05
6.025
6.175
6.55
6.175
6.35
6.725
6.125
7.075
5.725
5.925
6.15
6.075
5.75
5.975
5.725
6.3
5.9
6.75
5.925
7.225
6.15
5.95
6.275
5.7
6.1
6.825
5.975
6.725
5.7
6.25
6.4
7.05
5.9
~~~

> ## The Right Way to Do It {.callout}
>
> If our programs can take complex parameters or multiple filenames,
> we shouldn't handle `sys.argv` directly.
> Instead,
> we should use Python's `argparse` library,
> which handles common cases in a systematic way,
> and also makes it easy for us to provide sensible error messages for our users.

