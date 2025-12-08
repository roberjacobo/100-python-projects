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
