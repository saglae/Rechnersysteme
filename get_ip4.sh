ifconfig eth0 | grep inet |head -1 |awk '{print $2}'

#alternativ geht auch:
#ifconfig eth0 | grep 'inet ' |awk '{print $2}'

