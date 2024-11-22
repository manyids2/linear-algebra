#!/bin/bash

questions=$(find -name "q*.py" | sort)
for f in $questions; do
  python "$f"
done
