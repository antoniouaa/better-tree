# Examples

### Base invocation in current directory:

```
➜ poetry run better-tree .
🌱 .
├── 📝 .pre-commit-config.yaml
├── 📁 assets
├── 📁 better_tree
│   ├── 🐍 __init__.py
│   ├── 🐍 console.py
│   ├── 🐍 main.py
│   └── 🐍 parser.py
├── 📁 dist
├── 🔒 poetry.lock
├── 🔧 pyproject.toml
├── 〽 README.md
└── 📝 requirements.txt
```

### `--File` s only:

```
➜ poetry run better-tree . --File
🌱 .
├── 📝 .pre-commit-config.yaml
├── 🐍 __init__.py
├── 🐍 console.py
├── 🐍 main.py
├── 🐍 parser.py
├── 🔒 poetry.lock
├── 🔧 pyproject.toml
├── 〽 README.md
└── 📝 requirements.txt
```

### `--Include` only Python files

```
➜ poetry run better-tree . --File --Include "*.py"
🌱 .
├── 🐍 __init__.py
├── 🐍 console.py
├── 🐍 main.py
└── 🐍 parser.py
```

### `--Exclude` Python files starting with "m" from "better_tree"

```
➜ poetry run better-tree better_tree --Exclude "m*.py"
🌱 better_tree
├── 🐍 __init__.py
├── 🐍 console.py
└── 🐍 parser.py
```
