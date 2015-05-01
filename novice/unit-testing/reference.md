---
layout: page
title: Python Unit Testing
subtitle: Reference
---

## [Defensive Programming](Defensive.html)

*   Program defensively, i.e., assume that errors are going to arise, and write code to detect them when they do.
*   Put assertions in programs to check their state as they run, and to help readers understand how those programs are supposed to work.
*   Use preconditions to check that the inputs to a function are safe to use.
*   Use postconditions to check that the output from a function is safe to use.
*   Write tests before writing code in order to help determine exactly what that code is supposed to do.
*   Know what code is supposed to do *before* trying to debug it.
*   Make it fail every time.
*   Make it fail fast.
*   Change one thing at a time, and for a reason.
*   Keep track of what you've done.
*   Be humble.


## [Errors and Exceptions](errors.html)

*   Tracebacks can look intimidating, but they give us a lot of useful information about what went wrong in our program, including where the error occurred and what type of error it was.
*   An error having to do with the "grammar" or syntax of the program is called a `SyntaxError`. If the issue has to do with how the code is indented, then it will be called an `IndentationError`.
*   A `NameError` will occur if you use a variable that has not been defined (either because you meant to use quotes around a string, you forgot to define the variable, or you just made a typo).
*   Containers like lists and dictionaries will generate errors if you try to access items in them that do not exist. For lists, this type of error is called an `IndexError`; for dictionaries, it is called a `KeyError`.
*   Trying to read a file that does not exist will give you an `IOError`. Trying to read a file that is open for writing, or writing to a file that is open for reading, will also give you an `IOError`.

