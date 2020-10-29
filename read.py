data = []
import time
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			time.sleep(2)
			print(len(data))
print(len(data))
print(data[0])