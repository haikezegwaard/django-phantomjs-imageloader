from django.shortcuts import render_to_response
import urllib

def index(request):

    from selenium import webdriver

    driver = webdriver.PhantomJS() # or add to your PATH
    driver.set_window_size(1024, 768) # optional
    driver.get('http://buzzart.django-dev.fundament.nl/digest/2')
    #driver.save_screenshot('screen.png') # save a screenshot to disk
    # get the image source
    img = driver.find_element_by_xpath('//div[@id="availability_plot"]/img')
    src = img.get_attribute('src')

    # download the image
    urllib.urlretrieve(src, "captcha.png")
    return render_to_response('result.html', {'year': '1234'})