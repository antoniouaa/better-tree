from inspect import ismemberdescriptor
import pathlib

from tree import assemble_parser
from tree.console import console

END_PIPE = "\u2570"
CONTINUE_PIPE = "\u251C"
CONNECTOR = "\u2500"


def is_empty(path: pathlib.Path) -> bool:
    return not any(path.iterdir())


def dir_len(path: pathlib.Path) -> bool:
    return sum(1 for _ in path.iterdir())


def traverse(path: pathlib.Path):
    for i, p in enumerate(path.glob("*"), start=1):
        if any(p.name.startswith(char) for char in (".", "__")) and p.is_dir():
            continue

        depth = len(p.parts)
        pipe = CONTINUE_PIPE

        if p.is_dir():
            if is_empty(p):
                console.print(f"{pipe}{CONNECTOR * depth} ", style="pipe", end="")
                console.print(p.name, style="dir")
            else:
                pipe = END_PIPE
                console.print(f"{pipe}{CONNECTOR * depth} ", style="pipe", end="")
                console.print(p.name, style="dir")
                traverse(p)
        else:
            size_of_dir = dir_len(path)
            if i + 1 == size_of_dir:
                pipe = END_PIPE
            console.print(
                f"{'   ' * (depth - 1)}{pipe}{CONNECTOR} ",
                style="pipe",
                end="",
            )
            console.print(p.name, style="file")


args = assemble_parser()
print(args)
depth = args.depth

console.print(args.path[0], style="root")
root = pathlib.Path(args.path[0])
traverse(root)
