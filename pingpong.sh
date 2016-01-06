#!/bin/bash
# how to use? chmod +x pingpong.sh; ./pingpong.sh xxx.xxx.xxx.xxx

NOW=$(date +"%m-%d-%Y")
ping $1 | while read pong; do echo "$(date): $pong"; done > $1:"$NOW".log &
