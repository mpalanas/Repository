from sikuli import*
import unittest
import json


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
        find("barfootLogo-1.png")
        wheel("MainPage_FindUs.png", WHEEL_DOWN, 10)

    def tearDown(self):
        click(Pattern("closeButtonChrome-1.png").targetOffset(24,-2))
        wait(2)

    def test_FooterAuctions(self):
        click("MainPage_Footer_Auctions.png")
        wait(1)
        if exists(Pattern("ThisWkAuctionPage_Title.png").exact()):
            assert True
        else:
            assert False

    def test_FooterAuctionVenues(self):
        click("MainPage_Footer_AuctionsVenues.png")
        wait(1)
        if exists(Pattern("AuctionVenuesPage_Title.png").exact()):
            assert True
        else:
            assert False
    
    def test_FooterMortgageeSales(self):
        click("MainPage_Footer_MortgageeSales.png")
        #find(Pattern("PropertySearch_MortgageeSales_CheckBox.png").exact())
        
        if exists(Pattern("MainPageSearch_MortgageeSales_Title.png").exact()):
            assert True
        else:
            assert False
            
    def test_FooterMortgageeSales(self):
        click("MainPage_Footer_OpenHomes.png")
        wait(1)
        if exists(Pattern("PropertySearch_OpenHomes_CheckBox.png").exact()):
            assert True
        else:
            assert False
                    
    def test_FooterSearchSoldProperties(self):
        click(Pattern("MainPage_Footer_SearchSoldProperties.png").targetOffset(-3,1))
        wait(1)
        find(Pattern("SearchSoldProperties_SoldSticker.png").exact())
        if exists(Pattern("SoldPropertyPage_PropertyTitle.png").similar(0.91)):
            assert True
        else:
            assert False


    def test_MobileSite(self):
        click("MainPage_Footer_MobileSite.png")
        wait(1)

        if exists(Pattern("MobileSite_HamburgerButton.png").exact()):
            assert True
        else:
            assert False
        click("MobileSite_DesktopSite_Button.png")
        wait(4)
        
        
    def test_AppStoreLink(self):
        click("MainPage_DownloadApp.png")
        wait(3)
        if exists(Pattern("AppStore_BarfootAppLogo.png").exact()):
            assert True
        else:
            assert False
