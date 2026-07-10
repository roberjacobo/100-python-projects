# 🐍 100 Python Projects

A repository containing **100 Python projects** for hands-on practice.  
Includes examples across multiple domains:

- **Vanilla Python** (core language exercises)  
- **API development**  
- **MCP (Model Context Protocol)**  
- **AI Agents & automation**

---

## 📋 Projects List

1. **Hello World** - Basic Python introduction
2. **Calculator** - Basic arithmetic operations with user input
3. **Point** - Object-oriented programming with 2D coordinate points
4. **Inventory** - CSV file operations for product management
5. **FastAPI** - API development (in progress)

---

## ⚙️ Setup

Create a virtual environment using [uv](https://github.com/astral-sh/uv):

```bash
uv venv --python 3.11
source .venv/bin/activate  # Linux/macOS
```

## Dependency Management

Dependencies are managed in `pyproject.toml`. Common commands:

**Install all dependencies** (fresh setup on new machine):
```bash
uv sync
```

**Add new dependencies**:
```bash
uv add package-name
uv add "fastapi[standard]"  # with extras
uv pip install <package>  # works too
```

**Remove dependencies**:
```bash
uv remove package-name
```

**Update dependencies**:
```bash
uv lock --upgrade
uv sync
```

## 🧹 Cleaning `__pycache__` Folders

Python creates `__pycache__/` folders with compiled bytecode (`.pyc` files) every time a module is imported. They are harmless (and already git-ignored), but they clutter the project tree while learning.

### One-off cleanup: `clean-pycache.sh`

The repo includes a helper script that deletes every `__pycache__` folder recursively:

```bash
./clean-pycache.sh
```

**How it works:** the script is a Bash wrapper (so it runs from Git Bash) that calls PowerShell to do the actual work:

```powershell
Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
```

- `Get-ChildItem -Recurse -Directory -Filter '__pycache__'` finds all directories named `__pycache__` under the current folder.
- `Remove-Item -Recurse -Force` deletes each one along with its contents.

### Permanent option: disable bytecode caching (project-only)

This project's venv contains a `sitecustomize.py` that Python imports automatically at startup, so `__pycache__` folders are never created — but only when running through this venv, without affecting Python anywhere else on the machine:

```python
# .venv/Lib/site-packages/sitecustomize.py
import sys
sys.dont_write_bytecode = True
```

This applies to the activated venv, `uv run`, and IDEs pointed at `.venv`. **Note:** if the venv is ever recreated (`uv venv`), the file is wiped and must be re-created.

Alternatives for reference: `python -B` disables caching for a single run, and setting the `PYTHONDONTWRITEBYTECODE=1` environment variable disables it machine-wide. The only trade-off in all cases is slightly slower imports since Python re-compiles modules on every run — irrelevant for small learning projects.

## Running FastAPI Projects

**Development server with auto-reload**:
```bash
fastapi dev 05.FastAPI/main.py
```

**Production server**:
```bash
fastapi run 05.FastAPI/main.py
```

**Alternative using uvicorn directly**:
```bash
uvicorn 05.FastAPI.main:app --reload  # development
uvicorn 05.FastAPI.main:app           # production
```

**Access interactive documentation**:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
