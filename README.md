# UDP
UDP code for telimetry
socket is initiated in local host with 3550 as open port

ttl is made 1, so that it doesnt bounce out of the wifi network

Once socket is binded it is ready to send the data packets
For emulation it reads out each line from a file and sends them sequentially
the data is encripted in utf-8  and aditional headers are not being added to keep it simple
( not actually a neccesity for our requirement )

After each line being sent timeout and client closings are checked
Then finally socket is closed, indicating end of data.
