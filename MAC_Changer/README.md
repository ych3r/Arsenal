# MAC address changer

Check network info: `ifconfig`

Disable eth0: `ifconfig eth0 down`

Change MAC address: `ifconfig eth0 hw ether 00:11:22:33:44:55`

Enable eth0: `ifconfig eth0 up`

Original MAC address: `ethtool -P eth0`