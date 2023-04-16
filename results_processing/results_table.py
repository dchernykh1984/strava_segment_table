class ResultsItem:
    def __init__(self, data: dict, output_format):
        self.athlete_name = data["athlete_name"]
        self.athlete_id = data["athlete_id"]
        self.athlete_url = data["athlete_url"]
        self.result = data["result"]
        self.attempt_url = data["attempt_url"]
        self.output_format = output_format

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "\t".join(
            [getattr(self, self.output_format[column_name]) for column_name in self.output_format]
        )


class ResultsTable:
    def __init__(self, list_of_results: list[dict], group_name: str, output_format: dict):
        self.table = [ResultsItem(data) for data in list_of_results]
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
