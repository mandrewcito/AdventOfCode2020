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

#### [Day 7: Handy Haversacks](https://adventofcode.com/2020/day/7)
On the seventh day, i made i mistake, not model problem as a graph initially(with python you can use dict simply) and work with a list. i wasted a lot of time :(. As new funciton of the day added 'any' function.

This function can be used as it follows:

```python
any([True, False, False])
# output: True

any([False, False, False])
# output False
```

* [any](https://docs.python.org/3/library/functions.html#any)

#### [Day 8: Handheld Halting](https://adventofcode.com/2020/day/8)
Day 8, only a path finding was neccesary as new used language features i used 'copy' and 're.findall'.

```python
import copy
sample = [1,3,4,5]
sample_copy = copy.deepcopy(sample)
sample[3] = 99
sample
# output: [1, 3, 4, 99]
sample_copy
# output: [1, 3, 4, 5]
```

```python
import re
re.findall(r"(\w+) ([+-]\d+)", "nop -1")
# output: [('nop', '-1')]
```

* [path finding](https://en.wikipedia.org/wiki/Pathfinding)
* [copy](https://docs.python.org/3/library/copy.html)
* [regex](https://docs.python.org/3/library/re.html)

#### [Day 9: Encoding Error](https://adventofcode.com/2020/day/9)

This day for me was quite easier than the previous day, i didn't nothing special. 'New' language features that i used was 'min', 'max' and a 'shuffle' for testing.

```python
min([2222, 1, 1, 1, 0])
# output: 0

max([2222, 1, 1, 1, 0])
# output: 2222
```

```python
import random
sample = list(range(1, 26))
random.shuffle(sample)
sample
# output: [24, 6, 17, 14, 13, 25, 18, 19, 12, 1, 11, 7, 22, 9, 20, 3, 16, 15, 21, 8, 2, 23, 10, 4, 5]
```

* [max](https://docs.python.org/3/library/functions.html#max)
* [min](https://docs.python.org/3/library/functions.html#min)
* [random](https://docs.python.org/3/library/random.html)

#### [Day 10: Adapter Array](https://adventofcode.com/2020/day/10)

First problem´s part was quite simple but, on second part, i made a recursive function and it took a long time executing. Then i thought: Obviously, thats not the right choice. The result will be a stack overflow if number of choices is big. So here i had two choices:
* First approach: Refactor code as a tail recursion code.
* Second approach: model problem as a dinamic programing problem.

```python
 def get_paths(adapters, current):
    filtered = list(filter(lambda adapter: 0 <= adapter.diff(current) <= 3, adapters))
    values = list(map(lambda x: adapters[adapters.index(x):], filtered))
    return values

def explore_paths(adapters):
    if adapters == []:
        return 1
    adapter = adapters[0]   
    sublists = get_paths(adapters[2:], adapter)
    return explore_paths(adapters[1:]) +\
         sum([explore_paths(sublist_adapters) for sublist_adapters in sublists])
```

```python
def get_jolts_paths(adapters):
    data = collections.defaultdict(int)
    data[0] = 1
    for adapter in adapters: 
        data[adapter.output_joltage] = data[adapter.output_joltage-1] + data[adapter.output_joltage-2] + data[adapter.output_joltage-3] 
    return data[adapters[-1].output_joltage]
```
With previous code we 'store' with voltage index how many paths, take to that node. 

* [dynamic programing](https://en.wikipedia.org/wiki/Dynamic_programming)
* [tail recursion](https://en.wikipedia.org/wiki/Tail_call)

### Once ended ...

All the code, including this post is published in [my github](https://github.com/mandrewcito/AdventOfCode2020)

As a personal recommendation i encourage anybody to participate. I think that this kind of events improve your skills as a developer, and for me was a good way to remember some things that i used to do on my degree but i don't do on day a day work. So this was funny.

Did you participate in AoC2020 or something similar?, feel free to leave any thought below :)