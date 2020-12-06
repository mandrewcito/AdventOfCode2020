---
title: Advent of code 2020: A retrospective
published: false
description: A couple of things about my AoC2020 implementations
tags: AdventOfCode, python
cover_image: https://www.hindustantimes.com/rf/image_size_444x250/HT/p2/2020/01/13/Pictures/_67acd868-35de-11ea-bb16-55584621af3a.jpg
---

This year, encouraged by @fynardo i decided to participate in AoC 2020. Current post will be a retrospective about my AoC implementations language specific and non language specific. I will write about algorithms, patterns and data structures that was usefull during this month.

During this month?. Yes, AoC is an advent calendar so there will be a few of implementations here.


####  [Day 1: Report Repair](https://adventofcode.com/2020/day/1)

First problem was simple, i solved it filter function. Filter is a function that applies a function to each element of the list. If the result is true this element it will be included on the resulting list.

```python
my_list = [2,3,4,5,5,7]
filtered_list = list(filter(lambda x: x == 5, my_list))
# filtered_list: [5, 5]
```

* [filter](https://docs.python.org/3/library/functions.html#filter)

####  [Day 2: Password Philosophy](https://adventofcode.com/2020/day/2)
On the second day, splitting lines, counting elements was necessary. Both are commonly used, a few of examples:

```python
"abc:abc".split(":")
# output: ["abc", "abc"] 
"abc:abc".count("ab")
# output: 2
```

I also used XOR opperand, that is not freccuenly used. The statement is true if and only if one is true and the other is false.

```python
True ^ True 
# output: False
True ^ False 
# output: True
False ^ True 
# output: True
False ^ False
# output: False
```

* [list operations](https://docs.python.org/3/tutorial/datastructures.html)
* [XOR](https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations)

####  [Day 3: Toboggan Trajectory](https://adventofcode.com/2020/day/3)

Third day, i didnt used some complex operator,  i could solve problems with list functions. In the third problem i used 'map' and 'reduce' operands.

Map applies a function to each element of the list transforming all the list elements, in the example i will apply ord element to each element of the following list:

```python
list(map(ord, ["a", "b", "c"]))
# output: [97, 98, 99]
```

I also used 'reduce' operand, that is an operand that reduces a list applying an function in fact, python operand sum() is a concrete 'reduce' operand:

```python
from functools import reduce
sum([1, 2, 3, 4, 5, 6]) == reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6])
# Reduce is working as follows:
# 1 + 2
# 3 + 3
# 6 + 4
# 10 + 5
# 15 + 6
# 21
```

* [map](https://docs.python.org/3/library/functions.html#map)
* [reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

####  [Day 4: Passport Processing](https://adventofcode.com/2020/day/4)

With this solution i´m not happier at all, it could be done better, but it is solved ¯\_(ツ)_/¯.

This day i used, dataclasses, classmethods for validations and regex. I mapped input lines to an dictionary and used this dictionary to create class with dataclass.

```python
from dataclasses import dataclass

@dataclass
class A(object):
    b:str
    c:int

dt = {"b": "something", "c": 12}

A(**dt)
# output: A(b='something', c=12)
```

```python
import re
re.match("#[0-9]{2}$", "123")
# output: None
re.match("#[0-9]{2}$", "#123")
# output: None
re.match("#[0-9]{2}$", "#12")
# output: <re.Match object; span=(0, 3), match='#12'>
```

* [classmethods](https://docs.python.org/3/library/functions.html#classmethod)
* [dataclasses](https://docs.python.org/3/library/dataclasses.html)
* [regex](https://docs.python.org/3/library/re.html)

####  [Day 5: Binary Boarding](https://adventofcode.com/2020/day/5)

In this case i didn't use something 'code related'. This problems seemed to me a case of [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm). So i model plane seats as an array and searched into it.

* [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm)

#### [Day 6: Custom Customs](https://adventofcode.com/2020/day/6)

I used a lot of previously described operands like 'reduce', 'map' and 'sum'. In fact i only used a 'new' operand. This operand was 'all', that is a kind of 'reduce' applied with a boolean operator (an and operator).

```python
all([True, False, True])
# output: False
all([True, True, True])
# output: True
```

* [all](https://docs.python.org/3/library/functions.html#all)