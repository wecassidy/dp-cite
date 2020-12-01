#!/usr/bin/env python3

"""
Extract citations from CLST 308 practice cases
"""

import re

CITE_RE = r"\d+(?:\.\w+)+(?:\(\w+\))*"  # Match the reasonable 8.3.2(c)(ii) and the abomination 8.3.2.c.ii


def find_citations(text):
    """Given the text of a word document, extract citations from it (as strings)."""

    text = text.lower()  # normalize
    yield from re.findall(CITE_RE, text)
