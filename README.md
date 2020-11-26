# k8s-manifest-creator

This application creates a standard set of manifests for a kubernetes application on the go. It takes an input of requirements from a file in yaml format as follows:
```yaml
name: tzankoswebpage
type: microservice
ingress: external-ingress
hostname: tzankotzankov.net
registry: tzankotzankov.net
```

The path to the above yaml file can be passed in via the `-fp` command line argument.

It then validates those inputs based on the following available criteria:
```
valid_objects = {
    'name': '',
    'type': ['microservice', 'api'],
    'ingress': ['internal-ingress', 'external-ingress'],
    'hostname': '',
    'registry': '',
}
```

This is followed up by the generation of the required kubernetes files, based on preexisting templating, which can be found under creator/templates/. These are based on jinja2.

This tool is meant to be used as part of a CI/CD pipeline and run during the deployment of each microservice. This ensures that all deployments manifests in kubernetes are the same across DEV, SIT, UAT and PRD environments. The app can be run as standalone, or within Docker.

## Running & Testing the k8s-manifest-creator:

# Running
```bash
python3 creator.py -fp {PARAMETER_FILE_PATH}
```

# Testing
```bash
pytest -q test.py
```

## Building the k8s-manifest-creator in Docker:
 
docker build -t creator .

## Runing the k8s-manifest-creator in Docker:

```bash
docker run creator -fp {PARAMETER_FILE_PATH}
```