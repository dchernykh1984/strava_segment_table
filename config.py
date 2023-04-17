from results_processing.group_protocol import CupTable
from results_processing.results_table import ResultsTable

prize_fund_stage = {"Female": 10.0, "Male": 100.0}
prize_fund_total = {"Female": 90.0, "Male": 900.0}
segment_ids = ["7190094", "7258238"]
segment_protocol_columns = {
    "Rank": "rank",
    "Name": "athlete_name",
    "Result": "result",
    "Score": "score",
    "Reward": "reward",
    "Link_to_attempt": "attempt_url",
}
total_protocol_columns = {
    "Rank": "rank",
    "Name": "athlete_name",
    "ID": "athlete_id",
    "Stages_scores": "stages_scores",
    "Total_score": "cup_score",
    "Stage_rewards": "stages_rewards",
    "Cup_reward": "cup_reward",
    "Total_reward": "total_reward",
    "Link_to_athlete": "athlete_url",
}
total_protocol_sort_by = "total_reward"

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
}


def calculate_stage_score(results_table: ResultsTable):
    for competitor in results_table.table:
        competitor.score = (
            100.0 * results_table.get_leader().time_in_seconds / competitor.time_in_seconds
        )
    sum_score = sum([competitor.score for competitor in results_table.table])
    for competitor in results_table.table:
        competitor.reward = (
            competitor.score * prize_fund_stage[results_table.group_name] / sum_score
        )


def total_score_calculator(results_table: CupTable):
    for competitor in results_table.table:
        competitor.cup_score = sum(competitor.stages_scores)
    cup_sum_score = sum([competitor.cup_score for competitor in results_table.table])
    for competitor in results_table.table:
        competitor.cup_reward = (
            competitor.cup_score * prize_fund_stage[results_table.group_name] / cup_sum_score
        )
        competitor.total_reward = competitor.cup_reward + sum(competitor.stages_rewards)
