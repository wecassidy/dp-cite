#!/usr/bin/env python3

"""
Citation tree data structure.
"""


class Node:
    """Citation tree with cumulative weights."""

    def __init__(self, label):
        self.label = label
        self.weight = 1
        self.children = []

    def add_cite(self, cite):
        """Add a citation to a node, adjusting weights as necessary"""
        if len(cite) == 0:
            return

        section = cite[0]
        subsections = cite[1:]
        for child in self.children:
            if child.label == section:
                child.weight += 1
                child.add_cite(subsections)
                break
        else:
            new_child = Node(section)
            self.children.append(new_child)
            new_child.add_cite(subsections)

    def individual_weight(self):
        """
        Find number of direct citations of a node. This is the weight
        of a node minus the weight of its children.
        """
        return self.weight - sum(c.weight for c in self.children)

    def __str__(self, level=0):
        """Pretty-print a tree"""
        out = "{indent}{label}: {weight}".format(
            indent="  " * level, label=self.label, weight=self.weight
        )
        for child in self.children:
            out += "\n" + child.__str__(level + 1)

        return out


def test():
    dp = Node("Du Plessis")
    dp.add_cite(["8"])
    dp.add_cite(["7", "3", "2", "ii"])
    dp.add_cite(["7", "3", "3"])
    dp.add_cite(["7", "3", "3"])
    return dp
