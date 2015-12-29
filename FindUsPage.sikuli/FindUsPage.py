from sikuli import*
import unittest
import json

class FindUsPage(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)
        click("FrontPage_FindUS_Button.png")
        wait(1)

    def tearDown(self):
        click(Pattern("closeButtonChrome-1.png").targetOffset(24,-2))           
        wait(2)

    def test_FindABranch(self):
        click(Pattern("FindUs_FindABranch_button.png").targetOffset(-85,-27))
        click(Pattern("findABranch_textSearch.png").targetOffset(-39,6))
        type("glenfield branch")
        wait(1)
        find("FindABranch_Glenfield_Button.png")
        click("FindUs_SearchABranch_Button.png")
        wait(1)
        if exists(Pattern("BranchTitle_Glenfield.png").exact()):
            assert True
        else:
            assert False

    def test_FindASalesperson(self):        
        click("FindUs_FindASalesprson_Button.png")
        click("FindAsalesperson_SearchBar.png")
        type("Ketiesha")
        click("FindAsalesperson_SearchResult.png")
        wait(1)
        if exists(Pattern("AgentPage_AgentTitle.png").exact()):
            assert True
        else:
            assert False

    def test_FindASalespersonDropdown(self):        
        click("FindUs_FindASalesprson_Button.png")
        click("FindAsalesperson_Branch_Dropwdown.png")
        if exists(Pattern("FindASalesperson_Dropdown_Results.png").exact()):
            assert True
        else:
            assert False
           
    def test_FindAPropertyManager(self):
        click("FindUs_FindApropertyManager_Button.png")
        click("FindApropertyManager_SearchBar.png")
        type("Jane Auret")
        wait(1)
        click("FindApropertyManager_SearchResult.png")
        wait(1)
        if exists(Pattern("PropertyManager_PageTitle.png").exact()):
            assert True
        else:
            assert False

    def test_FindAPropertyManagerDropdown(self):
        click("FindUs_FindApropertyManager_Button.png")
        click("FindAPropertyManager_Dropdown.png")
        wait(1)
        if exists(Pattern("FundApropertyManager_Dropdown_Result.png").exact()):
            assert True
        else:
            assert False
       
    def test_FindACommercialSalesperson(self):
        click("FindUs_FindAcommercialSalesperson_Button.png")
        click("FindUs_FindACommercialSalesperson_SearchBar.png")
        type("cam paterson")
        wait(1)
        click("FindUs_FindACommercialAgent_Result.png")
        if exists(Pattern("CommercialAgent_AgentName.png").exact()):
            assert True
        else:
            assert False

    def test_FindACommercialSalespersonDropdown(self):
        click("FindUs_FindAcommercialSalesperson_Button.png")
        click("FindACommercialAgent_Branch_Dropdown.png")
        wait(1)
        if exists(Pattern("FindACommercialSalesperson_Dropdown_Results.png").exact()):
            assert True
        else:
            assert False
            
      
    def test_FindACommercialPropertyManager(self):
        click("FindUs_FindACommercialPropertyManager_Button.png")
        click("FundAcommercialPropertyManager_SearchBar.png")
        type("Hannah")
        
    def test_FindACommercialPropertyManagerDropdown(self):
        click("FindUs_FindACommercialPropertyManager_Button.png")
        click("FindUs_FindAcommercialPropertyManager_Dropdown.png")
        wait(1)
        if exists(Pattern("FindACommercialPorpertyManager_Dropdown_Results.png").exact()):
            assert True
        else:
            assert False        

    def test_AuctionVenue(self):            
        click("FindUs_AuctionVenues_Button.png")
        wait(1)
        if exists(Pattern("AuctionVenuesPage.png").exact()):
            assert True
        else:
            assert False

    def test_AuctionVenue(self): 
        click("FindUs_Complaints_Button.png")
        wait(1)
        find("Complaint_PageTitle.png")
        click("OurComplaintsProcess_Button.png")
        wait(1)
        if exists(Pattern("ComplaintsProcess_TitlePage.png").exact()):
            assert True
        else:
            assert False


        
        
        
        
        
        
        
        
        
        
        
