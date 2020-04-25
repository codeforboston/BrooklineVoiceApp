#!/usr/bin/env sh
if command -v coverage
then
    python -m coverage run --source='.' -m unittest discover -v -s mycity/test

    if [ $? -eq 0 ]
    then
        if command -v codecov
        then
            mv .coverage ..
        else
            python -m coverage report -m
        fi
    fi
else
    python -m unittest discover -v -s mycity/test
fi
