from config import segment_id, strava_login, strava_password
from login_page import LoginPage
from segment_page import SegmentPage

from selenium import webdriver

# Set the path to the chromedriver executable
chromedriver_path_os_part = "chromedriver_mac_arm64"
chromedriver_path = f"chrome_driver/{chromedriver_path_os_part}/chromedriver"
# Create a new Chrome browser instance
driver = webdriver.Chrome(chromedriver_path)
login_page = LoginPage(driver)
login_page.load()
login_page.set_email(email=strava_login)
login_page.set_password(password=strava_password)
login_page.click_login()

segment_page = SegmentPage(driver, segment_id, date_range="this_year", filter="current_year")
segment_page.load()
segment_page.get_leaderboard()


driver.quit()
