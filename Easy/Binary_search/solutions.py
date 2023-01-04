from typing import List

class SolutionOOfN:
    def search(self, nums: List[int], target: int) -> int:
        """Return -1 if target is not in nums list, else
        return list index of target."""
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1

class SolutionOLogN:
    def search(self, nums: List[int], target: int) -> int:
        """WIP.
        Return -1 if target is not in nums list, else
        return list index of target."""
        middle_num, middle_indice = get_middle_num()

        if middle_num == target:
            return middle_indice
        elif middle_num > target:
            self.search(nums = [nums[:middle_indice]])
        else:
            ...