from sikuli import*
import unittest
import json


class QuickSearch(unittest.TestCase):
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
        click("MainPage_quickSearch_textbox.png")

    def tearDown(self):
        click(Pattern("closeButtonChrome-1.png").targetOffset(24,-2))
        wait(2)

    def test_addressIDSearch(self):        
        
        type("Glenfield")
        find("MainPage_quicksearch_listingHeadingResult.png")
        click(Pattern("MainPage_quicksearch_Button.png").targetOffset(-1,26))
        wait(3)
        if exists(Pattern("PropertyDetailPage_saveProperty_Button.png").exact()):
            assert True
        else:
            assert False
            
    def test_branch(self): 
        paste("Manurewa branch")
        wait (3)
        find("mainPage_quickSearch_resultHeading.png")
        click(Pattern("MainPage_quicksearch_Button.png").targetOffset(-1,26))
        
        if exists(Pattern("BranchPage_BranchHeading_Manurewa.png").exact()):
            assert True
        else:
            assert False
            
    def test_propertyID(self): 
        type("15000")
        click(Pattern("MainPage_quicksearch_Button.png").targetOffset(-1,26))
        if exists(Pattern("propertyDetail_rentalapplication_Button.png").exact()):
            assert True
        else:
            assert False

    def test_propertyID(self): 
       
        type("Ketiesha" + Key.ENTER)
        if exists(Pattern("AgentPage_AgentHeading.png").similar(0.97)):
            assert True
        else:
            assert False
            











