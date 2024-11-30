#!/bin/bash

SCRIPT_DIR=$(realpath "${BASH_SOURCE[0]}")


HOUR="$1"
MINUTE="$2"

SERVICE=~/Library/LaunchAgents/com.atrophian_strength.alarmservice.plist
SERVICE_STATUS=$(launchctl list | grep "$SERVICE")

pushd $SCRIPT_DIR > /dev/null
  if [[ -z "$HOUR" || -z "$MINUTE" || ! -z $SERVICE_STATUS ]]; then
    .venv/bin/python alarm-clock/main.py
  else
    launchctl unload $SERVICE
    .venv/bin/python alarm-clock/main.py set-alarm "$HOUR" "$MINUTE"
    launchctl load $SERVICE
  fi
popd > /dev/null


