#!/bin/sh

if [ ! -f $0 ] ; then
	echo "No files"
else
	echo $0
fi

n=0
while [ $n -le 5 ] ; do
	echo "n="$n
	n=`expr $n + 1`
done

dir=.
for list in $dir/* ; do
	echo $list
done

while read line ; do
	echo $line
done < $0


