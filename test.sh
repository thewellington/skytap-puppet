#!/bin/bash
#
# by bill@wellingtonnet.net
#

# Get gateway address from routing table
GATEWAY=`route | grep UG | awk '{print $2}'`

curl http://$GATEWAY/skytap
