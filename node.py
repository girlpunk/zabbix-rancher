"""{
  "data": [
    {
      "allocatable": {
        "cpu": "2",
        "ephemeral-storage": "16999863064",
        "hugepages-2Mi": "0",
        "memory": "3948464Ki",
        "pods": "110"
      },
      "capacity": {
        "cpu": "2",
        "ephemeral-storage": "18446032Ki",
        "hugepages-2Mi": "0",
        "memory": "4050864Ki",
        "pods": "110"
      },
      "clusterId": "c-d8f82",
      "conditions": [
        {
          "status": "True",
          "type": "Initialized"
        },
        {
          "message": "registered with kubernetes",
          "status": "True",
          "type": "Registered"
        },
        {
          "status": "True",
          "type": "Provisioned"
        },
        {
          "lastHeartbeatTime": "2018-08-13T13:09:01Z",
          "lastHeartbeatTimeTS": 1534165741000,
          "lastTransitionTime": "2018-08-08T13:00:33Z",
          "lastTransitionTimeTS": 1533733233000,
          "message": "kubelet has sufficient disk space available",
          "reason": "KubeletHasSufficientDisk",
          "status": "False",
          "type": "OutOfDisk"
        },
        {
          "lastHeartbeatTime": "2018-08-13T13:09:01Z",
          "lastHeartbeatTimeTS": 1534165741000,
          "lastTransitionTime": "2018-08-08T13:00:33Z",
          "lastTransitionTimeTS": 1533733233000,
          "message": "kubelet has sufficient memory available",
          "reason": "KubeletHasSufficientMemory",
          "status": "False",
          "type": "MemoryPressure"
        },
        {
          "lastHeartbeatTime": "2018-08-13T13:09:01Z",
          "lastHeartbeatTimeTS": 1534165741000,
          "lastTransitionTime": "2018-08-08T13:00:33Z",
          "lastTransitionTimeTS": 1533733233000,
          "message": "kubelet has no disk pressure",
          "reason": "KubeletHasNoDiskPressure",
          "status": "False",
          "type": "DiskPressure"
        },
        {
          "lastHeartbeatTime": "2018-08-13T13:09:01Z",
          "lastHeartbeatTimeTS": 1534165741000,
          "lastTransitionTime": "2018-08-07T19:13:07Z",
          "lastTransitionTimeTS": 1533669187000,
          "message": "kubelet has sufficient PID available",
          "reason": "KubeletHasSufficientPID",
          "status": "False",
          "type": "PIDPressure"
        },
        {
          "lastHeartbeatTime": "2018-08-13T13:09:01Z",
          "lastHeartbeatTimeTS": 1534165741000,
          "lastTransitionTime": "2018-08-08T13:00:33Z",
          "lastTransitionTimeTS": 1533733233000,
          "message": "kubelet is posting ready status",
          "reason": "KubeletReady",
          "status": "True",
          "type": "Ready"
        }
      ],
      "controlPlane": true,
      "createdTS": 1533668030000,
      "creatorId": null,
      "dockerInfo": {
        "debug": false,
        "experimentalBuild": false,
        "type": "/v3/schemas/dockerInfo"
      },
      "etcd": true,
      "externalIpAddress": "192.168.42.52",
      "hostname": "docker",
      "id": "c-d8f82:m-05b6053c41a2",
      "imported": true,
      "info": {
        "cpu": {
          "count": 2
        },
        "kubernetes": {
          "kubeProxyVersion": "v1.10.5",
          "kubeletVersion": "v1.10.5"
        },
        "memory": {
          "memTotalKiB": 4050864
        },
        "os": {
          "dockerVersion": "18.6.0",
          "kernelVersion": "4.9.0-7-amd64",
          "operatingSystem": "Debian GNU/Linux 9 (stretch)"
        }
      },
      "ipAddress": "192.168.42.52",
      "limits": {
        "cpu": "310m",
        "memory": "422Mi"
      },
      "name": "",
      "namespaceId": null,
      "nodeName": "docker",
      "nodePoolId": "",
      "nodeTemplateId": null,
      "podCidr": "10.42.0.0/24",
      "publicEndpoints": [
        {
          "addresses": [
            "192.168.42.52",
            "192.168.42.52"
          ],
          "allNodes": true,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 31638,
          "protocol": "TCP",
          "serviceId": "default:ingress-ac9bb7888640cc6e2abd8e0e6a5e33fe"
        },
        {
          "addresses": [
            "192.168.42.52",
            "192.168.42.52"
          ],
          "allNodes": true,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 31012,
          "protocol": "TCP",
          "serviceId": "grafana-lsx7jl:grafana-lsx7jl-grafana"
        },
        {
          "addresses": [
            "192.168.42.52",
            "192.168.42.52"
          ],
          "allNodes": true,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 31030,
          "protocol": "TCP",
          "serviceId": "mediaserver:ingress-229a36f053f1538c11142644c7a2f2c0"
        },
        {
          "addresses": [
            "192.168.42.52",
            "192.168.42.52"
          ],
          "allNodes": true,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 32030,
          "protocol": "TCP",
          "serviceId": "default:ingress-1d2ea6f576b5d62ecd09266a88eb634a"
        },
        {
          "addresses": [
            "192.168.42.52"
          ],
          "allNodes": false,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 80,
          "protocol": "TCP",
          "serviceId": null
        },
        {
          "addresses": [
            "192.168.42.52"
          ],
          "allNodes": false,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 443,
          "protocol": "TCP",
          "serviceId": null
        },
        {
          "addresses": [
            "192.168.42.52"
          ],
          "allNodes": false,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 53,
          "protocol": "TCP",
          "serviceId": null
        },
        {
          "addresses": [
            "192.168.42.52"
          ],
          "allNodes": false,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 53,
          "protocol": "UDP",
          "serviceId": null
        },
        {
          "addresses": [
            "192.168.42.52"
          ],
          "allNodes": false,
          "ingressId": null,
          "nodeId": "c-d8f82:m-05b6053c41a2",
          "podId": null,
          "port": 67,
          "protocol": "UDP",
          "serviceId": null
        }
      ],
      "requested": {
        "cpu": "690m",
        "memory": "256Mi",
        "pods": "13"
      },
      "requestedHostname": "docker",
      "sshUser": "root",
      "state": "active",
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "node",
      "unschedulable": false,
      "uuid": "39211f01-9a73-11e8-932a-0242ac110003",
      "worker": true
    }
  ]
}"""