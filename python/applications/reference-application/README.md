# Reference Python Application

# Setup
```bash
python -m pip install --upgrade build pip-tools
```

# Makefile

### `dev_setup`
- We should only need to install requirements-dev.txt here as it includes all main dependencies as well.
- However, sometimes a specific dev dependency will cause second level dependencies from the main requirements to change, meaning that the main requirements in .txt and -dev.txt will be different.

