""" Resource measures """
import datetime
import statistics
from dataclasses import dataclass
from enum import Enum


@dataclass
class ResourceStat:
    stat_dttm: datetime.datetime
    stat_value: float

class UsageType(Enum):
    STABLE = "STABLE"
    REDUCED = "REDUCED"
    HOPS = "HOPS"

class Intensity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    INCREDIBLE = "INCREDIBLE"

class Decision(Enum):
    TURN_OFF = "TURN_OFF"
    USE_CURRENT = "USE_CURRENT"
    EXTEND = "EXTEND"

class BaseResourceMeasure:
    who_am_i = None

    def __init__(self, resource_measure_title: str):
        self._title = resource_measure_title
        self._resource_stats = []
        self._stats_average = None
        self._stats_median = None
        self._usage_type = None
        self._intensity = None
        self._decision = None

    @property
    def title(self):
        return self._title

    @property
    def resource_stats(self):
        return self._resource_stats

    @property
    def stats_average(self):
        return self._stats_average

    @property
    def stats_median(self):
        return self._stats_median

    @property
    def usage_type(self):
        return self._usage_type

    @property
    def intensity(self):
        return self._intensity

    @property
    def decision(self):
        return self._decision

    def append_stats(self, stat_dttm: datetime.datetime, stat_value: float):
        self._resource_stats.append(ResourceStat(stat_dttm, stat_value))
        self._get_decision()

    def _get_decision(self):
        self._calc_aggregation()
        self._calc_usage_type()
        self._calc_intensity()
        if self._intensity == Intensity.LOW:
            self._decision = Decision.TURN_OFF
        elif self._intensity == Intensity.MEDIUM:
            if self._usage_type == UsageType.REDUCED:
                self._decision = Decision.TURN_OFF
            else:
                self._decision = Decision.USE_CURRENT
        elif self._intensity == Intensity.HIGH:
            if self._usage_type == UsageType.REDUCED:
                self._decision = Decision.USE_CURRENT
            else:
                self._decision = Decision.EXTEND
        elif self._intensity == Intensity.INCREDIBLE:
            self._decision = Decision.EXTEND
        else:
            ValueError(f"Cannot make decision with {self._intensity} and {self._usage_type}")

    def _calc_aggregation(self):
        self._stats_average = statistics.mean([
            resource_stat.stat_value for resource_stat in self._resource_stats])
        self._stats_median = statistics.median([
            resource_stat.stat_value for resource_stat in self._resource_stats]) + 0.0000000001

    def _calc_usage_type(self):
        percent = self._stats_average / self._stats_median * 100
        if 75 <= percent <= 125:
            self._usage_type = UsageType.STABLE
        elif percent < 75:
            self._usage_type = UsageType.REDUCED
        elif percent > 125:
            self._usage_type = UsageType.HOPS
        else:
            raise ValueError(f"Got in trouble with percent {percent} of usage type for {self._title}")

    def _calc_intensity(self):
        if self._stats_median < 0:
            raise ValueError(f"Median {self._stats_median} is negative for {self._title}")
        elif self._stats_median <= 30:
            self._intensity = Intensity.LOW
        elif 30 < self._stats_median <= 60:
            self._intensity = Intensity.MEDIUM
        elif 60 < self._stats_median <= 90:
            self._intensity = Intensity.HIGH
        elif self._stats_median > 90:
            self._intensity = Intensity.INCREDIBLE
        else:
            raise ValueError(f"Got in trouble with median {self._stats_median} for {self._title}")


class NetFlowResourceMeasure(BaseResourceMeasure):
    who_am_i = "NetFlow"


class CPUResourceMeasure(BaseResourceMeasure):
    who_am_i = "CPU"


class RAMResourceMeasure(BaseResourceMeasure):
    who_am_i = "RAM"


class ResourceMeasureFactory(BaseResourceMeasure):
    def produce(self):
        if self._title == NetFlowResourceMeasure.who_am_i:
            return NetFlowResourceMeasure(self._title)
        if self._title == CPUResourceMeasure.who_am_i:
            return CPUResourceMeasure(self._title)
        if self._title == RAMResourceMeasure.who_am_i:
            return RAMResourceMeasure(self._title)
        else:
            ValueError(f"Unknown resource measure type: {self._title}")
