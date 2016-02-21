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

    def test_AuctionsAndOrderOfSaleDropdown(self):
        click(Pattern("MainPage_Footer_Auctions-1.png").similar(0.76))
        reg = Region(135,540,290,181)
        img = capture(reg)
        click("AuctionsPage_Venue_Dropdown.png")
        find("AuctionsPage_Venue_Dropdown.png").below(60).click()
        wait(3)
        if (reg.exists(Pattern(img).similar(0.99),0)): 
            assert False
        else:
            assert True

    def test_AuctionsAndOrderOfSaleSessions(self):
        click(Pattern("MainPage_Footer_Auctions-2.png").similar(0.76))
        reg = Region(135,540,290,181)
        img = capture(reg)
        find("AuctionsPage_Venue_Dropdown-1.png").right(800).click()
        wait(3)
        if (reg.exists(Pattern(img).similar(0.99),0)): 
            assert False
        else:
            assert True

        

    def test_FooterAuctionVenues(self):
        click(Pattern("MainPage_Footer_AuctionsVenues.png").similar(0.74))
        wait(1)
        if exists(Pattern("AuctionVenue_Map.png").similar(0.86)):
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
                    
    def test_FooterSoldProperties(self):
        click(Pattern("MainPage_Footer_SearchSoldProperties.png").similar(0.66).targetOffset(-3,1))
        wait(1)
        if exists(Pattern("SearchSoldProperties_SoldSticker.png").exact()):
            assert True
        else:
            assert False

    def test_FooterSearchSoldProperties(self):
        reg = Region(159,570,265,187)
        img = capture(reg)
        click("SearchSoldProperties_Region_Dropdown.png")
        wait(1)
        click("SearchSoldProperties_Auckland_Region.png")
        wait(2)
        click("SearchSoldProperties_Suburb_Dropdown.png")
        wait(1)
        click("SearchSoldProperties_Epsom_Suburb.png")
        click(Pattern("SearchSoldProperties_PropertyType_Dropdownv.png").targetOffset(-7,10))
        wait(1)
        find("SearchSoldProperties_House_PropertyType.png").left(15).click()
        find("SearchSoldProperties_Unit_PropertyType.png").left(15).click()
        wait(1)
        click(Pattern("SearchSoldProperties_Bedrooms_Dropdown.png").targetOffset(-4,7))
        wait(1)
        click(Pattern("SearchSoldProperties_2_Bedrooms.png").similar(0.81))
        wait(1)
        find("SearchSoldProperties_PropertyType2Selected_Dropdown.png").right(500).click()
        wait(1)
        click("SearchSoldProperties_2_PropertyType.png")
        wait(1)
        click("SearchSoldProperties_Bathrooms_Dropdown.png")
        wait(1)
        click("SearchSoldProperties_1_Bathroom.png")
        wait(1)
        find(Pattern("SearchSoldProperties_SoldBy_PageName.png").similar(0.78)).below(310).click()
        wait(1)
        click(Pattern("SearchSoldProperties_345_Bathroom.png").similar(0.59).targetOffset(-30,1))
        wait(1)
        click("SearchSoldProperties_Search_Button.png")
        wait(2)
        if (reg.exists(Pattern(img).similar(0.99),0)): 
            assert False
        else:
            assert True



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
        click("MainPage_DownloadAppIos.png")
        wait(3)
        if exists(Pattern("AppStore_BarfootAppLogo.png").exact()):
            assert True
        else:
            assert False

    def test_AppStoreLink(self):
        click("MainPage_DownloadAppAndroid.png")
        wait(3)
        if exists(Pattern("AndroidStore_BarfootAppLogo.png").exact()):
            assert True
        else:
            assert False
