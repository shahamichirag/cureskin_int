from selenium import webdriver
from app.application import Application
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.chrome.options import Options


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()

    #-----------BELOW CODE IS FOR GECKODRIVER WITH BINARY------------

    # options = Options()
    # options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # context.driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    #--------------HEADLESS MODE CODE AS BELOW--------------

    # options = webdriver.ChromeOptions()
    # options.add_argument('--window-size=1920,1080')
    # options.add_argument('--start-maximized')
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver.exe')
    # context.app = Application(context.driver)

    #------------------BROWSER STACK FOR CROSS BROWSER TESTING----------------------

    bs_user = ''
    bs_key = ''

    # desired_cap = {
    #     "browserName": "Firefox",
    #     "browserVersion": "102.0",
    #     "os": "Windows",
    #     "osVersion": "10",
    #     'name': test_name
    # }
    desired_cap = {
        "browserName": "Safari",
        "browserVersion": "16.3",
        "os": "MAC",
        "osVersion": "Ventura",
        'name': test_name
    }
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
