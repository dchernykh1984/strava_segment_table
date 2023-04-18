from results_processing.group_protocol import CupTable
from results_processing.results_table import ResultsTable

# male_count = 1
# female_count = 0

# prize_fund_stage = {"Female": 100.0*female_count, "Male": 100.0*male_count}
# prize_fund_total = {"Female": 600.0*female_count, "Male": 600.0*female_count}
segment_ids = ["7258238", "34037962", "34037973", "16055469", "34174721"]
segment_protocol_columns = {
    "Rank": "rank",
    "Name": "athlete_name",
    "Result": "result",
    "Score": "score",
    # "Reward": "reward",
    "Link_to_attempt": "attempt_url",
}
total_protocol_columns = {
    "Rank": "rank",
    "Name": "athlete_name",
    # "ID": "athlete_id",
    "Stages_scores": "stages_scores",
    "Total_score": "cup_score",
    # "Stage_rewards": "stages_rewards",
    # "Cup_reward": "cup_reward",
    # "Total_reward": "total_reward",
    "Link_to_athlete": "athlete_url",
}
total_protocol_sort_by = "cup_score"

groups = {
    "Female": {
        "age_group": "35_44",
        "club_id": "731125",
        "date_range": "this_month",
        "filter": "club",
        "gender": "F",
        "weight_class": "75_84",
    },
    "Male": {
        "age_group": "35_44",
        "club_id": "731125",
        "date_range": "this_month",
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
    # sum_score = sum([competitor.score for competitor in results_table.table])
    # for competitor in results_table.table:
    #     competitor.reward = (
    #         competitor.score * prize_fund_stage[results_table.group_name] / sum_score
    #     )


def total_score_calculator(results_table: CupTable):
    for competitor in results_table.table:
        stages_scores = sorted(competitor.stages_scores, reverse=True)
        competitor.cup_score = (
            sum(stages_scores[:3]) if len(stages_scores) >= 3 else sum(stages_scores)
        )
    # cup_sum_score = sum([competitor.cup_score for competitor in results_table.table])
    # for competitor in results_table.table:
    #     competitor.cup_reward = (
    #         competitor.cup_score * prize_fund_stage[results_table.group_name] / cup_sum_score
    #     )
    #     competitor.total_reward = competitor.cup_reward + sum(competitor.stages_rewards)

def total_score_calculator_alternative(results_table: CupTable):
    for competitor in results_table.table:
        stages_scores = sorted(competitor.stages_scores, reverse=True)
        competitor.cup_score = (
            sum(stages_scores[:2]) if len(stages_scores) >= 2 else sum(stages_scores)
        )