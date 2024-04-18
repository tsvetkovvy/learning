import argparse

from team import Team
from report import JsonReport


def split_teams(raw_stat: str):
    teams = [Team(team_stat) for team_stat in raw_stat.split("$")]
    for team in teams:
        print(JsonReport(team).build())


def main():
    parser = argparse.ArgumentParser(description="Resource usage report builder")
    parser.add_argument("raw_stat")
    parser.add_argument("-o", "--output", choices=["json", "markdown"])

    args = parser.parse_args()
    raw_stat = args.raw_stat
    split_teams(raw_stat)
    output = args.output


if __name__ == '__main__':
    main()
