| Key | Script |
|-----|--------|
| `rancher.cluster[{$API_URL}, {$API_USER}, {$API_PASSWORD}, discovery]` | cluster.py |
|-----|--------|
| `rancher.project[{$API_URL}, {$API_USER}, {$API_PASSWORD}, discovery]` | project.py |
| `rancher.project[{$API_URL}, {$API_USER}, {$API_PASSWORD}, clusterId, {#ProjectID}]` | project.py |
| `rancher.project[{$API_URL}, {$API_USER}, {$API_PASSWORD}, createdTS, {#ProjectID}]` | project.py |
| `rancher.project[{$API_URL}, {$API_USER}, {$API_PASSWORD}, creatorId, {#ProjectID}]` | project.py |
| `rancher.project[{$API_URL}, {$API_USER}, {$API_PASSWORD}, state, {#ProjectID}]` | project.py |
| `rancher.project[{$API_URL}, {$API_USER}, {$API_PASSWORD}, transitioning, {#ProjectID}]` | project.py |
|-----|--------|
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, discovery]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, alertState, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, createdTS, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, creatorId, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, description, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, initialWaitSeconds, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, namespaceId, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, projectId, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, repeatIntervalSeconds, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, severity, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, state, {#ProjectAlertID}]` | projectAlert.py |
| `rancher.projectAlert[{$API_URL}, {$API_USER}, {$API_PASSWORD}, transitioning, {#{rojectAlertID}]` | projectAlert.py |



```
UserParameter=rancher.project[*], project.py "$1" "$2" "$3" "$4" "$5"
UserParameter=rancher.cluster[*], cluster.py "$1" "$2" "$3" "$4" "$5"
UserParameter=rancher.projectAlert[*], projectAlert.py "$1" "$2" "$3" "$4" "$5"
```