import sys
import argparse

PROG = "tree"
USAGE = "%(prog)s <Path> [options]"
DESCRIPTION = "Featureful tree utility in Python"


class CLIParser(argparse.ArgumentParser):
    def error(self, *args, **kwargs):
        self.print_help()
        sys.exit(1)


def assemble_parser() -> CLIParser:
    parser = CLIParser(
        prog=PROG,
        usage=USAGE,
        description=DESCRIPTION,
    )
    parser.add_argument(
        "Path",
        help="The path to search in",
    )
    parser.add_argument(
        "--Depth",
        dest="depth",
        default=-1,
        type=int,
        help="Number of levels of depth",
    )
    parser.add_argument(
        "--Include",
        dest="include",
        default="*",
        type=str,
        help="Glob pattern to include in the search",
    )
    parser.add_argument(
        "--Exclude",
        dest="exclude",
        default="",
        type=str,
        help="Glob pattern to exclude from the search",
    )
    parser.add_argument(
        "--File",
        dest="file",
        action="store_true",
        help="Only show files",
    )
    parser.set_defaults(fuc=parser.print_help)
    return parser
