from sikuli import*
import unittest
import json
  
class PasswordReset(unittest.TestCase):
        
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
        click(Pattern("UsernameMyAccount.png").targetOffset(78,-3))
        click("MyAccount_SignOut_Button.png")
        wait(3)
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)

    def test_changePassword(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field-1.png").similar(0.62).targetOffset(-100,15))
        type(config["username"])
        type(Key.TAB)
        type(config["password"])
        click("SignInPopUp_SignIn_Button.png")
        wait(3)
        click(Pattern("UsernameMyAccount-2.png").targetOffset(79,-1))
        click("MyAccount_AccountSettings_Button.png")
        click(Pattern("AccountSettings_currentPassword_Field.png").targetOffset(-47,8))
        type(config["password"])
        click(Pattern("AccountSettings_newPassword_Field.png").targetOffset(-38,0))
        type(config["password2"])
        click("AccountSettings_changePassword_Button.png")
        wait(3)
        if exists("AccountSettings_PasswordChange_Confirmation.png"):
            assert True
        else:
            assert False

    def test_loginNewPassword(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field-1.png").similar(0.62).targetOffset(-100,15))
        type(config["username"])
        type(Key.TAB)
        type(config["password2"])
        click("SignInPopUp_SignIn_Button.png")
        wait(3)
        if exists(Pattern("UsernameMyAccount-2.png").targetOffset(79,-1)):
            assert True
        else:
            assert False

