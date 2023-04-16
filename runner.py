from config import (
    segment_id,
    strava_login,
    strava_password,
    groups,
    calculate_score, protocol_columns,
)
from pages.login_page import LoginPage
from pages.segment_page import SegmentPage

from selenium import webdriver

# Set the path to the chromedriver executable
from results_processing.results_table import ResultsTable

chromedriver_path_os_part = "chromedriver_mac_arm64"
chromedriver_path = f"chrome_driver/{chromedriver_path_os_part}/chromedriver"
# Create a new Chrome browser instance
driver = webdriver.Chrome(chromedriver_path)
login_page = LoginPage(driver)
login_page.load()
login_page.set_email(email=strava_login)
login_page.set_password(password=strava_password)
login_page.click_login()

for group_name, segment_filter in groups.items():
    segment_page = SegmentPage(driver, segment_id, **segment_filter)
    segment_page.load()
    leaderboard = segment_page.get_full_leaderboard()

    results = ResultsTable(leaderboard, group_name, protocol_columns)
    calculate_score(results)
    with open(f"{group_name}_{segment_id}.txt", "w") as protocol:
        protocol.write(str(results))
    with open(f"{group_name}_{segment_id}_raw.txt", "w") as raw_data:
        raw_data.write(str(leaderboard))


# driver.quit()
