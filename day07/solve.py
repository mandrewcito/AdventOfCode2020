import os
import re
from dataclasses import dataclass

@dataclass
class Bag(object):
    color: str
    children: list = None
    slots: int = None

def get_lines(file_path):
    with open(file_path) as fh:
        def map_bag(line):
            line = line.split("contain")
            children = line[1].split(",")
            
            if "no other bags" not in line[1]:
                children = [Bag(
                    slots=int(child.strip()[0]),
                    color=child[2:].replace(".", "").replace("bags", "").replace("bag", "").strip()) for child in children]
            else:
                children = []
            return Bag(
                color=line[0].replace("bags", "").strip(),
                children=children)
        return [ map_bag(line.strip()) for line in fh.readlines()]


example_bags = get_lines("day07/example")
input_bags = get_lines("day07/input")

def bags_containing(bags, colors):
    children_colors = lambda bag: list(map(lambda child: child.color, bag.children))
    containing = list(filter(lambda bag: any([color in children_colors(bag) for color in colors]), bags))
    not_containing = list(filter(lambda bag: not any([color in children_colors(bag) for color in colors]), bags))
    return (containing, not_containing)

def bag_can_contains(bags, colors):
    bags = list(filter(lambda bag: bag.children is not None and len(bag.children) > 0, bags)) # Only bags with children
    directly, remaining = bags_containing(bags, colors)
    if len(directly) == 0:
        return []
    bag_results = directly + bag_can_contains(remaining, [ bag.color for bag in directly])
    return bag_results

print(bag_can_contains(example_bags, "shiny gold"))

assert 4 == len(bag_can_contains(example_bags, ["shiny gold"]))
input_containing = len(bag_can_contains(input_bags, ["shiny gold"]))

print(f"Sol 1: {input_containing}")

def bag_amount(bags, color):
    data = {bag.color: bag for bag in bags}
    return 0 if color not in data else sum(
        [
            bag.slots +
            bag.slots * bag_amount(bags, bag.color)
            for bag in data[color].children if data[color].children is not None])
    
assert 32 == bag_amount(example_bags, "shiny gold")

example_bags2 = get_lines("day07/example2")
assert 126 == bag_amount(example_bags2, "shiny gold")

input_amount = bag_amount(input_bags, "shiny gold")
print(f"Sol 2: {input_amount}")