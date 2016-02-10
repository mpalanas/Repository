def test_SaveSearchEdit(self): 
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("SigninPage_SignIn_Button-2.png")
        click(Pattern("SignInPopUp_emailAddress_field-2.png").similar(0.62).targetOffset(-100,15))
        #type(config["username"])
        type("test405@test.com")
        type(Key.TAB)
        #type(config["password"])
        type("ayroso235")
        click(Pattern("SignInPopUp_SignIn_Button-2.png").similar(0.94))
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