#!/usr/bin/env python3

"""
Extract citations from CLST 308 practice cases
"""

import argparse
import re

import docx2txt

import tree

CITE_RE = r"\d+(?:\.\w+)+(?:\(\w+\))*"  # Match the reasonable 8.3.2(c)(ii) and the abomination 8.3.2.c.ii
SUBSECTION_RE = r"\b\w+\b"  # Match subsections in a citation


def find_citations(text):
    """Given the text of a word document, extract citations from it (as strings)."""
    text = text.lower()  # normalize
    yield from re.findall(CITE_RE, text)


def citation_sections(cite):
    """
    Given a string citation, process to an sequence of subsection numbers.

    For example, `citation_sections("8.7.3(b)") -> ["8", "7", "3", "b"]`
    """
    return re.findall(SUBSECTION_RE, cite)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("docs", nargs="+", help="List of documents to scrape")
    args = parser.parse_args()

    dp = tree.Node("", "")
    for doc in args.docs:
        text = docx2txt.process(doc)
        citations = map(citation_sections, find_citations(text))
        for c in citations:
            dp.add_cite(c)

    print("Section\t\tDirect\tCumulative")
    for sec in reversed(dp.flatten(tree.by_cumulative)):
        print("{}\t\t{}\t{}".format(sec.cite, sec.individual_weight(), sec.weight))
