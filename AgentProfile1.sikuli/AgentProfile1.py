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

    def test_AgentDetail(self):
        if exists(Pattern("AgentPage_AgentDetail.png").similar(0.94)):
            assert True
        else:
            assert False

    def test_AgentProperties(self):
        click(Pattern("AgentPage_Properties_Button.png").targetOffset(36,3))
        if exists("OpenHome_MoreDetailsProperty_Button.png"):
            assert True
        else:
            assert False

    def test_AgentOpenHome(self):
        click("AgentPage_OpenHome_Button.png")
        click("OpenHome_MoreDetailsProperty_Button.png")
        
        if exists(Pattern("PropertyDetailPage_OpenHomes.png").similar(0.79)):
            assert True
        else:
            assert False

    def test_AgentSoldProperties(self):
        click("AgentPage_SoldProperties_Button.png")
        if exists(Pattern("SoldProperty_SoldSticker.png").exact()):
            assert True
        else:
            assert False

        
        
        
        
        