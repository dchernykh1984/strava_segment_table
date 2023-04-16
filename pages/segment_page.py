import re
from time import sleep
from urllib.parse import urlparse, urlencode

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class SegmentPage:
    SEGMENT_URL_TEMPLATE = "https://www.strava.com/segments/{segment_id}"

    def __init__(self, driver, segment_id, **kwargs):
        self.driver = driver
        self.segment_id = segment_id
        self.segment_url = self.SEGMENT_URL_TEMPLATE.format(segment_id=segment_id)
        self.filter = kwargs
        if not self.filter:
            self.filter = {"filter": "overall"}
        self.url = urlparse(self.segment_url)._replace(query=urlencode(self.filter)).geturl()
        self.LEADERBOARD_TABLE = (By.XPATH, "//div[@id='results']/table")
        self.LEADERBOARD_ROWS = (By.XPATH, "//div[@id='results']/table/tbody/tr")
        self.NEXT_PAGE_BUTTON = (By.XPATH, "//li[@class='next_page']")

    def load(self):
        self.driver.get(self.url)

        # Wait for the page to load
        self.driver.implicitly_wait(10)

    def get_leaderboard(self):
        leaderboard = []
        wait = WebDriverWait(self.driver, 10)
        table = wait.until(EC.presence_of_element_located(self.LEADERBOARD_TABLE))
        rows = table.find_elements(*self.LEADERBOARD_ROWS)
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 4:
                rank = cells[0].text.strip() if cells[0].text else "1"
                athlete_name = cells[1].text.strip()
                date = cells[2].text.strip()
                result = cells[7].text.strip()
                athlete_url = cells[1].find_element(By.TAG_NAME, "a").get_attribute("href")
                athlete_id_match = re.search(r"/athletes/(\d+)", athlete_url)
                attempt_url = cells[2].find_element(By.TAG_NAME, "a").get_attribute("href")
                if athlete_id_match:
                    athlete_id = athlete_id_match.group(1)
                leaderboard.append(
                    {
                        "rank": rank,
                        "athlete_name": athlete_name,
                        "athlete_id": athlete_id,
                        "result": result,
                        "date": date,
                        "attempt_url": attempt_url,
                        "athlete_url": athlete_url,
                    }
                )
        self.leaderboard = leaderboard
        return leaderboard

    def get_full_leaderboard(self):
        full_leaderboard = []
        current_page = 1
        while True:
            leaderboard = self.get_leaderboard()
            full_leaderboard.extend(leaderboard)
            next_page_button = self.driver.find_elements(*self.NEXT_PAGE_BUTTON)
            if len(next_page_button) > 0 and not next_page_button[0].get_attribute(
                "class"
            ).startswith("disabled"):
                next_page_button[0].find_element(By.TAG_NAME, "a").click()
                sleep(5)
                current_page += 1
            else:
                break
        return full_leaderboard
