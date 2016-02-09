from sikuli import*
import unittest
import json
import os

class FooterLinks(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)
        type(Key.PAGE_DOWN + Key.PAGE_DOWN)

    def tearDown(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)
        wait(2)

    def test_FooterAuctions(self):
        click(Pattern("MainPage_Footer_Auctions.png").similar(0.76))
        wait(1)
        if exists(Pattern("ThisWkAuctionPage_Title.png").similar(0.68)):
            assert True
        else:
            assert False

    def test_FooterAuctionVenues(self):
        click(Pattern("MainPage_Footer_AuctionsVenues.png").similar(0.74))
        wait(1)
        if exists(Pattern("1454961118035.png").similar(0.86)):
            assert True
        else:
            assert False
    
    def test_FooterMortgageeSales(self):
        click(Pattern("MainPage_Footer_MortgageeSales.png").similar(0.76))
        
        if exists(Pattern("MainPageSearch_MortgageeSales_Title.png").similar(0.85)):
            assert True
        else:
            assert False
            
    def test_FooterMortgageeSales(self):
        click(Pattern("MainPage_Footer_OpenHomes.png").similar(0.76))
        wait(1)
        if exists(Pattern("PropertySearch_OpenHomes_CheckBox.png").similar(0.77)):
            assert True
        else:
            assert False
                    
    def test_FooterSearchSoldProperties(self):
        click(Pattern("MainPage_Footer_SearchSoldProperties.png").similar(0.66).targetOffset(-3,1))
        wait(1)
        if exists(Pattern("SearchSoldProperties_SoldSticker.png").exact()):
            assert True
        else:
            assert False


    def test_MobileSite(self):
        click(Pattern("MainPage_Footer_MobileSite.png").similar(0.73))
        wait(1)

        if exists(Pattern("MobileSite_HamburgerButton.png").exact()):
            assert True
        else:
            assert False
        click(Pattern("MobileSite_DesktopSite_Button.png").similar(0.74))
        wait(4)
        
        
    def test_AppStoreLink(self):
        click("MainPage_DownloadApp.png")
        wait(3)
        if exists(Pattern("AppStore_BarfootAppLogo.png").exact()):
            assert True
        else:
            assert False
