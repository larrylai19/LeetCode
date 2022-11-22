class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import time
        lst = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        t = time.struct_time([year, month, day, 0, 0, 0, 0, 0, -1])
        return lst[(time.localtime(time.mktime(t)).tm_wday + 1) % 7]