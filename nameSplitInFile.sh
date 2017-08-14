#!/bin/bash
file="$HOME/data.txt"
while IFS=':' read -r col1 col2
do
    echo "$col1"
done <$file

