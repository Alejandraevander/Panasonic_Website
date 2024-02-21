import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "edge":
        # options_obj = webdriver.EdgeOptions()
        # options_obj.add_argument("--guest")
        # options_obj.add_experimental_option('excludeSwitched', ['enable-logging'])
        # service_obj = Service(r"H:\Python_Project\Python_Selenium_Framework\Drivers\edgedriver_win64\msedgedriver.exe") 
        # driver = webdriver.Edge(service=service_obj, options=options_obj)
        
        options_obj = webdriver.EdgeOptions()
        options_obj.add_argument("--guest")
        #options_obj.add_argument("windows-size=1920x1080")
        #Code to disable devtools listening on ....
        options_obj.add_experimental_option('excludeSwitches', ['enable-logging'])
        #options_obj.add_argument("--headless=new")
        #ptions_obj.add_argument("--start-maximized")
        #options_obj.add_argument("headless")
        #options_obj.add_argument("--ignore-certificate-errors")
        service_obj = Service(r"H:\Python_Project\Section_9_RS_Testing_Framework\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj, options=options_obj)
        
    
    elif browser_name == "firefox":
        options_obj = webdriver.FirefoxOptions()
        options_obj.add_argument("--guest")
        options_obj.add_experimental_option('excludeSwitched', ['enable-logging'])
        service_obj = Service(r"H:\Python_Project\Python_Selenium_Framework\Drivers\geckodriver-v0.34.0-win-aarch64\geckodriver.exe") 
        driver = webdriver.Firefox(service=service_obj, options=options_obj)
    
    elif browser_name == "chrome":
        options_obj = webdriver.ChromeOptions()
        options_obj.add_argument("--guest")
        options_obj.add_experimental_option('excludeSwitched', ['enable-logging'])
        service_obj = Service(r"H:\Python_Project\Python_Selenium_Framework\Drivers\chromedriver-win64\chromedriver.exe") 
        driver = webdriver.Chrome(service=service_obj, options=options_obj)
     
     
    #Start Website using the one of the browser chosen
    driver.implicitly_wait(10)
    driver.get("https://papamy.panasonic.com.my/papamy/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extras', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)   