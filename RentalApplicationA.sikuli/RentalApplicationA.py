#Step1
find(Pattern("1455655966582.png").similar(0.55)).left(30).click()
click("1455656038270.png")
wait(2)
click(Pattern("1455656921387.png").similar(0.77))
type("glenfield")
find("1455656302174.png").below(30).click()
click("1455656339947.png")
if exists(Pattern("1455657408589.png").similar(0.60)):
    click(Pattern("1455657408589.png").similar(0.60).targetOffset(-21,8))
    
find("1455656385633.png")
click(Pattern("1455657761656.png").similar(0.65).targetOffset(28,13))
wheel(Pattern("1455657761656.png").similar(0.65).targetOffset(28,13),WHEEL_DOWN,5)
click("1455656413899.png")
click("1455656458134.png")
click("1455656477945.png")

#Step2
click(Pattern("1455659246497.png").similar(0.68).targetOffset(4,-20))
click("1455659447729.png")
click(Pattern("1455659246497.png").similar(0.68).targetOffset(1,39))
type("Applicant A")
    
click(Pattern("1455660142024.png").similar(0.84).targetOffset(-3,7))
type("1 Glenfield Road")
click(Pattern("1455660184558.png").similar(0.76).targetOffset(-3,13))
type("Glenfield")
click(Pattern("1455660225944.png").similar(0.77).targetOffset(2,7))
type("Auckland")    
wheel("1455660359664.png", WHEEL_DOWN,5)
click(Pattern("1455660502565.png").similar(0.90).targetOffset(-4,13))
type("Two Years")
click(Pattern("1455660552249.png").similar(0.79).targetOffset(4,15))
type("as soon as possible")
click(Pattern("1455660538873.png").similar(0.86).targetOffset(-3,4))
type("as long as possible!")

click(Pattern("1455660783646.png").similar(0.80).targetOffset(2,17))
type("09 444 3586")
click(Pattern("1455660813952.png").targetOffset(1,10))
type("0211145786")
click(Pattern("1455660843144.png").similar(0.81).targetOffset(0,6))
type("307 6320")
wheel("1455661017292.png", WHEEL_DOWN,3)
click("1455661206608.png")
type("testApplication@barfoot.co.nz")
click(Pattern("1455661240112.png").targetOffset(0,13))
type("testApplication@barfoot.co.nz")
click(Pattern("1455662832628.png").similar(0.77))
click("1455661682162.png")
click(Pattern("1455662855965.png").similar(0.78))
click("1455661716212.png")
click(Pattern("1455662878820.png").similar(0.82))
click("1455662032323.png")
click(Pattern("1455661968683.png").targetOffset(9,21))
wheel(Pattern("1455662145428.png").similar(0.87), WHEEL_DOWN,5)
find(Pattern("1455662171681.png").similar(0.80)).left(15).click()
find(Pattern("1455662230141.png").similar(0.80)).left(15).click()
click(Pattern("1455662466135.png").similar(0.82).targetOffset(-3,9))
type("PassportTest NDER12354")
click(Pattern("1455662505638.png").similar(0.91).targetOffset(-2,10))
type("Licence5a DE21341")
click(Pattern("1455662559766.png").similar(0.84).targetOffset(0,13))
type("Licence5b 542")
