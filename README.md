This script grabs all files in the mail spool and grabs who the sender is. It calculates the number of messages queued for all senders, and outputs the results to the screen.

It should be run with `watch` to get a constantly updating list of results:

`watch python queue-report.py`