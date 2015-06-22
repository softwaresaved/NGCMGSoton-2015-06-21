#!/usr/bin/python

def something(items):
    result = []
    for i in range(len(items)):
       for j in range(i+1, len(items)):
           result.append((items[i], items[j]))
    return result
