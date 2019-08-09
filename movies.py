#coding=utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def crawMovie():
    chrome_options = Options()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')  # 增加无界面选项
    chrome_options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver=webdriver.PhantomJS()
    driver.get("https://movie.douban.com/")
    movie_list=[]
    more_btn=driver.find_element_by_xpath('(//a[@class="more-link"])[1]')
    more_btn.click()

    while True:
        start_index=len(movie_list)
        xpath_str='//a[@class="item"][position()>%d]'%start_index
        item_tags=driver.find_elements_by_xpath(xpath_str)
        print "start_index:",start_index
        print item_tags
        print "number:",len(item_tags)
        for item_tag in item_tags:
            img_tag=item_tag.find_element_by_tag_name('img')
            cover=img_tag.get_attribute("src")
            title=img_tag.get_attribute("alt")
            rating=item_tag.find_element_by_xpath(".//p/strong").text

            movie="cover:%s,title:%s,rating:%s"%(cover,title,rating)
            #print "movie:",type(movie),movie

            print u"电影名："+title
            movie_list.append(movie.encode("gbk")+"\n")
        print "--"*20
        load_more_btn=driver.find_element_by_xpath('//a[@class="more"]')
        if load_more_btn.get_attribute("style"):
            break
        load_more_btn.click()

    with open("e:\\movie_list.txt","w") as fp:
        fp.writelines(movie_list)

if __name__=="__main__":
    crawMovie()