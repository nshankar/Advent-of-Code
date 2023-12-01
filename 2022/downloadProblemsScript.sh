#!/bin/bash
url="https://adventofcode.com" url_day="${url}/2022/day"
# mkdir aoc
cd aoc
# mkdir static
# curl "${url}/static/style.css" > static/style.css
# mkdir -p 2022/day
cd 2022/day
for i in $(seq 20)
do
    # mkdir $i
    # curl "${url_day}/${i}" > ${i}/index.html
    curl "${url_day}/${i}/input" > ${i}/input -H 'Cookie: _ga=GA1.2.1920093457.1670115815; session=53616c7465645f5fc36e1286b6c18b6a4c4e36292896ba7261d5ac11b47d705ec3f923f8c81d09bad2812e900b3b4b478fa00d756358fe3af12f6779a7a4998a'
done
