#!/bin/sh

htpasswd -bc /etc/nginx/auth.htpasswd $BASIC_USERNAME $BASIC_PASSWORD
