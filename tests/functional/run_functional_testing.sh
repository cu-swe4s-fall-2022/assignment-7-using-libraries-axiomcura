#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest



run formatter1 pycodestyle ../unit/tests.py
assert_exit_code 0

run formatter2 pycodestyle ../../*.py
assert_exit_code 0


# # running plot_gtex
run plotter plotter.py -i ../../iris.data -o pretty_flowers
assert_exit_code 0