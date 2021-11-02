import pathlib

from tree import assemble_parser
from tree.console import console
from tree.rich_tree import tree as r_tree


def traverse(path: pathlib.Path, subtree) -> None:
    for p in path.glob("*"):
        if any(p.name.startswith(char) for char in (".", "__")) and p.is_dir():
            continue

        if p.is_dir():
            node = subtree.add(f":file_folder: {p.name}")
            traverse(p, node)
        else:
            subtree.add(p.name)


args = assemble_parser()
depth = args.depth

root = pathlib.Path(args.path[0])
traverse(root, r_tree)
console.print(r_tree)
