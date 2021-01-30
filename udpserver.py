import socket
import sys
import time


# address of the server 
ip = socket.gethostbyname(socket.gethostname())  # server ip 
port = 3550 					# server port


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (ip, port)
sock.bind(server_address)


# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)

# opening a loop to send data

try:

    # Send data to the multicast group
    print(sys.stderr, 'sending "%s"' % message)
    with open('rc_3.log','r') as reader:   # opening the log file
	for i in range(0,1000):	
		send_data = reader.readline(256)  or f'No match for "{query}".' 			#fetching data line by line, encoding into utf-8
    		sock.sendto(send_data.encode('utf-8'), address)  # encoding and sending the data
    	

    # Look for responses from recipient
    # to confirm if the data reached
    while True:
        print(sys.stderr, 'waiting to receive')
        try:
        	data, server = sock.recvfrom(16)
        except socket.timeout:
            	print(sys.stderr, 'timed out, no more responses')
            	break
        else:
            	print(sys.stderr, 'received "%s" from %s' % (data, server))

finally:
    	print("####### END OF DRIVE #######")
    	sock.close()

    

    	
    	
