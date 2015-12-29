from sikuli import*
import unittest
import json




class AgentProfile1(unittest.TestCase):
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
        type("nadja court")
        click("FindUs_Search_Button.png")
        click("AgentName_NadjaCourt_Result.png")
    
    def tearDown(self):

        click(Pattern("closeButtonChrome.png").targetOffset(24,0))
        
           
        wait(2)

    def test_AgentDetail(self):
        if exists(Pattern("AgentPage_AgentDetail.png").exact()):
            assert True
        else:
            assert False

    def test_AgentProperties(self):
        click(Pattern("AgentPage_Properties_Button.png").targetOffset(36,3))
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

        
        
        
        
        