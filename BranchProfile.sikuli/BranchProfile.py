from sikuli import*
import unittest
import json
import os
  
class BranchProfile(unittest.TestCase):
        
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + "/albany" + Key.ENTER)
        wait(2)

    def tearDown(self):

        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)
        wait(2)
        
           
    def test_BranchDetails(self):   
            if exists(Pattern("BranchPage_BranchDetails.png").similar(0.61)):
                assert True
            else:
                assert False
                
    def test_BranchStaffManager(self):
            click("BranchPage_OurTeam_Button.png")
            wait(3)
            if exists("OurTeamPage_ManagersName.png"):
                assert True
            else:
                assert False
                
    def test_BranchStaffPropertyManagement(self):
            click("BranchPage_OurTeam_Button.png")   
            if exists(Pattern("OurTeamPage_PropertyManagement.png").similar(0.85)):
                assert True
            else:
                assert False

    def test_BranchStaffResidentialSalespeople(self):
            click("BranchPage_OurTeam_Button.png")
            wheel(Pattern("OurTeamPage_PropertyManagement.png").similar(0.76), WHEEL_DOWN, 4)
            
            if exists(Pattern("OurTeam_ResidentialSalespeople.png").similar(0.87)):
                assert True
            else:
                assert False    

    def test_BranchStaffRuralSalespeople(self):    
            click("BranchPage_OurTeam_Button.png")
            wheel(Pattern("OurTeamPage_PropertyManagement.png").similar(0.76), WHEEL_DOWN, 80)
            
            if exists(Pattern("OurTeam_RuralSalespeople.png.png").similar(0.89)):
                assert True
            else:
                assert False    
                
    def test_BranchProperties(self):
            click(Pattern("BranchPage_Properties_Button.png").similar(0.76))
            find("BranchPage_AlbanyProperties.png")
            if exists(Pattern("BranchPage_PropertiesMoreDetail_Button.png").similar(0.71)):
                assert True
            else:
                assert False

    def test_BranchRentals(self):            
            click("BranchPage_Rentals_Button.png")
            find("BranchPage_AlbanyRentals.png")
            click("BranchPage_PropertiesMoreDetail_Button.png")
            if exists(Pattern("BranchRetal_PropertyDetailApplyOnlineToRent_Button.png").similar(0.64)):
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
            if exists(Pattern("PropertyDetail_OpenHome.png").similar(0.82)):
                assert True
            else:
                assert False


