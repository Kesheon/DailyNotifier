from datetime import date
from pushbullet import Pushbullet

# Place scriptures on the first line of a txt file only,
# so that Pytohn doesn't have to read more than one line

#--------------------------------------------------------
# 01/01/2022
# (pick a scripture) is Scripture1Date
# date.fromisoformat('yyyy-mm-dd')

Scripture1Date = date.fromisoformat('2022-01-01')
if(Scripture1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "DailyText.txt"#file names need to be the same as its scripture
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daily Text', text)

#----------------------------------------------------------
# 01/02/2022
# (pick a scripture) is Scripture2Date
# date.fromisoformat('yyyy-mm-dd')

Scripture2Date = date.fromisoformat('2022-01-02')
if(Scripture2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "DailyText.txt"#file names need to be the same as its scripture
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daily Text', text)

#--------------------------------------------------------




