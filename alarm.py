import datetime
import winsound
from playsound import playsound


def alarm(timing):
    try:
        Diff=str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
        Diff = Diff[11:-3]
        hour = int(Diff[:2])
        Min = int(Diff[3:5])
        print(f"Alarm has beem set for {timing}")
        while True:
            if hour==datetime.datetime.now().hour:
                if Min==datetime.datetime.now().minute:
                    # winsound.PlaySound('alarm.mp3', winsound.SND_LOOP)
                    playsound('music.mpeg')
                    print("Alarm has been triggered")
                    Sec = datetime.datetime.now().second
                    afterSec = datetime.datetime.now().second + 30
                    if (Sec == afterSec):
                        playsound.close()
                    
                elif Min<datetime.datetime.now().minute:
                    break
    except:
        print('Something went Wrong....!!')
