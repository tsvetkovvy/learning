""" Reports """
import json

from team import Team


class BaseReport:
    def __init__(self, team: Team):
        self._team = team

    def build(self):
        NotImplementedError()


class JsonReport(BaseReport):

    def build(self):
        report = {}
        team_stat = report.setdefault(self._team.title, {})
        for team_resource in self._team.team_resources.values():
            team_resource_stat = team_stat.setdefault(team_resource.title, {})
            for team_resource_measure in team_resource.measures.values():
                team_resource_stat[team_resource_measure.title] = {
                    "mean": team_resource_measure.stats_average,
                    "median": team_resource_measure.stats_median,
                    "usage_type": team_resource_measure.usage_type.value,
                    "intensity": team_resource_measure.intensity.value,
                    "decision": team_resource_measure.decision.value,
                }
        return json.dumps(report)

