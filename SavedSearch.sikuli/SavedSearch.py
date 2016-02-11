from sikuli import*
import unittest
import json
import os

class SavedSearch(unittest.TestCase):

    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(4)
        if exists("UsernameMyAccount-1.png"):
            wait(1)
        else:
            click("SigninPage_SignIn_Button-1.png")
            click(Pattern("SignInPopUp_emailAddress_field-1.png").similar(0.62).targetOffset(-100,15))
            type(config["username"])
            type(Key.TAB)
            type(config["password"])
            click(Pattern("SignInPopUp_SignIn_Button-1.png").similar(0.94))

        

    def tearDown(self):
        if exists("UsernameMyAccount.png"):
            click(Pattern("UsernameMyAccount.png").targetOffset(104,3))
            click("MyAccount_SignOut_Button.png")
            wait(3)

            configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
            config = json.loads(open(configPath).read())
            appTaskName = config["appTaskName"]
            os.system("taskkill /f /im " +appTaskName)

            wait(2)
            
        else:
            configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
            config = json.loads(open(configPath).read())
            appTaskName = config["appTaskName"]
            os.system("taskkill /f /im " +appTaskName)
            wait(2)



    def test_1createSavedSearch(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        
        wait(2)
        click(Pattern("1447881615559.png").targetOffset(-23,4))
        click("1447881647079.png")
        wait("1447881739750.png")
        click("1447881739750.png")
        click("1455054875641.png")
        wait("1447882027042.png")
        click("1447882027042.png")
        click(Pattern("1447881820472.png").targetOffset(-65,2))
        click("1447882327038.png")
        click("1455054900783.png")
        click("1455054918572.png")
        type("SavedSearch")
        click("1455055124658.png")
        click("1455055148229.png")
        click("1455055160570.png")
        click("1447799262013.png")
        click("1455065452632.png")
        click("1455065462352.png")
        
        if exists("1455065478316.png"):
            assert True
        else:
            assert False


    def test_2EditSavedSearch(self): 
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        wait(3)
        click("1447799262013-1.png")
        click(Pattern("1455063340945.png").targetOffset(-29,10))
        click("1455063374783.png")
        click("1455063406796.png")
        type("a", KEY_CTRL)
        type(Key.DELETE)
        type("Saved Search Blockhouse Bay")
        click("1455063436229.png")
        if exists("1455063448150.png"):
            assert True
        else:
            assert False

        
    def test_3SavedSearchEditSchedule(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        wait(3)
        click("1447799262013.png")
        click("1455068889282.png")
        click("1455068899168.png")
        click("1455068908391.png")
        click("1455068919787.png")
        click("1455068946142.png")
        find("1455068959954.png").left(15).click()
        click("1455069008738.png")
        type(Key.F5)
        wait(3)
        if exists("1455069021326.png"):
            assert True
        else:
            assert False  


    def test_4SavedSearchRemove(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        wait(3)
        click("1447799262013.png")
        click("1455068889282.png")
        click("1455068899168.png")
        click("1455069528701.png")
        wait(1)
        type(Key.F5)
        wait(1)
        if exists("1455069562217.png"):
            assert True
        else:
            assert False
    
