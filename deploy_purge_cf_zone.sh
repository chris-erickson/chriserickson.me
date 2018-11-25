#! /bin/bash

# Purges the entire zone (all subdomains included)

curl --request POST \
  --url https://api.cloudflare.com/client/v4/zones/"$CF_ZONE_ID"/purge_cache \
  --header 'content-type: application/json' \
  --header "x-auth-email: $CF_USER_EMAIL" \
  --header "x-auth-key: $CF_USER_AUTH_KEY" \
  --data '{"purge_everything": true}' || exit 1
