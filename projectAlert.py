"""{
  "type": "collection",
  "data": [
    {
      "actions": {
        "activate": "https://192.168.42.52:445/v3/projectAlerts/p-vh55m:projectalert-workload?action=activate",
        "deactivate": "https://192.168.42.52:445/v3/projectAlerts/p-vh55m:projectalert-workload?action=deactivate",
        "mute": "https://192.168.42.52:445/v3/projectAlerts/p-vh55m:projectalert-workload?action=mute",
        "unmute": "https://192.168.42.52:445/v3/projectAlerts/p-vh55m:projectalert-workload?action=unmute"
      },
      "alertState": "active",
      "annotations": {
        "lifecycle.cattle.io/create.project-alert-podtarget_c-d8f82": "true"
      },
      "baseType": "projectAlert",
      "created": "2018-08-13T13:08:57Z",
      "createdTS": 1534165737000,
      "creatorId": null,
      "description": "Built-in Alert for Workload",
      "id": "p-vh55m:projectalert-workload",
      "initialWaitSeconds": 180,
      "links": {
        "remove": "https://192.168.42.52:445/v3/projectAlerts/p-vh55m:projectalert-workload",
        "self": "https://192.168.42.52:445/v3/projectAlerts/p-vh55m:projectalert-workload",
        "update": "https://192.168.42.52:445/v3/projectAlerts/p-vh55m:projectalert-workload"
      },
      "name": "Alert for Workload",
      "namespaceId": null,
      "projectId": "c-d8f82:p-vh55m",
      "repeatIntervalSeconds": 3600,
      "severity": "critical",
      "state": "active",
      "targetWorkload": {
        "availablePercentage": 50,
        "selector": {
          "app": "workload"
        },
        "type": "/v3/schemas/targetWorkload"
      },
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "projectAlert",
      "uuid": "095a7683-9efa-11e8-82ef-0242ac110002"
    },
    {
      "actions": {
        "activate": "https://192.168.42.52:445/v3/projectAlerts/project-vrgd9:projectalert-workload?action=activate",
        "deactivate": "https://192.168.42.52:445/v3/projectAlerts/project-vrgd9:projectalert-workload?action=deactivate",
        "mute": "https://192.168.42.52:445/v3/projectAlerts/project-vrgd9:projectalert-workload?action=mute",
        "unmute": "https://192.168.42.52:445/v3/projectAlerts/project-vrgd9:projectalert-workload?action=unmute"
      },
      "alertState": "active",
      "annotations": {
        "lifecycle.cattle.io/create.project-alert-podtarget_c-d8f82": "true"
      },
      "baseType": "projectAlert",
      "created": "2018-08-07T19:23:19Z",
      "createdTS": 1533669799000,
      "creatorId": null,
      "description": "Built-in Alert for Workload",
      "id": "project-vrgd9:projectalert-workload",
      "initialWaitSeconds": 180,
      "links": {
        "remove": "https://192.168.42.52:445/v3/projectAlerts/project-vrgd9:projectalert-workload",
        "self": "https://192.168.42.52:445/v3/projectAlerts/project-vrgd9:projectalert-workload",
        "update": "https://192.168.42.52:445/v3/projectAlerts/project-vrgd9:projectalert-workload"
      },
      "name": "Alert for Workload",
      "namespaceId": null,
      "projectId": "c-d8f82:project-vrgd9",
      "repeatIntervalSeconds": 3600,
      "severity": "critical",
      "state": "active",
      "targetWorkload": {
        "availablePercentage": 50,
        "selector": {
          "app": "workload"
        },
        "type": "/v3/schemas/targetWorkload"
      },
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "projectAlert",
      "uuid": "576789e6-9a77-11e8-9b04-0242ac110003"
    }
  ]
}"""