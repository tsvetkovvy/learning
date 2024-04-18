""" Teams """
import datetime
from typing import Tuple
from resource import Resource

class Team:
    def __init__(self, raw_stat: str):
        self._title, team_resources_stats = self._parse_team_resources(raw_stat)
        self._team_resources = {}

        for resource_title, resource_measure_title, stat_dttm, stat_value in self._parse_team_resources_stats(
                team_resources_stats
        ):
            resource = self._team_resources.setdefault(
                resource_title,
                Resource(
                    title=resource_title,
                )
            )
            resource.append_with_measure(resource_measure_title, stat_dttm, stat_value)

    @property
    def title(self):
        return self._title

    @property
    def team_resources(self):
        return self._team_resources

    @staticmethod
    def _parse_team_resources(team_stats: str) -> Tuple[str, str]:
        title, team_resources_stats = team_stats.split("|")
        return title, team_resources_stats

    @staticmethod
    def _parse_team_resources_stats(team_resources_stats):
        for team_resources_stat in team_resources_stats.split(";"):
            resource_title, resource_measure_title, stat_dttm, stat_value = team_resources_stat\
                .strip("()").split(",")
            yield (
                resource_title,
                resource_measure_title,
                datetime.datetime.strptime(stat_dttm, "%Y-%m-%d %H:%M:%S"),
                float(stat_value)
            )

