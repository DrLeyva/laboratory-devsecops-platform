\# Security Policy



\## Sensitive information



Do not commit passwords, API keys, private keys, AWS credentials, kubeconfig files, Terraform state files, personal email addresses, or authentication tokens.



\## Pull request security



All application and platform changes should be made through feature branches.



Pull requests must pass automated tests and security checks before merging.



Direct changes to the main branch should be avoided.



\## Container security



Application containers must run as nonroot users.



Production images must use versioned tags.



Container images must be scanned before deployment.



Secrets must not be embedded inside container images.



\## Kubernetes security



Kubernetes workloads must define resource requests and limits.



Workloads must disable privilege escalation.



Applications must use readiness and liveness probes.



Secrets must be supplied through an approved secret management mechanism.



\## Notifications



Personal subscriber addresses must not be stored in the public repository.



Notification systems should use AWS SNS topics or approved integrations rather than storing email credentials in the pipeline.



\## Logging



Applications must not log passwords, tokens, private keys, or confidential values.

