#!/bin/bash
# $1 = start url, $2 = prefix, $3 = cutoff ISO date (stop when oldest updated < cutoff)
url="$1"; pre="$2"; cut="$3"; i=0
while [ -n "$url" ]; do
  f="${pre}_$(printf %04d $i).atom"
  curl -sS -m 120 -o "$f" "$url" || break
  old=$(grep -o '<updated>[^<]*' "$f" | tail -1 | cut -c10-19)
  url=$(grep -o '<link href="[^"]*" rel="next"/>' "$f" | head -1 | sed 's/<link href="//;s/" rel="next"\/>//')
  echo "$i $old"
  [[ "$old" < "$cut" ]] && break
  i=$((i+1))
done
