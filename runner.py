import platform

from selenium import webdriver

from config import (
    segment_ids,
    groups,
    calculate_stage_score,
    segment_protocol_columns,
    total_protocol_columns,
    total_score_calculator,
    total_protocol_sort_by,
    total_score_calculator_alternative,
)
from credentials import (
    strava_login,
    strava_password,
)
from pages.login_page import LoginPage
from pages.segment_page import SegmentPage

# Set the path to the chromedriver executable
from results_processing.group_protocol import CupTable
from results_processing.results_table import ResultsTable


def get_chromedriver_path():
    system = platform.system()
    machine = platform.machine()
    if system == 'Linux' and machine == 'x86_64':
        return 'chromedriver_linux64'
    elif system == 'Darwin' and machine == 'arm64':
        return 'chromedriver_mac_arm64'
    elif system == 'Darwin' and machine == 'x86_64':
        return 'chromedriver_mac64'
    elif system == 'Windows':
        return 'chromedriver_win32'
    else:
        raise ValueError(f'Unsupported system: {system} {machine}')


chromedriver_path_os_part = get_chromedriver_path()
chromedriver_path = f"chrome_driver/{chromedriver_path_os_part}/chromedriver"
# Create a new Chrome browser instance
driver = webdriver.Chrome(chromedriver_path)
login_page = LoginPage(driver)
login_page.load()
login_page.set_email(email=strava_login)
login_page.set_password(password=strava_password)
login_page.click_login()

with open(f"results.txt", "w", encoding="utf-8") as protocol:
    protocol.write(f"Results of strava cup")
with open(f"index.html", "w", encoding="utf-8") as html_protocol:
    html_protocol.write(f"Results of strava cup<BR>\n")

for group_name, segment_filter in groups.items():
    with open(f"results.txt", "a", encoding="utf-8") as protocol:
        protocol.write(f"Group {group_name} results")
    with open(f"index.html", "a", encoding="utf-8") as html_protocol:
        html_protocol.write(f"<BR><b>Group {group_name} results</b><BR>\n")
    group_results = []
    for segment_id in segment_ids:
        segment_page = SegmentPage(driver, segment_id, **segment_filter)
        segment_page.load()
        segment_name = segment_page.get_segment_name()
        leaderboard = segment_page.get_full_leaderboard()

        segment_results = ResultsTable(leaderboard, group_name, segment_protocol_columns)
        calculate_stage_score(segment_results)
        with open(f"results.txt", "a", encoding="utf-8") as protocol:
            protocol.write(
                f"Link to segment table: {segment_page.url}\n{str(segment_results)}"
            )
        with open(f"index.html", "a", encoding="utf-8") as html_protocol:
            html_protocol.write(
                f'<a href="{segment_page.url}">{segment_name}</a> segment results: \n'
                f'<BR>{segment_results.to_html()}'
            )
        #         with open(f"{group_name}_{segment_id}_raw.txt", "w", encoding="utf-8") as raw_data:
        #             raw_data.write(f"Link to segment table: {segment_page.segment_url}\n{str(leaderboard)}")
        group_results.append(segment_results)
    cup_table = CupTable(group_results, group_name, total_protocol_columns)
    total_score_calculator(cup_table)
    cup_table.sort_by(total_protocol_sort_by)

    cup_table_alternative = CupTable(group_results, group_name, total_protocol_columns)
    total_score_calculator_alternative(cup_table_alternative)
    cup_table_alternative.sort_by(total_protocol_sort_by)

    with open(f"results.txt", "a", encoding="utf-8") as protocol:
        protocol.write(f"Cup results\n{str(cup_table)}")
    with open(f"index.html", "a", encoding="utf-8") as html_protocol:
        html_protocol.write(f"Cup results (3 best stages)\n<BR>{cup_table.to_html()}")

    with open(f"results.txt", "a", encoding="utf-8") as protocol:
        protocol.write(f"Cup results\n{str(cup_table_alternative)}")
    with open(f"index.html", "a", encoding="utf-8") as html_protocol:
        html_protocol.write(
            f"Alternative cup results (2 best stages)\n<BR>{cup_table_alternative.to_html()}"
        )

driver.quit()
print("Results is located https://dchernykh1984.github.io/strava_segment_table/")
