# fabric8-analytics.github.io
GitHub pages

 * [QA Dashboard](dashboard/dashboard.html)

# Performance tests

## Stack analysis on production

 * [100 parallel calls](perf-tests/core_api/stack_analysis/production_100_calls/stack_analysis_parallel_calls_100_threads.png)
 * [statistic](perf-tests/core_api/stack_analysis/production_100_calls/stack_analysis_parallel_calls_100_threads_concurrent_100_threads_min_max_avg_times.png)

# FAQs

## What is the overall archicture and flow graph of Fabric8-Anaytics system?

Coming soon...

## Where are all project repos located?


You may want to get familiar with:

 * [Common](https://github.com/fabric8-analytics/fabric8-analytics-common)
 * [Worker](https://github.com/fabric8-analytics/fabric8-analytics-worker)
 * [Server](https://github.com/fabric8-analytics/fabric8-analytics-server)
 * [Jobs](https://github.com/fabric8-analytics/fabric8-analytics-jobs)
 * [Data-Model-Importer](https://github.com/fabric8-analytics/fabric8-analytics-data-model)
 * and others located here at [github.com/fabric8-analytics/](https://github.com/fabric8-analytics/)


## How to develop or run on local machine?

Almost all of the development can be done on local machine using containerized setup. We use Docker Compose based setup for such use-case. Take a look at this repo for more details: https://github.com/fabric8-analytics/fabric8-analytics-deployment

## How is production deployment done?

All the services are run on OpenShift v3 cluster. This is described here: https://github.com/fabric8-analytics/fabric8-analytics-deployment/blob/master/openshift/README.md

If you have or can setup your own OpenShift v3 cluster, you can use this mechanism to develop and test directly on OpenShift v3.

## How do we push changes to STAGING environment?

Our [CI system](https://ci.centos.org/view/Devtools/) tracks individual project repositories hosted on GitHub ( listed above ). Anytime a PR is submitted in these projects, builds are created against those changes. This ensures that all the submitted changes go through code-style checks, documentation style checks, and test suite.

Once all goes well through the review and PR is merged into master, the changes are deployed to staging environment directly by the CI system.

## How do we push changes to PRODUCTION environment?

For pushing the changes already incorporated into master branch, the merge commit ID should be updated in the [saas-analytics](https://github.com/openshiftio/saas-analytics/tree/master/bay-services) repo.

This works by tagging each of the container images using commit ids from git logs. So whenever a PR was merged, an image is build using that commit ID. This id is used to pull the corresponding image when deploying to production.

## Who manages the services required for deploying onto STAGING / PRODUCTION ?

It is the  Service Delivery team that manages all the infrastructure for STAGING and PRODUCTION. Talk to them :-)

## Where are Dev Cluster, Staging Cluster and Production Cluster located?

Dev Cluster, Staging Cluster and Production Cluster are OpenShift v3 clusters managed by Service Delivery team.


 * Dev Cluster is meant for individual developer's own use.
 * Staging Cluster is meant for deployment of services via CI, for pre-production stage verification and testing.
 * Production Cluster is for end users.

All these clusters have different endpoints, which you can find from your local teams. Talk to them :-)

# Get in touch with Fabric8 Analytics Community!

 * Chat with us on [fabric8-analytics](https://chat.openshift.io/developers/channels/fabric8-analytics) channel on Mattermost.
 * [Try it out](https://github.com/fabric8-analytics/fabric8-analytics-deployment) and contribute to [our projects on GitHub](https://github.com/fabric8-analytics)

