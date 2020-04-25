from selenium import webdriver

#封装selenium基本方法，初始化、打开url，定位方法等，还没写完，还要修改
class BasePage():
    def __init__(self, brower_driver, brower_url, pagetitle):
        self.brower_driver = brower_driver
        self.brower_url = brower_url
        self.pagetitle = pagetitle
    
    def open_url(self,waittime):
        self.brower_driver.get(self.brower_url)
        self.brower_driver.maximize_window()
        self.brower_driver.implicitly_wait(waittime)
        assert self.pagetitle in self.brower_driver.title, u"打开页面失败，%s" %self.brower_url

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.brower_driver.find_element(*loc)
        except:
            print(u"%s页面中未能找到%s元素" %(self, loc))