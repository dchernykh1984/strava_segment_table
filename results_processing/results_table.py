from datetime import time, datetime


class ResultsItem:
    def __init__(self, data: dict, output_format):
        self.rank = data["rank"]
        self.athlete_name = data["athlete_name"]
        self.athlete_id = data["athlete_id"]
        self.athlete_url = data["athlete_url"]
        self.result = self.strava_time_string_to_datetime(data["result"])
        self.attempt_url = data["attempt_url"]
        self.output_format = output_format
        self.score = 0
        self.reward = 0

    @property
    def time_in_seconds(self) -> int:
        return int(self.result.hour * 3600 + self.result.minute * 60 + self.result.second)

    @staticmethod
    def strava_time_string_to_datetime(time_str: str) -> time:
        for format_str in ["%H:%M:%S", "%-H:%M:%S", "%M:%S", "%-M:%S", "%S", "%-S"]:
            try:
                time_obj = datetime.strptime(time_str, format_str).time()
                return time_obj
            except ValueError:
                pass
        raise ValueError(f"Unparsable data in time string:{time_str}")

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "\t".join(
            [str(getattr(self, self.output_format[column_name])) for column_name in self.output_format]
        )


class ResultsTable:
    def __init__(self, list_of_results: list[dict], group_name: str, output_format: dict):
        self.table = [ResultsItem(data, output_format) for data in list_of_results]
        self.group_name = group_name
        self.output_format = output_format

    def get_leader(self):
        return self.table[0]

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        result = "\t".join(self.output_format.keys())
        for item in self.table:
            result += f"\n{item}"
        return result