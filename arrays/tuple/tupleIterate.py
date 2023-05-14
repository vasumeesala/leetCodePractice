# let results = [
# (result: "PASS", name: "Stress test"),
# (result: "FAIL", name: "UI test"),
# (result: "FAIL", name: "Functional test"),
# (result: "PASS", name: "System test"),
# (result: "FAIL", name: "Network test")
# ]


# Pass -> 2 and name = "Stress test", "System test"
from collections import defaultdict
def testResultParsing(testResults):
    lookUpTable = defaultdict(list)
    for i in range(len(testResults)):
        lookUpTable[testResults[i][0]].append(testResults[i][1])
    for key, value in lookUpTable.items():
        print(f"test result: {key} count: {len(value)}, test names: {value}")


testResults = [
    ("PASS", "Stress Test"),
    ("PASS", "Functional Test"),
    ("FAIL", "Memory Test"),
    ("FAIL", "Unit Test"),
    ("FAIL", "GPU Test")
]

print(testResultParsing(testResults))