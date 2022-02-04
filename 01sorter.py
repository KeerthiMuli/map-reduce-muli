# Keerthi Muli
# Practice Sorting

n = open("Demo.txt","r")  # open file, read-only
s = open("Demo2.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
	s.write(line)
n.close()
s.close()
