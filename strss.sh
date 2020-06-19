#! /bin/bash
stress-ng --cpu 0 -l $1 --timeout $2 &> /dev/null 2> /dev/null &
echo $!
