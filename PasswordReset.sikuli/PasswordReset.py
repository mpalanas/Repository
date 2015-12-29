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
        click(Pattern("closeButtonChrome.png").targetOffset(27,0))

    def test_resetPassword(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field.png").targetOffset(-120,51))
        type(config["username"])
        click(Pattern("SignInPopUp_Password_field.png").targetOffset(-89,-14))
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
        if exists(Pattern("AccountSettings_PasswordChange_Confirmation.png").exact()):
            assert True
        else:
            assert False


