#coding=utf-8
import unittest
import os
import logging
from appium import webdriver
import time
from time import sleep
import shutil

class HotVideoTest(unittest.TestCase):

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
#         print self.LOG_FILENAME
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

    def testHotVideo(self):
        try:
            
            self.starttime=time.time()
            self.starttime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.starttime))
            #self.l("Start time: "+str(starttime2))
            self.l("==测试准备中==")
            location=self.driver.get_window_size('current')
            self.l(str(location))
            findCoordinateX=location["width"]/6
            #IPCCoordinateX=location["width"]/2
            #我的选项坐标
            #myCoordinateX=(location["width"]/6)*5
            heightY=(location["height"]-10)
            
            x=self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]")
            a=x.location_in_view
            self.l("==测试准备完成==")
            
            self.driver.tap([(findCoordinateX,heightY)], 2)
            sleep(2)
            self.driver.find_element_by_name("热门").click()
            for i in range(8):
                self.l("第 "+str(i+1)+" 次下拉播放")
                self.driver.flick(a.get('x',0), a.get('y',0), a.get('x',0), a.get('y',0)*4)
                sleep(5)
                self.driver.find_element_by_name("btn 播放").click()
                self.l("播放10秒后自动退出")
                sleep(10)
#             for j in range(2):
#                 self.l("第 "+str(j+1)+" 次上拉播放")
#                 self.driver.flick(a.get('x',0), a.get('y',0)*5, a.get('x',0), a.get('y',0))
#                 sleep(8)
#                 self.driver.find_element_by_name("btn 播放").click()
#                 self.l("播放10秒后自动退出")
#                 sleep(10)

            self.l("==Test Result: Pass===")
            self.endtime=time.time()
            self.endtime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.endtime))
            self.runtime=self.endtime-self.starttime
            #self.l("EndTime: "+str(endtime2))
            #self.l("RunTime: "+str(runtime))
        except Exception, e:
            self.driver.save_screenshot(self.logPath+"TakeFavoriteVideoTest_"+".png")
            self.l("==Test Result: Fail===")
            self.l("Fail Reason: "+ repr(e) +" ===")
            self.endtime=time.time()
            self.runtime=self.endtime-self.starttime
            #self.l("RunTime: "+str(runtime))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()