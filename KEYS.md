| Key | Script |
|-----|--------|
| `rancher.project[${API_URL}, ${API_USER}, ${API_PASSWORD}, discovery]` | rancher_project.py |
| `rancher.project[${API_URL}, ${API_USER$}, ${API_PASSWORD}, clusterId, {#ProjectID}]` | rancher_project.py |
| `rancher.project[${API_URL}, ${API_USER$}, ${API_PASSWORD}, createdTS, {#ProjectID}]` | rancher_project.py |
| `rancher.project[${API_URL}, ${API_USER$}, ${API_PASSWORD}, creatorId, {#ProjectID}]` | rancher_project.py |
| `rancher.project[${API_URL}, ${API_USER$}, ${API_PASSWORD}, state, {#ProjectID}]` | rancher_project.py |
| `rancher.project[${API_URL}, ${API_USER$}, ${API_PASSWORD}, transitioning, {#ProjectID}]` | rancher_project.py |

```
UserParameter=rancher.project[*], rancher_project.py "$1" "$2" "$3" "$4" "$5"
```