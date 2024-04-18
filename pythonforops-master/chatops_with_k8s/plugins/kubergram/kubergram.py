import re
from typing import Mapping
from errbot import BotPlugin, re_botcmd, Message
import kubernetes as k8s

class Kubergram(BotPlugin):

    def get_configuration_template(self) -> Mapping:
        return {
            "K8S_CONFIG_FILE": "/qweqeqe/qweqwe"
        }

    def __auth_in_cluster(self):
        import os
        if os.getenv("K8S_CONFIG_FILE") is None:
            return "Сначала нужно заполнить конфиг плагина!"
        k8s.config.load_kube_config()

    @re_botcmd(pattern="^Хочу поды из (?P<namespace>\S*?)$", prefixed=False)
    def get_pods(self, msg, matcher: re.Match):
        namespace = matcher.group("namespace")
        if not namespace:
            return "Неймспейс не валиден"
        auth_err = self.__auth_in_cluster()
        if auth_err is not None:
            return auth_err
        core_api = k8s.client.CoreV1Api()
        result = "IP\tИмя\tN_Реплик"
        for pod in core_api.list_namespaced_pod(namespace=namespace).items:
            pod_name = pod.metadata.name
            apps_api = k8s.client.AppsV1Api()
            repplicaset = apps_api.read_namespaced_replica_set(namespace=namespace, name=pod_name.rsplit("-", 1)[0])
            result += f"\n{pod.status.pod_ip}\t{pod_name}\t{repplicaset.status.replicas}"
        return result

    @re_botcmd(pattern="^Хочу (лог|log) пода (?P<name>.*?) из (?P<namespace>\S*?)$", prefixed=False)
    def get_pod_log(self, msg, matcher: re.Match):
        namespace = matcher.group("namespace")
        pod_name = matcher.group("name")
        if not namespace:
            return "Неймспейс не валиден"
        auth_err = self.__auth_in_cluster()
        if auth_err is not None:
            return auth_err
        core_api = k8s.client.CoreV1Api()
        return core_api.read_namespaced_pod_log(namespace=namespace, name=pod_name)

    @re_botcmd(pattern="^Реплицируй под (?P<name>.*?) из (?P<namespace>\S*?) в (?P<replicas>\d+?)$", prefixed=False)
    def create_replica(self, msg, matcher: re.Match):
        namespace = matcher.group("namespace")
        pod_name = matcher.group("name")
        replicas = matcher.group("replicas")

        auth_err = self.__auth_in_cluster()
        if auth_err is not None:
            return auth_err
        apps_api = k8s.client.AppsV1Api()
        replicaset_name = pod_name.rsplit("-", 1)[0]
        replicaset_scale = apps_api.read_namespaced_replica_set_scale(namespace=namespace,
                                                                      name=replicaset_name)
        replicaset_scale.spec.replicas = int(replicas)
        apps_api.patch_namespaced_replica_set_scale(namespace=namespace, name=replicaset_name, body=replicaset_scale)
        return f"Сказано - сделано. Заскейлил {replicaset_name} в {replicas}"
