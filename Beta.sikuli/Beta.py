import json
import os

configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
config = json.loads(open(configPath).read())

type("l", KeyModifier.CTRL)
type(config["url"]+"/sell/property-appraisal" + Key.ENTER)
wait(1)
wheel(Pattern("1456279042865-1.png").similar(0.89), WHEEL_DOWN,2)
wait(1)
click(Pattern("1456278494997-1.png").similar(0.68).targetOffset(-29,13))
type("Lambrown drive")
type(Key.TAB)
type("TestName")
type(Key.TAB)
type("TestEmail@test.com")
type(Key.TAB)
type("09 123 5689")
type(Key.TAB)
wait(1)
wheel(Pattern("1456279554509-1.png").targetOffset(-35,-1), WHEEL_DOWN,2)
click(Pattern("1456279554509-1.png").targetOffset(-35,-1))
click(Pattern("1456280641894.png").targetOffset(-27,7))
type("anytime")

click("1456280363910.png")
type("albany" + Key.ENTER)
wait(2)
click("1456280938856.png")

type("amber" + Key.ENTER)
click("1456278623428-1.png")