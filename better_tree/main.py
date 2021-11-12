import pathlib

from rich.tree import Tree

from better_tree.parser import assemble_parser
from better_tree.console import console

EMOJIS: dict[str, tuple[str, str]] = {
    ".yaml": (":memo:", "red"),
    ".md": (":part_alternation_mark:", "red"),
    ".py": (":snake:", "green"),
    ".lock": (":lock:", "#e6e4e1"),
    ".toml": (":wrench:", "blue"),
    ".txt": (":memo:", "#e6e6e6"),
    ".xlsm": (":green_book:", "#1f6e43"),
    ".xlsx": (":green_book:", "#1f6e43"),
    ".xls": (":green_book:", "#1f6e43"),
    ".html": (":computer:", "#5dadec"),
    ".pdf": (":bookmark_tabs:", "#e81224"),
}


def traverse(
    path: pathlib.Path,
    subtree: Tree,
    depth: int = 1,
    include: str = "*",
    exclude: str = "",
    file: bool = False,
) -> None:
    for p in sorted(path.glob("*")):
        if exclude and p.match(exclude):
            continue

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
                exclude=exclude,
                file=file,
            )
        elif p.match(include):
            for suffix, (emoji, style) in EMOJIS.items():
                if p.suffix == suffix:
                    subtree.add(f"{emoji:<3s} {p.name}", style=style)


def run() -> None:
    cliparser = assemble_parser()
    args = cliparser.parse_args()

    root = pathlib.Path(args.Path)
    depth = args.depth
    include = args.include
    exclude = args.exclude
    file = args.file

    tree = Tree(f":seedling: {root}", highlight=True)
    traverse(
        path=root,
        subtree=tree,
        depth=depth,
        include=include,
        exclude=exclude,
        file=file,
    )
    console.print(tree)
