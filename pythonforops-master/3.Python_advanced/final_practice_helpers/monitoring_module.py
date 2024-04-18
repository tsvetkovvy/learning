import datetime
from collections import deque
from functools import partial
import random
from flask import Flask
from faker import Faker


app = Flask(__name__)


def get_team_resource_using(faker: Faker, observations_conf: dict, max_resources: int = 10):
    observations = []
    monitoring_delta = datetime.timedelta(hours=1)
    time_format = "%Y-%m-%d %H:%M:%S"

    for _ in range(max_resources):
        resource = faker.license_plate()
        for observations_type in observations_conf["observations_types"]:
            observation_datetime = datetime.datetime.now() - datetime.timedelta(hours=observations_conf["max_observations"])
            for _ in range(observations_conf["max_observations"]):
                observations.append("(" + ",".join((
                    resource,
                    observations_type,
                    observation_datetime.strftime(time_format),
                    str(int(observations_conf["distribution"]() * 100))
                )) + ")")
                observation_datetime += monitoring_delta

    print(observations)
    print(observations_conf["distribution"])
    return faker.bs() + "|" + ";".join(observations)


@app.route("/monitoring/infrastructure/using/summary/<int:company_branch>")
def get_infrastructure_using_summary(company_branch):
    team_count = 4
    seed = int(company_branch)
    Faker.seed(seed)
    fake = Faker()
    random.seed(seed)

    team_stats = []

    distributions = deque((partial(random.betavariate, alpha=0.1, beta=0.1),
                           partial(random.betavariate, alpha=1, beta=3),
                           partial(random.betavariate, alpha=8, beta=8),
                           partial(random.betavariate, alpha=1, beta=1))
                          )

    for _ in range(team_count):
        distribution = distributions.pop()
        team_stats.append(get_team_resource_using(fake,
                                                  observations_conf={
                                                      "max_observations": 200,
                                                      "observations_types": ["CPU", "RAM", "NetFlow"],
                                                      "distribution": distribution
                                                  }))
        distributions.appendleft(distribution)
    return "$".join(team_stats), 200


if __name__ == '__main__':
    app.run(port=21122)

