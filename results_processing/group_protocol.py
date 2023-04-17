from __future__ import annotations

from pages.output_page import table_to_html
from results_processing.results_table import ResultsTable, ResultsItem


class CupItem:
    def __init__(self, first_result: ResultsItem, output_format):
        self.athlete_name = first_result.athlete_name
        self.athlete_id = first_result.athlete_id
        self.athlete_url = first_result.athlete_url
        self.stages_scores = []
        self.stages_rewards = []
        self.cup_score = 0
        self.cup_reward = 0
        self.total_reward = 0
        self.output_format = output_format

    def add_result(self, result: ResultsItem):
        self.stages_scores.append(result.score)
        self.stages_rewards.append(result.reward)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "\t".join(
            [
                str(getattr(self, self.output_format[column_name]))
                for column_name in self.output_format
            ]
        )


class CupTable:
    def __init__(self, segments_results: list[ResultsTable], group_name: str, output_format: dict):
        self.group_name = group_name
        self.output_format = output_format
        self.segments_results = segments_results
        self._build_scores_lists()

    def _build_scores_lists(self):
        self.table: list[CupItem] = []
        for segment_result in self.segments_results:
            for result in segment_result.table:
                self._add_athlete_result(result)

    def _add_athlete_result(self, result: ResultsItem):
        athlete = self._get_athlete_by_id(result.athlete_id)
        if not athlete:
            athlete = CupItem(result, self.output_format)
            self.table.append(athlete)
        athlete.add_result(result)

    def _get_athlete_by_id(self, athlete_id: str) -> CupItem | None:
        for athlete in self.table:
            if athlete.athlete_id == athlete_id:
                return athlete
        return None

    def sort_by_total_reward(self):
        self.table = sorted(
            self.table, key=lambda competotor: competotor.total_reward, reverse=True
        )

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        result = "\t".join(self.output_format.keys())
        for item in self.table:
            result += f"\n{item}"
        return result

    def to_html(self):
        return table_to_html(str(self))
