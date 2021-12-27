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

#----------------------------------------------------------
# 01/11/2022
# (Psalm 36:9) is Scripture11Date
# date.fromisoformat('yyyy-mm-dd')

Scripture11Date = date.fromisoformat('2022-01-11')
if(Scripture11Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture11.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 36:9', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/12/2022
# (Matthew 24:9) is Scripture12Date
# date.fromisoformat('yyyy-mm-dd')

Scripture12Date = date.fromisoformat('2022-01-12')
if(Scripture12Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture12.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 24:9', text)

    file2 = "scripture12Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
        pb = Pushbullet(API_KEY)
        push = pb.push_note("continued", text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/13/2022
# (1 John 5:19) is Scripture13Date
# date.fromisoformat('yyyy-mm-dd')

Scripture13Date = date.fromisoformat('2022-01-13')
if(Scripture13Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture13.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 5:19', text)

    file2 = "scripture13Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
        pb = Pushbullet(API_KEY)
        push = pb.push_note("continued", text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/14/2022
# (Matthew 10:16) is Scripture14Date
# date.fromisoformat('yyyy-mm-dd')

Scripture14Date = date.fromisoformat('2022-01-14')
if(Scripture14Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture14.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 10:16', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/15/2022
# (2 Chronicles 14:6) is Scripture15Date
# date.fromisoformat('yyyy-mm-dd')

Scripture15Date = date.fromisoformat('2022-01-15')
if(Scripture15Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture15.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Chronicles 14:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/16/2022
# (1 Timothy 6:20) is Scripture16Date
# date.fromisoformat('yyyy-mm-dd')

Scripture16Date = date.fromisoformat('2022-01-16')
if(Scripture16Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture16.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 6:20', text)

    file2 = "scripture16Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
        pb = Pushbullet(API_KEY)
        push = pb.push_note("continued", text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/17/2022
# (1 Thessalonians 1:5) is Scripture17Date
# date.fromisoformat('yyyy-mm-dd')

Scripture17Date = date.fromisoformat('2022-01-17')
if(Scripture17Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture17.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Thessalonians 1:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/18/2022
# (Deuteronomy 6:7) is Scripture18Date
# date.fromisoformat('yyyy-mm-dd')

Scripture18Date = date.fromisoformat('2022-01-18')
if(Scripture18Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture18.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Deuteronomy 6:7', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/19/2022
# (Ezra 7:10) is Scripture19Date
# date.fromisoformat('yyyy-mm-dd')

Scripture19Date = date.fromisoformat('2022-01-19')
if(Scripture19Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture19.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ezra 7:10', text)

    file2 = "scripture19Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
        pb = Pushbullet(API_KEY)
        push = pb.push_note("continued", text2)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 01/20/2022
# (Acts 23:11) is Scripture20Date
# date.fromisoformat('yyyy-mm-dd')

Scripture20Date = date.fromisoformat('2022-01-22')
if(Scripture20Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture20.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 23:11', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/21/2022
# (1 John 3:20) is Scripture21Date
# date.fromisoformat('yyyy-mm-dd')

Scripture21Date = date.fromisoformat('2022-01-21')
if(Scripture21Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture21.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 3:20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/22/2022
# (Psalm 73:13) is Scripture22Date
# date.fromisoformat('yyyy-mm-dd')

Scripture22Date = date.fromisoformat('2022-01-22')
if(Scripture22Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture22.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 73:13', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/23/2022
# (Romans 8:26) is Scripture23Date
# date.fromisoformat('yyyy-mm-dd')

Scripture23Date = date.fromisoformat('2022-01-23')
if(Scripture23Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture23.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 8:26', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/24/2022
# (Revelation 7:4) is Scripture24Date
# date.fromisoformat('yyyy-mm-dd')

Scripture24Date = date.fromisoformat('2022-01-24')
if(Scripture24Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture24.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 7:4', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/25/2022
# (2 Samuel 22:36) is Scripture25Date
# date.fromisoformat('yyyy-mm-dd')

Scripture25Date = date.fromisoformat('2022-01-25')
if(Scripture25Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture25.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Samuel 22:36', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/26/2022
# (Proverbs 20:29) is Scripture26Date
# date.fromisoformat('yyyy-mm-dd')

Scripture26Date = date.fromisoformat('2022-01-26')
if(Scripture26Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture26.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 20:29', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/27/2022
# (Galatians 6:5) is Scripture27Date
# date.fromisoformat('yyyy-mm-dd')

Scripture27Date = date.fromisoformat('2021-12-27')
if(Scripture27Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture27.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Galatians 6:5', text)

#--------------------------------------------------------
