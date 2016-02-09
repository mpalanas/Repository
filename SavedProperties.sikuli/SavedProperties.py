from sikuli import*
import unittest
import json
import os


class SavedProperties(unittest.TestCase):

    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)
        click("SigninPage_SignIn_Button.png")
        click(Pattern("SignInPopUp_emailAddress_field-1.png").similar(0.62).targetOffset(-100,15))
        type(config["username"])
        type(Key.TAB)
        type(config["password"])
        click(Pattern("SignInPopUp_SignIn_Button.png").similar(0.92))
        wait(3)
        find("UsernameMyAccount.png")

    def tearDown(self):
        type(Key.BACKSPACE)
        click("SavedPropertiesPage_Remove_Button.png")
        type(Key.F5)
        wait(1)
        click(Pattern("UsernameMyAccount-1.png").targetOffset(81,-2))
        click("MyAccountDropdown_SignOut_Button.png")
        wait(3)
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)

        
    def test_CommercialSaveProperty(self):           
        wait(2)
        click(Pattern("FrontPage_Commercial_Button.png").similar(0.80))
        click("FrontPage_Search_Button-1.png")
        wait(2)
        find("FrontPage_CommercialFacet.png")
        click("FrontPageSearchResults_SaveProperty_Button-1.png")
        find("SaveProperty_Check_Button-1.png")
        click(Pattern("UsernameMyAccount-2.png").targetOffset(86,-5))
        click("AccountDropdown_Profile_Button-1.png")
        click("ProfilePage_SavedProperties_Button-1.png")
        find("SavedPropertiesPage_MoreDetailsRemove_Button-1.png")
        click("SavedPropertiesPage_MoreDetails_Button.png")
        wait(1)
        if exists("PropertyDetailPage_SavedProperty_Button-1.png"):
            assert True
        else:
            assert False

    def test_ResidentialSavedProperties(self):
        wait(2)
        click("FrontPage_Buy_Button.png")
        click("FrontPage_Search_Button.png")
        wait(2)
        find("1447889264312.png")
        click("FrontPageSearchResults_SaveProperty_Button.png")
        find("SaveProperty_Check_Button.png")
        click(Pattern("UsernameMyAccount-3.png").targetOffset(85,-5))
        click("AccountDropdown_Profile_Button.png")
        click("ProfilePage_SavedProperties_Button.png")
        find("SavedPropertiesPage_MoreDetailsRemove_Button.png")
        click("SavedPropertiesPage_MoreDetails_Button-2.png")
        wait(1)
        if exists("PropertyDetailPage_SavedProperty_Button-1.png"):
            assert True
        else:
            assert False

    def test_RuralSavedProperties(self):
        wait(2)
        click("1447889176530.png")
        click("1447882327038.png")
        wait(2)
        find("1447889247040.png")
        click("1447888350266.png")
        find("1447888392634.png")
        click("1447799262013.png")
        click("1447884837635.png")
        click("1447888701806.png")
        find("1447888720119.png")
        click("1447888759150.png")
        wait(1)
        if exists("PropertyDetailPage_SavedProperty_Button-1.png"):
            assert True
        else:
            assert False

    def test_RentalSavedProperties(self):
        wait(2)
        click("1447889347592.png")
        click("1447882327038-1.png")
        wait(2)
        find("1447889368574.png")
        click("1447888350266-1.png")
        find("1447888392634-1.png")
        click("1447799262013-1.png")
        click("1447884837635-1.png")
        click("1447888701806-1.png")
        find("1447888720119-1.png")
        click("1447888759150-1.png")
        wait(1)
        if exists("PropertyDetailPage_SavedProperty_Button-1.png"):
            assert True
        else:
            assert False
        

