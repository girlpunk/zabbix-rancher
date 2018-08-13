"""{
  "type": "collection",
  "links": {
    "self": "https://192.168.42.52:445/v3/clusters"
  },
  "createTypes": {
    "cluster": "https://192.168.42.52:445/v3/clusters"
  },
  "actions": {},
  "pagination": {
    "limit": 1000,
    "total": 1
  },
  "sort": {
    "order": "asc",
    "reverse": "https://192.168.42.52:445/v3/clusters?order=desc",
    "links": {
      "agentImage": "https://192.168.42.52:445/v3/clusters?sort=agentImage",
      "apiEndpoint": "https://192.168.42.52:445/v3/clusters?sort=apiEndpoint",
      "appliedPodSecurityPolicyTemplateId": "https://192.168.42.52:445/v3/clusters?sort=appliedPodSecurityPolicyTemplateId",
      "caCert": "https://192.168.42.52:445/v3/clusters?sort=caCert",
      "description": "https://192.168.42.52:445/v3/clusters?sort=description",
      "desiredAgentImage": "https://192.168.42.52:445/v3/clusters?sort=desiredAgentImage",
      "driver": "https://192.168.42.52:445/v3/clusters?sort=driver",
      "state": "https://192.168.42.52:445/v3/clusters?sort=state",
      "transitioning": "https://192.168.42.52:445/v3/clusters?sort=transitioning",
      "transitioningMessage": "https://192.168.42.52:445/v3/clusters?sort=transitioningMessage",
      "uuid": "https://192.168.42.52:445/v3/clusters?sort=uuid"
    }
  },
  "filters": {
    "agentImage": null,
    "apiEndpoint": null,
    "appliedPodSecurityPolicyTemplateId": null,
    "caCert": null,
    "creatorId": null,
    "defaultClusterRoleForProjectMembers": null,
    "defaultPodSecurityPolicyTemplateId": null,
    "description": null,
    "desiredAgentImage": null,
    "driver": null,
    "id": null,
    "internal": null,
    "name": null,
    "state": null,
    "transitioning": null,
    "transitioningMessage": null,
    "uuid": null
  },
  "resourceType": "cluster",
  "data": [
    {
      "actions": {
        "exportYaml": "https://192.168.42.52:445/v3/clusters/c-d8f82?action=exportYaml",
        "generateKubeconfig": "https://192.168.42.52:445/v3/clusters/c-d8f82?action=generateKubeconfig",
        "importYaml": "https://192.168.42.52:445/v3/clusters/c-d8f82?action=importYaml"
      },
      "agentImage": "rancher/rancher-agent:v2.0.6",
      "allocatable": {
        "cpu": "2",
        "memory": "3948464Ki",
        "pods": "110"
      },
      "annotations": {
        "lifecycle.cattle.io/create.cluster-agent-controller": "true",
        "lifecycle.cattle.io/create.cluster-agent-controller-cleanup": "true",
        "lifecycle.cattle.io/create.cluster-provisioner-controller": "true",
        "lifecycle.cattle.io/create.cluster-scoped-gc": "true",
        "lifecycle.cattle.io/create.mgmt-cluster-rbac-remove": "true"
      },
      "apiEndpoint": "https://192.168.42.52:6443",
      "appliedPodSecurityPolicyTemplateId": "",
      "appliedSpec": {
        "defaultClusterRoleForProjectMembers": null,
        "defaultPodSecurityPolicyTemplateId": null,
        "description": "",
        "desiredAgentImage": "",
        "displayName": "home",
        "internal": false,
        "rancherKubernetesEngineConfig": {
          "addonJobTimeout": 30,
          "authentication": {
            "strategy": "x509",
            "type": "/v3/schemas/authnConfig"
          },
          "authorization": {
            "type": "/v3/schemas/authzConfig"
          },
          "bastionHost": {
            "sshAgentAuth": false,
            "type": "/v3/schemas/bastionHost"
          },
          "cloudProvider": {
            "type": "/v3/schemas/cloudProvider"
          },
          "ignoreDockerVersion": true,
          "ingress": {
            "provider": "nginx",
            "type": "/v3/schemas/ingressConfig"
          },
          "kubernetesVersion": "v1.10.5-rancher1-1",
          "network": {
            "plugin": "canal",
            "type": "/v3/schemas/networkConfig"
          },
          "nodes": [
            {
              "address": "192.168.42.52",
              "hostnameOverride": "docker",
              "nodeId": "c-d8f82:m-05b6053c41a2",
              "port": "22",
              "role": [
                "etcd",
                "controlplane",
                "worker"
              ],
              "sshAgentAuth": false,
              "type": "/v3/schemas/rkeConfigNode",
              "user": "root"
            }
          ],
          "services": {
            "etcd": {
              "extraArgs": {
                "election-timeout": "5000",
                "heartbeat-interval": "500"
              },
              "snapshot": false,
              "type": "/v3/schemas/etcdService"
            },
            "kubeApi": {
              "podSecurityPolicy": false,
              "type": "/v3/schemas/kubeAPIService"
            },
            "kubeController": {
              "type": "/v3/schemas/kubeControllerService"
            },
            "kubelet": {
              "failSwapOn": false,
              "type": "/v3/schemas/kubeletService"
            },
            "kubeproxy": {
              "type": "/v3/schemas/kubeproxyService"
            },
            "scheduler": {
              "type": "/v3/schemas/schedulerService"
            },
            "type": "/v3/schemas/rkeConfigServices"
          },
          "sshAgentAuth": false,
          "type": "/v3/schemas/rancherKubernetesEngineConfig"
        },
        "type": "/v3/schemas/clusterSpec"
      },
      "baseType": "cluster",
      "caCert": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN3akNDQWFxZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFTTVJBd0RnWURWUVFERXdkcmRXSmwKTFdOaE1CNFhEVEU0TURnd056RTROVGN4TTFvWERUSTRNRGd3TkRFNE5UY3hNMW93RWpFUU1BNEdBMVVFQXhNSAphM1ZpWlMxallUQ0NBU0l3RFFZSktvWklodmNOQVFFQkJRQURnZ0VQQURDQ0FRb0NnZ0VCQUtpa0FaTUJpTFlEClJXV1h5MVlMT3BiOU1jbXIxZ1phUHZ3d2N6ZnVCNGZ1NVlYbENLeTA3elBlZks2ZTJLZDkwYnZhQlVZMkdtMmsKYnRVZnZLR0xNRDRLRmtqUGdVTE5XQVRUVko0NlFia05ndUJ4bExpZVkyZGEyd2N1c2dWR3UrQW1HU0lRb2hqUQpuSDgvS2F3ZUZJK3ZnL2phRUVmTTFwRGVZa0NJV3g0MkYyZlo1RklrWlBrb3VVeUJVMm52Yys3TW0yUFVzeXpjCktoanVPd1B4M0JGcG80OSt4cUJkWEw4M2VmYkpIQnB6bDYwRjZCcGw1VDFWWjNhZFoxcng1cG9pQWJZbnNwcjEKbEFQeWpwQ09yUWdTZDRUVVo4Q2JSdWM1bGRYWTNTR0tIaWt3SU4zR21CcmlJZmVZOFZwdTBWdnBvR2dpdUNtQwo3Y2NhTWdOOXpQVUNBd0VBQWFNak1DRXdEZ1lEVlIwUEFRSC9CQVFEQWdLa01BOEdBMVVkRXdFQi93UUZNQU1CCkFmOHdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJBRWNFYjA2Ujd1Q3VQWmFzVzlPcS95WkdPbEFDaUlCcE1XYTUKdnRCYTN6UXVtSE9JQVlycVVCR2VUcmFsb1dTKzh6UDE4UUl4WEM5K1ZZZzhpbVdWVjhTejhQN3E3djJWTGtlUQp1UEVMdkFZM3FpaXZsZFhOdFpBMjhIcVBPT3VIRlFUbFZnYW8yVTh3RXM3Y3lkSmlkV0JSRDM0T1YvK3FSTytxCmEvYnpMMGJtdXBScWE1S25keTRTMXhGb1RxNmhsSjROMjh3TnM3YTdjbFdRandqYnRyTGFqU2VyQ000Q0duTFMKaHhaVjFHcVZnR0JzRitUOU5NYUg2eTM2ZzJDWGhnZlZrblNDUVdDc2dweXpQa3JYRU1ud21Wenl2TXJCUE1FbQp4bi9sblVaL1Rwa3FrSW1wVmF6N3BLL1ZjMWxJaEFWeVBZSW9selg3UTY4ZkZWdjdjc0U9Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K",
      "capacity": {
        "cpu": "2",
        "memory": "4050864Ki",
        "pods": "110"
      },
      "componentStatuses": [
        {
          "conditions": [
            {
              "message": "ok",
              "status": "True",
              "type": "Healthy"
            }
          ],
          "name": "controller-manager",
          "type": "/v3/schemas/clusterComponentStatus"
        },
        {
          "conditions": [
            {
              "message": "{\"health\": \"true\"}",
              "status": "True",
              "type": "Healthy"
            }
          ],
          "name": "etcd-0",
          "type": "/v3/schemas/clusterComponentStatus"
        },
        {
          "conditions": [
            {
              "message": "ok",
              "status": "True",
              "type": "Healthy"
            }
          ],
          "name": "scheduler",
          "type": "/v3/schemas/clusterComponentStatus"
        }
      ],
      "conditions": [
        {
          "lastUpdateTime": "2018-08-07T18:52:15Z",
          "status": "True",
          "type": "BackingNamespaceCreated"
        },
        {
          "lastUpdateTime": "2018-08-07T18:52:15Z",
          "status": "True",
          "type": "DefaultProjectCreated"
        },
        {
          "lastUpdateTime": "2018-08-07T18:52:15Z",
          "status": "True",
          "type": "CreatorMadeOwner"
        },
        {
          "lastUpdateTime": "2018-08-07T18:52:17Z",
          "status": "True",
          "type": "Pending"
        },
        {
          "lastUpdateTime": "2018-08-07T19:23:07Z",
          "status": "True",
          "type": "Provisioned"
        },
        {
          "lastUpdateTime": "2018-08-07T19:23:43Z",
          "status": "True",
          "type": "Waiting"
        },
        {
          "lastUpdateTime": "2018-08-07T18:52:17Z",
          "status": "True",
          "type": "NoDiskPressure"
        },
        {
          "lastUpdateTime": "2018-08-07T18:52:17Z",
          "status": "True",
          "type": "NoMemoryPressure"
        },
        {
          "lastUpdateTime": "2018-08-07T18:52:20Z",
          "status": "True",
          "type": "InitialRolesPopulated"
        },
        {
          "lastUpdateTime": "2018-08-07T19:23:18Z",
          "status": "True",
          "type": "GlobalAdminsSynced"
        },
        {
          "lastUpdateTime": "2018-08-07T19:23:24Z",
          "status": "True",
          "type": "DefaultNamespaceAssigned"
        },
        {
          "lastUpdateTime": "2018-08-13T12:59:22Z",
          "status": "True",
          "type": "Ready"
        },
        {
          "lastUpdateTime": "2018-08-07T19:24:30Z",
          "status": "True",
          "type": "Updated"
        },
        {
          "lastUpdateTime": "2018-08-07T19:25:56Z",
          "status": "True",
          "type": "SystemAccountCreated"
        },
        {
          "lastUpdateTime": "2018-08-07T19:26:06Z",
          "status": "True",
          "type": "AgentDeployed"
        }
      ],
      "created": "2018-08-07T18:52:15Z",
      "createdTS": 1533667935000,
      "creatorId": "user-r7dsw",
      "defaultClusterRoleForProjectMembers": null,
      "defaultPodSecurityPolicyTemplateId": null,
      "description": "",
      "desiredAgentImage": "",
      "driver": "rancherKubernetesEngine",
      "id": "c-d8f82",
      "internal": false,
      "limits": {
        "cpu": "310m",
        "memory": "422Mi",
        "pods": "0"
      },
      "links": {
        "clusterAlerts": "https://192.168.42.52:445/v3/clusters/c-d8f82/clusteralerts",
        "clusterEvents": "https://192.168.42.52:445/v3/clusters/c-d8f82/clusterevents",
        "clusterLoggings": "https://192.168.42.52:445/v3/clusters/c-d8f82/clusterloggings",
        "clusterPipelines": "https://192.168.42.52:445/v3/clusters/c-d8f82/clusterpipelines",
        "clusterRegistrationTokens": "https://192.168.42.52:445/v3/clusters/c-d8f82/clusterregistrationtokens",
        "clusterRoleTemplateBindings": "https://192.168.42.52:445/v3/clusters/c-d8f82/clusterroletemplatebindings",
        "namespaces": "https://192.168.42.52:445/v3/clusters/c-d8f82/namespaces",
        "nodePools": "https://192.168.42.52:445/v3/clusters/c-d8f82/nodepools",
        "nodes": "https://192.168.42.52:445/v3/clusters/c-d8f82/nodes",
        "notifiers": "https://192.168.42.52:445/v3/clusters/c-d8f82/notifiers",
        "persistentVolumes": "https://192.168.42.52:445/v3/clusters/c-d8f82/persistentvolumes",
        "projects": "https://192.168.42.52:445/v3/clusters/c-d8f82/projects",
        "remove": "https://192.168.42.52:445/v3/clusters/c-d8f82",
        "self": "https://192.168.42.52:445/v3/clusters/c-d8f82",
        "shell": "wss://192.168.42.52:445/v3/clusters/c-d8f82?shell=true",
        "sourceCodeCredentials": "https://192.168.42.52:445/v3/clusters/c-d8f82/sourcecodecredentials",
        "sourceCodeRepositories": "https://192.168.42.52:445/v3/clusters/c-d8f82/sourcecoderepositories",
        "storageClasses": "https://192.168.42.52:445/v3/clusters/c-d8f82/storageclasses",
        "subscribe": "https://192.168.42.52:445/v3/clusters/c-d8f82/subscribe",
        "update": "https://192.168.42.52:445/v3/clusters/c-d8f82"
      },
      "name": "home",
      "rancherKubernetesEngineConfig": {
        "addonJobTimeout": 30,
        "authentication": {
          "strategy": "x509",
          "type": "/v3/schemas/authnConfig"
        },
        "authorization": {
          "type": "/v3/schemas/authzConfig"
        },
        "bastionHost": {
          "sshAgentAuth": false,
          "type": "/v3/schemas/bastionHost"
        },
        "cloudProvider": {
          "type": "/v3/schemas/cloudProvider"
        },
        "ignoreDockerVersion": true,
        "ingress": {
          "provider": "nginx",
          "type": "/v3/schemas/ingressConfig"
        },
        "kubernetesVersion": "v1.10.5-rancher1-1",
        "network": {
          "plugin": "canal",
          "type": "/v3/schemas/networkConfig"
        },
        "services": {
          "etcd": {
            "extraArgs": {
              "election-timeout": "5000",
              "heartbeat-interval": "500"
            },
            "snapshot": false,
            "type": "/v3/schemas/etcdService"
          },
          "kubeApi": {
            "podSecurityPolicy": false,
            "type": "/v3/schemas/kubeAPIService"
          },
          "kubeController": {
            "type": "/v3/schemas/kubeControllerService"
          },
          "kubelet": {
            "failSwapOn": false,
            "type": "/v3/schemas/kubeletService"
          },
          "kubeproxy": {
            "type": "/v3/schemas/kubeproxyService"
          },
          "scheduler": {
            "type": "/v3/schemas/schedulerService"
          },
          "type": "/v3/schemas/rkeConfigServices"
        },
        "sshAgentAuth": false,
        "type": "/v3/schemas/rancherKubernetesEngineConfig"
      },
      "requested": {
        "cpu": "690m",
        "memory": "256Mi",
        "pods": "13"
      },
      "state": "active",
      "transitioning": "no",
      "transitioningMessage": "",
      "type": "cluster",
      "uuid": "00a1e41d-9a73-11e8-932a-0242ac110003",
      "version": {
        "buildDate": "2018-06-21T11:34:22Z",
        "compiler": "gc",
        "gitCommit": "32ac1c9073b132b8ba18aa830f46b77dcceb0723",
        "gitTreeState": "clean",
        "gitVersion": "v1.10.5",
        "goVersion": "go1.9.3",
        "major": "1",
        "minor": "10",
        "platform": "linux/amd64",
        "type": "/v3/schemas/info"
      }
    }
  ]
}"""