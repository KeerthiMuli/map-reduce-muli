# KeerthiMuli - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 5) : 
    Date,State,TotalSamples,Negative,Positive= datalist

    # print intermediate key-value pairs to standard output
    print(State,"\t",Positive)