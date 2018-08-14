# coding=utf-8
"""Project-related monitoring"""
import json
import sys

import requests

class ProjectAlert:
    def __init__(self):
        self.API_URL = sys.argv[1]
        self.API_USER = sys.argv[2]
        self.API_PASSWORD = sys.argv[3]

        if sys.argv[4] == "discovery":
            self.discovery()
        elif sys.argv[4] == "alertState":
            print(self._getProjectAlert(sys.argv[5])["alertState"])
        elif sys.argv[4] == "createdTS":
            print(self._getProjectAlert(sys.argv[5])["createdTS"])
        elif sys.argv[4] == "creatorId":
            print(self._getProjectAlert(sys.argv[5])["creatorId"])
        elif sys.argv[4] == "description":
            print(self._getProjectAlert(sys.argv[5])["description"])
        elif sys.argv[4] == "initialWaitSeconds":
            print(self._getProjectAlert(sys.argv[5])["initialWaitSeconds"])
        elif sys.argv[4] == "namespaceId":
            print(self._getProjectAlert(sys.argv[5])["namespaceId"])
        elif sys.argv[4] == "projectId":
            print(self._getProjectAlert(sys.argv[5])["projectId"])
        elif sys.argv[4] == "repeatIntervalSeconds":
            print(self._getProjectAlert(sys.argv[5])["repeatIntervalSeconds"])
        elif sys.argv[4] == "severity":
            print(self._getProjectAlert(sys.argv[5])["severity"])
        elif sys.argv[4] == "state":
            print(self._getProjectAlert(sys.argv[5])["state"])
        elif sys.argv[4] == "transitioning":
            print(self._getProjectAlert(sys.argv[5])["transitioning"])

    def discovery(self):
        raw_request = requests.get(self.API_URL + "projectAlert", auth=(self.API_USER, self.API_PASSWORD), verify=False)
        raw_request.raise_for_status()
        request = raw_request.json()

        response = {'data': []}

        for projectAlert in request["data"]:
            response['data'].append({
                "{#ClusterID}": projectAlert["id"],
                "{#Name}": projectAlert["name"]
            })

        print(json.dumps(response))

    def _getProjectAlert(self, projectAlertId):
        raw_request = requests.get(
            self.API_URL + "projectAlert/" + projectAlertId,
            auth=(self.API_USER, self.API_PASSWORD),
            verify=False
        )
        raw_request.raise_for_status()
        return raw_request.json()

