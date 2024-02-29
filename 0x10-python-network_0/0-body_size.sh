#!/bin/bash

curl -s -i $1 | grep -i 'Content-Length' | awk '{print $2}'
