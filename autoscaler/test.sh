#!/bin/sh

TESTING="$(kubectl get pods | grep y)"
if [ $TESTING ]
then 
	echo "blue"
else
	echo "red" 
fi
