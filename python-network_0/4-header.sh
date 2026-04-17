#!/bin/bash
# Sends a GET request with a custom header X-School-User-Id set to 98
curl -sH "X-School-User-Id: 98" "$1"
