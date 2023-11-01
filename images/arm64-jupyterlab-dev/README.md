# arm64-jupyterlab-dev
A persistent container for hosting a jupyterlabs server. Once deployed, container will keep running until force closed i.e. `docker container stop <container name>`

## DISCLAIMER
As this container is solely used for the purpose of spinning up a labs env locally, security features such as password/tokens have been disabled + server is startd with --allow-root. This server is intended to only be used locally (localhost:3000) but should be modified if ever being deployed.
