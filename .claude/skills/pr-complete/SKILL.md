---
name: pr-complete
description: Approve and merge one Azure DevOps pull request by ID.
disable-model-invocation: true
---


#Approve and complete PR $ARGUMENTS

1. If no PR id was given, ask for one and stop

2. Show the PR so the user can see what will be merged:

   `az repos pr show --id $ARGUMENTS --output table`


3. Approve:

   `az repos pr set-vote --id $ARGUMENTS --vote approve`

4. Complete (this merges on the server):
    `az repos pr update --id $ARGUMENTS --status completed`

5. Confirm the result:
    `az repos pr show --id $ARGUMENTS --query table`