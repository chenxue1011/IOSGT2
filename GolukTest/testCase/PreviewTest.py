#coding=utf-8
import unittest
import os
import logging
from appium import webdriver
import time
from time import sleep
import shutil

class PreviewTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'iPhone 5s'
        desired_caps['app'] = os.path.abspath('/Users/apple/Downloads/GoLuk-appstore-GoLuk-201507172034.ipa')
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        
        self.className=self.__class__.__name__
        self.logPath=os.getcwd()+"/"+self.className+"/"
        if os.path.isdir(self.logPath):
            shutil.rmtree(self.logPath)
        os.mkdir(self.logPath)
#         self.LOG_FILENAME=self.className+".txt"
#         root = logging.getLogger()
#         if root.handlers:
#             for handler in root.handlers:
#                     root.removeHandler(handler)
#         logging.basicConfig(filename=self.logPath+self.LOG_FILENAME,filemode='a+',level=logging.INFO,format = '%(asctime)s : %(message)s')
    def tearDown(self):
        try:
            for i in range(10):
                print '--Try to quit '+str(i)+' times---'
                s=self.driver.quit()
                if int(s['status'])==0:
                    self.l('tearDown has been done')
                    break
                else:
                    sleep(3)
            logging.atexit
        except Exception,msg:
            self.l(">>>>App Crash<<<<")
            self.l("Exception info： "+"\n"+msg)
            logging.atexit
    def l(self,msg):
        logging.info(msg)
        print msg

    def testPreview(self):
        try:
            self.starttime=time.time()
            self.starttime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.starttime))
            
            self.l("==测试准备中==")
            location=self.driver.get_window_size('current')
            self.l(str(location))
            #findCoordinateX=location["width"]/6
            IPCCoordinateX=location["width"]/2
            #myCoordinateX=(location["width"]/6)*5
            heightY=(location["height"]-10)
            self.l("==测试准备完成==")
            
            self.driver.tap([(IPCCoordinateX,heightY)], 2)
            sleep(2)
            wificonnect=self.driver.find_elements_by_name("icon_wifi_连接")
            if wificonnect>0:
                self.l("IPC已经连接成功")
                btnplay=self.driver.find_element_by_name("btn 播放")
                btnplay.click()
                playtime=1
                while playtime<5:
                    self.l("拍摄第"+str(playtime)+" 秒预览视频")
                    self.driver.save_screenshot(self.logPath+"PreviewTest_"+str(playtime*5)+".png")
                    sleep(5)
                    playtime=playtime+1
            else:
                raise NameError('IPC 断开连接')         
            self.l("==Test Result: Pass===")
            self.endtime=time.time()
            self.endtime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.endtime))
            self.runtime=self.endtime-self.starttime
                    
        except Exception, e:
            self.l("==Test Result: Fail===")
            self.l("Fail Reason: "+ repr(e) +" ===")
            self.endtime=time.time()
            self.runtime=self.endtime-self.starttime

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()