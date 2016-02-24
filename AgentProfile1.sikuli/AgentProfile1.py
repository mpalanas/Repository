from sikuli import*
import unittest
import json
import os




class AgentProfile1(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        appTaskName = config["appTaskName"]
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"]+"/n.court" + Key.ENTER)
    
    def tearDown(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)
        
           
        wait(2)

    def test_AgentDetail_BW112(self):
        if exists(Pattern("AgentPage_AgentDetail.png").similar(0.94)):
            assert True
        else:
            assert False

    def test_AgentProperties_BW113(self):
        click(Pattern("AgentPage_Properties_Button.png").targetOffset(36,3))
        if exists("OpenHome_MoreDetailsProperty_Button.png"):
            assert True
        else:
            assert False

    def test_AgentOpenHome_BW115(self):
        click("AgentPage_OpenHome_Button.png")
        click("OpenHome_MoreDetailsProperty_Button.png")
        
        if exists(Pattern("PropertyDetailPage_OpenHomes.png").similar(0.79)):
            assert True
        else:
            assert False

    def test_AgentSoldPropertiesBW114(self):
        click("AgentPage_SoldProperties_Button.png")
        if exists(Pattern("SoldProperty_SoldSticker.png").exact()):
            assert True
        else:
            assert False

    def test_RequestAnAppraisal(self):
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
        
        
        
        
        