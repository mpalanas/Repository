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
    
    def test_BuyContent_BW3(self):
        
        click(Pattern("MainPage_Buy_Button.png").similar(0.76))
        wait(1)
        if exists(Pattern("MainPage_Buy.png").similar(0.87)):
            assert True
        else:
            assert False

    def test_SellContent(self):
        click("MainPage_Sell_Button.png")
        wait(1)
        if exists(Pattern("MainPage_Sell.png").similar(0.84)):
            assert True
        else:
            assert False

    def test_CommercialContent(self):
        click(Pattern("MainPage_Commercial_Button.png").similar(0.76))
        wait(1)
        if exists(Pattern("MainPage_Commercial.png").similar(0.77)):
            assert True
        else:
            assert False
            
    def test_RentContent(self):
        click("MainPage_Rent_Button.png")
        wait(1)
        if exists(Pattern("1456262407403.png").similar(0.75)):
            assert True
        else:
            assert False

    def test_PropertyManagementContent_BW3(self):
        click("MainPage_PropertyManagement_Button.png")
        if exists("MainPage_PropertyManagement.png"):
            assert True
        else:
            assert False

    def test_BodyCorporateContent_BW3(self):            
        click("MainPage_BodyCorporate_Button.png")
        wait(1)
        if exists(Pattern("MainPage_BodyCorporate.png").similar(0.86)):
            assert True
        else:
            assert False

    def test_AboutUs_BW3(self):            
        click("MainPage_About_Button.png")
        if exists(Pattern("AboutUsPage.png").exact()):
            assert True
        else:
            assert False

    def test_Careers_BW3(self):
        click("MainPage_Careers_Button.png")
        if exists(Pattern("CareersPage_TitlePage.png").exact()):
            assert True
        else:
            assert False

    def test_MarketReport_BW4(self):
        click("MainPage_MarketReports_Button.png")
        wait(3)
        find("MarketReport_MarketReport_Button.png").below(50).left(-50).click()
        wait(1)
        click(Pattern("MarketReport_2015January_Button.png").similar(0.82))
        wait(1)
        click(Pattern("MarketReport_2015HousingMarketUpdate_Button.png").similar(0.82))
        wait(1)
        if exists(Pattern("MarketReport_MarketUpdate_Title.png").similar(0.89)):
            assert True
        else:
            assert False

    def test_News_BW3(self):
        click("MainPage_News_Button.png")
        if exists(Pattern("NewsPage_Title.png").similar(0.80)):
            assert True
        else:
            assert False

    def test_FindUs_BW3(self):
        click(Pattern("MainPage_FindUs_Button.png").similar(0.82))
        if exists(Pattern("MainPage_FindUsPage.png").similar(0.85)):
            assert True
        else:
            assert False

    def test_SellContent(self):
        type("l", KeyModifier.CTRL)
        type(config["url"]+"/sell/property-appraisal" + Key.ENTER)
        wait(1)
        wheel(Pattern("Title_PropertyAppraisal.png").similar(0.89), WHEEL_DOWN,2)
        wait(1)
        click(Pattern("RequestAppraisalPage_AddressField_Text.png").similar(0.68).targetOffset(-29,13))
        type("Lambrown drive")
        type(Key.TAB)
        type("TestName")
        type(Key.TAB)
        type("TestEmail@test.com")
        type(Key.TAB)
        type("09 123 5689")
        type(Key.TAB)
        wait(1)
        wheel(Pattern("RequestAppraisalPage_ByPhone_RadioButton.png").targetOffset(-35,-1), WHEEL_DOWN,2)
        click(Pattern("RequestAppraisalPage_ByPhone_RadioButton.png").targetOffset(-35,-1))
        click(Pattern("RequestAppraisalPage_BestTimeToCall_Text.png").targetOffset(-27,7))
        type("anytime")
        
        click("RequestAppraisalPage_SelectBranch_Dropdown.png")
        type("albany" + Key.ENTER)
        wait(2)
        click("RequestAppraisalPage_SelectSalesperson_Dropdown.png")
        
        type("amber" + Key.ENTER)
        click("RequestAppraisalPage_Submit_Button.png")
        if exists("RequestAppraisalPage_EmailConfirmation.png"):
            assert True
        else:
            assert False







