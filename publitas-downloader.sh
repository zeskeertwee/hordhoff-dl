#!/bin/sh
#
# Source: https://gist.github.com/wvengen/27162f92acadfaf3ac6b782b9a018285
#
# Generates PDF from Publitas images (online folder service)
# Stores generated PDF and JSON (which may contains links).
#
# Requirements:
# - wget        https://www.gnu.org/software/wget/
# - jq          https://stedolan.github.io/jq/
#
#

if [ ! "$2" ]; then
  echo "Usage: $0 <publitas_folder_url> <output_name>"
  exit 1
fi

URL="$1"
OUT="$2"

DIR=`mktemp -d --suffix=.getpublitas`

wget -q -O /dev/stdout "$URL" | sed 's/^\s*var\s\+data\s\+=\s\+\(.*\);\s*$/\1/p;d' > "$DIR/$NAME.json"
echo $DIR

cat "$DIR/$NAME.json" | jq -r '.spreads[].pages[].images | .at2400 // .at2000 // .at1600 // .at1200 // .at1000' >"$DIR/img_urls"

i=1
for u in `cat "$DIR/img_urls"`; do
  echo "$u" >"$DIR/cur_url" # use file to be able to use base
  wget -q --base="$URL" -O `printf "$DIR/image-page-%04d.jpg" $i` -i "$DIR/cur_url"
  echo "Downloaded page $i"
  i=$(( $i + 1 ))
done
