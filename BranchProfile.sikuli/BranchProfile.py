from sikuli import*
import unittest
import json
  
class BranchProfile(unittest.TestCase):
        
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)
        click(Pattern("findUs.png").targetOffset(-90,38))
        click("FindUs_BranchName_Button.png") 

    def tearDown(self):

        click(Pattern("closeButtonChrome.png").targetOffset(17,-1)) 
           
    def test_BranchDetails(self):   
            if exists("BranchPage_BranchDetails.png"):
                assert True
            else:
                assert False
                
    def test_BranchStaffManager(self):
            click("BranchPage_OurTeam_Button.png")   
            if exists(Pattern("OurTeamPage_ManagersName.png").exact()):
                assert True
            else:
                assert False
                
    def test_BranchStaffPropertyManagement(self):
            click("BranchPage_OurTeam_Button.png")   
            if exists(Pattern("OurTeamPage_PropertyManagement.png").exact()):
                assert True
            else:
                assert False

    def test_BranchStaffResidentialSalespeople(self):
            click("BranchPage_OurTeam_Button.png")
            wheel("OurTeamPage_PropertyManagement.png", WHEEL_DOWN, 4)
            
            if exists(Pattern("OurTeam_ResidentialSalespeople.png").exact()):
                assert True
            else:
                assert False    

    def test_BranchStaffRuralSalespeople(self):
            click("BranchPage_OurTeam_Button.png")
            wheel("OurTeamPage_PropertyManagement.png", WHEEL_DOWN, 80)
            
            if exists(Pattern("OurTeam_RuralSalespeople.png.png").exact()):
                assert True
            else:
                assert False    
                
    def test_BranchProperties(self):
            click("BranchPage_Properties_Button.png")
            find("BranchPage_AlbanyProperties.png")
            if exists(Pattern("BranchPage_PropertiesMoreDetail_Button.png").exact()):
                assert True
            else:
                assert False

    def test_BranchRentals(self):            
            click("BranchPage_Rentals_Button.png")
            find("BranchPage_AlbanyRentals.png")
            click("BranchPage_PropertiesMoreDetail_Button.png")
            if exists(Pattern("BranchRetal_PropertyDetailApplyOnlineToRent_Button.png").exact()):
                assert True
            else:
                assert False

    def test_BranchSold(self):                
            click("BranchPage_SoldProperties_Button.png")
            find("BranchPAge_AlbanySoldProperties.png")
            if exists(Pattern("BranchPage_SoldSticker.png").exact()):
                assert True
            else:
                assert False

    def test_branchOpenHome(self):                
            click("BranchPage_OpenHome_Button.png")
            find("BranchPage_AlbanyOpenHomes.png")
            click("BranchPage_OpenHomeMoreDetails.png")
            wait(2)
            if exists(Pattern("PropertyDetail_OpenHome.png").exact()):
                assert True
            else:
                assert False


