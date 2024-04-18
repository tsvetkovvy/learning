""" Resource """
from resource_measure import ResourceMeasureFactory


class Resource:
    def __init__(self, title):
        self._title = title
        self._measures = {}

    @property
    def title(self):
        return self._title

    @property
    def measures(self):
        return self._measures

    def append_with_measure(self, resource_measure_title, stat_dttm, stat_value):
        resource_measure = self._measures.setdefault(
            resource_measure_title,
            ResourceMeasureFactory(resource_measure_title).produce()
        )

        resource_measure.append_stats(stat_dttm, stat_value)
