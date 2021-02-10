
class Solution:
    def checkStraightLine(self, coor):
        output = True

        x_values = [x[0] for x in coor]
        y_values = [y[1] for y in coor]

        if x_values.count(x_values[0]) == len(x_values):
            return output

        elif y_values.count(y_values[0]) == len(y_values):
            return output

        else:
            for i in range(0,len(coor)):
                try:
                    y2_y1 = (coor[i][1] - coor[0][1])
                    x2_x1 = (coor[i][0] - coor[0][0])

                    m = y2_y1 / x2_x1
                    c = float(coor[0][1]) - m * float(coor[0][0])

                    def line_eq_y(x):
                        y = m * x + c
                        return y

                    for coor in coor[2:]:
                        if line_eq_y(coor[0]) != coor[1]:
                            output = False
                            return output
                except:
                    pass

        return output

obj = Solution()

obj.checkStraightLine([[2,0],[2,1],[2,-1]]) # Horizontal
obj.checkStraightLine([[2,3],[2,3],[1,3]]) # Vertical
obj.checkStraightLine([[1,2],[2,3],[3,4],[4,5]]) # Gradient
obj.checkStraightLine([[0,0],[0,5],[5,5],[5,0]]) # Random
