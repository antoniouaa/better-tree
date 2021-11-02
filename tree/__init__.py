import argparse

PROG = "tree"
USAGE = "%(prog)s <path> [options]"
DESCRIPTION = "Tree utility in Python"


def assemble_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=PROG,
        usage=USAGE,
        description=DESCRIPTION,
    )
    parser.add_argument(
        "path",
        nargs=1,
        help="The path to search in",
    )
    parser.add_argument(
        "--Depth",
        dest="depth",
        default=1,
        type=int,
        nargs=1,
        help="Number of levels of depth",
    )
    return parser.parse_args()
