from urllib.parse import urlparse, urlencode

from selenium.webdriver.common.by import By

from results_table import ResultsTable


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

    def load(self):
        self.driver.get(self.url)

        # Wait for the page to load
        self.driver.implicitly_wait(10)

    def get_leaderboard(self):
        leaderboard = []
        table = self.driver.find_element(*self.LEADERBOARD_TABLE)
        rows = table.find_elements(*self.LEADERBOARD_ROWS)
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 4:
                leaderboard.append(
                    {
                        "rank": cells[0].text.strip() if cells[0].text else "1",
                        "athlete": cells[1].text.strip(),
                        "time": cells[2].text.strip(),
                        "date": cells[3].text.strip(),
                    }
                )
        self.leaderboard = leaderboard
        return leaderboard

    def get_results(self) -> ResultsTable:
        return ResultsTable()
