from sikuli import*
import unittest
import json

class AlternateAgentProfile(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)
        click("findUs.png")
        type("ketiesha elliott")
        click("FindUs_Search_Button.png")
        click("FindUs_AgentName_Result.png")

    def tearDown(self):

        click(Pattern("closeButtonChrome.png").targetOffset(20,0))
           
        wait(2)
    def test_AgentDetail(self):
        if exists(Pattern("AgentPage_AgentDetails.png").exact()):
            assert True
        else:
            assert False

    def test_AgentProperties(self):
        click(Pattern("AgentPage_Properties_Button.png").targetOffset(37,1))
        if exists(Pattern("AgentPage_Properties_MoreDetailsSaveProperty.png").exact()):
            assert True
        else:
            assert False

    def test_AgentOpenHome(self):
        click("AgentPage_OpenHome_Button.png")
        click("OpenHome_MoreDetailsProperty_Button.png")
        
        if exists(Pattern("PropertyDetailPage_OpenHomes.png").exact()):
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
        click("AgentPage_Video_Button.png")
        click("AgentPage_VideoPlay_Button.png")
        wait(4)
        hover("AgentPage_AgentVideo.png")
        
        if exists(Pattern("AgentPage_VideoControl.png").exact()):
            assert True
        else:
            assert False