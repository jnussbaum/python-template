# Template repo for python projects

Replace `your-pkg` / `your_pkg` at these places:

- `pyproject.toml` (2 x)
- directory `src/your_pkg` (via IDE refactoring - it is used in the code)


## Quick Start

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync --all-extras --dev
source .venv/bin/activate
pre-commit install
```
