"""{
  "type": "collection",
  "links": {
    "self": "https://192.168.42.52:445/v3/clusterAlerts"
  },
  "createTypes": {
    "clusterAlert": "https://192.168.42.52:445/v3/clusteralerts"
  },
  "actions": {},
  "pagination": {
    "limit": 1000,
    "total": 5
  },
  "sort": {
    "order": "asc",
    "reverse": "https://192.168.42.52:445/v3/clusterAlerts?order=desc",
    "links": {
      "alertState": "https://192.168.42.52:445/v3/clusterAlerts?sort=alertState",
      "description": "https://192.168.42.52:445/v3/clusterAlerts?sort=description",
      "name": "https://192.168.42.52:445/v3/clusterAlerts?sort=name",
      "severity": "https://192.168.42.52:445/v3/clusterAlerts?sort=severity",
      "state": "https://192.168.42.52:445/v3/clusterAlerts?sort=state",
      "transitioning": "https://192.168.42.52:445/v3/clusterAlerts?sort=transitioning",
      "transitioningMessage": "https://192.168.42.52:445/v3/clusterAlerts?sort=transitioningMessage",
      "uuid": "https://192.168.42.52:445/v3/clusterAlerts?sort=uuid"
    }
  },
  "filters": {
    "alertState": null,
    "clusterId": null,
    "creatorId": null,
    "description": null,
    "id": null,
    "initialWaitSeconds": null,
    "name": null,
    "namespaceId": null,
    "repeatIntervalSeconds": null,
    "severity": null,
    "state": null,
    "transitioning": null,
    "transitioningMessage": null,
    "uuid": null
  },
  "resourceType": "clusterAlert",
  "data": [
    {
      "actions": {
        "activate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-controllermanager?action=activate",
        "deactivate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-controllermanager?action=deactivate",
        "mute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-controllermanager?action=mute",
        "unmute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-controllermanager?action=unmute"
      },
      "alertState": "active",
      "baseType": "clusterAlert",
      "clusterId": "c-d8f82",
      "created": "2018-08-07T19:23:09Z",
      "createdTS": 1533669789000,
      "creatorId": null,
      "description": "Built-in Alert for controller-manager component",
      "id": "c-d8f82:clusteralert-controllermanager",
      "initialWaitSeconds": 180,
      "links": {
        "remove": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-controllermanager",
        "self": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-controllermanager",
        "update": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-controllermanager"
      },
      "name": "Alert for controller-manager",
      "namespaceId": null,
      "removed": null,
      "repeatIntervalSeconds": 3600,
      "severity": "critical",
      "state": "active",
      "targetSystemService": {
        "condition": "controller-manager",
        "type": "/v3/schemas/targetSystemService"
      },
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "clusterAlert",
      "uuid": "51cc8c3c-9a77-11e8-9b04-0242ac110003"
    },
    {
      "actions": {
        "activate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-deploment-event?action=activate",
        "deactivate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-deploment-event?action=deactivate",
        "mute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-deploment-event?action=mute",
        "unmute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-deploment-event?action=unmute"
      },
      "alertState": "active",
      "baseType": "clusterAlert",
      "clusterId": "c-d8f82",
      "created": "2018-08-07T19:23:11Z",
      "createdTS": 1533669791000,
      "creatorId": null,
      "description": "Built-in Alert for warning event",
      "id": "c-d8f82:clusteralert-deploment-event",
      "initialWaitSeconds": 180,
      "links": {
        "remove": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-deploment-event",
        "self": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-deploment-event",
        "update": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-deploment-event"
      },
      "name": "Alert for Warning Event of Deployment",
      "namespaceId": null,
      "removed": null,
      "repeatIntervalSeconds": 3600,
      "severity": "critical",
      "state": "active",
      "targetEvent": {
        "eventType": "Warning",
        "resourceKind": "Deployment",
        "type": "/v3/schemas/targetEvent"
      },
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "clusterAlert",
      "uuid": "52d70bfc-9a77-11e8-9b04-0242ac110003"
    },
    {
      "actions": {
        "activate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-etcd?action=activate",
        "deactivate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-etcd?action=deactivate",
        "mute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-etcd?action=mute",
        "unmute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-etcd?action=unmute"
      },
      "alertState": "active",
      "baseType": "clusterAlert",
      "clusterId": "c-d8f82",
      "created": "2018-08-07T19:23:08Z",
      "createdTS": 1533669788000,
      "creatorId": null,
      "description": "Built-in Alert for etcd component",
      "id": "c-d8f82:clusteralert-etcd",
      "initialWaitSeconds": 180,
      "links": {
        "remove": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-etcd",
        "self": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-etcd",
        "update": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-etcd"
      },
      "name": "Alert for etcd",
      "namespaceId": null,
      "removed": null,
      "repeatIntervalSeconds": 3600,
      "severity": "critical",
      "state": "active",
      "targetSystemService": {
        "condition": "etcd",
        "type": "/v3/schemas/targetSystemService"
      },
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "clusterAlert",
      "uuid": "5124e842-9a77-11e8-9b04-0242ac110003"
    },
    {
      "actions": {
        "activate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-node-mem?action=activate",
        "deactivate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-node-mem?action=deactivate",
        "mute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-node-mem?action=mute",
        "unmute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-node-mem?action=unmute"
      },
      "alertState": "active",
      "baseType": "clusterAlert",
      "clusterId": "c-d8f82",
      "created": "2018-08-07T19:23:10Z",
      "createdTS": 1533669790000,
      "creatorId": null,
      "description": "Built-in Alert for node mem usage",
      "id": "c-d8f82:clusteralert-node-mem",
      "initialWaitSeconds": 180,
      "links": {
        "remove": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-node-mem",
        "self": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-node-mem",
        "update": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-node-mem"
      },
      "name": "Alert for Node Memory Usage",
      "namespaceId": null,
      "removed": null,
      "repeatIntervalSeconds": 3600,
      "severity": "critical",
      "state": "active",
      "targetNode": {
        "condition": "mem",
        "cpuThreshold": 70,
        "memThreshold": 70,
        "nodeId": null,
        "selector": {
          "node": "node"
        },
        "type": "/v3/schemas/targetNode"
      },
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "clusterAlert",
      "uuid": "52733c13-9a77-11e8-9b04-0242ac110003"
    },
    {
      "actions": {
        "activate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-scheduler?action=activate",
        "deactivate": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-scheduler?action=deactivate",
        "mute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-scheduler?action=mute",
        "unmute": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-scheduler?action=unmute"
      },
      "alertState": "active",
      "baseType": "clusterAlert",
      "clusterId": "c-d8f82",
      "created": "2018-08-07T19:23:10Z",
      "createdTS": 1533669790000,
      "creatorId": null,
      "description": "Built-in Alert for scheduler component",
      "id": "c-d8f82:clusteralert-scheduler",
      "initialWaitSeconds": 180,
      "links": {
        "remove": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-scheduler",
        "self": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-scheduler",
        "update": "https://192.168.42.52:445/v3/clusterAlerts/c-d8f82:clusteralert-scheduler"
      },
      "name": "Alert for scheduler",
      "namespaceId": null,
      "removed": null,
      "repeatIntervalSeconds": 3600,
      "severity": "critical",
      "state": "active",
      "targetSystemService": {
        "condition": "scheduler",
        "type": "/v3/schemas/targetSystemService"
      },
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "clusterAlert",
      "uuid": "522417b8-9a77-11e8-9b04-0242ac110003"
    }
  ]
}"""