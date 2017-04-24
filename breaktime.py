import datetime
import ctypes
import time

def currenttime():
    return datetime.datetime.now().time()
def addminutes(min):
    now = currenttime();
    timebeing = datetime.datetime(100, 1, 1, now.hour, now.minute, now.second)
    timebeing = timebeing + datetime.timedelta(minutes=min)
    return timebeing.time()

#print currenttime()
#print addminutes(1)
ct = currenttime()
stopTime = ct.replace(hour =20,minute=30,second = 0,microsecond =0)
lunchTimeStart = ct.replace(hour = 13,minute=00,second = 0,microsecond =0)
lunchTimeEnd = ct.replace(hour = 14,minute=00,second = 0,microsecond =0)
teaTimeStart = ct.replace(hour = 16,minute=45,second = 0,microsecond =0)
teaTimeEnd = ct.replace(hour = 15,minute=15,second = 0,microsecond =0)
count = 1
while stopTime > currenttime():
    updatedTime = addminutes(30);
    print updatedTime
    time.sleep(1805)
    if updatedTime < currenttime():
        if currenttime() > lunchTimeStart and currenttime() < lunchTimeEnd:
            ctypes.windll.user32.MessageBoxA(0, "Grab lunch box and go !!! \n Namaku soru than mukiyam :D :D", "Break time", 1)
            time.sleep(3600)
        elif currenttime() > teaTimeStart and currenttime() < teaTimeEnd:
            ctypes.windll.user32.MessageBoxA(0, "Snack Time !!! Go and grab a cup of coffee \n ", "Break time", 1)
            time.sleep(1800)
        elif count %2 !=0:
            ctypes.windll.user32.MessageBoxA(0, "Grab and sip !!! \n      WATER :D ", "Break time", 1)
            count +=1
        elif count % 2 ==0:
            ctypes.windll.user32.MessageBoxA(0, "Go for child walk and refill bottle !!! \n      :D :D", "Break time", 1)
            count +=1
if stopTime < currenttime():
    ctypes.windll.user32.MessageBoxA(0, " EOD !!! \n You should SERIOUSLY get a girl friend -_-", "Shut down", 1)
