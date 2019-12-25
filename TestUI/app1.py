from appium import webdriver
import time


# 滑动屏幕
# 获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 查找元素是否存在
def findItem(el):
    source = driver.page_source
    if el in source:
        return True
    else:
        return False


def findNewsADItem(el1, el2):
    r_el1 = findItem(el1)
    r_el2 = findItem(el2)
    return r_el1 or r_el2


# 判断滑动到的是否是广告
def isAD(el):
    if not findItem(el):
        return False
    if findItem("com.hupu.games:id/tt_native_video_layout"):  # 是否找到头条视频广告
        driver.find_element_by_id("com.hupu.games:id/tt_native_video_layout").click()
        time.sleep(2)
        driver.find_element_by_id("com.hupu.games:id/tt_titlebar_back").click()
        return True
    elif findItem("com.hupu.games:id/layout_ad_content"):  # 否则是否找到推荐列表非头条视频广告（品牌大图，头条大图）
        driver.find_element_by_id("com.hupu.games:id/layout_ad_content").click()
        time.sleep(2)
        if findItem("com.hupu.games:id/btn_back_arrow"):
            driver.find_element_by_id("com.hupu.games:id/btn_back_arrow").click()
            if findItem("com.hupu.games:id/btn_close"):
                driver.find_element_by_id("com.hupu.games:id/btn_close").click()
        elif findItem("com.hupu.games:id/tt_titlebar_back"):
            driver.find_element_by_id("com.hupu.games:id/tt_titlebar_back").click()
        return True
    elif findItem("com.hupu.games:id/item_news_big_layout"):  # 是否找到新闻列表的大图广告
        driver.find_element_by_id("com.hupu.games:id/item_news_big_layout").click()
        time.sleep(2)
        if findItem("com.hupu.games:id/btn_back_arrow"):
            driver.find_element_by_id("com.hupu.games:id/btn_back_arrow").click()
            if findItem("com.hupu.games:id/btn_close"):
                driver.find_element_by_id("com.hupu.games:id/btn_close").click()
        elif findItem("com.hupu.games:id/tt_titlebar_back"):
            driver.find_element_by_id("com.hupu.games:id/tt_titlebar_back").click()
        return True
    return False
    # if findItem("com.hupu.games:id/newsVideoContainer"):
    #     driver.find_element_by_id("com.hupu.games:id/newsVideoContainer").click()
    #     time.sleep(2)
    #     if findItem("com.hupu.games:id/tt_titlebar_back"):
    #         driver.find_element_by_id("com.hupu.games:id/tt_titlebar_back").click()
    # if findItem("android:id/parentPanel"):  # 判断是否有弹出弹窗
    #     swipeUp(t)
    # if findItem("android:id/alertTitle"):  # 判断是否有弹出弹窗
    #     driver.find_element_by_id("android:id/button2").click()


def isNewsAD(el1, el2):
    if not findNewsADItem(el1, el2):
        return False
    if findItem("com.hupu.games:id/tt_native_video_layout"):  # 是否找到头条视频广告
        time.sleep(2)
        driver.find_element_by_id("com.hupu.games:id/tt_native_video_layout").click()
        time.sleep(2)
        driver.find_element_by_id("com.hupu.games:id/tt_titlebar_back").click()
        return True
    elif findItem("com.hupu.games:id/layout_ad_content"):
        time.sleep(2)  # 否则是否找到推荐列表非头条视频广告（品牌大图，头条大图）
        driver.find_element_by_id("com.hupu.games:id/layout_ad_content").click()
        time.sleep(2)
        if findItem("com.hupu.games:id/btn_back_arrow"):
            driver.find_element_by_id("com.hupu.games:id/btn_back_arrow").click()
            if findItem("com.hupu.games:id/btn_close"):
                driver.find_element_by_id("com.hupu.games:id/btn_close").click()
        elif findItem("com.hupu.games:id/tt_titlebar_back"):
            driver.find_element_by_id("com.hupu.games:id/tt_titlebar_back").click()
        return True
    elif findItem("com.hupu.games:id/item_news_big_layout"):
        time.sleep(2)  # 是否找到新闻列表的大图广告
        driver.find_element_by_id("com.hupu.games:id/item_news_big_layout").click()
        time.sleep(2)
        if findItem("com.hupu.games:id/btn_back_arrow"):
            driver.find_element_by_id("com.hupu.games:id/btn_back_arrow").click()
            if findItem("com.hupu.games:id/btn_close"):
                driver.find_element_by_id("com.hupu.games:id/btn_close").click()
        elif findItem("com.hupu.games:id/tt_titlebar_back"):
            driver.find_element_by_id("com.hupu.games:id/tt_titlebar_back").click()
        return True
    return False


if __name__ == "__main__":
    # 配置设备和App信息

    # 安卓
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '5ENDU19124004356',  # OPPO:O74LKZEY99999999  小米8：e89fc8ee  华为V20：5ENDU19124004356
        'platformVersion': '9',  # OPPO：5.1 小米8：8.1.0  华为V20：9
        'appPackage': 'com.hupu.games',
        'appActivity': 'com.hupu.games.activity.LaunchActivity',
        'noReset': 'true'
    }

    # 启动appium后，确认手机连上电脑，然后执行，就会启动App
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 休眠3秒等待页面加载完成
    time.sleep(3)

    # 切换到线下环境
    # driver.find_element_by_xpath("//android.widget.RadioGroup[@content-desc=\"server\"]/android.widget.RadioButton[3]").click()
    # driver.find_element_by_id("com.hupu.games:id/btn_save").click()
    # driver.close_app()

    # 点击开屏并且返回

    # driver.find_element_by_id("com.hupu.games:id/action_bar_root").click()
    # driver.find_element_by_id("com.hupu.games:id/img_ads_container").click()
    # time.sleep(3)
    # driver.find_element_by_id("com.hupu.games:id/btn_back_arrow").click()
    # driver.find_element_by_id("com.hupu.games:id/btn_close").click()

    # 点击开屏的跳过按钮
    if findItem("com.hupu.games:id/tv_timer_jump"):
        driver.find_element_by_id("com.hupu.games:id/tv_timer_jump").click()
    time.sleep(4)

    # 首页推荐点击三个广告位
    # i = 0
    # sum = 0
    # while (i < 20):
    #     result = isAD("com.hupu.games:id/advertiser_layout")
    #     if result:
    #         sum += 1
    #     if sum == 3:
    #         break
    #     else:
    #         i += 1
    #         time.sleep(2)
    #         swipeUp(1000)

    # NBA新闻列表广告位
    driver.find_element_by_xpath("//*[@text='NBA']").click()

    ids = ["com.hupu.games:id/no_interest_icon", "com.hupu.games:id/bottom_layout",
           "text=\"广告\" class=\"android.widget.TextView\""]
    i = 0
    sum = 0
    while (i < 20):
        for id in ids:
            result = isAD(id)
            if result:
                break
        if result:
            sum += 1
        if sum == 8:
            break
        else:
            i += 1
            time.sleep(2)
            swipeUp(1200)
