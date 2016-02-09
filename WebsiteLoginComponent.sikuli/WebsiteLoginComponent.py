from sikuli import*
import unittest
import json
import os

class WebsiteLoginComponent(unittest.TestCase):

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

        if exists("UsernameMyAccount.png"):
            click(Pattern("UsernameMyAccount.png").targetOffset(104,3))
            click("MyAccount_SignOut_Button.png")
            wait(3)
            configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
            config = json.loads(open(configPath).read())
            appTaskName = config["appTaskName"]
            os.system("taskkill /f /im " +appTaskName)
        else:
            configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
            config = json.loads(open(configPath).read())
            appTaskName = config["appTaskName"]
            os.system("taskkill /f /im " +appTaskName)

        

    def test_CreateAccount(self): 
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("Account_Register_Button.png")
        click(Pattern("RegisterPage_FirstName_TextBox.png").targetOffset(-133,12))
        type("FirstName")
        click(Pattern("RegisterPage_LastName_TextBox.png").similar(0.86).targetOffset(-144,1))
        type("LastName")
        click(Pattern("RegisterPage_Email_TextBox.png").similar(0.80))
        type(config["username"])
        click(Pattern("RegisterPage_Password_TextBox.png").similar(0.93))
        type(config["password"])
        click("RegisterPage_Register_Button.png")
        wait(4)
        
        if exists("UsernameMyAccount-1.png"):
            assert True
        else:
            assert False
   

    def test_login(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field.png").similar(0.62).targetOffset(-100,15))
        type(config["username"])
        type(Key.TAB)
        type(config["password"])
        click(Pattern("SignInPopUp_SignIn_Button.png").similar(0.94))
        wait(3)
        if exists("UsernameMyAccount-1.png"):
            assert True
        else:
            assert False

    def test_savedSearch(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field.png").similar(0.62).targetOffset(-100,15))
        type(config["username"])
        type(Key.TAB)
        type(config["password"])
        click(Pattern("SignInPopUp_SignIn_Button.png").similar(0.94))
        click(Pattern("1447881615559.png").targetOffset(-23,4))
        click("1447881647079.png")
        click("1447881739750.png")
        click("1455054875641.png")
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
        if exists("1455055258153.png"):
            assert True
        else:
            assert False

    def test_editSavedSearchName(self): 
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field.png").similar(0.62).targetOffset(-100,15))
        type(config["username"])
        type(Key.TAB)
        type(config["password"])
        click(Pattern("SignInPopUp_SignIn_Button.png").similar(0.94))
        click("1447799262013.png")
        click("1455060570362.png")
        click("1455060648507.png")
        click("1455060660245.png")
        click("1455060717044.png")
        click("1455060809298.png")
        type("x", KEY_CTRL)
        type(Key.DELETE)
        type("Saved Search Blockhouse Bay")
        click("1455061111707.png")
        if exists("1455061140016.png"):
            assert True
        else:
            assert False

    def test_editSavedSchedule(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field.png").similar(0.62).targetOffset(-100,15))
        type(config["username"])
        type(Key.TAB)
        type(config["password"])
        click(Pattern("SignInPopUp_SignIn_Button.png").similar(0.94))
        click("1447799262013.png")
        click("1455060570362.png")
        click("1455060648507.png")
        click("1455060660245.png")
        click("1455061213918.png")
        click("1455061237888.png")
        find("1455061835326.png").left(15).click()
        
        click("1455061111707.png")
        if exists("1455061935673.png"):
            assert True
        else:
            assert False

    def test_deleteSavedSearch(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field.png").similar(0.62).targetOffset(-100,15))
        type(config["username"])
        type(Key.TAB)
        type(config["password"])
        click(Pattern("SignInPopUp_SignIn_Button.png").similar(0.94))
        click("1447799262013.png")
        click("1455060570362.png")
        click("1455060648507.png")
        type(Key.F5)
        if exists("1455062036151.png"):
            assert True
        else:
            assert False
            