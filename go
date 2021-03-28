#!/bin/bash

case $1 in
	d|deploy)
		echo "Deploying to serverless..."
		serverless deploy
		;;
	t|test)
		echo "Testing..."

		DOMAIN="g2d2kfveoc.execute-api.eu-west-1.amazonaws.com"

		GETURL="https://$DOMAIN/dev/incident"
		echo "Calling curl get to: $GETURL"
		curl -X GET $GETURL | python3 -m json.tool

    POSTURL="https://$DOMAIN/dev/incident"
    POSTDATA='{ "location": "here", "category": 8, "incidentDate": "1970-04-14 03:08:53", "People": { "staff": "Alice", "witness": "Bob", "offender": "Mallory" } }'
    echo "Calling curl post to: $POSTURL"
    curl -X POST "$POSTURL" -d "$POSTDATA" -H 'content-type: application/json'| python3 -m json.tool
		;;
  *)
    echo "Usage: $0 deploy|test"
    echo "    deploy - Deploy the current version to aws"
    echo "    test   - Run some basic smoke tests"
    ;;
esac
