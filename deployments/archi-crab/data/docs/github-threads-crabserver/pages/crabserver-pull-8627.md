# dmwm/CRABServer pull request #8627: Kaniko to DinD & implement registry caching  #8522

State: closed
Opened: 2024-08-16T09:54:18Z
Closed: 2024-08-16T14:54:24Z
Merged: 2024-08-16T14:54:24Z
URL: https://github.com/dmwm/CRABServer/pull/8627

## Opening post (jannakam, 2024-08-16T09:54:18Z)

Issue #8522 
The following commit includes the following changes:

**.gitlab-ci.yml file:**
- Switched from kaniko to dind (Docker-in-Docker) service. Applied to these jobs: build_rest_image, build-image (formerly build_tw_image), and build_crabtwfilebeat_image.
- Implemented registry caching using the Docker Buildkit tool in jobs build_rest_image and build_image. This uploads an image cache into the registry and pulls from it every time a new image is built, then replaces it with a new cache incase something has changed. Notice this in the use of the same naming of the image 'pypi-$(REST_Instance}-cache' as a parameter for 'cache-to' and 'cache-from' flags, which will pull the current user's test environment from the .env file saved as an artifact in the pipeline. 

**Dockerfile:**
- Removed line 143 which was creating a duplicate image
- Added the changing of user ownership manually to the relevant lines of code in the Dockerfile

**Other:**
- Configured a custom runner for compatibility with the dind service. see https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#docker-in-docker-with-tls-enabled-in-the-docker-executor

## Comment (cmsdmwmbot, 2024-08-16T09:55:01Z)

Can one of the admins verify this patch?

## Comment (novicecpp, 2024-08-16T11:45:07Z)

I am instructing Janna in-person on how to improve this pull request.
I might post some short fix/script in this PR and it will create email noti but you can unsubscribe the PR by click Unsubscribe button on the right hand side in the same Reviewer section.

## Comment (novicecpp, 2024-08-16T14:53:48Z)

Thanks Janna. Feel free to merge.
