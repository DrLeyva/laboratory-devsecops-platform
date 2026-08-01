#!/usr/bin/env bash

set -euo pipefail

STATUS="${1:-unknown}"
APPLICATION="${2:-unknown}"
VERSION="${3:-unknown}"
ENVIRONMENT="${4:-development}"

if [ -z "${SNS_TOPIC_ARN:-}" ]; then
    echo "SNS_TOPIC_ARN is not configured."
    exit 1
fi

MESSAGE=$(cat <<EOF
Laboratory DevSecOps Platform notification

Application: ${APPLICATION}
Environment: ${ENVIRONMENT}
Version: ${VERSION}
Status: ${STATUS}
EOF
)

aws sns publish \
    --topic-arn "${SNS_TOPIC_ARN}" \
    --subject "Deployment ${STATUS}: ${APPLICATION}" \
    --message "${MESSAGE}"