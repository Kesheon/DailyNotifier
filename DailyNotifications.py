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

Scripture4Date = date.fromisoformat('2022-01-04')
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

#----------------------------------------------------------
# 03/21/2022
# (John 8:29) is ScriptureMar21Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar21Date = date.fromisoformat('2022-03-21')
if(ScriptureMar21Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar21.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 8:29', text)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/22/2022
# (Hebrews 13:5) is ScriptureMar22Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar22Date = date.fromisoformat('2022-03-22')
if(ScriptureMar22Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar22.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Hebrews 13:5', text)

    file2 = "scriptureMar22Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/23/2022
# (Isaiah 30:15) is ScriptureMar23Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar23Date = date.fromisoformat('2022-03-23')
if(ScriptureMar23Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar23.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Isaiah 30:15', text)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/24/2022
# (Acts 24:15) is ScriptureMar24Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar24Date = date.fromisoformat('2022-03-24')
if(ScriptureMar24Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar24.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 24:15', text)
    
#--------------------------------------------------------

#----------------------------------------------------------
# 03/25/2022
# (Matthew 26:75) is ScriptureMar25Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar25Date = date.fromisoformat('2022-03-25')
if(ScriptureMar25Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar25.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 26:75', text)
    
    file2 = "scriptureMar25Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/26/2022
# (Psalm 27:3) is ScriptureMar26Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar26Date = date.fromisoformat('2022-03-26')
if(ScriptureMar26Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar26.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 27:3', text)

    file2 = "scriptureMar26Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/27/2022
# (Revelation 7:16) is ScriptureMar27Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar27Date = date.fromisoformat('2022-03-27')
if(ScriptureMar27Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar27.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 7:16', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/28/2022
# (2 Thessalonians 3:3) is ScriptureMar28Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar28Date = date.fromisoformat('2022-03-28')
if(ScriptureMar28Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar28.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Thessalonians 3:3', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/29/2022
# (Romans 8:39) is ScriptureMar29Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar29Date = date.fromisoformat('2022-03-29')
if(ScriptureMar29Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar29.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 8:39', text)

    file2 = "scriptureMar29Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/30/2022
# (Psalm 55:22) is ScriptureMar30Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar30Date = date.fromisoformat('2022-03-30')
if(ScriptureMar30Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar30.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 55:22', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 03/31/2022
# (1 Timothy 5:2) is ScriptureMar30Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMar31Date = date.fromisoformat('2022-03-31')
if(ScriptureMar31Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMar31.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 5:2', text)

    file2 = "scriptureMar31Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/01/2022
# (Romans 15:4) is ScriptureApr1Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr1Date = date.fromisoformat('2022-04-01')
if(ScriptureApr1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr1.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 15:4', text)

    file2 = "scriptureApr1Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/02/2022
# (John 4:35) is ScriptureApr2Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr2Date = date.fromisoformat('2022-04-02')
if(ScriptureApr2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr2.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 4:35', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/03/2022
# (Proverbs 15:11) is ScriptureApr3Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr3Date = date.fromisoformat('2022-04-03')
if(ScriptureApr3Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr3.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 15:11', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/04/2022
# (1 Peter 2:21) is ScriptureApr4Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr4Date = date.fromisoformat('2022-04-04')
if(ScriptureApr4Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr4.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Peter 2:21', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/05/2022
# (Romans 14:13) is ScriptureApr5Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr5Date = date.fromisoformat('2022-04-05')
if(ScriptureApr5Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr5.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 14:13', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/06/2022
# (Revelation 7:14) is ScriptureApr6Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr6Date = date.fromisoformat('2022-04-06')
if(ScriptureApr6Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr6.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 7:14', text)

    file2 = "scriptureApr6Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/07/2022
# (Revelation 19:19) is ScriptureApr7Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr7Date = date.fromisoformat('2022-04-07')
if(ScriptureApr7Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr7.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 19:19', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/08/2022
# (Luke 11:13) is ScriptureApr8Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr8Date = date.fromisoformat('2022-04-08')
if(ScriptureApr8Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr8.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Luke 11:13', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/09/2022
# (1 Corinthians 15:21) is ScriptureApr9Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr9Date = date.fromisoformat('2022-04-09')
if(ScriptureApr9Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr9.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:21', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/10/2022
# (Revelation 7:10) is ScriptureApr10Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr10Date = date.fromisoformat('2022-04-10')
if(ScriptureApr10Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr10.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 7:10', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/11/2022
# (1 Corinthians 11:25) is ScriptureApr11Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr11Date = date.fromisoformat('2022-04-11')
if(ScriptureApr11Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr11.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 11:25', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/12/2022
# (1 John 4:9) is ScriptureApr12Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr12Date = date.fromisoformat('2022-04-12')
if(ScriptureApr12Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr12.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 4:9', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/13/2022
# (John 15:15) is ScriptureApr13Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr13Date = date.fromisoformat('2022-04-13')
if(ScriptureApr13Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr13.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 15:15', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/14/2022
# (1 Corinthians 15:22) is ScriptureApr14Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr14Date = date.fromisoformat('2022-04-14')
if(ScriptureApr14Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr14.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:22', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/15/2022
# (1 Thessalonians 4:17) is ScriptureApr15Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr15Date = date.fromisoformat('2022-04-15')
if(ScriptureApr15Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr15.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Thessalonians 4:17', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/16/2022
# (1 Corinthians 15:20) is ScriptureApr16Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr16Date = date.fromisoformat('2022-04-16')
if(ScriptureApr16Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr16.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/17/2022
# (1 Corinthians 15:42) is ScriptureApr17Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr17Date = date.fromisoformat('2022-04-17')
if(ScriptureApr17Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr17.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:42', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/18/2022
# (1 Corinthians 15:55) is ScriptureApr18Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr18Date = date.fromisoformat('2022-04-18')
if(ScriptureApr18Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr18.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:55', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/19/2022
# (Acts 24:15) is ScriptureApr19Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr19Date = date.fromisoformat('2022-04-19')
if(ScriptureApr19Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr19.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 24:15', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/20/2022
# (Galatians 2:20) is ScriptureApr20Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr20Date = date.fromisoformat('2022-04-20')
if(ScriptureApr20Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr20.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Galatians 2:20', text)

    file2 = "scriptureApr20Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/21/2022
# (James 1:5) is ScriptureApr21Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr21Date = date.fromisoformat('2022-04-21')
if(ScriptureApr21Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr21.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 1:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/22/2022
# (Romans 12:3) is ScriptureApr22Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr22Date = date.fromisoformat('2022-04-22')
if(ScriptureApr22Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr22.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 12:3', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/23/2022
# (2 Chronicles 14:6) is ScriptureApr23Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr23Date = date.fromisoformat('2022-04-23')
if(ScriptureApr23Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr23.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Chronicles 14:6', text)

    file2 = "scriptureApr23Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/24/2022
# (2 Corinthians 12:10) is ScriptureApr24Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr24Date = date.fromisoformat('2022-04-24')
if(ScriptureApr24Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr24.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Corinthians 12:10', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/25/2022
# (1 John 4:7) is ScriptureApr25Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr25Date = date.fromisoformat('2022-04-25')
if(ScriptureApr25Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr25.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 4:7', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/26/2022
# (1 Corinthians 12:18) is ScriptureApr26Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr26Date = date.fromisoformat('2022-04-26')
if(ScriptureApr26Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr26.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 12:18', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/27/2022
# (1 Corinthians 7:31) is ScriptureApr27Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr27Date = date.fromisoformat('2022-04-27')
if(ScriptureApr27Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr27.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 7:31', text)

    file2 = "scriptureApr27Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/28/2022
# (Ecclesiastes 11:4) is ScriptureApr28Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr28Date = date.fromisoformat('2022-04-28')
if(ScriptureApr28Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr28.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ecclesiastes 11:4', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/29/2022
# (1 Timothy 6:20) is ScriptureApr28Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr29Date = date.fromisoformat('2022-04-29')
if(ScriptureApr29Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr29.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 6:20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 04/30/2022
# (Isaiah 30:20) is ScriptureApr28Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureApr30Date = date.fromisoformat('2022-04-30')
if(ScriptureApr30Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureApr30.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Isaiah 30:20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/01/2022
# (Luke 2:51) is ScriptureMay1Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay1Date = date.fromisoformat('2022-05-01')
if(ScriptureMay1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay1.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Luke 2:51', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/02/2022
# (1 Corinthians 15:12) is ScriptureMay2Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay2Date = date.fromisoformat('2022-05-02')
if(ScriptureMay2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay2.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:12', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/03/2022
# (Philippians 3:4) is ScriptureMay3Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay3Date = date.fromisoformat('2022-05-03')
if(ScriptureMay3Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay3.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Philippians 3:4', text)

    file2 = "scriptureMay3Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/04/2022
# (Romans 7:21) is ScriptureMay4Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay4Date = date.fromisoformat('2022-05-04')
if(ScriptureMay4Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay4.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 7:21', text)

    file2 = "scriptureMay4Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/05/2022
# (John 15:15) is ScriptureMay5Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay5Date = date.fromisoformat('2022-05-05')
if(ScriptureMay5Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay5.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 15:15', text)

    file2 = "scriptureMay5Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/06/2022
# (1 Peter 5:10) is ScriptureMay6Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay6Date = date.fromisoformat('2022-05-06')
if(ScriptureMay6Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay6.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Peter 5:10', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/07/2022
# (John 6:44) is ScriptureMay7Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay7Date = date.fromisoformat('2022-05-07')
if(ScriptureMay7Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay7.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 6:44', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/08/2022
# (Romans 12:2) is ScriptureMay8Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay8Date = date.fromisoformat('2022-05-08')
if(ScriptureMay8Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay8.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 12:2', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/09/2022
# (Psalm 86:11) is ScriptureMay9Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay9Date = date.fromisoformat('2022-05-09')
if(ScriptureMay9Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay9.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 86:11', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/10/2022
# (Daniel 11:44) is ScriptureMay10Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay10Date = date.fromisoformat('2022-05-10')
if(ScriptureMay10Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay10.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daniel 11:44', text)

    file2 = "scriptureMay10Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/11/2022
# (Genesis 39:1) is ScriptureMay11Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay11Date = date.fromisoformat('2022-05-11')
if(ScriptureMay11Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay11.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Genesis 39:1', text)

    file2 = "scriptureMay11Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/12/2022
# (Acts 5:40) is ScriptureMay12Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay12Date = date.fromisoformat('2022-05-12')
if(ScriptureMay12Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay12.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 5:40', text)

    file2 = "scriptureMay12Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/13/2022
# (Hebrews 11:10) is ScriptureMay13Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay13Date = date.fromisoformat('2022-05-13')
if(ScriptureMay13Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay13.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Hebrews 11:10', text)

    file2 = "scriptureMay13Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/14/2022
# (Romans 6:7) is ScriptureMay14Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay14Date = date.fromisoformat('2022-05-14')
if(ScriptureMay14Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay14.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 6:7', text)

    file2 = "scriptureMay14Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/15/2022
# (1 Corinthians 7:7) is ScriptureMay15Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay15Date = date.fromisoformat('2022-05-15')
if(ScriptureMay15Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay15.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 7:7', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/16/2022
# (Matthew 24:36) is ScriptureMay16Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay16Date = date.fromisoformat('2022-05-16')
if(ScriptureMay16Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay16.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 24:36', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/17/2022
# (2 Timothy 3:12) is ScriptureMay17Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay17Date = date.fromisoformat('2022-05-17')
if(ScriptureMay17Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay17.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Timothy 3:12', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/18/2022
# (Proverbs 21:1) is ScriptureMay18Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay18Date = date.fromisoformat('2022-05-18')
if(ScriptureMay18Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay18.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 21:1', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/19/2022
# (Matthew 28:19) is ScriptureMay19Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay19Date = date.fromisoformat('2022-05-19')
if(ScriptureMay19Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay19.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 28:19', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/20/2022
# (James 4:6) is ScriptureMay20Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay20Date = date.fromisoformat('2022-05-20')
if(ScriptureMay20Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay20.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 4:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/21/2022
# (Ecclesiates 12:1) is ScriptureMay21Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay21Date = date.fromisoformat('2022-05-21')
if(ScriptureMay21Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay21.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ecclesiastes 12:1', text)

    file2 = "scriptureMay21Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/22/2022
# (Luke 4:43) is ScriptureMay22Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay22Date = date.fromisoformat('2022-05-22')
if(ScriptureMay22Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay22.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Luke 4:43', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/23/2022
# (1 Corinthians 15:3,4) is ScriptureMay23Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay23Date = date.fromisoformat('2022-05-23')
if(ScriptureMay23Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay23.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:3,4', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/24/2022
# (Psalm 41:3) is ScriptureMay24Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay24Date = date.fromisoformat('2022-05-24')
if(ScriptureMay24Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay24.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 41:3', text)

    file2 = "scriptureMay24Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/25/2022
# (Psalm 118:6) is ScriptureMay25Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay25Date = date.fromisoformat('2022-05-25')
if(ScriptureMay25Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay25.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 118:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/26/2022
# (Hebrews 6:19) is ScriptureMay26Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay26Date = date.fromisoformat('2022-05-26')
if(ScriptureMay26Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay26.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Hebrews 6:19', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/27/2022
# (James 5:11) is ScriptureMay27Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay27Date = date.fromisoformat('2022-05-27')
if(ScriptureMay27Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay27.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 5:11', text)

    file2 = "scriptureMay27Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/28/2022
# (1 Peter 2:21) is ScriptureMay28Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay28Date = date.fromisoformat('2022-05-28')
if(ScriptureMay28Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay28.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Peter 2:21', text)

    file2 = "scriptureMay28Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/29/2022
# (Psalm 150:6) is ScriptureMay29Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay29Date = date.fromisoformat('2022-05-29')
if(ScriptureMay29Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay29.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 150:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/30/2022
# (1 Samuel 30:8) is ScriptureMay30Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay30Date = date.fromisoformat('2022-05-30')
if(ScriptureMay30Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay30.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Samuel 30:8', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 05/31/2022
# (Romans 8:38,39) is ScriptureMay31Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureMay31Date = date.fromisoformat('2022-05-31')
if(ScriptureMay31Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureMay31.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 8:38,39', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/01/2022
# (1 Thessalonians 2:8) is ScriptureJun1Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun1Date = date.fromisoformat('2022-06-01')
if(ScriptureJun1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun1.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Thessalonians 2:8', text)

    file2 = "scriptureJun1Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/02/2022
# (Matthew 28:18) is ScriptureJun2Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun2Date = date.fromisoformat('2022-06-02')
if(ScriptureJun2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun2.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 28:18', text)

    file2 = "scriptureJun2Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/03/2022
# (2 Corinthians 12:10) is ScriptureJun3Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun3Date = date.fromisoformat('2022-06-03')
if(ScriptureJun3Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun3.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Corinthians 12:10', text)

#--------------------------------------------------------


#----------------------------------------------------------
# 06/04/2022
# (1 Corinthians 9:23) is ScriptureJun4Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun4Date = date.fromisoformat('2022-06-04')
if(ScriptureJun4Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun4.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 9:23', text)

    file2 = "scriptureJun4Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/05/2022
# (Daniel 12:1) is ScriptureJun5Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun5Date = date.fromisoformat('2022-06-05')
if(ScriptureJun5Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun5.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daniel 12:1', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/06/2022
# (Psalm 135:13) is ScriptureJun6Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun6Date = date.fromisoformat('2022-06-06')
if(ScriptureJun6Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun6.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 135:13', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/07/2022
# (Colossians 3:13) is ScriptureJun7Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun7Date = date.fromisoformat('2022-06-07')
if(ScriptureJun7Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun7.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Colossians 3:13', text)

    file2 = "scriptureJun7Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/08/2022
# (Proverbs 22:3) is ScriptureJun8Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun8Date = date.fromisoformat('2022-06-08')
if(ScriptureJun8Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun8.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 22:3', text)

    file2 = "scriptureJun8Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/09/2022
# (1 Corinthians 10:24) is ScriptureJun9Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun9Date = date.fromisoformat('2022-06-09')
if(ScriptureJun9Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun9.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 10:24', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/10/2022
# (Galatians 1:14) is ScriptureJun10Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun10Date = date.fromisoformat('2022-06-10')
if(ScriptureJun10Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun10.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Galatians 1:14', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/11/2022
# (John 14:12) is ScriptureJun11Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun11Date = date.fromisoformat('2022-06-11')
if(ScriptureJun11Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun11.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 14:12', text)

    file2 = "scriptureJun11Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/12/2022
# (Hebrews 11:17) is ScriptureJun12Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun12Date = date.fromisoformat('2022-06-12')
if(ScriptureJun12Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun12.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Hebrews 11:17', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/13/2022
# (Ephesians 4:24) is ScriptureJun13Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun13Date = date.fromisoformat('2022-06-13')
if(ScriptureJun13Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun13.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ephesians 4:24', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/14/2022
# (1 Thessalonians 4:11) is ScriptureJun14Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun14Date = date.fromisoformat('2022-06-14')
if(ScriptureJun14Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun14.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Thessalonians 4:11', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/15/2022
# (1 Corinthians 15:6) is ScriptureJun15Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun15Date = date.fromisoformat('2022-06-15')
if(ScriptureJun15Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun15.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/16/2022
# (2 Chronicles 15:2) is ScriptureJun16Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun16Date = date.fromisoformat('2022-06-16')
if(ScriptureJun16Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun16.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Chronicles 15:2', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/17/2022
# (Luke 14:33) is ScriptureJun17Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun17Date = date.fromisoformat('2022-06-17')
if(ScriptureJun17Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun17.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Luke 14:33', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/18/2022
# (Matthew 29:19,20) is ScriptureJun18Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun18Date = date.fromisoformat('2022-06-18')
if(ScriptureJun18Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun18.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 29:19,20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/19/2022
# (Zechariah 4:6) is ScriptureJun19Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun19Date = date.fromisoformat('2022-06-19')
if(ScriptureJun19Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun19.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Zechariah 4:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/20/2022
# (2 Samuel 22:28) is ScriptureJun20Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun20Date = date.fromisoformat('2022-06-20')
if(ScriptureJun20Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun20.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Samuel 22:28', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/21/2022
# (Acts 17:32) is ScriptureJun21Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun21Date = date.fromisoformat('2022-06-21')
if(ScriptureJun21Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun21.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 17:32', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/22/2022
# (Acts 16:4) is ScriptureJun22Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun22Date = date.fromisoformat('2022-06-22')
if(ScriptureJun22Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun22.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 16:4', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/23/2022
# (1 Chronicles 29:1) is ScriptureJun23Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun23Date = date.fromisoformat('2022-06-23')
if(ScriptureJun23Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun23.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Chronicles 29:1', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/24/2022
# (1 John 4:7) is ScriptureJun24Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun24Date = date.fromisoformat('2022-06-24')
if(ScriptureJun24Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun24.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 4:7', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/25/2022
# (Romans 15:3) is ScriptureJun25Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun25Date = date.fromisoformat('2022-06-25')
if(ScriptureJun25Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun25.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 15:3', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/26/2022
# (2 Chronicles 14:2) is ScriptureJun26Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun26Date = date.fromisoformat('2022-06-26')
if(ScriptureJun26Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun26.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Chronicles 14:2', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/27/2022
# (Romans 12:10) is ScriptureJun27Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun27Date = date.fromisoformat('2022-06-27')
if(ScriptureJun27Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun27.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 12:10', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/28/2022
# (James 1:2) is ScriptureJun28Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun28Date = date.fromisoformat('2022-06-28')
if(ScriptureJun28Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun28.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 1:2', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/29/2022
# (1 Timothy 6:20) is ScriptureJun29Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun29Date = date.fromisoformat('2022-06-29')
if(ScriptureJun29Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun29.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 6:20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 06/30/2022
# (Psalm 6:9) is ScriptureJun30Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJun30Date = date.fromisoformat('2022-06-30')
if(ScriptureJun30Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJun30.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 6:9', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/01/2022
# (Matthew 28:18) is ScriptureJul1Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul1Date = date.fromisoformat('2022-07-01')
if(ScriptureJul1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul1.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 28:18', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/02/2022
# (Acts 14:15) is ScriptureJul2Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul2Date = date.fromisoformat('2022-07-02')
if(ScriptureJul2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul2.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 14:15', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/03/2022
# (1 Peter 5:7) is ScriptureJul3Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul3Date = date.fromisoformat('2022-07-03')
if(ScriptureJul3Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul3.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Peter 5:7', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/04/2022
# (Romans 1:20) is ScriptureJul4Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul4Date = date.fromisoformat('2022-07-04')
if(ScriptureJul4Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul4.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 1:20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/05/2022
# (Genesis 3:4) is ScriptureJul5Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul5Date = date.fromisoformat('2022-07-05')
if(ScriptureJul5Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul5.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Genesis 3:4', text)

    file2 = "scriptureJul5Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/06/2022
# (Psalm 68:11) is ScriptureJul6Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul6Date = date.fromisoformat('2022-07-06')
if(ScriptureJul6Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul6.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 68:11', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/07/2022
# (Matthew 18:14) is ScriptureJul7Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul7Date = date.fromisoformat('2022-07-07')
if(ScriptureJul7Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul7.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 18:14', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/08/2022
# (1 Timothy 3:1) is ScriptureJul8Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul8Date = date.fromisoformat('2022-07-08')
if(ScriptureJul8Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul8.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 3:1', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/09/2022
# (Galatians 6:5) is ScriptureJul9Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul9Date = date.fromisoformat('2022-07-09')
if(ScriptureJul9Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul9.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Galatians 6:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/10/2022
# (1 Corinthians 1:27) is ScriptureJul10Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul10Date = date.fromisoformat('2022-07-10')
if(ScriptureJul10Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul10.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 1:27', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/11/2022
# (Matthew 6:33) is ScriptureJul11Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul11Date = date.fromisoformat('2022-07-11')
if(ScriptureJul11Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul11.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 6:33', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/12/2022
# (Revelation 2:10) is ScriptureJul12Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul12Date = date.fromisoformat('2022-07-12')
if(ScriptureJul12Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul12.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 2:10', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/13/2022
# (2 Timothy 2:15) is ScriptureJul13Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul13Date = date.fromisoformat('2022-07-13')
if(ScriptureJul13Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul13.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Timothy 2:15', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/14/2022
# (Hebrews 12:3) is ScriptureJul14Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul14Date = date.fromisoformat('2022-07-14')
if(ScriptureJul14Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul14.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Hebrews 12:3', text)

    file2 = "scriptureJul14Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/15/2022
# (1 Corinthians 11:1) is ScriptureJul15Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul15Date = date.fromisoformat('2022-07-15')
if(ScriptureJul15Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul15.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 11:1', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/16/2022
# (Matthew 28:19,20) is ScriptureJul16Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul16Date = date.fromisoformat('2022-07-16')
if(ScriptureJul16Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul16.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 28:19,20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/17/2022
# (Colossians 1:9) is ScriptureJul17Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul17Date = date.fromisoformat('2022-07-17')
if(ScriptureJul17Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul17.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Colossians 1:9', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/18/2022
# (Ephesians 4:3) is ScriptureJul18Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul18Date = date.fromisoformat('2022-07-18')
if(ScriptureJul18Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul18.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ephesians 4:3', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/19/2022
# (James 1:22) is ScriptureJul19Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul19Date = date.fromisoformat('2022-07-19')
if(ScriptureJul19Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul19.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 1:22', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/20/2022
# (Acts 16:5) is ScriptureJul20Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul20Date = date.fromisoformat('2022-07-20')
if(ScriptureJul20Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul20.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 16:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/21/2022
# (1 Corinthians 15:21) is ScriptureJul21Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul21Date = date.fromisoformat('2022-07-21')
if(ScriptureJul21Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul21.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:21', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/22/2022
# (Psalm 138:6) is ScriptureJul22Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul22Date = date.fromisoformat('2022-07-22')
if(ScriptureJul22Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul22.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 138:6', text)

    file2 = "scriptureJul22Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/23/2022
# (Ephesians 6:17) is ScriptureJul23Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul23Date = date.fromisoformat('2022-07-23')
if(ScriptureJul23Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul23.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ephesians 6:17', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/24/2022
# (Revelation 1:9) is ScriptureJul24Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul24Date = date.fromisoformat('2022-07-24')
if(ScriptureJul24Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul24.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Revelation 1:9', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/25/2022
# (1 Samuel 18:1) is ScriptureJul25Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul25Date = date.fromisoformat('2022-07-25')
if(ScriptureJul25Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul25.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Samuel 18:1', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/26/2022
# (1 Corinthians 11:3) is ScriptureJul26Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul26Date = date.fromisoformat('2022-07-26')
if(ScriptureJul26Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul26.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 11:3', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/27/2022
# (Acts 16:9) is ScriptureJul27Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul27Date = date.fromisoformat('2022-07-27')
if(ScriptureJul27Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul27.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 16:9', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/28/2022
# (James 1:2) is ScriptureJul28Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul28Date = date.fromisoformat('2022-07-28')
if(ScriptureJul28Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul28.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('James 1:2', text)

    file2 = "scriptureJul28Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/29/2022
# (Proverbs 12:25) is ScriptureJul29Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul29Date = date.fromisoformat('2022-07-29')
if(ScriptureJul29Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul29.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 12:25', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/30/2022
# (1 Timothy 4:12) is ScriptureJul30Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul30Date = date.fromisoformat('2022-07-30')
if(ScriptureJul30Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul30.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Timothy 4:12', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 07/31/2022
# (2 Timothy 4:17) is ScriptureJul31Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureJul31Date = date.fromisoformat('2022-07-31')
if(ScriptureJul31Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureJul31.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Timothy 4:17', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/01/2022
# (John 15:5) is ScriptureAug1Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug1Date = date.fromisoformat('2022-08-01')
if(ScriptureAug1Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug1.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 15:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/02/2022
# (Daniel 11:27) is ScriptureAug2Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug2Date = date.fromisoformat('2022-08-02')
if(ScriptureAug2Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug2.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Daniel 11:27', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/03/2022
# (Exodus 3:14) is ScriptureAug3Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug3Date = date.fromisoformat('2022-08-03')
if(ScriptureAug3Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug3.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Exodus 3:14', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/04/2022
# (Acts 17:24,25) is ScriptureAug4Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug4Date = date.fromisoformat('2022-08-04')
if(ScriptureAug4Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug4.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 17:24,25', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/05/2022
# (Acts 17:24,25) is ScriptureAug5Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug5Date = date.fromisoformat('2022-08-05')
if(ScriptureAug5Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug5.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Ezekiel 36:23', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/06/2022
# (Colossians 3:11) is ScriptureAug6Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug6Date = date.fromisoformat('2022-08-06')
if(ScriptureAug6Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug6.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Colossians 3:11', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/07/2022
# (Acts 17:34) is ScriptureAug7Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug7Date = date.fromisoformat('2022-08-07')
if(ScriptureAug7Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug7.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 17:34', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/08/2022
# (1 Kings 19:4) is ScriptureAug8Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug8Date = date.fromisoformat('2022-08-08')
if(ScriptureAug8Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug8.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Kings 19:4', text)

    file2 = "scriptureAug8Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/09/2022
# (Proverbs 17:17) is ScriptureAug9Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug9Date = date.fromisoformat('2022-08-09')
if(ScriptureAug9Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug9.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 17:17', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/10/2022
# (Acts 15:6) is ScriptureAug10Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug10Date = date.fromisoformat('2022-08-10')
if(ScriptureAug10Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug10.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 15:6', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/11/2022
# (Romans 12:21) is ScriptureAug11Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug11Date = date.fromisoformat('2022-08-11')
if(ScriptureAug11Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug11.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Romans 12:21', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/12/2022
# (2 Samuel 22:36) is ScriptureAug12Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug12Date = date.fromisoformat('2022-08-12')
if(ScriptureAug12Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug12.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Samuel 22:36', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/13/2022
# (2 Peter 3:9) is ScriptureAug13Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug13Date = date.fromisoformat('2022-08-13')
if(ScriptureAug13Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug13.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('2 Peter 3:9', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/14/2022
# (Psalm 25:4) is ScriptureAug14Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug14Date = date.fromisoformat('2022-08-14')
if(ScriptureAug14Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug14.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 25:4', text)

    file2 = "scriptureAug14Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/15/2022
# (John 11:5) is ScriptureAug15Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug15Date = date.fromisoformat('2022-08-15')
if(ScriptureAug15Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug15.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('John 11:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/16/2022
# (Luke 19:11) is ScriptureAug16Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug16Date = date.fromisoformat('2022-08-16')
if(ScriptureAug16Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug16.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Luke 19:11', text)

    file2 = "scriptureAug16Continued.txt"
    with open(file2, mode='r') as f2:
        text2 = f2.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('continued', text2)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/17/2022
# (Acts 24:15) is ScriptureAug17Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug17Date = date.fromisoformat('2022-08-17')
if(ScriptureAug17Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug17.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Acts 24:15', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/18/2022
# (Psalm 32:8) is ScriptureAug18Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug18Date = date.fromisoformat('2022-08-18')
if(ScriptureAug18Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug18.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Psalm 32:8', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/19/2022
# (Proverbs 1:5) is ScriptureAug19Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug19Date = date.fromisoformat('2022-08-19')
if(ScriptureAug19Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug19.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Proverbs 1:5', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/20/2022
# (Matthew 28:19,20) is ScriptureAug20Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug20Date = date.fromisoformat('2022-08-20')
if(ScriptureAug20Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug20.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Matthew 28:19,20', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/21/2022
# (1 Corinthians 15:32) is ScriptureAug21Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug21Date = date.fromisoformat('2022-08-21')
if(ScriptureAug21Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug21.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 15:32', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/22/2022
# (1 Corinthians 3:9) is ScriptureAug22Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug22Date = date.fromisoformat('2022-08-22')
if(ScriptureAug22Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug22.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 3:9', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/23/2022
# (1 John 4:7) is ScriptureAug23Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug23Date = date.fromisoformat('2022-08-23')
if(ScriptureAug23Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug23.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 John 4:7', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/24/2022
# (Galatians 5:26) is ScriptureAug24Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug24Date = date.fromisoformat('2022-08-24')
if(ScriptureAug24Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug24.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Galatians 5:26', text)

#--------------------------------------------------------

#----------------------------------------------------------
# 08/25/2022
# (1 Corinthians 7:28) is ScriptureAug25Date
# date.fromisoformat('yyyy-mm-dd')

ScriptureAug25Date = date.fromisoformat('2022-08-25')
if(ScriptureAug25Date == date.today()):
    API_KEY = "o.LqGwAtH8QWLr5KyqYeYCHgxXElxhMkGn"
    file = "scriptureAug25.txt"
    with open(file, mode='r') as f:
        text = f.read()
    pb = Pushbullet(API_KEY)
    push = pb.push_note('1 Corinthians 7:28', text)

#--------------------------------------------------------