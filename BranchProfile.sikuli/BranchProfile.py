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
        
           
    def test_BranchProfile_BW119(self):   
        if exists(Pattern("BranchPage_BranchDetails.png").similar(0.61)):
            assert True
        else:
            assert False
                
    def test_BranchStaffManager_BW120(self):
        click("BranchPage_OurTeam_Button.png")
        wait(3)
        if exists("OurTeamPage_ManagersName.png"):
            assert True
        else:
            assert False
                
    def test_BranchStaffPropertyManagement_BW120(self):
        click("BranchPage_OurTeam_Button.png")   
        if exists(Pattern("OurTeamPage_PropertyManagement.png").similar(0.85)):
            assert True
        else:
            assert False

    def test_BranchStaffResidentialSalespeople_BW120(self):
        click("BranchPage_OurTeam_Button.png")
        wheel(Pattern("OurTeamPage_PropertyManagement.png").similar(0.76), WHEEL_DOWN, 4)
        
        if exists(Pattern("OurTeam_ResidentialSalespeople.png").similar(0.87)):
            assert True
        else:
            assert False    

    def test_BranchStaffRuralSalespeople_BW120(self):    
        click("BranchPage_OurTeam_Button.png")
        wheel(Pattern("OurTeamPage_PropertyManagement.png").similar(0.76), WHEEL_DOWN, 80)
        
        if exists(Pattern("OurTeam_RuralSalespeople.png.png").similar(0.89)):
            assert True
        else:
            assert False    
                
    def test_BranchProperties_BW121(self):
        click(Pattern("BranchPage_Properties_Button.png").similar(0.76))
        find("BranchPage_AlbanyProperties.png")
        if exists(Pattern("BranchPage_PropertiesMoreDetail_Button.png").similar(0.71)):
            assert True
        else:
            assert False

    def test_BranchRentals_BW181(self):            
        click("BranchPage_Rentals_Button.png")
        find("BranchPage_AlbanyRentals.png")
        click("BranchPage_PropertiesMoreDetail_Button.png")
        if exists(Pattern("BranchRetal_PropertyDetailApplyOnlineToRent_Button.png").similar(0.64)):
            assert True
        else:
            assert False

    def test_BranchSold_BW122(self):                
        click("BranchPage_SoldProperties_Button.png")
        find("BranchPAge_AlbanySoldProperties.png")
        if exists(Pattern("BranchPage_SoldSticker.png").exact()):
            assert True
        else:
            assert False

    def test_branchOpenHome_BW182(self):                
        click("BranchPage_OpenHome_Button.png")
        find("BranchPage_AlbanyOpenHomes.png")
        click("BranchPage_OpenHomeMoreDetails.png")
        wait(2)
        if exists(Pattern("PropertyDetail_OpenHome.png").similar(0.82)):
            assert True
        else:
            assert False

    def test_branchSorroundingSuburbs_BW179(self): 
        find("BrancPage_SorroundingSuburbs.png").below(30).left(-15).click()
        if exists(Pattern("ResultsPage_Title.png").similar(0.79)):
            assert True
        
        else:
            assert False
    
    def test_requestAnAppraisal_BW124(self):
        click(Pattern("AgentPage_RequestAnAppraisal_Button.png").similar(0.68))
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
        
        click("RequestAppraisalPage_Submit_Button.png")
        
        if exists("RequestAppraisalPage_EmailConfirmation.png"):
            assert True
        else:
            assert False

