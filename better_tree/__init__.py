import argparse

PROG = "tree"
USAGE = "%(prog)s <Path> [options]"
DESCRIPTION = "Tree utility in Python"


def assemble_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
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
        "--File",
        dest="file",
        action="store_true",
        help="Only show files",
    )
    return parser.parse_args()


from better_tree.main import main as main
