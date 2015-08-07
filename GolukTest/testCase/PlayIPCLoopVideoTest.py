#coding=utf-8
import unittest
import os
import logging
from appium import webdriver
import time
from time import sleep
import shutil

class PlayIPCLoopVideoTest(unittest.TestCase):

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
            self.driver.quit()
            logging.atexit
    def l(self,msg):
        logging.info(msg)
        print msg

    def testPlayIPCLoopVideo(self):
        try:
            self.starttime=time.time()
            self.starttime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.starttime))
            #self.l("Start time: "+str(self.starttime2))
            self.l("==测试准备中==")
            location=self.driver.get_window_size('current')
            self.l(str(location))
            HalfScreenHeight=(location["height"]/2)
            #findCoordinateX=location["width"]/6
            IPCCoordinateX=location["width"]/2
            #我的选项坐标
            myCoordinateX=(location["width"]/6)*5
            heightY=(location["height"]-10)
            
            self.driver.tap([(IPCCoordinateX,heightY)], 2)
            self.driver.find_element_by_name("icon IPC设置 默认").click()
            sleep(10)
            btn=self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIASwitch[1]")
            if int(btn.get_attribute('value'))==1:
                btn.click()
            sleep(10)
            self.driver.find_element_by_name("返回").click()
            self.driver.find_element_by_name("icon 关闭 默认").click()
            self.l("==测试准备完成==")
            self.driver.tap([(myCoordinateX,heightY)], 2)
            sleep(2)
            self.driver.find_element_by_name("我的相册").click()
            if self.driver.find_elements_by_name("远程视频")>0: 
                self.driver.find_element_by_name("远程视频").click()
                sleep(5)
                self.driver.find_element_by_name("循环视频").click()
                sleep(5)
                self.driver.flick(IPCCoordinateX, HalfScreenHeight/2, IPCCoordinateX, heightY/2)
                sleep(5)
                self.fvl=self.driver.find_elements_by_name("180s")
                self.fvll=len(self.fvl)
                n=0
                if self.fvll-1>0:
                    while n<(self.fvll):
                        if n==5:
                            break
                        self.l("第 "+str(n+1)+" 个远程循环影像被点击")
                        self.driver.find_elements_by_name("180s")[n].click()
                        sleep(10)
                        n=n+1
                        if len(self.driver.find_elements_by_name("知道了"))>0:
                            self.driver.find_element_by_name("知道了").click()
                            self.l("第 "+str((n))+" 个远程循环影像损坏")
                        else:
                            if len(self.driver.find_elements_by_name("我的相册")) == 0:
                                self.l("视频开始播放")
                                sleep(16)
                                if len(self.driver.find_elements_by_name("远程视频"))==0:
                                    self.driver.tap([(IPCCoordinateX,heightY)], 1)
                                    if len(self.driver.find_elements_by_name("完成")) >0:
                                        self.l("找到 完成")
                                        try:
                                            self.driver.find_element_by_name("完成").click()
                                        except:
                                            self.l("播放完成")
                                    else:
                                        self.l("没有找到完成")
                                        self.driver.tap([(myCoordinateX,heightY)], 1)
                                        try:
                                            self.driver.find_element_by_name("完成").click()
                                        except:
                                            self.l("播放完成")
                                                                           
                                else:
                                        self.l("播放完成")
                            else:
                                self.l("视频播放超时，超时时间10秒")
                                raise NameError("视频播放超时，超时时间10秒")
                                                       
                else:
                    self.l("Error: IPC没有远程视频")
                    raise NameError('IPC没有远程视频')
            else:
                self.l("Error: IPC 断开连接")
                raise NameError('IPC 断开连接')  
            #打开循环录像
            if self.driver.find_elements_by_name("编辑")>0:
                self.driver.find_element_by_name("我的").click()
            sleep(1) 
            self.driver.tap([(IPCCoordinateX,heightY)], 2)
            self.driver.find_element_by_name("icon IPC设置 默认").click()
            sleep(10)
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIASwitch[1]").click()
            sleep(10)
            self.driver.find_element_by_name("返回").click()
            self.driver.find_element_by_name("icon 关闭 默认").click()
            self.l("==Test Result: Pass===")
            self.endtime=time.time()
            self.endtime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.endtime))
            self.runtime=self.endtime-self.starttime
            
        except Exception, e:
            if self.driver.find_elements_by_name("编辑")>0:
                self.driver.find_element_by_name("我的").click()
            self.driver.tap([(IPCCoordinateX,heightY)], 2)
            self.driver.find_element_by_name("icon IPC设置 默认").click()
            sleep(10)
            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIASwitch[1]").click()
            sleep(10)
            self.driver.find_element_by_name("返回").click()
            self.driver.find_element_by_name("icon 关闭 默认").click()
            self.driver.save_screenshot(self.logPath+"TakeFavoriteVideoTest_"+".png")
            self.l("==Test Result: Fail===")
            self.l("Fail Reason: "+ repr(e) +" ===")
            self.endtime=time.time()
            self.runtime=self.endtime-self.starttime
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()