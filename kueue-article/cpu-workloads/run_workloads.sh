#!/bin/bash

while :
do
  kubectl create -f ${1}
  sleep ${3:-10}
done