!#/bin/bash
rm -rf dist
python3 -m build
twine check dist/*
twine upload dist/*