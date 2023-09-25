#!/bin/bash

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in
    -v|--print)
      PRINT_OPTION="-v"
      shift
      ;;
    *)
      XML_PATH="$1"
      shift
      ;;
  esac
done

# Check if the required argument is provided
if [ -z "$XML_PATH" ]; then
  echo "Usage: $0 [-v|--print] <required_argument>"
  exit 1
fi

# Run Tests
docker-compose run python-test-app

# Check if the -v or --print option is set
if [ -n "$PRINT_OPTION" ]; then
  echo "PRINT_OPTION is set to: $PRINT_OPTION"
  echo "XML_PATH is set to: $XML_PATH"
  docker-compose run python-app $PRINT_OPTION $XML_PATH

else
  echo "PRINT_OPTION is not set"
  echo "XML_PATH is set to: $XML_PATH"
  docker-compose run python-app $XML_PATH

fi


docker-compose down
