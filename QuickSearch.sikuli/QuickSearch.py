from sikuli import*
import unittest
import json
import os

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
        click(Pattern("MainPage_quickSearch_textbox.png").similar(0.94).targetOffset(-24,19))

    def tearDown(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)
        wait(2)

    def test_addressIDSearch_BW5(self):        
        
        type("Glenfield")
        find(Pattern("MainPage_SearchBar_Results.png").similar(0.50))
        click(Pattern("MainPage_quicksearch_Button.png").similar(0.91).targetOffset(-1,26))
        wait(3)
        if exists(Pattern("PropertyDetailPage_saveProperty_Button.png").similar(0.82)):
            assert True
        else:
            assert False
            
    def test_branch_BW5(self): 
        paste("Manurewa branch")
        wait (3)
        #find("mainPage_quickSearch_resultHeading.png")
        click(Pattern("MainPage_quicksearch_Button.png").similar(0.90).targetOffset(-1,26))
        
        if exists(Pattern("BranchPage_BranchHeading_Manurewa.png").similar(0.85)):
            assert True
        else:
            assert False
            
    def test_propertyID_BW5(self): 
        type("15000")
        click(Pattern("MainPage_quicksearch_Button.png").similar(0.89).targetOffset(-1,26))
        if exists(Pattern("propertyDetail_rentalapplication_Button.png").similar(0.72)):
            assert True
        else:
            assert False

    def test_agentName_BW5(self): 
       
        type("Ketiesha" + Key.ENTER)
        if exists(Pattern("AgentPage_AgentHeading.png").similar(0.85)):
            assert True
        else:
            assert False
            
    def test_noResults(self):
        type("incorrect details" + Key.ENTER)
        if exists("quickSearch_noResult.png"):
            assert True
        else:
            assert False
        
        










