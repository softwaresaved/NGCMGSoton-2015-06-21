#!/usr/bin/python

def running(values):
   result = []
   lastval = 0
   for v in values:
      count = v + lastval
      lastval = v
      result.append(count)
   return result
