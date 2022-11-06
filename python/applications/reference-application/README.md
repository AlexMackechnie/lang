# Reference Python Application

# Setup

## Production
```bash
# Build Wheel and Requirements
python -m pip install --upgrade build pip-tools
python -m piptools compile -o requirements.txt pyproject.toml
python -m build

# Copy requirements.txt and <wheel-file> to prod env.

# Install
python -m pip install -r requirements.txt
python -m pip install dist/<wheel-file> --no-deps

# Run
python -m <module-name>
```

## Development
```bash
# Build Requirements
python -m pip install --upgrade pip-tools
python -m piptools compile -o requirements.txt pyproject.toml
python -m piptools compile --extra dev -o dev-requirements.txt pyproject.toml

# Install
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
python -m pip install -e . --no-deps

# Run
python -m <module-name>
```

# Makefile

### `dev_setup`
- We should only need to install requirements-dev.txt here as it includes all main dependencies as well.
- However, sometimes a specific dev dependency will cause second level dependencies from the main requirements to change, meaning that the main requirements in .txt and -dev.txt will be different.

