import pathlib

from rich.tree import Tree

from tree import assemble_parser
from tree.console import console

EMOJIS = {
    "yaml": (":memo:", "red"),
    "md": (":part_alternation_mark:", "red"),
    "py": (":snake:", "green"),
    "lock": (":lock:", "#e6e4e1"),
    "toml": (":wrench:", "blue"),
}


def traverse(path: pathlib.Path, subtree: Tree, depth: int = 1) -> None:
    for p in sorted(path.glob("*")):
        if any(p.name.startswith(char) for char in (".", "__")) and p.is_dir():
            continue

        level = len(p.parts)
        if level > depth:
            return None

        if p.is_dir():
            node = subtree.add(f":file_folder: {p.name}", style="#ffdf87")
            traverse(p, node, depth)
        else:
            for suffix, (emoji, style) in EMOJIS.items():
                if p.name.endswith(suffix):
                    subtree.add(f"{emoji:<3s} {p.name}", style=style)


args = assemble_parser()
depth = args.depth[0]

root = pathlib.Path(args.path[0])

tree = Tree(str(root))
traverse(path=root, subtree=tree, depth=depth)
console.print(tree)
