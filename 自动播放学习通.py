import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
Driver_path=r'D:\pycharm\new\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Driver_path)
driver.get('https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=690556805&courseId=230355923&clazzid=67432045&cpi=266351710&enc=21b2e75fb1add745369c29cb44efa0d1&mooc2=1&openc=33302f79177ff6fa4fe56b13fcc2607c')
time.sleep(1)
#  登录
zhanghao = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[2]/form/div[1]/input')
mima = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[2]/form/div[2]/input')
zhanghao.send_keys('15101608475')
mima.send_keys('dongxinyang2004')
login = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[2]/form/div[3]/button')
login.click()
print("登录成功")
time.sleep(3)
# 完成登录


def time_add(nh,nm,h,m):
    global fm, fh
    if nm+m >= 60:
        fm = nm+m-60
        fh = nh+1+h
    else:
        fm = nm+m
        fh = nh+h


def play(chapter,start,finish):
    # 多节连播
    for i in range(int(start),int(finish)):
        #               开始小节-结束小节+1
        lesson_button = driver.find_element(by=By.XPATH,
                                            value='/html/body/div[5]/div[3]/div[2]/div[1]/div[2]/ul/li[{0}]/div[2]/ul/li[{1}]/div/span[1]'.format(
                                                int(chapter), int(i)))  # 第一个ul后的是章节，第二个是小节
        driver.execute_script("arguments[0].click();", lesson_button)
        time.sleep(3)
        driver.switch_to.frame(0)
        driver.find_element(by=By.XPATH,value='//*[@id="ext-gen1045"]/div[2]/div').click()
        time.sleep(5)
        driver.switch_to.frame(0)
        try:
            lesson_time = driver.find_element(by=By.XPATH,
                                              value='//*[@id="video"]/div[5]/div[4]/span[2]').get_attribute(
                "textContent")
        except Exception as e:
            lesson_time = driver.find_element(by=By.XPATH,
                                              value='//*[@id="video"]/div[6]/div[4]/span[2]').get_attribute(
                "textContent")
        now = datetime.datetime.now()
        now_time = now.strftime('%H:%M')

        driver.switch_to.default_content()
        try:
            m,s=lesson_time.strip().split(':')
            h=0
        except Exception as e:
            h, m, s = lesson_time.strip().split(':')
        lesson_second = int(h) * 3600 + int(m) * 60 + int(s)
        nh,nm=now_time.strip().split(':')
        time_add(int(nh),int(nm),int(h),int(m))
        print("第{0}章第{1}节正在播放".format(int(chapter),int(i)),"播放时间：",now_time,"时长为：",lesson_time,"结束时间：",'{0}:{1}'.format(fh,fm))
        time.sleep(lesson_second+10)


def play_one(chapter,lesson):
    #  单节播放
    lesson_button=driver.find_element(by=By.XPATH,value='/html/body/div[5]/div[3]/div[2]/div[1]/div[2]/ul/li[{0}]/'
                                                        'div[2]/ul/li[{1}]/div/span[1]'.format(int(chapter),
                                                                                               int(lesson)))
    #第一个ul后的是章节，第二个是小节
    driver.execute_script("arguments[0].click();", lesson_button)
    time.sleep(3)
    driver.switch_to.frame(0)
    driver.find_element(by=By.XPATH,value='//*[@id="ext-gen1045"]/div[2]/div').click()
    time.sleep(2)
    driver.switch_to.frame(0)
    try:
        lesson_time = driver.find_element(by=By.XPATH, value='//*[@id="video"]/div[5]/div[4]/span[2]').get_attribute("textContent")
    except Exception as e:
        lesson_time = driver.find_element(by=By.XPATH, value='//*[@id="video"]/div[6]/div[4]/span[2]').get_attribute("textContent")
    now = datetime.datetime.now()
    now_time = now.strftime('%H:%M')
    print("第{0}章第{1}节正在播放".format(int(chapter),int(lesson)),"播放时间：",now_time,"时长为：",lesson_time)
    driver.switch_to.default_content()
    try:
        m, s = lesson_time.strip().split(':')
        h = 0
    except Exception as e:
        h, m, s = lesson_time.strip().split(':')
    lesson_second = int(h) * 3600 + int(m) * 60 + int(s)
    nh, nm = now_time.strip().split(':')
    time_add(int(nh), int(nm), int(h), int(m))
    print("第{0}章第{1}节正在播放".format(int(chapter), int(lesson)), "播放时间：", now_time, "时长为：", lesson_time,
          "结束时间：", '{0}:{1}'.format(fh, fm))
    time.sleep(lesson_second + 10)


play(3,1,6)
print("结束")
