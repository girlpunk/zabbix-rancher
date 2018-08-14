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

        if sys.argv[4] == "discovery":
            self.discovery()
        elif sys.argv[4] == "clusterId":
            print(self._getProject(sys.argv[5])["clusterId"])
        elif sys.argv[4] == "created":
            print(self._getProject(sys.argv[5])["createdTS"])
        elif sys.argv[4] == "creatorId":
            print(self._getProject(sys.argv[5])["creatorId"])
        elif sys.argv[4] == "state":
            print(self._getProject(sys.argv[5])["state"])
        elif sys.argv[4] == "transitioning":
            print(self._getProject(sys.argv[5])["transitioning"])
        else:
            print("Unknown action")


if __name__ == "__main__":
    Project()
