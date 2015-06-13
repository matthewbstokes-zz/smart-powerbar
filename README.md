Add the following function to your .bashrc
```bash
function relay() {
 sudo python /home/pi/Desktop/relay.py -d $1 -s $2
}
export -f relay
```
