import pathlib

from rich.tree import Tree

from tree import assemble_parser
from tree.console import console

EMOJIS: dict[str, tuple[str, str]] = {
    ".yaml": (":memo:", "red"),
    ".md": (":part_alternation_mark:", "red"),
    ".py": (":snake:", "green"),
    ".lock": (":lock:", "#e6e4e1"),
    ".toml": (":wrench:", "blue"),
    ".txt": (":memo:", "#e6e6e6"),
}


def traverse(
    path: pathlib.Path,
    subtree: Tree,
    depth: int = 1,
    include: str = "*",
    file: bool = False,
) -> None:
    for p in sorted(path.glob("*")):
        if any(p.name.startswith(char) for char in (".", "__")) and p.is_dir():
            continue

        level = len(p.parts)
        if depth != -1 and level > depth:
            return None

        if p.is_dir():
            if not any(sub_p.match(include) for sub_p in p.iterdir()):
                continue

            node = subtree
            if not file:
                node = subtree.add(
                    f":file_folder: {p.name}", style="#ffdf87", highlight=True
                )
            traverse(
                path=p,
                subtree=node,
                depth=depth,
                include=include,
            )
        elif p.match(include):
            for suffix, (emoji, style) in EMOJIS.items():
                if p.suffix == suffix:
                    subtree.add(f"{emoji:<3s} {p.name}", style=style)


def main() -> None:
    args = assemble_parser()

    root = pathlib.Path(args.Path)
    depth = args.depth
    include = args.include
    file = args.file

    tree = Tree(f":seedling: {root}", highlight=True)
    traverse(
        path=root,
        subtree=tree,
        depth=depth,
        include=include,
        file=file,
    )
    console.print(tree)


main()
