#!/bin/bash
curl -s http://127.0.0.1:3413/v1/status | jq .header_height
