#!/usr/bin/env bash

input="$1"
file_name="leetcode-""${input// /-}"
file_name="${file_name/./}"
echo content/"$file_name"".md"
echo $input
#cp content/leetcode_template content/$file_name".md"
#
#sed -i '' "/^Title:/ s/$/ $input/" content/"$file_name"".md"
#sed -i '' "/^Date:/ s/$/ $(date +"%Y-%m-%d %H:%M:%S")/" content/"$file_name"".md"
#sed -i '' "/^Slug:/ s/$/ $file_name/" content/"$file_name"".md"
#sed -i '' "/^Summary:/ s/$/ $input/" content/"$file_name"".md"

file="$("$input".py)"
echo $file

sed -i '' "s/python$/python\n$file/" content/"$file_name"".md"