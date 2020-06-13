Run rule.sh to package dependencies (PRAW) and upload file to AWS lambda.

Currently uses Cloudwatch to run

1. `add_rule` with input `{ "add_rule": true }` and cron `0 0 ? * 2 *` (every Monday at midnight).
2. `remove_rule` with input `{ "remove_rule": false }` and cron `0 21 ? * 6 *` (every Friday at 9 pm).