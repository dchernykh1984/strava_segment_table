from config import segment_id
from segment_page import SegmentPage

print(SegmentPage(segment_id, date_range="this_year", filter="current_year").url)
print(SegmentPage(segment_id).url)
print(SegmentPage(segment_id, date_range="this_year", filter="club", club_id="40126").url)
print(SegmentPage(segment_id, date_range="today", filter="overall").url)
print(SegmentPage(segment_id, date_range="this_week", filter="overall").url)
print(SegmentPage(segment_id, date_range="this_month", filter="overall").url)
