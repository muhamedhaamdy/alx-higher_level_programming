#!/bin/bash
#displays all HTTP methods the server will accept
curl -s -i -X OPTIONS $1 | grep -i 'Allow' | cut -d " " -f 2-
