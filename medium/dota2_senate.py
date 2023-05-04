from collections import deque

class Solution:
    def predict_party_victory(self, senate: str) -> str:
        # convert senate to list
        senate = list(senate)
        # create two queues for each party
        D, R = deque(), deque()

        # add each senator to their respective queue
        for i, s in enumerate(senate):
            if s == 'R':
                R.append(i)
            else:
                D.append(i)
        
        # while both parties have senators
        while D and R:
            # get the index of the next senator from each party
            d_turn = D.popleft()
            r_turn = R.popleft()

            # if the index of the next senator from the Radiant party is less than the index of the next senator from the Dire party
            # then the next senator from the Radiant party will ban the next senator from the Dire party
            # else the next senator from the Dire party will ban the next senator from the Radiant party
            if r_turn < d_turn:
                # add the next senator from the Radiant party to the end of the queue with the index of the next senator from the Dire party
                R.append(d_turn + len(senate))
            else:
                # add the next senator from the Dire party to the end of the queue with the index of the next senator from the Radiant party
                D.append(r_turn + len(senate))

        # return the party with the remaining senator
        return 'Radiant' if R else 'Dire'

solution = Solution()
print(solution.predict_party_victory('RDRDDR'))