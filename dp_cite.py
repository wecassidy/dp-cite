#!/usr/bin/env python3

"""
Extract citations from CLST 308 practice cases
"""

import re

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
    yield from re.findall(SUBSECTION_RE, cite)
