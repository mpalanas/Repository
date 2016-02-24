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
        wait("MainPage_residentialSearch_Button.png")
        click("MainPage_residentialSearch_Button.png")
        wait(2)
        click("FrontPage_Search_Button.png")
        wait(2)
        click("ResultsPage_moreDetails_Button.png")

    def tearDown(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)


    def test_PropertyDetailAgentProperties_BW42(self):
        wheel("PropertyDetail_Detail_Tab.png", WHEEL_DOWN, 40)
        click("PropertyDetail_AgentProperties_Button.png")
        if exists("AgentPage_PropertiesPage_Title.png"):
            assert True
        else:
            assert False

    def test_PropertyDetailPrintPage_BW58(self):
        wheel("PropertyDetail_Detail_Tab.png", WHEEL_DOWN, 4)
        click("PropertyDetail_PrintPage_Button.png")
        if exists("PropertyDetail_Print_Page.png"):
            assert True
        else:
            assert False

    def test_ImageScroll_BW88(self):
        wait(2)
        click("FrontPage_Buy_Button.png")
        click("FrontPage_Search_Button.png")
        wait(2)
        find("MainPage_residentialSearch_Button.png")
        click("ResultsPage_moreDetails_Button.png")
        reg = Region(151,377,702,516)
        img = capture(reg) # take a shot
        click(Region(839,589,67,88))
        wait(3)
        if (reg.exists(Pattern(img).similar(0.99),0)): 
            assert False
        else:
            assert True

    def test_SurroundingSuburbs_BW180(self):
        wheel("PropertyDetail_Detail_Title.png", WHEEL_DOWN, 10)
        find("PropertyDetail_SurroundingSuburbs.png").below(30).left(-15).click()
        if exists(Pattern("ResultsPage_Title.png").similar(0.79)):
            assert True
        else:
            assert False
