#! /bin/bash
stress-ng --cpu $1 --timeout $2 &> /dev/null 2> /dev/null &
echo $!
