### pySimpleClientUDP allows to show how to connect to Xilinx board using Ethernet cable

There is example **lwip UDP Perf Server** in Xilinx SDK so this client works with Xilinx example.

For checking connections you may use tcpdump:
```console
  sudo tcpdump -i enp1s0 host 192.168.1.10
```
only choose correct Ethernet interface (for me it's enp1s0).
