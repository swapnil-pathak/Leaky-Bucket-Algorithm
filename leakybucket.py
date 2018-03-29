#!/usr/bin/python
import time

packets=[]
pkt_timing=[]
MAX_PKT_COUNT=20
	
oprate=int(input("\nEnter output rate of the bucket(Bytes/sec): "))
bcktsize=int(input("\nEnter Bucketsize (Bytes): "))
pkt_count=int(input("\nSpecify the number of packets you want to transmit: "))

for i in range(0, pkt_count):
	print"\nSpecify the packet size (Bytes) and time of arrival(non negative, non descending, in sec.) for packet ",i,": "
	pkt_size=input()
	pkt_time=input()
	packets.append(pkt_size)
	pkt_timing.append(pkt_time)

content=0
	
for i in range(0, pkt_count):
	if packets[i]+content > bcktsize:
		if packets[i] > bcktsize:
			print"\nIncoming packet size ",packets[i]," greater than the size of the bucket.\n"
		else:
			print"\nBucket size exceeded by",packets[i]+content-bcktsize," bytes..!!\n"
	else:
		newcontent=packets[i];
		content+=newcontent;
		print"\nIncoming Packet : ",newcontent
		print"Transmission left : ",content
		if i!=pkt_count-1:
			temp=pkt_timing[i+1]-pkt_timing[i];
			print"Next packet will comes in ",temp," seconds\n"
		else:
			temp=content
			print"\nThis is the last packet"
		for clk in range (0,temp):
			print"\nTime Left: ",temp-clk
			time.sleep(1)
			if content:
				print oprate," Bytes Transmitted"
				if content < oprate:
					content=0
				else:
					content=content-oprate
				print"Bytes remaining : ",content
			else:
				print"\nNo packets to send"
