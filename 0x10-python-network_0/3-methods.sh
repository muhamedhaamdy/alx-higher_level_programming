curl -s -i -X OPTIONS 0.0.0.0:5000/route_4 | grep -i 'Allow' | sed 's/Allow: //i'
