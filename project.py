# coding=utf-8
"""Project-related monitoring"""
import json
import sys

import requests


class Project:
    def discovery(self):
        raw_request = requests.get(self.API_URL+"projects", auth=(self.API_USER, self.API_PASSWORD), verify=False)
        raw_request.raise_for_status()
        request = raw_request.json()

        response = {'data': []}

        for project in request["data"]:
            response['data'].append({
                "{#ID}": project["id"],
                "{#Name}": project["name"]
            })

        print(json.dumps(response))

    def _getProject(self, projectId):
        raw_request = requests.get(
            self.API_URL + "projects/" + projectId,
            auth=(self.API_USER, self.API_PASSWORD),
            verify=False
        )
        raw_request.raise_for_status()
        return raw_request.json()

    def __init__(self):
        self.API_URL = sys.argv[1]
        self.API_USER = sys.argv[2]
        self.API_PASSWORD = sys.argv[3]

        if sys.argv[5] == "discovery":
            self.discovery()
        elif sys.argv[5] == "clusterId":
            print(self._getProject(sys.argv[6])["clusterId"])
        elif sys.argv[5] == "created":
            print(self._getProject(sys.argv[6])["createdTS"])
        elif sys.argv[5] == "creatorId":
            print(self._getProject(sys.argv[6])["creatorId"])
        elif sys.argv[5] == "state":
            print(self._getProject(sys.argv[6])["state"])
        elif sys.argv[5] == "transitioning":
            print(self._getProject(sys.argv[6])["transitioning"])
        else:
            print("Unknown action")


"""Further actions to investigate:
{
  "appRevisions": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/apprevisions",
  "apps": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/apps",
  "basicAuths": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/basicauths",
  "certificates": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/certificates",
  "configMaps": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/configmaps",
  "cronJobs": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/cronjobs",
  "daemonSets": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/daemonsets",
  "deployments": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/deployments",
  "dnsRecords": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/dnsrecords",
  "dockerCredentials": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/dockercredentials",
  "ingresses": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/ingresses",
  "jobs": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/jobs",
  "namespacedBasicAuths": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/namespacedbasicauths",
  "namespacedCertificates": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/namespacedcertificates",
  "namespacedDockerCredentials": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/namespaceddockercredentials",
  "namespacedSecrets": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/namespacedsecrets",
  "namespacedServiceAccountTokens":
    "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/namespacedserviceaccounttokens",
  "namespacedSshAuths": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/namespacedsshauths",
  "persistentVolumeClaims": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/persistentvolumeclaims",
  "pipelineExecutionLogs": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/pipelineexecutionlogs",
  "pipelineExecutions": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/pipelineexecutions",
  "pipelines": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/pipelines",
  "podSecurityPolicyTemplateProjectBindings":
    "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/podsecuritypolicytemplateprojectbindings",
  "pods": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/pods",
  "projectAlerts": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/projectalerts",
  "projectLoggings": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/projectloggings",
  "projectNetworkPolicies": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/projectnetworkpolicies",
  "projectRoleTemplateBindings": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/projectroletemplatebindings",
  "remove": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m",
  "replicaSets": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/replicasets",
  "replicationControllers": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/replicationcontrollers",
  "secrets": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/secrets",
  "self": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m",
  "serviceAccountTokens": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/serviceaccounttokens",
  "services": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/services",
  "sshAuths": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/sshauths",
  "statefulSets": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/statefulsets",
  "subscribe": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/subscribe",
  "update": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m",
  "workloads": "https://192.168.42.52:445/v3/projects/c-d8f82:p-vh55m/workloads"
}
"""
