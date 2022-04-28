from msedge.selenium_tools import Edge, EdgeOptions
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
MSEDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge Beta\Application\msedge.exe"
MSEDGE_DRIVER_PATH = './msedgedriver.exe'  #https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
COOKIES_JSON_PATH = './cookies.json'  #json.dumps(driver.get_cookies(), indent=2)
HREF = 'https://shangoue.meituan.com/'
IFRAME_ID = "hashframe"
TIMEOUT = 15


def init_imitate_edge_driver() -> Edge:
    '''初始化一般反反爬模式的edge_driver'''
    options = EdgeOptions()
    options.use_chromium = True
    options.binary_location = MSEDGE_PATH
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = Edge(options=options, executable_path=MSEDGE_DRIVER_PATH)
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument", {
            "source":
            """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
        })
    return driver


def switch_to_iframe_app_content(driver: Edge,
                                 iframe_id: str = IFRAME_ID,
                                 timeout: int = TIMEOUT):
    '''进入并等待iframe_app加载和数据渲染'''
    WebDriverWait(driver, timeout).until(
        expected_conditions.presence_of_element_located((By.ID, iframe_id)))
    driver.switch_to_frame(iframe_id)
    WebDriverWait(driver, timeout).until(
        expected_conditions.invisibility_of_element_located((By.ID, 'app')))


def add_default_cookies(driver: Edge,
                        domain: str = HREF,
                        cookies_json_path: str = COOKIES_JSON_PATH):
    '''进入指定的域按照预设的cookies文件设置cookie'''
    driver.get(domain)
    with open(cookies_json_path, 'r') as cookies_json:
        for cookie in json.loads(cookies_json.read()):
            del cookie['domain']
            driver.add_cookie(cookie)


if __name__ == "__main__":

    driver = init_imitate_edge_driver()

    add_default_cookies(driver)
    input("\n请手动最大化和关闭edge的已登录微软账户以及无法同步的提示\n回车继续\n\n")

    driver.get(HREF)
    switch_to_iframe_app_content(driver)
    driver.switch_to_default_content()

    driver.execute_script("location.hash = '#/v2/shop/manage'")
    switch_to_iframe_app_content(driver)
    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '[pindex="3"]>a'))).click()
    driver.switch_to_default_content()
    '''
    WebDriverWait(driver, 15).until('a.J-poi-name'
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, 'span.text.J-mark-tip')))
    driver.find_elements_by_css_selector('span.text.J-mark-tip')[1].click()
    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, 'span.submenu-label'))).click()
    input()
    driver.delete_cookie('wmPoiId')
    driver.add_cookie(wmPoiId)

    '''
    input()