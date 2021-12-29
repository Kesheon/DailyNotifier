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

Scripture20Date = date.fromisoformat('2022-01-20')
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

Scripture27Date = date.fromisoformat('2022-01-27')
if(Scripture27Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture27.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Galatians 6:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/28/2022
# (James 4:8) is Scripture28Date
# date.fromisoformat('yyyy-mm-dd')

Scripture28Date = date.fromisoformat('2022-01-28')
if(Scripture28Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture28.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 4:8', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/29/2022
# (Proverbs 27:17) is Scripture29Date
# date.fromisoformat('yyyy-mm-dd')

Scripture29Date = date.fromisoformat('2022-01-29')
if(Scripture29Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture29.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 27:17', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/30/2022
# (Romans 12:17) is Scripture30Date
# date.fromisoformat('yyyy-mm-dd')

Scripture30Date = date.fromisoformat('2022-01-30')
if(Scripture30Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture30.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 12:17', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 01/31/2022
# (Joel 1:6) is Scripture31Date
# date.fromisoformat('yyyy-mm-dd')

Scripture31Date = date.fromisoformat('2022-01-31')
if(Scripture31Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scripture31.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Joel 1:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/01/2022
# (Philippians 2:3) is ScriptureFeb1Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb1Date = date.fromisoformat('2022-02-01')
if(ScriptureFeb1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb1.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Philippians 2:3', text)

    file2 = "scriptureFeb1Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)
#--------------------------------------------------------

#----------------------------------------------------------
# 02/02/2022
# (John 15:13) is ScriptureFeb2Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb2Date = date.fromisoformat('2022-02-02')
if(ScriptureFeb2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb2.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 15:13', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/03/2022
# (Hebrews 12:1) is ScriptureFeb3Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb3Date = date.fromisoformat('2022-02-03')
if(ScriptureFeb3Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb3.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Hebrews 12:1', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/04/2022
# (1 Timothy 2:1,2) is ScriptureFeb4Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb4Date = date.fromisoformat('2022-02-04')
if(ScriptureFeb4Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb4.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 2:1,2', text)

    file2 = "scriptureFeb4Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/05/2022
# (1 Timothy 4:16) is ScriptureFeb5Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb5Date = date.fromisoformat('2022-02-05')
if(ScriptureFeb5Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb5.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 4:16', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/06/2022
# (Proverbs 3:32) is ScriptureFeb6Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb6Date = date.fromisoformat('2022-02-06')
if(ScriptureFeb6Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb6.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 3:32', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/07/2022
# (Psalm 86:11) is ScriptureFeb7Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb7Date = date.fromisoformat('2022-02-07')
if(ScriptureFeb7Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb7.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 86:11', text)

    file2 = "scriptureFeb7Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/08/2022
# (Hosea 11:4) is ScriptureFeb8Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb8Date = date.fromisoformat('2022-02-08')
if(ScriptureFeb8Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb8.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Hosea 11:4', text)

    file2 = "scriptureFeb8Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/09/2022
# (James 1:12) is ScriptureFeb9Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb9Date = date.fromisoformat('2022-02-09')
if(ScriptureFeb9Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb9.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 1:12', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/10/2022
# (Revelation 12:12) is ScriptureFeb10Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb10Date = date.fromisoformat('2022-02-10')
if(ScriptureFeb10Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb10.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revalation 12:12', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/11/2022
# (Romans 6:23) is ScriptureFeb11Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb11Date = date.fromisoformat('2022-02-11')
if(ScriptureFeb11Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb11.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 6:23', text)

    file2 = "scriptureFeb11Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/12/2022
# (1 Timothy 4:16) is ScriptureFeb12Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb12Date = date.fromisoformat('2022-02-12')
if(ScriptureFeb12Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb12.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 4:16', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/13/2022
# (1 Corinthians 12:15) is ScriptureFeb13Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb13Date = date.fromisoformat('2022-02-13')
if(ScriptureFeb13Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb13.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 12:15', text)

    file2 = "scriptureFeb13Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/14/2022
# (Psalm 118:6) is ScriptureFeb14Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb14Date = date.fromisoformat('2022-02-14')
if(ScriptureFeb14Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb14.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 118:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/15/2022
# (2 Chronicles 14:2) is ScriptureFeb15Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb15Date = date.fromisoformat('2022-02-15')
if(ScriptureFeb15Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb15.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Chronicles 14:2', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/16/2022
# (1 Corinthians 4:6) is ScriptureFeb16Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb16Date = date.fromisoformat('2022-02-16')
if(ScriptureFeb16Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb16.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 4:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/17/2022
# (Proverbs 3:15) is ScriptureFeb17Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb17Date = date.fromisoformat('2022-02-17')
if(ScriptureFeb17Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb17.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 3:15', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/18/2022
# (Acts 28:14) is ScriptureFeb18Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb18Date = date.fromisoformat('2022-02-18')
if(ScriptureFeb18Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb18.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 28:14', text)

    file2 = "scriptureFeb18Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/19/2022
# (1 Timothy 4:8) is ScriptureFeb19Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb19Date = date.fromisoformat('2022-02-19')
if(ScriptureFeb19Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb19.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 4:8', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/20/2022
# (Matthew 16:22) is ScriptureFeb20Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb20Date = date.fromisoformat('2022-02-20')
if(ScriptureFeb20Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb20.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 16:22', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/21/2022
# (1 Peter 3:7) is ScriptureFeb21Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb21Date = date.fromisoformat('2022-02-21')
if(ScriptureFeb21Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb21.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Peter 3:7', text)

    file2 = "scriptureFeb21Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/22/2022
# (Philippians 3:13,14) is ScriptureFeb22Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb22Date = date.fromisoformat('2022-02-22')
if(ScriptureFeb22Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb22.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Philippians 3:13,14', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/23/2022
# (Revelation 7:9,10) is ScriptureFeb23Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb23Date = date.fromisoformat('2022-02-23')
if(ScriptureFeb23Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb23.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 7:9,10', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/24/2022
# (Isaiah 30:15) is ScriptureFeb24Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb24Date = date.fromisoformat('2022-02-24')
if(ScriptureFeb24Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb24.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Isaiah 30:15', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/25/2022
# (Revelation 7:14) is ScriptureFeb25Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb25Date = date.fromisoformat('2022-02-25')
if(ScriptureFeb25Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb25.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 7:14', text)

    file2 = "scriptureFeb25Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/26/2022
# (Acts 2:17) is ScriptureFeb26Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb26Date = date.fromisoformat('2022-02-26')
if(ScriptureFeb26Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb26.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 2:17', text)

    file2 = "scriptureFeb26Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/27/2022
# (Acts 20:28) is ScriptureFeb27Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb27Date = date.fromisoformat('2022-02-27')
if(ScriptureFeb27Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb27.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 20:28', text)

    file2 = "scriptureFeb27Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 02/28/2022
# (Psalm 25:14) is ScriptureFeb28Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureFeb28Date = date.fromisoformat('2022-02-28')
if(ScriptureFeb28Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureFeb28.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 25:14', text)

    file2 = "scriptureFeb28Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/01/2022
# (Luke 6:22) is ScriptureMar1Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar1Date = date.fromisoformat('2022-03-01')
if(ScriptureMar1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar1.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Luke 6:22', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/02/2022
# (Ecclesiastes 3:11) is ScriptureMar2Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar2Date = date.fromisoformat('2022-03-02')
if(ScriptureMar2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar2.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ecclesiastes 3:11', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/03/2022
# (2 Chronicles 36:19) is ScriptureMar3Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar3Date = date.fromisoformat('2022-03-03')
if(ScriptureMar3Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar3.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Chronicles 36:19', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/04/2022
# (Genesis 19:16) is ScriptureMar4Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar4Date = date.fromisoformat('2022-03-04')
if(ScriptureMar4Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar4.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Genesis 19:16', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/05/2022
# (Psalm 110:3) is ScriptureMar5Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar5Date = date.fromisoformat('2022-03-05')
if(ScriptureMar5Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar5.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 110:3', text)

    file2 = "scriptureMar5Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/06/2022
# (Proverbs 15:8) is ScriptureMar6Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar6Date = date.fromisoformat('2022-03-06')
if(ScriptureMar6Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar6.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 15:8', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/07/2022
# (Matthew 24:13) is ScriptureMar7Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar7Date = date.fromisoformat('2022-03-07')
if(ScriptureMar7Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar7.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 24:13', text)

    file2 = "scriptureMar7Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/08/2022
# (Daniel 2:44) is ScriptureMar8Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar8Date = date.fromisoformat('2022-03-08')
if(ScriptureMar8Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar8.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daniel 2:44', text)

    file2 = "scriptureMar8Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/09/2022
# (1 John 4:8) is ScriptureMar9Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar9Date = date.fromisoformat('2022-03-09')
if(ScriptureMar9Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar9.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 4:8', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/10/2022
# (2 Corinthians 2:11) is ScriptureMar10Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar10Date = date.fromisoformat('2022-03-10')
if(ScriptureMar10Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar10.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Corinthians 2:11', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/11/2022
# (Romans 15:1) is ScriptureMar11Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar11Date = date.fromisoformat('2022-03-11')
if(ScriptureMar11Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar11.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 15:1', text)

    file2 = "scriptureMar11Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/12/2022
# (John 13:35) is ScriptureMar12Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar12Date = date.fromisoformat('2022-03-12')
if(ScriptureMar12Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar12.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 13:35', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/13/2022
# (1 John 3:18) is ScriptureMar13Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar13Date = date.fromisoformat('2022-03-13')
if(ScriptureMar13Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar13.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 3:18', text)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/14/2022
# (Acts 24:14) is ScriptureMar14Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar14Date = date.fromisoformat('2022-03-14')
if(ScriptureMar14Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar14.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 24:15', text)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/15/2022
# (Galatians 6:4) is ScriptureMar15Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar15Date = date.fromisoformat('2022-03-15')
if(ScriptureMar15Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar15.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Galatians 6:4', text)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/16/2022
# (Revelation 7:9) is ScriptureMar16Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar16Date = date.fromisoformat('2022-03-16')
if(ScriptureMar16Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar16.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 7:9', text)

    file2 = "scriptureMar16Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/17/2022
# (Matthew 6:22) is ScriptureMar17Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar17Date = date.fromisoformat('2022-03-17')
if(ScriptureMar17Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar17.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 6:22', text)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/18/2022
# (Mark 13:10) is ScriptureMar18Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar18Date = date.fromisoformat('2022-03-18')
if(ScriptureMar18Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar18.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Mark 13:10', text)

    file2 = "scriptureMar18Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/19/2022
# (1 Timothy 1:18) is ScriptureMar19Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar19Date = date.fromisoformat('2022-03-19')
if(ScriptureMar19Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar19.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 1:18', text)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/20/2022
# (Psalm 119:112) is ScriptureMar20Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar20Date = date.fromisoformat('2022-03-20')
if(ScriptureMar20Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar20.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 119:112', text)
    
#--------------------------------------------------------

