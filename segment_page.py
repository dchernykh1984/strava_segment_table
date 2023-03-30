from urllib.parse import urlparse, urlencode

from results_table import ResultsTable


class SegmentPage:
    SEGMENT_URL_TEMPLATE = "https://www.strava.com/segments/{segment_id}"

    def __init__(self, segment_id, **kwargs):
        self.segment_id = segment_id
        self.segment_url = self.SEGMENT_URL_TEMPLATE.format(segment_id=segment_id)
        self.filter = kwargs
        if not self.filter:
            self.filter = {"filter": "overall"}
        self.url = urlparse(self.segment_url)._replace(query=urlencode(self.filter)).geturl()

    def _open_page(self):
        pass

    def _close_page(self):
        pass

    def get_results(self) -> ResultsTable:
        return ResultsTable()
