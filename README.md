This repository contains the code and data used in my research comparing the practical performance of four sorting algorithms: bubble sort, selection sort, insertion sort, and merge sort. The code generates random datasets, measures execution times across increasing input sizes, and produces the results shown in my research paper.

Contents

sorting_test.py: sorting functions, timing logic, and data generation

multiple_trials.py: averaged execution times

data.json: recorded execution times from experimental runs

How to run

Install Python 3.10 or later, then run:

sorting_test.py first

multiple_trials.py next

This will create a data folder containing graphs and another folder containing a JSON file.
