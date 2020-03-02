import random
from datetime import datetime
import math

# func to trunctate float to specified digits
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


### open file
f = open("dummyData.csv", "a")

### write timestamp
# Returns a datetime object containing the local date and time
dateTimeObj = datetime.now()
f.write("'")
f.write(str(dateTimeObj))
f.write("\n")

### write in random data 

for pp in range(32):
    f.write("Sns_")
    f.write(str(pp + 1))
    f.write(",")
    for qq in range(16):
        f.write(str(truncate(random.random(), 3)))
        if qq < 15:
            f.write(",")
        else:
            f.write("\n")

f.close()

### Create copy and corrupt an entry in the dataset

# Read in the file
with open('dummyData.csv', 'r') as file :
  filedata = file.read()

## Replace the target string
snsId = str(random.randint(1,32))
strQQ = 'Sns_' + snsId + ','
# find occurance, replace value immediately after it
posStt = filedata.find(strQQ) + len(strQQ)
posNxt = filedata.find(',', posStt, posStt + 7)
filedata = filedata[:posStt]  + 'err' + filedata[posNxt:]

# Write the file out again
with open('corruptData.csv', 'w') as file:
  file.write(filedata)

#close
file.close()


### Test for error, write log
## Function to test for error
def testError(fileName='corruptData.csv'):

    with open(fileName, 'r') as file :
      filedata = file.read()
    
    errStartPos = filedata.find('err')
    errSensorStr = filedata[errStartPos - 7:errStartPos-1]
    crLfPostn = errSensorStr.find('\n')
    errSensorStr = errSensorStr[crLfPostn+1:]
    
    with open('errorLog.txt', 'a') as file:
      dateTimeObj = datetime.now()
      file.write("'")
      file.write(str(dateTimeObj))
      file.write(' [Error in ')
      file.write(errSensorStr)
      file.write(' data]\n')

    file.close()

#function call
testError('corruptData.csv')

