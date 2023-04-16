from results_processing.results_table import ResultsTable

prize_fund = 100000.0
strava_login = "my_login"
strava_password = "my_password"
segment_id = "7190094"
protocol_columns = {
    "Rank": "rank",
    "Name": "athlete_name",
    "Result":"result",
    "Score": "score",
    "Reward": "reward",
    "Link to attempt": "attempt_url",
}

groups = {
    "Female": {
        "age_group": "35_44",
        "club_id": "156006",
        # "date_range": "this_month",
        "filter": "club",
        "gender": "F",
        "weight_class": "75_84",
    },
    "Male": {
        "age_group": "35_44",
        "club_id": "156006",
        # "date_range": "this_month",
        "filter": "club",
        "gender": "M",
        "weight_class": "75_84",
    },
    "Absolute": {
        "age_group": "35_44",
        "club_id": "156006",
        # "date_range": "this_month",
        "filter": "club",
        "gender": "all",
        "weight_class": "75_84",
    },
}


def calculate_score(results_table: ResultsTable):
    for competitor in results_table.table:
        competitor.score = 100.0 * results_table.get_leader().time_in_seconds / competitor.time_in_seconds
    sum_score = sum([competitor.score for competitor in results_table.table])
    for competitor in results_table.table:
        competitor.reward = competitor.score * prize_fund / sum_score
