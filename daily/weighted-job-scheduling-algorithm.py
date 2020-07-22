

class Job:

    def __init__(self, name, start, end, profit):
        self.name = name
        self.start_end = (start, end)
        self.profit = profit
        self.acc_prof = profit


list_jobs = [Job('A', 2, 5, 6),
             Job('B', 6, 7, 4),
             Job('C', 7, 9, 2),
             Job('D', 1, 3, 5),
             Job('E', 5, 8, 11),
             Job('F', 4, 6, 5),
             ]

list_jobs = sorted(list_jobs, key=lambda job: job.start_end[1])

#print(len(list_jobs))
acc_prof = []

for i in range(1, len(list_jobs)):
    for j in range(0, (i-1)):
        if list_jobs[j].start_end[1] <= list_jobs[i].start_end[0]:
            if list_jobs[j].acc_prof + list_jobs[i].profit > list_jobs[i].acc_prof:
                list_jobs[i].acc_prof = list_jobs[j].acc_prof + list_jobs[i].profit


max_profit = 0

for i in range(0, len(list_jobs)):
    if max_profit < list_jobs[i].acc_prof:
        max_profit = list_jobs[i].acc_prof

print(max_profit)

# https://riptutorial.com/dynamic-programming/example/25784/weighted-job-scheduling-algorithm
