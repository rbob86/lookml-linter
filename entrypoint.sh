#!/usr/bin/env bash

find ./ -type d

find ./ -type f 


python -m linter.main config.example.yaml
