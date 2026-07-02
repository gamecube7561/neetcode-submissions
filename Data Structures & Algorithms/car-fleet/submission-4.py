class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        total_fleets = 0
        for i in range(len(speed)):
            fleets.append([position[i], speed[i]])
        
        fleets.sort()
        stack = []

        while fleets:
            fleet = fleets.pop()
            
            time = (target - fleet[0]) / fleet[1]

            if stack and stack[-1] < time:
                stack.append(time)
            elif not stack:
                stack.append(time)

        return len(stack)
        
