#!/bin/bash
hostname > text1.log
i=1
while true; do
md5sum text"$i".log
sleep 5s
date
cp text"$i".log text"$(($i + 1))".log
i=$(($i + 1))
done
