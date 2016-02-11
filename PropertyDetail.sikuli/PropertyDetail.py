from sikuli import*
import unittest
import json
import os

class PropertyDetail(unittest.TestCase):

    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)
        wait(2)
        click("FrontPage_Search_Button.png")
        wait(2)
        find("1447889264312.png")
        click("1455070789944.png")

    def tearDown(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)


    def test_PropertyDetailAgentProperties(self):
        wheel("1455070857902.png", WHEEL_DOWN, 40)
        click("1455070876266.png")
        if exists("1455070888622.png"):
            assert True
        else:
            assert False

    def test_PropertyDetailPrintPage(self):
        wheel("1455070857902.png", WHEEL_DOWN, 4)
        click("1455070946211.png")
        if exists("1455070967717.png"):
            assert True
        else:
            assert False

    def test_ImageScroll(self):
        wait(2)
        click("FrontPage_Buy_Button.png")
        click("FrontPage_Search_Button.png")
        wait(2)
        find("1447889264312.png")
        click("1455070789944.png")
        reg = Region(151,377,702,516)
        img = capture(reg) # take a shot
        click(Region(839,589,67,88))
        wait(3)
        if (reg.exists(Pattern(img).similar(0.99),0)): 
            assert False
        else:
            assert True
