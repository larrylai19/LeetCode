class Solution:
    def dayOfYear(self, date: str) -> int:
        sp = date.split('-')
        d1 = datetime.datetime.strptime(f'{date}', '%Y-%m-%d')
        d2 = datetime.datetime.strptime(f'{sp[0]}-01-01', '%Y-%m-%d')
        delta = d1 - d2
        return delta.days + 1