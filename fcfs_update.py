class FcFs:
    def findWaitingTime(self, processes, n, bt, wt, at):
        service_time = [0] * n
        service_time[0] = min(at)
        wt[0] = 0

        # calculating waiting time
        for i in range(1, n):

            # Add burst time of previous processes
            service_time[i] = (service_time[i - 1] +
                               bt[i - 1])

            # Find waiting time for current
            # process = sum - at[i]
            wt[i] = service_time[i] - at[i]

            # If waiting time for a process is in
            # negative that means it is already
            # in the ready queue before CPU becomes
            # idle so its waiting time is 0
            if (wt[i] < 0):
                wt[i] = 0

    # Function to calculate turn around time
    def findTurnAroundTime(self, processes, n, bt, wt, tat):
        # Calculating turnaround time by
        # adding bt[i] + wt[i]
        for i in range(n):
            tat[i] = bt[i] + wt[i]

        # Function to calculate average waiting

    # and turn-around times.
    def findavgTime(self, processes, n, bt, at):
        wt = [0] * n
        tat = [0] * n

        # Function to find waiting time
        # of all processes
        self.findWaitingTime(processes, n, bt, wt, at)

        # Function to find turn around time for
        # all processes
        self.findTurnAroundTime(processes, n, bt, wt, tat)
        return wt, tat, at, bt


