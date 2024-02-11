from splinter import Browser
import cv2 as cv
import pyautogui
import time

browser = Browser()


def open_web(what_wordle):
    if what_wordle == 1:
        browser.visit('https://www.nytimes.com/games/wordle/index.html')
        browser.find_by_css('.Welcome-module_button__ZG0Zh').click()
        browser.find_by_css('.Modal-module_closeIcon__TcEKb').click()
    if what_wordle == 2:
        browser.visit('https://wordlegame.org')


def type_word(word, what_wordle):
    for letter in word:
        browser.find_by_text(letter).last.click()
    if what_wordle == 1:
        browser.find_by_text('enter').last.click()
    if what_wordle == 2:
        browser.find_by_text('Enter').last.click()


# open_web()
# type_word('trend')

def color_scraper(row, what_wordle):
    change_down = 88
    x = 585
    y = 774
    time_sleep = 3
    if what_wordle == 1:
        x = 585
        y = 774
        change_down = 88
        time_sleep = 2

    if what_wordle == 2:
        x = 234
        y = 763
        change_down = 93
        time_sleep = 1

    x += change_down * row
    letter_color = ""
    time.sleep(time_sleep)
    image = pyautogui.screenshot()
    image.save('screenshot.png')
    image = cv.imread('screenshot.png')
    if what_wordle == 1:
        for i in range(5):
            if image[x, y][2] > 100 and image[x, y][1] > 100:
                letter_color = letter_color + "Y"
            elif image[x, y][1] > 100:
                letter_color = letter_color + "G"
            elif image[x, y][0] < 100 and image[x, y][1] < 100 and image[x, y][2] < 100:
                letter_color = letter_color + "N"
            y += 87  # 87
    if what_wordle == 2:
        for i in range(5):
            if image[x, y][2] > 200 and image[x, y][1] > 100:
                letter_color = letter_color + "Y"
            elif image[x, y][1] > 100 and image[x, y][0] < 100:
                letter_color = letter_color + "G"
            else:
                letter_color = letter_color + "N"
            y += 90  # 87
    return letter_color


def main():
    open_web(2)
    type_word("trend", 2)
    print(color_scraper(0, 2))


if __name__ == "__main__":
    main()
