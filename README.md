# Code demo 'incident'

## Instalation

### Pre-requisites

 - OS: Linux/UNIX (tested on xubuntu 20.04 LTS)
 - Tools:
    - serverless via npm
    - python 3.8
    - AWS Command line tools (configured with AWS access keys)
    - curl (for smoke test only)

### Deploy

  The AWS region is configured in the serverless.yml file

  If you have the pre-requisites installed, simply execute the following command line to deploy:

    $ go deploy

### Smoke test

  The first time you run, you will need to make a note of the domain in the handlers, and update the DOMAIN environment variable in the go script, manually.

  To run the basic moke test, execute the following command;

    $ go test




