class Solution:
    def maximumUnits(self, boxtypes, trucksize):
        boxtypes_sorted = sorted(boxtypes, key=lambda x: -x[1])

        loaded, units = 0, 0
        for i in boxtypes_sorted:
            for j in range(0, boxtype[0]):
                if loaded < trucksize:
                    loaded += 1
                    units  += boxtype[1]

        return units

obj = Solution()
obj.maximumUnits([[1,3],[2,2],[3,1]],4)

