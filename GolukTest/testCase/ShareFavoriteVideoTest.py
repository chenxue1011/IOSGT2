#coding=utf-8
import unittest
import os
import logging
from appium import webdriver
import time
from time import sleep
import shutil
import random

class ShareFavoriteVideoTest(unittest.TestCase):

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

    def testShareFavoriteVideo(self):
            try:
                self.starttime=time.time()
                self.starttime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.starttime))
                
                self.l("==测试准备中==")
                self.filterlist=["btn 滤镜 古典胶片","btn 滤镜 黑白经典","btn 滤镜 柔和静谧","btn 滤镜 复古怀旧","btn 滤镜 多彩夏日","btn 滤镜 缤纷梦幻","btn 滤镜 清新淡雅"]
                self.typelist=["曝光台","事故大爆料","美丽风景","随手拍"]
                self.shareitem=["icon 分享 朋友圈","icon 分享 微信","icon 分享 微博","icon 分享 QQ空间","icon 分享 QQ"]
                location=self.driver.get_window_size('current')
                self.l(str(location))
                #findCoordinateX=location["width"]/6
                IPCCoordinateX=location["width"]/2
                #myCoordinateX=(location["width"]/6)*5
                heightY=(location["height"]-10)
                self.topButtonlocation=self.driver.find_element_by_name("广场").location
                self.topButtonlocationX=repr(self.topButtonlocation['x'])
                self.topButtonlocationY=repr(self.topButtonlocation['y'])
                self.l("得到顶部按钮坐标")
                self.l("==测试准备完成==")
                
                self.driver.tap([(IPCCoordinateX,heightY)], 2)
                sleep(2)
                self.driver.find_element_by_name("bg 进入相册").click()
                self.driver.find_element_by_name("本地视频").click()
                self.driver.find_element_by_name("精彩视频").click()
                self.fvl=self.driver.find_elements_by_name("12s")
                self.fvll=len(self.fvl)
                n=0
                if self.fvll>0:
                    while n<(self.fvll-1):
                        n=n+1
                        if n==5:
                            break
                        self.l("点击第 "+str(n)+" 个精彩视频")
                        sleep(1)
                        self.driver.find_elements_by_name("12s")[n].click()
                        
                        #判断即可分享界面已经打开
                        if self.driver.find_elements_by_name("即刻分享")>0:
                            #播放精彩视频5秒
                            sleep(5)
                            #选择 滤镜 选项
                            self.driver.find_element_by_name("滤镜").click()
                            #随机选择一个滤镜效果
                            self.item=random.choice(self.filterlist)
                            self.l("滤镜: "+self.item+" 已被选择")
                            self.driver.find_element_by_name(self.item).click()
                            #选择 类型 选项
                            self.driver.find_element_by_name("类型").click()
                            #随机选择一个广场项目
                            self.item2=random.choice(self.typelist)
                            self.l("广场类型: "+self.item2+" 已被选择")
                            self.driver.find_element_by_name(self.item2).click()
                            #随机选择一个评论
                            randomnumner=[random.randint(1,3)]
                            self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell"+str(randomnumner)).click()
                            sleep(10)
                            self.itemshare=random.choice(self.shareitem)
                            self.l("分享选项: "+self.itemshare+" 被选择")
                            self.driver.find_element_by_name(self.itemshare).click()
                            sleep(2)
                            self.driver.tap([(self.topButtonlocationX,self.topButtonlocationY)],1)
                            sleep(3)                    
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