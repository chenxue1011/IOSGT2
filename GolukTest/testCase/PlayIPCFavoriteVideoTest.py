#coding=utf-8
import unittest
import os
import logging
from appium import webdriver
import time
from time import sleep
import shutil

class PlayIPCFavoriteVideoTest(unittest.TestCase):

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

    def testIPCFavoriteVideo(self):
        try:
            self.starttime=time.time()
            self.starttime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.starttime))
            #self.l("Start time: "+str(starttime2))
            self.l("==测试准备中==")
            location=self.driver.get_window_size('current')
            self.l(str(location))
            HalfScreenHeight=(location["height"]/2)
            #findCoordinateX=location["width"]/6
            IPCCoordinateX=location["width"]/2
            #我的选项坐标
            myCoordinateX=(location["width"]/6)*5
            heightY=(location["height"]-10)
            self.l("==测试准备完成==")
            self.driver.tap([(myCoordinateX,heightY)], 2)
            sleep(2)
            self.driver.find_element_by_name("我的相册").click() 
            if self.driver.find_elements_by_name("远程视频")>0:
                self.driver.find_element_by_name("远程视频").click()
                sleep(3)
                self.driver.find_element_by_name("精彩视频").click()
                sleep(3)
                self.driver.flick(IPCCoordinateX, HalfScreenHeight/2, IPCCoordinateX, heightY/2)
                sleep(3)
                self.fvl=self.driver.find_elements_by_name("12s")
                self.fvll=len(self.fvl)
                n=0
                if self.fvll>0:
                    while n<(self.fvll-1):
                        n=n+1
                        if n==5:
                            break
                        self.l("第 "+str(n)+" 个远程精彩视频被点击")
                        self.driver.find_elements_by_name("12s")[n].click()
                        sleep(6)
                        if len(self.driver.find_elements_by_name("知道了"))>0:
                            self.driver.find_element_by_name("知道了").click()
                            self.l("第 "+str((n))+" 个视频损坏")
                        else:
                            if len(self.driver.find_elements_by_name("我的相册")) == 0:
                                self.l("视频开始播放")
                                sleep(16)
                                if len(self.driver.find_elements_by_name("远程视频"))==0:
                                    self.l("没有找到远程视频标签，视频还在播放")
                                    self.driver.tap([(IPCCoordinateX,heightY)], 1)
                                    if len(self.driver.find_elements_by_name("完成")) >0:
                                        self.l("找到 完成")
                                        try:
                                            self.driver.find_element_by_name("完成").click()
                                        except:
                                            self.l("视频播放完成")
                                    else:
                                        self.l("没有找到完成")
                                        self.driver.tap([(myCoordinateX,heightY)], 1)
                                        try:
                                            self.driver.find_element_by_name("完成").click()
                                        except:
                                            self.l("视频播放完成")                                                                           
                                else:
                                    self.l("视频播放完成")
                            else:
                                raise NameError("视频播放超时，超时时间6秒")  
                else:
                    self.l("Error: IPC远程没有精彩视频")
                    raise NameError('IPC远程没有精彩视频')                                                  
            else:
                self.l("Error: IPC 断开连接")
                raise NameError('IPC PC 断开连接')            
            self.l("==Test Result: Pass===")
            self.endtime=time.time()
            self.endtime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.endtime))
            self.runtime=self.endtime-self.starttime

        except Exception, e:
            self.driver.save_screenshot(self.logPath+"TakeFavoriteVideoTest_"+".png")
            self.l("==Test Result: Fail===")
            self.l("Fail Reason: "+ repr(e) +" ===")
            self.endtime=time.time()
            self.runtime=self.endtime-self.starttime
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()