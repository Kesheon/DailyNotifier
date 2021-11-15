from datetime import date
from pushbullet import Pushbullet


#--------------------------------------------------------
# 01/01/2022 (pick a scripture) is Scripture1
#date.fromisoformat('yyyy-mm-dd')

Scripture1Date = date.fromisoformat('2022-01-01')
if(Scripture1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "DailyText.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daily Text', text)

#----------------------------------------------------------
# 01/02/2022 (pick a scripture) is Scripture2
#date.fromisoformat('yyyy-mm-dd')

Scripture2Date = date.fromisoformat('2022-01-02')
if(Scripture2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "DailyText.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daily Text', text)

#--------------------------------------------------------




    
#NOTE: A "RANDOM" VERSION OF THIS PROGRAM CAN BE MADE
#-----------------------------------------------
#from pushbullet import Pushbullet

#API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"

#file = "DailyText.txt"

#with open(file, mode='r') as f:
    #text = f.read()

#pb = Pushbullet(API_KEY)
#push = pb.push_note('Daily Text', text) 
