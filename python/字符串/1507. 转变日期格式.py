class Solution:
    def reformatDate(self, date: str) -> str:
        d_str,m_str,y = date.split(" ")
        d = d_str[:-2]
        if len(d) == 1:
            d = "0"+d
        month_dict = {
                         "Jan":"01",
                         "Feb":"02",
                         "Mar":"03",
                         "Apr":"04",
                         "May":"05",
                         "Jun":"06",
                         "Jul":"07",
                         "Aug":"08",
                         "Sep":"09",
                         "Oct":"10",
                         "Nov":"11",
                         "Dec":"12"
        }
        m = month_dict[m_str]
        return y + "-" + m + "-" + d

# 写法更优雅
class Solution:
    def reformatDate(self, date: str) -> str:
        s2month = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
            "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        date = date.split(" ")

        date[0] = date[0][: -2].zfill(2)
        date[1] = s2month.get(date[1])
        date.reverse()

        return "-".join(date)
