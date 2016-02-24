from sikuli import*
import unittest
import json
import os


class FindUsPage(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + "/find-us" + Key.ENTER)
        wait(2)

    def tearDown(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)          
        wait(2)

    def test_FindABranch_BW107(self):
        click(Pattern("FindUsPage_FindABranch_Button.png").similar(0.86).targetOffset(47,-27))
        click(Pattern("findABranch_textSearch.png").targetOffset(-39,6))
        type("glen eden")
        wait(2)
        click(Pattern("FindUs_SearchABranch_Button.png").similar(0.79))
        wait(1)
        if exists(Pattern("BranchProfile_GlenEden_Title.png").similar(0.78)):
            assert True
        else:
            assert False

    def test_FindASalesperson_BW103(self):        
        click("FindUs_FindASalesprson_Button.png")
        click("FindAsalesperson_SearchBar.png")
        type("Ketiesha")
        click(Pattern("FindAsalesperson_SearchResult.png").similar(0.68))
        wait(1)
        if exists(Pattern("AgentPage_AgentTitle.png").similar(0.89)):
            assert True
        else:
            assert False

    def test_FindASalespersonDropdown_BW103(self):        
        click("FindUs_FindASalesprson_Button.png")
        click(Pattern("FindAsalesperson_Branch_Dropwdown.png").similar(0.62))
        if exists("FindUs_Dropdown_ResultResRental.png"):
            assert True
        else:
            assert False
           
    def test_FindAPropertyManager_BW104(self):
        click("FindUs_FindApropertyManager_Button.png")
        click("FindApropertyManager_SearchBar.png")
        type("Jane Auret")
        wait(1)
        click("FindApropertyManager_SearchResult.png")
        wait(1)
        if exists(Pattern("PropertyManager_PageTitle.png").similar(0.91)):
            assert True
        else:
            assert False

    def test_FindAPropertyManagerDropdown_BW104(self):
        click("FindUs_FindApropertyManager_Button.png")
        click(Pattern("FindAPropertyManager_Dropdown.png").similar(0.65))
        wait(1)
        if exists("FindUs_Dropdown_ResultResRental.png"):
            assert True
        else:
            assert False
       
    def test_FindACommercialSalesperson_BW105(self):
        click("FindUs_FindAcommercialSalesperson_Button.png")
        click("FindUs_FindACommercialSalesperson_SearchBar.png")
        type("cam paterson")
        wait(1)
        click("FindUs_FindACommercialAgent_Result.png")
        if exists(Pattern("CommercialAgent_AgentName.png").similar(0.95)):
            assert True
        else:
            assert False

    def test_FindACommercialSalespersonDropdown_BW105(self):
        click("FindUs_FindAcommercialSalesperson_Button.png")
        click(Pattern("FindACommercialAgent_Branch_Dropdown.png").similar(0.62))
        wait(1)
        if exists(Pattern("FindACommercialSalesperson_Dropdown.png").similar(0.63)):
            assert True
        else:
            assert False
            
      
    def test_FindACommercialPropertyManager_BW106(self):
        click("FindUs_FindACommercialPropertyManager_Button.png")
        click("FundAcommercialPropertyManager_SearchBar.png")
        type("Hannah")
        click("FindAcommercialPRopertyManager_Search_Button.png")
        if exists (Pattern("FindACommercialPropertyManager_Agent_Name-1.png").similar(0.78)):
            assert True
        else:
            assert False
        
    def test_FindACommercialPropertyManagerDropdown_BW106(self):
        click("FindUs_FindACommercialPropertyManager_Button.png")
        click(Pattern("FindUs_FindAcommercialPropertyManager_Dropdown.png").similar(0.62))
        wait(1)
        if exists(Pattern("FindACommercialPropertyManager_Dropdown.png").similar(0.65)):
            assert True
        else:
            assert False        

    def test_AuctionVenue_BW108(self):            
        click("FindUs_AuctionVenues_Button.png")
        wait(1)
        if exists("VenuePage_Map_Map.png"):
            assert True
        else:
            assert False

    def test_Complaints_BW109(self): 
        click("FindUs_Complaints_Button.png")
        wait(1)
        find("Complaint_PageTitle.png")
        click("OurComplaintsProcess_Button.png")
        wait(1)
        if exists(Pattern("ComplaintsProcess_TitlePage.png").similar(0.87)):
            assert True
        else:
            assert False


        
        
        
        
        
        
        
        
        
        
        
