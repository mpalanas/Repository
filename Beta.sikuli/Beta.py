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
