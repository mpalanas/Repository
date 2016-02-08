from sikuli import*
import unittest
import json

class FindUsBar(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)

    def tearDown(self):

        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)
           
        wait(2)


    def test_FindABranch(self):
        click(Pattern("findUs-2.png").targetOffset(-90,37))
        if exists(Pattern("MainPage_FindABranch.png").similar(0.89)):
            assert True
        else:
            assert False
    def test_OurTeam(self):
        click(Pattern("findUs.png").targetOffset(-10,38))
        if exists(Pattern("FindUs_FindASalesperson.png").similar(0.89)):
            assert True
        else:
            assert False

    def test_FindPersonsName(self):
        click(Pattern("findUs-1.png").targetOffset(-97,6))
        type("bob voss")
        wait(2)
        click(Pattern("MainPage_FindUs_SearchResult.png").similar(0.75))
            
        if exists(Pattern("BobVoss_ProfilePage_Title.png").similar(0.79)): 
            assert True
        else:
            assert False

            
