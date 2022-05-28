#!/usr/bin/env bash

yourfilenames=`ls -la`
for eachfile in $yourfilenames
do
   echo $eachfile
done

python -m linter.main config.example.yaml
