from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:  input numbers
        :param target: target sum
        :return: sum index numbers

        5332 ms 14.9 MB
        """
        ls = len(nums)
        if ls < 2:
            return []
        for i in range(ls):
            for j in range(i + 1, ls):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :param int:
        :return:

        68 ms  16.7 MB
        """
        hash_index: dict = {}
        for idx, num in enumerate(nums):
            try:
                hash_index[num].append(idx)
            except KeyError:
                hash_index[num] = [idx]
        for idx, num in enumerate(nums):
            another = target - num
            try:
                candidates = hash_index[another]
                if another == num:
                    if len(candidates) > 1:
                        return candidates
                    else:
                        continue
                else:
                    return [idx, candidates[0]]
            except KeyError:
                pass
        return []

    def twoSumV3(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        52 ms 15.1 MB
        """
        hash_index: dict = {}
        for idx, num in enumerate(nums):
            another = target - num
            try:
                another_idx = hash_index[another]
                return [another_idx, idx]
            except KeyError:
                hash_index[num] = idx
        return []

    def twoSumV4(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        56 ms 15.7 MB
        """
        nums_idx = [(num, idx) for idx, num in enumerate(nums)]
        sorted_nums_idx = sorted(nums_idx)
        start, end = 0, len(sorted_nums_idx) - 1
        while start < end:
            current = sorted_nums_idx[start][0] + sorted_nums_idx[end][0]
            if current == target:
                return [sorted_nums_idx[start][1], sorted_nums_idx[end][1]]
            if current < target:
                start += 1
            else:
                end -= 1
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([1, 2, 3, 4], 5))
    print(s.twoSumV2([1, 2, 3, 4], 5))
    print(s.twoSumV3([1, 2, 3, 4], 5))
    print(s.twoSumV4([1, 2, 3, 4], 5))