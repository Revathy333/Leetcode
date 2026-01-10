class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        emp = 0
        for h in hours:
            if h >= target:
                emp+=1
        return emp         