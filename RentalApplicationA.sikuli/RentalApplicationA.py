import time
timestr = time.strftime("%d%m%Y%H%M%S")
applicantName = timestr + " LastName"
#Step1
find(Pattern("1455655966582.png").similar(0.55)).left(30).click()
click("1455656038270.png")
wait(2)
click(Pattern("1455656921387.png").similar(0.77))
type("glenfield")
find("1455656302174.png").below(30).click()
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
click(Pattern("1455660843144-4.png").similar(0.81).targetOffset(0,6))
type("307 6320")
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
click(Pattern("1455681860026.png").targetOffset(13,-39))
wheel("1455673062585-1.png", WHEEL_DOWN,5)
find(Pattern("1455662171681-2.png").similar(0.80)).left(15).click()
find(Pattern("1455662230141-2.png").similar(0.80)).left(15).click()
click(Pattern("1455662466135-2.png").similar(0.82).targetOffset(-3,9))
type("PassportTest NDER12354")
click(Pattern("1455662505638-2.png").similar(0.91).targetOffset(-2,10))
type("Licence5a DE21341")
click(Pattern("1455662559766-2.png").similar(0.84).targetOffset(0,13))
type("Licence5b 542")
click("1455673329856-2.png")

#Step3
click(Pattern("1455674896081-1.png").similar(0.67).targetOffset(13,11))
click(Pattern("1455674999136-1.png").similar(0.62))
type("Dog")
click(Pattern("1455675044240-1.png").targetOffset(26,13))
wheel("1455675282089-1.png", WHEEL_DOWN,5)
wait(1)
click(Pattern("1455675060320-1.png").similar(0.73).targetOffset(32,17))

click(Pattern("1455675073709-1.png").similar(0.76))
type("Nissan")
wait(1)
click("1455677033216-1.png")
type("Demio")
wait(1)
click(Pattern("1455675147869-1.png").similar(0.71).targetOffset(4,8))
type("GMF123")
wheel("1455675562883-1.png", WHEEL_DOWN,3)
wait(1)
click(Pattern("1455676740079-1.png").targetOffset(-6,-19))
type("Maric")
click(Pattern("1455675602911-1.png").targetOffset(0,-9))
wait(1)
click(Pattern("1455676740079-1.png").targetOffset(-6,-19))
type("Chris")
click("1455675602911-1.png")
wait(1)
click(Pattern("1455675676709-1.png").similar(0.63))

#step4
click(Pattern("1455677614717-5.png").targetOffset(31,20))
wait(2)
find(Pattern("1455761442965-7.png").similar(0.80)).below(100).click()
type("$470")
click(Pattern("1455677717710-9.png").similar(0.75))
click(Pattern("1455761602491-7.png").similar(0.77))
click("1455677755600-8.png")
type("Carol")
wheel("1455677782110-8.png", WHEEL_DOWN,3)
wait(1)
click("1455677782110-8.png")
type("021 145 6987")
click("1455677882084-8.png")
type("09 444 3580")
click("1455677904961-8.png")
type("carol@landlord.co.nz")
find("1455761731489-7.png").below(115).click()
type("Looking for a better Property")
wheel("1455761731489-7.png", WHEEL_DOWN,4)
wait(1)
find("1455762039229-6.png").below(115).click()
wheel("1455678464106-8.png", WHEEL_DOWN,2)
wait(1)
click("1455678524281-8.png")
type("2 Waratah Street")
click(Pattern("1455678557284-8.png").targetOffset(19,8))
wait(1)
click("1455661682162-11.png")
click("1455678745204-8.png")
wait(1)
click("1455678757278-8.png")
click(Pattern("1455762426071-4.png").similar(0.74))
wait(1)
click("1455679433388-8.png")
click(Pattern("1455679089434-8.png").targetOffset(2,5))
type("$390")
find("1455762836799-5.png").above(90).click()
type("2 years")
wheel("1455762836799-5.png", WHEEL_DOWN,2)
wait(1)
click(Pattern("1455677717710-9.png").similar(0.75))
click(Pattern("1455763202366-3.png").similar(0.78))
click("1455679301627-8.png")
type("Tracey Manurewa")
click(Pattern("1455679332376-8.png").targetOffset(4,14))
type("021987654")
wheel("1455679626494-8.png", WHEEL_DOWN,4)
wait(1)
find(Pattern("1455763977615-7.png").targetOffset(32,-1)).below(135).click()
wait(1)
find(Pattern("1455763977615-6.png").targetOffset(32,-1)).below(300).click()
type("Tenancy was terminated due to the property manager")
wheel("1455680005858-9.png", WHEEL_DOWN,4)
click(Pattern("1455679863250-9.png").targetOffset(20,-13))
click(Pattern("1455680592123-9.png").similar(0.66).targetOffset(-1,-36))

type("Property was left in a bad condition")
click(Pattern("1455679905486-8.png").similar(0.57))

#Step5
click(Pattern("1455759702970-1.png").similar(0.66).targetOffset(-7,15))
wait(1)
click(Pattern("1456086792446.png").similar(0.71).targetOffset(-1,11))
type("Barfoot")
wait(1)
click(Pattern("1456086801834.png").similar(0.69))
type("TestAnalyst")
wait(1)
click(Pattern("1456086899636.png").similar(0.65))
type("3 years")
click("1455759828241-1.png")
wait(1)
click(Pattern("1456087155050.png").similar(0.73))
wheel("1455760115161-1.png", WHEEL_DOWN,3)
wait(2)
click("1455760150000-1.png")
type("Simon Casey")
click("1455760179837-1.png")
type("09 444 6320")
click("1455760705886-1.png")
type("09 444 6321")
click("1455760727159-1.png")
type("simon@test.com")
wheel("1455761100673-1.png", WHEEL_DOWN,2)
wait(1)
find(Pattern("1456093773287.png").similar(0.64)).below(50).left(-50).click()
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
type(Key.TAB)  
type("Referee 2 Test")
type(Key.TAB) 
type("09 358 2136")
type(Key.TAB)
type("Referee 3 Test")
type(Key.TAB)
type("021 111 5469")
wait(1)
click(Pattern("1456090427512.png").similar(0.91).targetOffset(33,-4))
wait(1)
wheel("1456090484018.png", WHEEL_DOWN, 2)
wait(1)
click(Pattern("1456089711355.png").similar(0.77).targetOffset(-30,-20))
click(Pattern("1456089761599.png").similar(0.68))
type("Additional comments to help out on the application")

click("1456091721790.png")

print(applicantName)



















