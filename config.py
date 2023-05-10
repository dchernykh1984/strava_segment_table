from results_processing.group_protocol import CupTable
from results_processing.results_table import ResultsTable

# male_count = 1
# female_count = 0

# prize_fund_stage = {"Female": 100.0*female_count, "Male": 100.0*male_count}
# prize_fund_total = {"Female": 600.0*female_count, "Male": 600.0*female_count}
segment_ids = [
    "34174721",  # [1] Road race uphill butakovka (The best one I suppose) - main one
    "34192312",  # [1] Road race flat promzona
    "34204769",  # [1] MTB uphill, volnyi veter (easier - need to have a look and create my own segment, also check if it is possible to ride there by road race bike
    "34212945",  # [3] MTB downhill, japan road (need to create my own segment and check current one
]
segment_protocol_columns = {
    "Rank": "rank",
    "Name": "athlete_name",
    "Result": "result",
    "Score": "score",
    "Link_to_attempt": "attempt_url",
}
total_protocol_columns = {
    "Rank": "rank",
    "Name": "athlete_name",
    "Stages_scores": "stages_scores",
    "Total_score": "cup_score",
    "Link_to_athlete": "athlete_url",
}
total_protocol_sort_by = "cup_score"

groups = {
    "Female": {
        "age_group": "35_44",
        "club_id": "731125",
        "date_range": "this_year",
        "filter": "current_year",
        "gender": "F",
        "weight_class": "75_84",
    },
    "Male": {
        "age_group": "35_44",
        "club_id": "731125",
        "date_range": "this_year",
        "filter": "current_year",
        "gender": "M",
        "weight_class": "75_84",
    },
}


def calculate_stage_score(results_table: ResultsTable):
    for competitor in results_table.table:
        competitor.score = (
            100.0 * results_table.get_leader().time_in_seconds / competitor.time_in_seconds
        )


def total_score_calculator(results_table: CupTable):
    for competitor in results_table.table:
        stages_scores = sorted(competitor.stages_scores, reverse=True)
        competitor.cup_score = (
            sum(stages_scores[:3]) if len(stages_scores) >= 3 else sum(stages_scores)
        )


def total_score_calculator_alternative(results_table: CupTable):
    for competitor in results_table.table:
        stages_scores = sorted(competitor.stages_scores, reverse=True)
        competitor.cup_score = (
            sum(stages_scores[:2]) if len(stages_scores) >= 2 else sum(stages_scores)
        )
