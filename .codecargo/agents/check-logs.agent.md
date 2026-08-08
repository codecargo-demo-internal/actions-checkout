---
name: Check Logs
description: Check the Grafana logs for any issues in our clusters.
engine: codecargo
mcp-servers:
  - name: Grafana
    tools:
      - search_dashboards
      - list_datasources
      - query_prometheus
---

Review Grafana for any operational issues affecting the Kubernetes stack during the last 30 minutes.

Investigate available alerts, dashboards, metrics, logs, and traces. Use the Grafana data sources that are configured, such as Prometheus, Loki, Tempo, or equivalent systems.

Check specifically for:

* Firing, pending, or recently resolved alerts
* Pods that are crashing, restarting, stuck pending, evicted, or not ready
* CrashLoopBackOff, ImagePullBackOff, OOMKilled, failed probes, and abnormal container exits
* Deployments, StatefulSets, DaemonSets, or Jobs that are unavailable or failing
* Unexpected increases in pod restart counts
* Kubernetes nodes that are unavailable or experiencing memory, disk, PID, or CPU pressure
* CPU throttling, sustained high CPU, memory saturation, or resource-limit exhaustion
* Unschedulable pods or insufficient cluster capacity
* Elevated HTTP 4xx or 5xx responses
* Increased application error rates or exceptions
* Abnormal request latency, timeouts, or reduced throughput
* Database, queue, cache, DNS, ingress, service-mesh, networking, persistent-volume, or storage errors
* Recent deployments or configuration changes that correlate with an issue
* Any meaningful deviation from the normal baseline, even when no alert is firing

For each suspected issue:

1. Correlate evidence across metrics, logs, traces, alerts, and Kubernetes resources where possible.
2. Identify the affected cluster, namespace, workload, pod, container, service, node, and endpoint.
3. Determine the approximate start time and whether the problem is ongoing, worsening, improving, or resolved.
4. Include the relevant metric values, error messages, alert names, and Grafana panel or dashboard references.
5. Distinguish the likely root cause from downstream symptoms.
6. Do not make changes to the environment.

Return the result in this format:

## Overall status

Use one of: Healthy, Degraded, or Critical.

## Issues found

For each issue, provide:

* Severity: Critical, High, Medium, or Low
* Status: Ongoing, Intermittent, or Resolved
* Started:
* Affected components:
* Evidence:
* Likely cause:
* User or system impact:
* Recommended next action:

## Recent changes

List any deployments, rollouts, configuration changes, scaling events, or node events that may be relevant.

## Summary

Provide a concise explanation of what requires attention now.

If no meaningful issues are found, state:

“No significant operational issues were detected in the Kubernetes stack during the last 30 minutes.”

Do not treat isolated warnings, one-off log errors, or brief metric spikes as incidents unless they caused measurable impact or represent a recurring pattern. Clearly identify any areas you could not inspect because the necessary Grafana dashboards or data sources were unavailable.
