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
# login_page.load()
# login_page.set_email(email=strava_login)
# login_page.set_password(password=strava_password)
# login_page.click_login()

for group_name, segment_filter in groups.items():
    segment_page = SegmentPage(driver, segment_id, **segment_filter)
    # segment_page.load()
    # leaderboard = segment_page.get_full_leaderboard()
    leaderboard = [{'rank': '1', 'athlete_name': 'Faina Potapova', 'athlete_id': '29208031', 'result': '6:26', 'date': 'Aug 16, 2021', 'attempt_url': 'https://www.strava.com/segment_efforts/2862222963493234268', 'athlete_url': 'https://www.strava.com/athletes/29208031'}, {'rank': '2', 'athlete_name': 'Ekaterina 🐎 Stepanova', 'athlete_id': '15132446', 'result': '6:28', 'date': 'Sep 22, 2020', 'attempt_url': 'https://www.strava.com/segment_efforts/2743432038256845638', 'athlete_url': 'https://www.strava.com/athletes/15132446'}, {'rank': '3', 'athlete_name': 'Nadia :P', 'athlete_id': '4293910', 'result': '6:45', 'date': 'Aug 28, 2021', 'attempt_url': 'https://www.strava.com/segment_efforts/2866602647908150830', 'athlete_url': 'https://www.strava.com/athletes/4293910'}, {'rank': '4', 'athlete_name': 'Zhanar Terekbay', 'athlete_id': '29487934', 'result': '9:43', 'date': 'Sep 29, 2020', 'attempt_url': 'https://www.strava.com/segment_efforts/2746029278403541440', 'athlete_url': 'https://www.strava.com/athletes/29487934'}, {'rank': '5', 'athlete_name': 'Madina Akbayeva', 'athlete_id': '16374300', 'result': '10:33', 'date': 'Jun 21, 2022', 'attempt_url': 'https://www.strava.com/segment_efforts/2974324586279201176', 'athlete_url': 'https://www.strava.com/athletes/16374300'}, {'rank': '6', 'athlete_name': 'Анастасия Донец', 'athlete_id': '5967769', 'result': '10:42', 'date': 'Apr 27, 2022', 'attempt_url': 'https://www.strava.com/segment_efforts/2954298123330345206', 'athlete_url': 'https://www.strava.com/athletes/5967769'}, {'rank': '7', 'athlete_name': 'Svetlana Krassilnikova', 'athlete_id': '29050741', 'result': '11:28', 'date': 'Apr 28, 2019', 'attempt_url': 'https://www.strava.com/segment_efforts/58714348652', 'athlete_url': 'https://www.strava.com/athletes/29050741'}, {'rank': '8', 'athlete_name': 'Marina Varibrus', 'athlete_id': '20410204', 'result': '13:13', 'date': 'Sep 5, 2020', 'attempt_url': 'https://www.strava.com/segment_efforts/2737211651404381056', 'athlete_url': 'https://www.strava.com/athletes/20410204'}, {'rank': '9', 'athlete_name': 'Evgenia Tkacheva', 'athlete_id': '35597461', 'result': '14:54', 'date': 'Nov 11, 2018', 'attempt_url': 'https://www.strava.com/segment_efforts/49338400892', 'athlete_url': 'https://www.strava.com/athletes/35597461'}]

    results = ResultsTable(leaderboard, group_name, protocol_columns)
    calculate_score(results)
    with open(f"{group_name}.txt", "w") as protocol:
        protocol.write(str(results))
    with open(f"{group_name}_raw.txt", "w") as raw_data:
        raw_data.write(str(leaderboard))
    print(results)
    print(len(leaderboard))
    print(group_name)
    print(leaderboard)


# driver.quit()
