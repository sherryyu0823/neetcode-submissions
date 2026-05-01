class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        max_freq = max(cnt.values())
        freq = list(cnt.values())
        max_task = freq.count(max_freq)
        idle = (max_freq-1)*n
        empty = idle-(max_task-1)*(max_freq-1)
        rem_task = len(tasks)-max_task*max_freq
        ans = max_freq*max_task+ max(empty-rem_task, 0) + (len(tasks)-max_freq*max_task)
        return ans