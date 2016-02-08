from sikuli import*
import unittest
import json

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
        click(Pattern("UsernameMyAccount.png").targetOffset(104,3))
        click("MyAccount_SignOut_Button.png")
        wait(3)
        click(Pattern("closeButtonChrome.png").targetOffset(26,0))

    def test_CreateAccount(self): 
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click(Pattern("Account_Register_Button.png").targetOffset(26,-4))
        click(Pattern("RegisterPage_FirstName_TextBox.png").targetOffset(-133,12))
        type("FirstName")
        click(Pattern("RegisterPage_LastName_TextBox.png").targetOffset(-144,1))
        type("LastName")
        click("RegisterPage_Email_TextBox.png")
        type(config["username"])
        click("RegisterPage_Password_TextBox.png")
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
        click(Pattern("SignInPopUp_emailAddress_field.png").targetOffset(-84,48))
        type(config["username"])
        click(Pattern("SignInPopUp_Password_field.png").targetOffset(-91,-16))
        type(config["password"])
        click("SignInPopUp_SignIn_Button.png")
        wait(3)
        if exists("UsernameMyAccount-1.png"):
            assert True
        else:
            assert False