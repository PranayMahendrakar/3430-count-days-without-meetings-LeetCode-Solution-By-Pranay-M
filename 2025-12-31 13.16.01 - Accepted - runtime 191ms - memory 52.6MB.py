class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        # Sort meetings by start time
        meetings.sort()
        
        # Merge overlapping meetings
        merged = []
        for start, end in meetings:
            if merged and start <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        # Count total meeting days
        meeting_days = sum(end - start + 1 for start, end in merged)
        
        return days - meeting_days