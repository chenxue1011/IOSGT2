import unittest
import logging
import os
import PlayIPCEmergencyVideoTest
import PlayIPCFavoriteVideoTest
import PlayIPCLoopVideoTest
import PlayLocalLoopVideoTest
import PlayLocalEmergencyVideoTest
import PlayLocalFavoriteVideoTest
import PreviewTest
import ShareEmergencyVideoTest
import ShareFavoriteVideoTest
import TakeFavoriteVideoTest
import time

def getTime():
    return time.time()

def l(msg):
    print msg
    logging.info(msg)
    
def titleshow(msg):
    print '*****************************'
    logging.info('*****************************')
    print ' '+msg
    logging.info(' '+msg)
    print '*****************************'
    logging.info('*****************************')
    
if __name__ == '__main__':
    starttime=time.time()
    starttime2=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starttime))
    timesstamp=str(starttime2)
    logPath=os.getcwd()+"/testLog_"+timesstamp+".txt"
    print str(logPath)
    logging.basicConfig(filename=logPath,filemode='a',level=logging.INFO,format = '%(asctime)s : %(message)s')
    
    suite1 = unittest.TestLoader().loadTestsFromTestCase(PlayIPCEmergencyVideoTest.PlayIPCEmergencyVideoTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(PlayIPCFavoriteVideoTest.PlayIPCFavoriteVideoTest)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(PlayIPCLoopVideoTest.PlayIPCLoopVideoTest)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(PlayLocalLoopVideoTest.PlayLocalLoopVideoTest)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(PlayLocalEmergencyVideoTest.PlayLocalEmergencyVideoTest)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(PlayLocalFavoriteVideoTest.PlayLocalFavoriteVideoTest)
    suite7 = unittest.TestLoader().loadTestsFromTestCase(PreviewTest.PreviewTest)
    suite8 = unittest.TestLoader().loadTestsFromTestCase(ShareEmergencyVideoTest.ShareEmergencyVideoTest)
    suite9 = unittest.TestLoader().loadTestsFromTestCase(ShareFavoriteVideoTest.ShareFavoriteVideoTest)
    suite10 = unittest.TestLoader().loadTestsFromTestCase(TakeFavoriteVideoTest.TakeFavoriteVideoTest)
    
    #testSuite=unittest.TestSuite([suite1,suite2,suite3,suite4,suite5,suite6,suite7,suite8,suite9,suite10])
    #(suite1,1),(suite2,1),(suite3,1),(suite4,1),(suite5,1),(suite6,1),(suite7,1),
    s=[(suite8,1),(suite9,1),(suite10,1),(suite1,1),(suite2,1),(suite3,1),(suite4,1),(suite5,1),(suite6,1),(suite7,1)]
    for tc in s:
        caseName=str(tc[0]).split("[<")[1].split(".")[0]
        n=tc[1]
        titleshow("TestCase: "+caseName+" ==!^_^!==  Run Time: "+str(n))
        stime=getTime()
        for i in range(n):
            l("-->Execute "+str(i+1)+" Round")
            unittest.TextTestRunner(verbosity=2).run(tc[0])
        etime=getTime()
        rtime=etime-stime
        l("RunTime: "+str(rtime))
    
#     testSuite2=unittest.TestSuite([suite2])
#     titleshow("suite2: PlayIPCFavoriteVideoTest")
#     stime=getTime()
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite2)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime))
#         
#     testSuite3=unittest.TestSuite([suite3])
#     titleshow("suite3: PlayIPCLoopVideoTest")
#     stime=getTime()    
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite3)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime))    
#     
#     testSuite4=unittest.TestSuite([suite4])
#     titleshow("suite4: PlayLocalLoopVideoTest")
#     stime=getTime()
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite4)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime))    
#     testSuite5=unittest.TestSuite([suite5])
#     titleshow("suite5: PlayLocalEmergencyVideoTest") 
#     stime=getTime()  
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite5)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime))
#        
#     testSuite6=unittest.TestSuite([suite6])
#     titleshow("suite6: PlayLocalFavoriteVideoTest")  
#     stime=getTime() 
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite6)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime))
#          
#     testSuite7=unittest.TestSuite([suite7])
#     titleshow("suite7: PreviewTest")   
#     stime=getTime()
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite7)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime)) 
#              
#     testSuite8=unittest.TestSuite([suite8])
#     titleshow("suite8: ShareEmergencyVideoTest")  
#     stime=getTime()
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite8)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime)) 
#              
#     testSuite9=unittest.TestSuite([suite9])
#     titleshow("suite9: ShareFavoriteVideoTest")
#     stime=getTime()   
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite9)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime)) 
#              
#     testSuite10=unittest.TestSuite([suite10])
#     titleshow("suite10: TakeFavoriteVideoTest")   
#     stime=getTime()
#     for i in range(2):
#         print '-->'+str(i)
#         unittest.TextTestRunner(verbosity=2).run(testSuite10)
#     etime=getTime()
#     rtime=etime-stime
#     l("RunTime: "+str(rtime)) 