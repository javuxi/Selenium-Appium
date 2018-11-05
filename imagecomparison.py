#This program interects with both Web and Native appiums on an Android platform.
#Screenshots are taken with full screen, so you need to crop them, based on what do you want to comapre, either just a piece of actual screen or the whole app screen
#Using MD5 for image comparison


import os
import time
import hashlib
import unittest
from PIL import Image
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'platformName'  
        desired_caps['platformVersion'] = 'platformVersion'  
        desired_caps['deviceName'] = 'deviceName'  
        desired_caps['appPackage'] = 'appPackage'
        desired_caps['appActivity'] = 'appActivity'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['noReset'] = False  

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def switch_to_webview(self):
        webview = self.driver.contexts[1]
        self.driver.switch_to.context(webview)

    def switch_to_nativeapp(self):
        self.driver.switch_to.context('NATIVE_APP')

    def take_photo_of_loaded_banner(self):
        loaded_banner = self.driver.find_element_by_id("")
        path = "location"
        begin = loaded_banner.location
        size = loaded_banner.size
        start_x = begin['x']
        start_y = begin['y']
        end_x = start_x + size['width']
        end_y = start_y + size['height']
        name = 'final'
        box =(start_x, start_y, end_x, end_y)
        self.driver.get_screenshot_as_file(path + '/' + 'full_screen.png')
        image = Image.open(path + '/' + 'full_screen.png')
        newimage = image.crop(box)
        newimage.save(path + '/' + name + '.png')
        os.popen('rm %s/full_screen.png' % path)

        digests = []
        for filename in [path + "/" + 'pre_recorded_image.png', path + "/" + 'final.png']:
            hasher = hashlib.md5()
            with open(filename, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
                a = hasher.hexdigest()
                digests.append(a)
                print(a)

        if digests[0] == digests[1]:
            print ("Displayed Image matches prerecorded one.")
        else:
            print ("Displayed Image does not match prerecorded one.")

    def take_photo_of_expanded_banner(self):
        expanded_banner = self.driver.find_element_by_id("")
        path = "location"
        begin = expanded_banner.location
        size = expanded_banner.size
        start_x = begin['x']
        start_y = begin['y']
        end_x = start_x + size['width']
        end_y = start_y + size['height']
        name = 'final1'
        box = (start_x, start_y, end_x, end_y)
        self.driver.get_screenshot_as_file(path + '/' + 'full_screen.png')
        image = Image.open(path + '/' + 'full_screen.png')
        newimage = image.crop(box)
        newimage.save(path + '/' + name + '.png')
        os.popen('rm %s/full_screen.png' % path)

        digests = []
        for filename in [path + "/" + 'pre_recorded_image1.png', path + "/" + 'final.png1']:
            hasher = hashlib.md5()
            with open(filename, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
                a = hasher.hexdigest()
                digests.append(a)
                print(a)

        if digests[0] == digests[1]:
            print ("Displayed Image matches prerecorded one.")
        else:
            print ("Displayed Image does not match prerecorded one.")

    def take_photo_of_disappeared_logo(self):
        disappeared_logo = self.driver.find_element_by_id("")
        path = "location"
        begin = disappeared_logo.location
        size = disappeared_logo.size
        start_x = begin['x']
        start_y = begin['y']
        end_x = start_x + size['width']
        end_y = start_y + size['height']
        name = 'final2'
        box = (start_x, start_y, end_x, end_y)
        self.driver.get_screenshot_as_file(path + '/' + 'full_screen.png')
        image = Image.open(path + '/' + 'full_screen.png')
        newimage = image.crop(box)
        newimage.save(path + '/' + name + '.png')
        os.popen('rm %s/full_screen.png' % path)

        digests = []
        for filename in [path + "/" + 'pre_recorded_image2', path + "/" + 'final.png2']:
            hasher = hashlib.md5()
            with open(filename, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
                a = hasher.hexdigest()
                digests.append(a)
                print(a)

        if digests[0] == digests[1]:
            print ("Displayed Image matches prerecorded one.")
        else:
            print ("Displayed Image does not match prerecorded one.")

    def take_photo_of_reappeared_banner(self):
        reappeared_banner = self.driver.find_element_by_id("")
        path = "location"
        begin = reappeared_banner.location
        size = reappeared_banner.size
        start_x = begin['x']
        start_y = begin['y']
        end_x = start_x + size['width']
        end_y = start_y + size['height']
        name = 'final3'
        box = (start_x, start_y, end_x, end_y)
        self.driver.get_screenshot_as_file(path + '/' + 'full_screen.png')
        image = Image.open(path + '/' + 'full_screen.png')
        newimage = image.crop(box)
        newimage.save(path + '/' + name + '.png')
        os.popen('rm %s/full_screen.png' % path)

        digests = []
        for filename in [path + "/" + 'pre_recorded_image3.png', path + "/" + 'final.png3']:
            hasher = hashlib.md5()
            with open(filename, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
                a = hasher.hexdigest()
                digests.append(a)
                print(a)

        if digests[0] == digests[1]:
            print ("Displayed Image matches prerecorded one.")
        else:
            print ("Displayed Image does not match prerecorded one.")

    def test_app(self):

        #can be done automatically with appium, without finding elements with autoGrantPermissions
        allow_settings_1 = self.driver.find_element_by_id(
            "com.android.packageinstaller:id/permission_allow_button").click()
        allow_settings_2 = self.driver.find_element_by_id(
            "com.android.packageinstaller:id/permission_allow_button").click() 

        self.driver.implicitly_wait(10)

        click_to_load_banner_in_new_tab = self.driver.find_element_by_id("").click()

        time.sleep(5)

        self.take_photo_of_loaded_banner()

        self.switch_to_webview()

        try:
            text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((MobileBy.CSS_SELECTOR, "")))
            logo = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((MobileBy.CSS_SELECTOR, "")))
        except NoSuchElementException:
            print ("Either text or logo did not appear.")
            self.tearDown()

        self.switch_to_nativeapp()

        banner_text_logo = self.driver.find_element_by_id("")
        location_banner_text_logo = banner_text_logo.location
        location_banner_text_logo_x = banner_text_logo.get('x')
        location_banner_text_logo_y = banner_text_logo.get('y')
        TouchAction(self.driver).tap(None, location_banner_text_logo_x,location_banner_text_logo_y, 1).perform()

        time.sleep(5)

        self.take_photo_of_expanded_banner()

        self.switch_to_webview()

        try:
            logo = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((MobileBy.CSS_SELECTOR, "")))
            unit = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((MobileBy.CSS_SELECTOR, "")))
        except NoSuchElementException:
            print ("Either unit or logo did not appear.")
            self.tearDown()

        self.switch_to_nativeapp()

        click_logo_to_disappear = self.driver.find_element_by_xpath(""""]""")
        location_click_logo_to_disappear = click_to_disappear.location
        location_click_logo_to_disappear_x = location_click_logo_to_disappear.get('x')
        location_click_logo_to_disappear_y = location_click_logo_to_disappear.get('y')
        TouchAction(self.driver).tap(None, location_click_logo_to_disappear_x,location_click_logo_to_disappear_y, 1).perform()

        time.sleep(5)

        self.take_photo_of_disappeared_logo()

        find_close_button = self.driver.find_element_by_xpath("""""")
        location_find_close_button = find_close_button.location
        location_find_close_button_x = location_find_close_button.get('x')
        location_find_close_button_y = location_find_close_button.get('y')
        TouchAction(self.driver).tap(None, location_find_close_button_x, location_find_close_button_y, 1).perform()

        self.switch_to_webview()

        try:
            banner_reappeared = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((MobileBy.CSS_SELECTOR, ""))).is_displayed()
        except NoSuchElementException:
            print ("Banner did not reappear.")
            self.tearDown()

        self.switch_to_nativeapp()

        time.sleep(8)

        self.take_photo_of_reappeared_banner()

        self.driver.press_keycode(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
