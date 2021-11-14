from pushbullet import Pushbullet

API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"

file = "DailyText.txt"

with open(file, mode='r') as f:
    text = f.read()

pb = Pushbullet(API_KEY)
push = pb.push_note('Daily Text', text) 
