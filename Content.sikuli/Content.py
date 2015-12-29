from sikuli import*
import unittest
import json

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

        click(Pattern("closeButtonChrome.png").targetOffset(17,-1))
    
    def test_BuyContent(self):
        
        click("MainPage_Buy_Button.png")
        if exists(Pattern("MainPage_Buy.png").exact()):
            assert True
        else:
            assert False

    def test_SellContent(self):
        click("MainPage_Sell_Button.png")
        if exists(Pattern("MainPage_Sell.png").exact()):
            assert True
        else:
            assert False

    def test_CommercialContent(self):
        click("MainPage_Commercial_Button.png")
        if exists("MainPage_Commercial.png"):
            assert True
        else:
            assert False
            
    def test_RentContent(self):
        click("MainPage_Rent_Button.png")
        if exists(Pattern("MainPage_Rent.png").exact()):
            assert True
        else:
            assert False

    def test_PropertyManagementContent(self):
        click("MainPage_PropertyManagement_Button.png")
        if exists(Pattern("MainPage_PropertyManagement.png").exact()):
            assert True
        else:
            assert False

    def test_BodyCorporateContent(self):            
        click("MainPage_BodyCorporate_Button.png")
        if exists(Pattern("MainPage_BodyCorporate.png").exact()):
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
        click("MarketReport_2011_Button.png")
        click("MarketReport_2011December_Button.png")
        click("MarketReport_2011DecemberMarketUpdate_Button.png")
        if exists(Pattern("MarketReport_MarketUpdate_Title.png").exact()):
            assert True
        else:
            assert False

    def test_News(self):
        click("MainPage_News_Button.png")
        if exists(Pattern("NewsPage_Title.png").exact()):
            assert True
        else:
            assert False

    def test_News(self):
        click("MainPage_FindUs_Button.png")
        if exists(Pattern("FindUsPage_FindUs.png").exact()):
            assert True
        else:
            assert False







