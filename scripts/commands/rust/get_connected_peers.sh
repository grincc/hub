#!/bin/bash
curl -s --user grin:$(cat ~/.grin/main/.api_secret)  -d '{"id":"1","method":"get_connected_peers","params":{}}' -o - http://127.0.0.1:3413/v2/owner | jq .result.Ok
