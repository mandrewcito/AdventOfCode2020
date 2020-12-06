import os
from functools import reduce
from dataclasses import dataclass

@dataclass
class Group(object):
    people: list

    def get_unique_responses(self):
        responses = reduce(lambda x, y: x + y, map(lambda z: z.response, self.people))
        return list(set(responses))
    
    def all_aswered_yes(self):
        response = self.people[0].response
        responses = [
            1
            if all(map(lambda response: letter in response, map(lambda x: x.response, self.people)))
            else 0 for letter in response]
        return sum(responses)

    def answered_yes(self):
        return len(self.get_unique_responses())
    
    def answered_no(self):
        return 26 - self.answered_yes()

@dataclass
class Person(object):
    response: str

@dataclass
class Plane(object):
    groups: list

def get_lines(file_path):
    with open(file_path) as fh:
        people = []
        person = Person(response=fh.readline().strip())
        current_line = person.response
        while len(current_line) != 0:
            if current_line == "\n":
                yield Group(people=people)
                people = []
            else:
                person = Person(response=current_line.strip())
                people.append(person)
            current_line = fh.readline()
        yield Group(people=people)

example = Group(people=[Person(response="abcx"), Person(response="abcy"), Person(response="abcz")])

def check_responses(responses, group_responses):
    for letter in responses:
        assert letter in group_responses

check_responses(["a", "b", "c", "x", "y", "z"],  example.get_unique_responses())

def check_group(responses, size, group):
    check_responses(responses, group.get_unique_responses())
    assert size == len(group.people)

example_groups = list(get_lines("day06/example"))
input_groups = list(get_lines("day06/input"))

check_group("abc", 1, example_groups[0])
check_group("abc", 3, example_groups[1])
check_group("abc", 2, example_groups[2])
check_group("a", 4, example_groups[3])
check_group("b", 1, example_groups[4])

assert 11 == sum([y.answered_yes() for y in example_groups])

respones = sum([group.answered_yes() for group in input_groups])

print(f"Sol 1: {respones}")

assert 6 == sum([group.all_aswered_yes() for group in example_groups])

respones = sum([group.all_aswered_yes() for group in input_groups])

print(f"Sol 2: {respones}")