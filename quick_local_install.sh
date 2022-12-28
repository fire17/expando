cd -
python3 setup.py sdist bdist_wheel
python3 -m pip install --force-reinstall --no-deps . 
cd -
python3