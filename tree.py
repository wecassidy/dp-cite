#!/usr/bin/env python3

"""
Citation tree data structure.
"""

from collections import namedtuple

Node = namedtuple("Node", ("label", "weight", "children"))


def cumulative_weight(node):
    """
    Find the cumulative weight of a node: sum of the node and its
    children's cumulative weights.
    """
    if len(node.children) == 0:
        return node.weight

    return node.weight + sum(map(cumulative_weight, node.children))


def add_cite(node, cite):
    """Add a citation of a node, adjusting weights as necessary"""
    if len(cite) == 0:
        return

    section = cite[0]
    subsections = cite[1:]
    for child in node.children:
        if child.label == section:
            child.weight += 1
            add_cite(child, subsections)
            break
    else:
        new_child = Node(section, 1, [])
        node.children.append(new_child)
        add_cite(new_child, subsections)


def print_tree(node, level=0):
    """Pretty-print a tree"""
    print(
        "{indent}{label}: {weight}".format(
            indent="  " * level, label=node.label, weight=node.weight
        )
    )
    for child in node.children:
        print_tree(child, level + 1)
