import numpy as np

scores = np.array(
    [[12,15,16,18],
    [10,20,17,15],
    [10,20,20,19],
    [10,11,12,16]]
)

sub_avg=np.mean(scores,axis=0)

highest_avg = np.argmax(sub_avg)

subjects = ["C","Math","Python","C++"]
high_sub = subjects[highest_avg]
print("Average score for subject: ",sub_avg)
print("Highest Average score for subject:",high_sub)