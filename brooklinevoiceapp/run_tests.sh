#!/usr/bin/env sh

# Test if 'coverage' command exists
if command -v coverage
then
    # test w/ coverage
    python -m coverage run --source='.' -m unittest discover -v -s mycity/test

    # if exit code is 0, test is success and continue on, else exit w/ code
    if [ $? -eq 0 ]
    then
        # test if 'codecov' in TravisCI exists
        if command -v codecov
        then
            # move .coverage report file to root
            mv .coverage ..
        else
            # just show coverage report for local
            python -m coverage report -m
        fi
    else
        exit $?
    fi
else
    # run the old command
    python -m unittest discover -v -s mycity/test
fi
