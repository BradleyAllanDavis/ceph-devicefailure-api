#!/usr/bin/env bash

echo $PWD
java -jar swagger-codegen-cli.jar generate -i com/src/swagger.json -l python-flask -o com