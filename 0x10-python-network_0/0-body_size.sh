#!/bin/bash
# displays the size of the body of the response
curl -s -i $1 | grep -i 'Content-Length' | awk '{print $2}'
