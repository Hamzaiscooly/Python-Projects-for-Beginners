# Command-Line Arguments with argparse

import argparse

parser = argparse.ArgumentParser(description="Simple CLI tool")
parser.add_argument("name", help="Your name")
args = parser.parse_args()

print(f"Hello, {args.name}!")