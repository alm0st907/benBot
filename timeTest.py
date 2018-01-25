import time #python time defaults
cur_time = time.localtime()#nabs th local time, shoves the struct into curtime

while cur_time[5]!=0: #does this only for a minute since it resets at 0

    if cur_time[5]%5==0: #5 second interval for print messages
        print("test tweeet")
        if (cur_time[4]==50 and cur_time[5]==20):
            print("not 420")
        time.sleep(1) #sleep the console for 1 sec
        cur_time=time.localtime() #update our time
    else:
        print("not time yet: "+str(cur_time[3])+':'+str(cur_time[4])+':'+str(cur_time[5])) #stringify our seconds which are an int
        time.sleep(1)
        cur_time = time.localtime()
    
    #cur_time[3]==16 and cur_time[4]==20 is 4:20 by time standards
