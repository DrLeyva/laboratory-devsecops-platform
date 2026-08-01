\# Notification Design



\## Pull request notifications



GitHub notifications will be used for:



Pull request creation



Review requests



Pull request comments



Approvals



Pull request merges



\## Pipeline notifications



CircleCI will publish deployment results to an Amazon SNS topic.



Planned deployment notifications include:



Deployment started



Deployment succeeded



Deployment failed



Automatic rollback started



Automatic rollback completed



Security scan blocked deployment



\## Monitoring notifications



Grafana alerting will later use the notification system for:



Application unavailable



High HTTP error rate



Kubernetes Pod restart increase



High memory usage



High CPU usage



Failed readiness checks



\## Security requirements



Personal email addresses will not be committed to the repository.



Gmail credentials will not be stored in CircleCI.



CircleCI will receive permission only to publish to the approved SNS topic.



SNS subscribers will confirm their subscriptions directly through email.

