#!/usr/bin/env bash
source env/bin/activate
python setup.py sdist upload -r pypi
python setup.py bdist_wheel upload -r pypi