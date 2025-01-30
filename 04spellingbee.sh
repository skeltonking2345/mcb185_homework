gunzip -c ~/code/MCB185/data/dictionary.gz | grep "^[acinozr]*r[acinozr]*$" | grep -E "^.{4,}$"
