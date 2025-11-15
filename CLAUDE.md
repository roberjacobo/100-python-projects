# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a learning repository containing 100 Python practice projects across multiple domains:
- Vanilla Python (core language exercises)
- API development
- MCP (Model Context Protocol)
- AI Agents & automation

## Project Structure

Each project is in its own numbered directory (e.g., `01.hello-world/`, `02.calculator/`). Projects are standalone exercises with independent Python files.

## Environment Setup

Python version: 3.11.13

Virtual environment is managed with `uv`:
```bash
uv venv --python 3.11
source .venv/bin/activate  # Linux/macOS
```

## Running Projects

Each project is executed independently:
```bash
python 01.hello-world/hello_world.py
python 02.calculator/calculator.py
```

## Development Notes

- Projects are simple, standalone exercises - no complex build or test infrastructure
- Each project directory contains only the necessary Python files for that exercise
- No shared utilities or common modules between projects
- Focus on individual project functionality rather than repository-wide architecture
