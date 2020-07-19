'''
There will be a meeting at New York and San Francisco offices. We will have to fly the participants to 
either one of these two offices. Let's say each office can accommodate half of the participants. 
Our goal is to assign each participant to an office in a way that the total travel cost for the 
company is minimized. What is this minimal cost?

SF NY A 500 700 B 200 600 C 400 500 D 600 200 Output : 1400 (A:500 + B:200 + C:500 +D: 200)
'''


def twoCitySchedCost(costs):

    costs = sorted(costs, key = lambda x: x[0] - x[1])
    cost = 0
    for i in range(len(costs) // 2):
        cost += costs[i][0]
    for i in range(len(costs) // 2, len(costs)):
        cost += costs[i][1]
 
    return cost


