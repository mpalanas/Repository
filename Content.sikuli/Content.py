from sikuli import*
import unittest
import json
import os


class Content(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)
        find("barfootLogo.png")

    def tearDown(self):

        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)
        wait(2)
    
    def test_BuyContent(self):
        
        click(Pattern("MainPage_Buy_Button.png").similar(0.76))
        if exists(Pattern("MainPage_Buy.png").similar(0.92)):
            assert True
        else:
            assert False

    def test_SellContent(self):
        click("MainPage_Sell_Button.png")
        if exists(Pattern("MainPage_Sell.png").similar(0.95)):
            assert True
        else:
            assert False

    def test_CommercialContent(self):
        click(Pattern("MainPage_Commercial_Button.png").similar(0.76))
        if exists("MainPage_Commercial.png"):
            assert True
        else:
            assert False
            
    def test_RentContent(self):
        click("MainPage_Rent_Button.png")
        if exists(Pattern("MainPage_Rent.png").similar(0.85)):
            assert True
        else:
            assert False

    def test_PropertyManagementContent(self):
        click("MainPage_PropertyManagement_Button.png")
        if exists(Pattern("MainPage_PropertyManagement.png").similar(0.95)):
            assert True
        else:
            assert False

    def test_BodyCorporateContent(self):            
        click("MainPage_BodyCorporate_Button.png")
        if exists(Pattern("MainPage_BodyCorporate.png").similar(0.90)):
            assert True
        else:
            assert False

    def test_AboutUs(self):            
        click("MainPage_About_Button.png")
        if exists(Pattern("AboutUsPage.png").exact()):
            assert True
        else:
            assert False

    def test_Careers(self):
        click("MainPage_Careers_Button.png")
        if exists(Pattern("CareersPage_TitlePage.png").exact()):
            assert True
        else:
            assert False

    def test_MarketReport(self):
        click("MainPage_MarketReports_Button.png")                
        click(Pattern("MarketReport_2011_Button.png").similar(0.79))
        click(Pattern("MarketReport_2011December_Button.png").similar(0.83))
        click("MarketReport_2011DecemberMarketUpdate_Button.png")
        if exists(Pattern("MarketReport_MarketUpdate_Title.png").similar(0.91)):
            assert True
        else:
            assert False

    def test_News(self):
        click("MainPage_News_Button.png")
        if exists(Pattern("NewsPage_Title.png").similar(0.80)):
            assert True
        else:
            assert False

    def test_FindUs(self):
        click(Pattern("MainPage_FindUs_Button.png").similar(0.82))
        if exists(Pattern("1454382321041.png").similar(0.85)):
            assert True
        else:
            assert False







