\# Platform Architecture



\## Source control



GitHub stores application code, infrastructure code, Kubernetes manifests, pipeline configuration, and documentation.



Development occurs through feature branches and pull requests.



\## Continuous integration and delivery



CircleCI runs tests, linting, security scanning, container builds, and deployments.



GitHub Actions provides repository security and governance checks.



\## Container platform



Docker packages each application.



K3s runs the containers on an AWS hosted Linux server.



Kubernetes Ingress routes separate hostnames to each application.



\## Applications



Chromatography Insights



Mass Spectrometry Explorer



Cell Analysis Portal



\## Monitoring



Prometheus collects application and Kubernetes metrics.



Grafana displays dashboards and sends operational alerts.



\## Notifications



GitHub sends collaboration notifications.



CircleCI publishes deployment notifications to Amazon SNS.



Grafana will publish operational notifications through an approved alert channel.



\## Infrastructure



Terraform will provision supported AWS resources where practical.



AWS cost alerts will be configured before billable infrastructure is created.

