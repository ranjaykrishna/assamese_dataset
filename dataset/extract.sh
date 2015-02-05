for dir in [^\.]*/ ; 
do
  for file in $dir*
  do
    python extract.py "$file" "$dir"; 
  done
done
