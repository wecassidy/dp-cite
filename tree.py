#!/usr/bin/env python3

"""
Citation tree data structure.
"""


class Node:
    """Citation tree with cumulative weights."""

    def __init__(self, label, cite):
        self.label = label
        self.cite = cite
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
            new_child = Node(section, rebuild_cite(self.cite, section))
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
            indent="  " * level, label=self.cite, weight=self.weight
        )
        for child in self.children:
            out += "\n" + child.__str__(level + 1)

        return out

    def flatten(self, key):
        lst = [self]
        for child in self.children:
            lst.extend(child.flatten(key))
        return sorted(lst, key=key)


def rebuild_cite(supersection, subsection):
    if supersection == "":
        return subsection
    elif subsection.isnumeric():
        return supersection + "." + subsection
    else:
        return supersection + "(" + subsection + ")"


def by_cumulative(node):
    return node.weight


def by_direct(node):
    return node.individual_weight()


def test():
    dp = Node("", "")
    dp.add_cite(["8"])
    dp.add_cite(["7", "3", "2", "ii"])
    dp.add_cite(["7", "3", "3"])
    dp.add_cite(["7", "3", "3"])
    return dp
