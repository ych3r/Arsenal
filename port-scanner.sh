#!/bin/bash

for port in {1..1000};
do
    timeout 1 bash -c "echo > /dev/tcp/$1/$port" 2>/dev/null && echo "port $port is open"
done
