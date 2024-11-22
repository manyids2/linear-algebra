#!/bin/bash

questions=$(find -name "q*.py" | sort)
for f in $questions; do
  clear
  python "$f"
  read -p "$f" -n 1 -r
done
