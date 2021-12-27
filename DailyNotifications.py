from datetime import date
from pushbullet import Pushbullet

#--------------------------------------------------------
# 01/01/2022
# (2 Timothy 3:15) is Scripture1Date
# date.fromisoformat('yyyy-mm-dd')

Scripture1Date = date.fromisoformat('2022-01-01')
if(Scripture1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture1.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Timothy 3:15', text)
    
    file2 = "scripture1Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)
    
#----------------------------------------------------------
# 01/02/2022
# (Revelation 9:5) is Scripture2Date
# date.fromisoformat('yyyy-mm-dd')

Scripture2Date = date.fromisoformat('2022-01-02')
if(Scripture2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture2.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 9:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/03/2022
# (Proverbs 15:3) is Scripture3Date
# date.fromisoformat('yyyy-mm-dd')

Scripture3Date = date.fromisoformat('2022-01-03')
if(Scripture3Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture3.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 15:3', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/04/2022
# (2 Timothy 4:7) is Scripture4Date
# date.fromisoformat('yyyy-mm-dd')

Scripture4Date = date.fromisoformat('2021-01-04')
if(Scripture4Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture4.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Timothy 4:3', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/05/2022
# (Ephesians 6:13) is Scripture5Date
# date.fromisoformat('yyyy-mm-dd')

Scripture5Date = date.fromisoformat('2022-01-05')
if(Scripture5Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture5.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ephesians 6:13', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/06/2022
# (Daniel 11:41) is Scripture6Date
# date.fromisoformat('yyyy-mm-dd')

Scripture6Date = date.fromisoformat('2022-01-06')
if(Scripture6Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture6.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daniel 11:41', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/07/2022
# (Psalm 25:14) is Scripture7Date
# date.fromisoformat('yyyy-mm-dd')

Scripture7Date = date.fromisoformat('2022-01-07')
if(Scripture7Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture7.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 25:14', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/08/2022
# (Psalm 119:68) is Scripture8Date
# date.fromisoformat('yyyy-mm-dd')

Scripture8Date = date.fromisoformat('2022-01-08')
if(Scripture8Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture8.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 119:68', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/09/2022
# (James 1:19) is Scripture9Date
# date.fromisoformat('yyyy-mm-dd')

Scripture9Date = date.fromisoformat('2022-01-09')
if(Scripture9Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture9.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 1:19', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/10/2022
# (1 John 2:14) is Scripture10Date
# date.fromisoformat('yyyy-mm-dd')

Scripture10Date = date.fromisoformat('2022-01-10')
if(Scripture10Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture10.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 2:14', text)

#--------------------------------------------------------