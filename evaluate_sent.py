from collections import defaultdict
baseline_score = []
multitask_score = []
with open('baseline_score.txt','r') as f1:
    for line in f1:
        line = line.strip()
        split_line = line.split('\t')
        baseline_score.append((split_line[0],float(split_line[1])))


with open('multitask-reinforce_score.txt','r') as f2:
    for line in f2:
        line = line.strip()
        split_line = line.split('\t')
        multitask_score.append((split_line[0],float(split_line[1])))

for videoid, score in multitask_score:

    for videoid1, score1 in baseline_score:

      if score > 0 and score1 == 0 and videoid == videoid1:
         print 'video id: ', videoid

