# Description
Currently power bar outfitted with a relay. GPIO pins on a Raspberry Pi toggle the relay. The Raspberry Pi is controlled through the home network.

# Hardware
  - Powerbar
  - 8 Channel Relay
  - Raspberry Pi 2
  - Wireless Dongle

# CLI
Add the following function to your .bashrc
```bash
function relay() {
 sudo python /home/pi/Desktop/relay.py -d $1 -s $2
}
export -f relay
```
Usage: 
``` bash
  $ relay [keyword] [action]
```

# TODO
  - IOT Edison, or Google weave type IOT connection.
  - Android App
  - Chrome App
  - Power usage monitoring
