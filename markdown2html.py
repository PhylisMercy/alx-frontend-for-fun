#!/usr/bin/python3

"""
markdown2html.py

This script converts a Markdown file to HTML.

Usage: ./markdown2html.py README.md README.html
"""

import sys
import os

def convert_to_html(markdown_file, output_file):
    """
    Convert the given Markdown file to HTML and save it to the output file.
    """
    # Add your code here for Markdown to HTML conversion
    pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = "README.md"
    output_file = "README.html"

    if not os.path.exists(markdown_file):
        sys.stderr.write("Missing {}\n".format(markdown_file))
        sys.exit(1)

    convert_to_html(markdown_file, output_file)
    sys.exit(0)

