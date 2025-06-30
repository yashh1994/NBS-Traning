def triangleType(self, nums: List[int]) -> str:
        side1,side2,side3 = sorted(nums)
        if side1+side2 <= side3:
            return "none"
        elif side1==side3:
            return "equilateral"
        elif side1 == side2 or side2 == side3:
            return "isosceles"
        else:
            return "scalene"