class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for num in digits:
            string += str(num)
        number = str(int(string) + 1)
        return [c for c in number]