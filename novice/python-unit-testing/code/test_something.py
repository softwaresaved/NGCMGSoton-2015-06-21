from something import something

def test_empty():
   assert something([]) == []

def test_single_value():
   assert something(['a']) == []

def test_two_values():
   assert something(['a', 'b']) == [('a', 'b')]

def test_three_values():
   assert something(['a', 'b', 'c']) == [('a', 'b'), ('a', 'c'), ('b', 'c')]
