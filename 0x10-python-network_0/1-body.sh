#!/bin/bash
#displays the body of the response
curl -i -L -s $1 | tail -n 1
