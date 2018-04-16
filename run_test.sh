#!/usr/bin/env bash

python3 project.py < dataset1 > test1 && python3 test1.py
python3 project.py < dataset2 > test2 && python3 test2.py

rm test1
rm test2