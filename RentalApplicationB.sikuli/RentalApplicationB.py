import time
timestr = time.strftime("%d%m%Y%H%M%S")
applicantName = timestr + " LastName"
find(Pattern("1455655966582.png").similar(0.55)).left(30).click()
click("1455656038270.png")
wait(2)
click(Pattern("1455656921387.png").similar(0.77))
type("11000957")
wait(1)
#find("1455656302174.png").below(30).click()
find("1456185817505.png").below(30).click()
click("1455656339947.png")
wait(2)
if exists(Pattern("1455657408589.png").similar(0.60)):
    click(Pattern("1455657408589.png").similar(0.60).targetOffset(-21,8))
    
find("1455656385633.png")
click(Pattern("1455657761656.png").similar(0.65).targetOffset(28,13))
wheel("1455681983074.png",WHEEL_DOWN,5)
wait(1)
click(Pattern("1455656413899.png").similar(0.77))
click("1455656458134.png")
click("1455656477945.png")

#Step2

click(Pattern("1455659246497-2.png").similar(0.68).targetOffset(4,-20))
click("1455659447729-2.png")
click(Pattern("1455659246497-2.png").similar(0.68).targetOffset(1,39))
type(applicantName)
    
click(Pattern("1455660142024-2.png").similar(0.84).targetOffset(-3,7))
type("1 Glenfield Road")
click(Pattern("1455660184558-2.png").similar(0.76).targetOffset(-3,13))
type("Glenfield")
click(Pattern("1455660225944-2.png").similar(0.77).targetOffset(2,7))
type("Auckland")  
wheel("1455660359664-5.png", WHEEL_DOWN,5)
wait(1)
click(Pattern("1455660502565-4.png").similar(0.82).targetOffset(-4,13))
type("Two Years")
click(Pattern("1455660552249-4.png").similar(0.82).targetOffset(4,15))
type("as soon as possible")
click(Pattern("1455660538873-4.png").similar(0.86).targetOffset(-3,4))
type("as long as possible!")

click(Pattern("1455660783646-4.png").similar(0.80).targetOffset(2,17))
type("09 444 3586")
click(Pattern("1455660813952-4.png").targetOffset(1,10))
type("0211145786")

wheel("1455661017292-2.png", WHEEL_DOWN,3)
wait(1)
click("1455661206608-3.png")
type("testApplication@barfoot.co.nz")
click(Pattern("1455661240112-3.png").targetOffset(0,13))
type("testApplication@barfoot.co.nz")
click(Pattern("1455662832628-2.png").similar(0.77))
click("1455661682162-3.png")
click(Pattern("1455662855965-2.png").similar(0.78))
click("1455661716212-2.png")
click(Pattern("1455662878820-2.png").similar(0.82))
click("1455662032323-2.png")
click(Pattern("1455681860026.png").targetOffset(-31,-35))
wheel("1455673062585-1.png", WHEEL_DOWN,5)
find(Pattern("1455662171681-2.png").similar(0.80)).left(15).click()
click(Pattern("1455662466135-2.png").similar(0.82).targetOffset(-3,9))
type("PassportTest NDER12354")
click("1455673329856-2.png")

#Step3
click(Pattern("1455674896081-1.png").similar(0.67).targetOffset(-30,21))

click(Pattern("1455675044240-1.png").targetOffset(-14,14))
wheel("1455675282089-1.png", WHEEL_DOWN,5)
wait(1)
click(Pattern("1455675060320-1.png").similar(0.73).targetOffset(-9,20))

wheel("1455675562883-1.png", WHEEL_DOWN,3)

wait(1)
click(Pattern("1455675676709-1.png").similar(0.63))

#step4

click(Pattern("1455677614717-5.png").targetOffset(-16,21))
find("1456100413941-2.png").below(170).left(-80).click()
find("1456100586243.png").below(170).left(-80).click()
find("1456100597372.png").below(170).left(-80).click()

click(Pattern("1455679905486-8.png").similar(0.57))

#step5

click(Pattern("1455759702970-2.png").similar(0.66).targetOffset(-62,16))
wait(1)
find("1456100812877-1.png").below(170).left(-80).click()
wait(1)
type("Contract work")
click("1456100859888-1.png")
wait(1)
click(Pattern("1456102204827-1.png").similar(0.54))
wait(1)
find("1456101029615.png").below(150).click()
wait(1)
wheel("1455761100673-2.png", WHEEL_DOWN,5)
wait(1)
click(Pattern("1456086792446-1.png").similar(0.71).targetOffset(-1,11))
type("Voda")
wait(1)
click(Pattern("1456086801834-1.png").similar(0.69))
type("Tier 2 Tech")
wait(1)
click(Pattern("1456086899636-1.png").similar(0.65))
type("2 years")
wheel("1456101341357.png", WHEEL_DOWN,3)
wait(2)
click("1455760150000-1.png")
type("Previous Manager")
click("1455760179837-1.png")
type("0900 586 321")
click("1455760727159-1.png")
type("simon@test.com")
click(Pattern("1456087338568.png").similar(0.55))

#Step6
find(Pattern("1456088158446.png").similar(0.75)).below(30).click()
type("Joe Bloggs")
find(Pattern("1456088187639.png").similar(0.78)).below(30).click()
type( "Colin Wild Place Glenfield")
find(Pattern("1456088209202.png").similar(0.67)).below(30).click()
type("Brother")
find(Pattern("1456088230246.png").similar(0.75)).below(30).click()
type("09 358 1236")
find(Pattern("1456088463164.png").similar(0.75)).below(30).click()
type("test@Contact.com")
click("1456087793261.png")

#Step7
click(Pattern("1456089231619.png").similar(0.52).targetOffset(-127,26))
type("Referee 1 Test")
type(Key.TAB)           
type("referee@email.com")

wait(1)
click(Pattern("1456090427512.png").similar(0.91).targetOffset(33,-4))
wait(1)
wheel("1456090484018.png", WHEEL_DOWN, 2)
wait(1)
click(Pattern("1456089711355.png").similar(0.77).targetOffset(-68,-15))
click("1456091721790.png")

print(applicantName)