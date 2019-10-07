from collections import OrderedDict, defaultdict
import os
import csv

queue_ids = []
queue_count = defaultdict(list)

mail_list = os.listdir("/var/spool/mqueue/")

for mail in mail_list:
        if mail[:2] == "qf":
                queue_ids.append(mail)

for item in queue_ids:
        with open("/var/spool/mqueue/%s" % item, "r") as f:
                data = f.read()
                data_split = data.split("\n")
                for line in data_split:
                        if line[:4] == "RFDA":
                                queue_count[line[5:]].append(item)
                        if line[:4] == "RPFD":
                                queue_count[line[6:-1]].append(item)


ordered_d = OrderedDict(sorted(queue_count.viewitems(), key=lambda x: len(x[1])))
print("{: <30} {: ^30}".format("Email", "Queue"))
for k,v in ordered_d.items():
        print("{: <30} {: ^30}".format(k,len(v)))
