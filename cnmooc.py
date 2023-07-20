from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from exception import do_exception


def cnmooc_search(keyword):
    url = f'https://www.cnmooc.org/portal/frontCourseIndex/course.mooc?k={keyword}&n=course&f=0&t=&m=&e=all&l=all&c=all&p=1&s='
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'view-item')))
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        content_list = soup.find_all(class_='view-item')
        for data in content_list:
            courseName = ''.join(data.find(class_='link-default').contents[0].split())
            courseTime = data.find(class_='cview-time').text
            teacherName = data.find(class_='t-name').text
            schoolName = data.find(class_='t-school').text
            imgUrl = data.find(class_='view-img').find('img')['src']
            courseUrl = 'https://www.cnmooc.org/' + data.find(class_='view-img')['href']
            print(courseName, courseTime, schoolName, teacherName, courseUrl)
    except Exception as e:
        do_exception("cnmooc", keyword)
