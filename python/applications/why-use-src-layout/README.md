# Why use a source layout?

Experiment to show a situation where testing your app locally using a flat layout would actually cause different behaviour than to running your app in a production environment.

In `pyproject.toml`, we have:
```toml
packages = ["mainpkg", "pkg1"]
```

In mainpkg.main we have:
```python3
from pkg1 import p1
from pkg2 import p2

p1.main()
p2.main()
```

Running this from the root of the project, there are no issues, as the packages are being picked up from the root dir, and not site-packages.
```python
python3 -m venv venv
. venv/bin/activate

python -m mainpkg.main
```

If we run the same thing (in a new venv) from the root dir but use `pip install -e .` this time, there are no issues (however, the packages are being picked up from the root and not site-packages, even though we've installed it).
```bash
python -m venv venv
. venv/bin/activate

pip install -e .

python -m mainpkg.main
```

This can be confirmed by cd'ing to tmp_dir in the same venv and trying the same thing.

```bash
cd tmp_dir

python -m mainpkg.main

# Output:
# ModuleNotFoundError: No module named 'pkg2'
```

# Why is this an issue?



This shows that even when installing with `pip install -e .`, the packages will still be picked up from the root dir. This is particularly dangerous as we could be testing our app locally in the root dir, using the following method:
```bash
python -m venv venv
. venv/bin/activate

pip install -e .

python -m mainpkg.main
```

From this, we could then confirm our app is running fine (spoiler, because pkg2 is available from the source).

From here, we build a wheel of our app, copy it to our production environment (which doesn't have our source).
```bash
python -m venv venv
. venv/bin/activate

pip install --upgrade build
python -m build

cp dist/why_use_src_layout-0.0.1-py2.py3-none-any.whl tmp_dir/
```

Note: We're assuming our production environment is just a fresh venv in `tmp_dir` for simplicity.

In our production environment, we just have the wheel - and no source code. We then install it, and run it.
```python
cd tmp_dir

python -m venv venv
. venv/bin/activate

pip install why_use_src_layout-0.0.1-py2.py3-none-any.whl

python -m mainpkg.main

# Output:
# ModuleNotFoundError: No module named 'pkg2'
```

We get this error, because pkg2 is not distributed with the distribution, as it was not included in our original `pyproject.toml`:
```toml
packages = ["mainpkg", "pkg1"]
```

This is an error that we wouldn't have caught in our development environment, but would have surfaced in production.

# Conclusion

Use `src` layouts. 😃

# Footnote

This doesn't confirm that mainpkg and pkg1 are being picked up from the source directly instead of being linked through from site-packages. I'm still unsure about this. It confirms that pkg2 is being picked up through site-packages and linked back to the source, which is what we expect. I don't know if this is happening for mainpkg and pkg1 as well; or if site-packages for these is just being ignored and they are being picked up straight from the source.
