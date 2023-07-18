#!/usr/bin/python3

"""
markdown2html.py

This script converts a Markdown file to HTML.

Usage: ./markdown2html.py README.md README.html
"""

import sys
import os
import re

def convert_to_html(markdown_file, output_file):
    """
    Convert the given Markdown file to HTML and save it to the output file.
    """
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Replace heading syntax with HTML tags
    html_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdown_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^###### (.+)$', r'<h6>\1</h6>', html_content, flags=re.MULTILINE)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

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

