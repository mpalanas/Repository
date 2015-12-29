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
        find("barfootLogo.png")
        wheel("barfootLogo-1.png", WHEEL_DOWN, 3)

    def tearDown(self):

        click(Pattern("closeButtonChrome-1.png").targetOffset(24,0))
           
        wait(2)


    def test_FindABranch(self):
        click(Pattern("findUs-2.png").targetOffset(-86,38))
        if exists(Pattern("MainPage_FindABranch.png").exact()):
            assert True
        else:
            assert False
    def test_OurTeam(self):
        click(Pattern("findUs.png").targetOffset(-8,37))
        if exists(Pattern("FindUs_FindASalesperson.png").exact()):
            assert True
        else:
            assert False

    def test_FindPersonsName(self):
        click(Pattern("findUs-1.png").targetOffset(-97,6))
        click("MainPage_FindUs_TextBox.png")
        type("bob voss")
        wait(2)
        if exists(Pattern("MainPage_FindUs_SearchResult.png").exact()):
            assert True
        else:
            assert False
