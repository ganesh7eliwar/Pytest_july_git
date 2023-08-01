from selenium import webdriver


class Test_Credence_2:

    def test_credence_2(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are @ Credence")
            assert True
        else:
            print("You are @ Wrong Site")
            assert False

        driver.quit()


    def test_sub(self):
        a = 5
        b = 3
        sub = a - b
        print(sub)
        if sub == 2:
            print("Correct Calculation")
            assert True
        else:
            print("Wrong Calculation")
            assert False
