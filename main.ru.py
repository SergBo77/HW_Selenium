from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
import time

browser = webdriver.Chrome()

browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

print('Приветствуем вас в поисковом сервие Википедии!')
request = input('Введите ваш запрос на поиск информации в Википедии: ')

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(request)
search_box = browser.find_element(By.ID, 'searchButton')
search_box.send_keys(Keys.RETURN)

while True:

 selection = input('Вы находитесь на выбранной странице, для выбора действия выберите команду:'
                  ' \n читать параграфы - p, \n перейти на одну из связанных страниц - s, \n '
                  'выйти из программы - q \n ваш выбор: ')

 if selection == 'p':
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    #Для перебора пишем цикл
    for paragraph in paragraphs:
        print(paragraph.text)
        select = input('Читаем следующий параграф y/n?: ')
        if select == 'y':
           continue
        else:
            break
    continue


 elif selection == 's':
      hatnotes = []
      for element in browser.find_elements(By.TAG_NAME, "div"):
          cl = element.get_attribute("class")
          if cl == "hatnote navigation-not-searchable":
           hatnotes.append(element)

      hatnote = random.choice(hatnotes)
      link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
      browser.get(link)

      continue

 elif selection == 'q':
     print('Программа завершена! До новых встреч!')
     break