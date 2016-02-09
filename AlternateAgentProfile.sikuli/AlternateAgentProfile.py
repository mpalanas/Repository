from sikuli import*
import unittest
import json
import os

class AlternateAgentProfile(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"]+ "/k.elliott" + Key.ENTER)

    def tearDown(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)
           
        wait(2)
    def test_AgentDetail(self):
        if exists(Pattern("AgentPage_AgentDetails.png").similar(0.94)):
            assert True
        else:
            assert False

    def test_AgentProperties(self):
        click(Pattern("AgentPage_Properties_Button.png").targetOffset(37,1))
        if exists("OpenHome_MoreDetailsProperty_Button-1.png"):
            assert True
        else:
            assert False

    def test_AgentOpenHome(self):
        click("AgentPage_OpenHome_Button.png")
        click(Pattern("1454634416653.png").similar(0.73))
        
        if exists(Pattern("PropertyDetailPage_OpenHomes.png").similar(0.77)):
            assert True
        else:
            assert False

    def test_AgentSoldProperties(self):
        click("AgentPage_SoldProperties_Button.png")
        if exists(Pattern("SoldProperty_SoldSticker.png").exact()):
            assert True
        else:
            assert False

    def test_AgentVideo(self):
        click(Pattern("AgentPage_Video_Button.png").similar(0.84))
        wait(4)
        hover("AgentPage_AgentVideo.png")
        
        if exists("1454633061357.png"):
            assert True
        else:
            assert False