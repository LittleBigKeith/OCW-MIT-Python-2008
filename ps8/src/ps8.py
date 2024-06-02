from functools import cmp_to_key
import time

SUBJECT_FILENAME = "src/subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    course_dict = dict()
    inputFile = open(filename)
    for line in inputFile:
        name, value, work = line.strip().split(",")
        try:
            course_dict.update({name: (int(value), int(work))})
        except ValueError:
            pass
    return course_dict

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = list(subjects.keys())
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)

def cmpValue(subject1, subject2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subject1[1][VALUE]
    val2 = subject2[1][VALUE]
    return  val2 - val1

def cmpWork(subject1, subject2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subject1[1][WORK]
    work2 = subject2[1][WORK]
    return  work1 - work2

def cmpRatio(subject1, subject2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subject1[1][VALUE]
    val2 = subject2[1][VALUE]
    work1 = subject1[1][WORK]
    work2 = subject2[1][WORK]
    return float(val2) / work2 - float(val1) / work1

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    sorted_subjects = sorted(subjects.items(), key=cmp_to_key(comparator))
    while sum([subject[1][WORK] for subject in sorted_subjects]) > maxWork:
        sorted_subjects.pop()
    return dict(sorted_subjects)

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[list(nameList)[i]] = list(tupleList)[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = list(subjects)[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime(maxWork):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    subjects = loadSubjects(SUBJECT_FILENAME)
    start_time = time.time()
    print(bruteForceAdvisor(subjects, maxWork))
    end_time = time.time()
    print(f"BruteForceAdvisor took {end_time - start_time:.2f} seconds.")


# Problem 3 Observations
# ======================
#
# max_work | Time(s)
# ------------------
#     1    |  0.01
#     2    |  0.04
#     3    |  0.17
#     4    |  0.71
#     5    |  2.61
#     6    |  8.48
#     7    |  26.43
#     8    |  76.78
#     9    |  207.92
#     10   |  541.05

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork,memoSet,memoVal):
    print("Calling with {},{}".format(i,subsetWork))
    #if (i,subsetWork) in memoVal:
    #    print("Value already present in cache for {},{}".format(i,subsetWork))
    #    return memoSet[(i,subsetWork)], memoVal[(i,subsetWork)]
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
        # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = list(subjects)[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK],memoSet,memoVal)
            memoSet[(i + 1, subsetWork + s[WORK])] = bestSubset
            memoVal[(i + 1, subsetWork + s[WORK])] = bestSubsetValue
            subset.pop()
        bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
            maxWork, i+1, bestSubset, bestSubsetValue, subset,
            subsetValue, subsetWork,memoSet,memoVal)
        memoSet[(i + 1, subsetWork)] = bestSubset
        memoVal[(i + 1, subsetWork)] = bestSubsetValue
        return bestSubset, bestSubsetValue

def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    memoSet  = {}
    memoVal = {}
    bestSubset, bestSubsetValue = \
       dpAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0,memoSet,memoVal)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[list(nameList)[i]] = list(tupleList)[i]
    print(memoSet)
    print(memoVal)
    print(bestSubset, bestSubsetValue)
    return outputSubjects
#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

def find_max_value_by_work(subjects, work):
    try:
        max_value = max(filter(lambda x: x[1][WORK] == work, subjects.items()), key=lambda x: x[1][VALUE])
    except ValueError:
        max_value = 0
    return max_value

def advisor(subjects, max_work):
    if max_work == 0:
        return (0, ())

    #if (tuple(subjects), max_work) in advisor_mem:
    #    return advisor_mem[tuple(subjects), max_work]

    curr_max = find_max_value_by_work(subjects, max_work)
    curr_course = ()
    temp_key, temp_value = None, None
    if curr_max != 0:
        subjects.pop(curr_max[0])
        curr_course = curr_max
        curr_max = curr_max[1][VALUE]
    for i in range(1, max_work // 2 + 1):
        a, course_a = advisor(subjects, i)
        b, course_b = advisor(subjects, max_work - i)
        
        curr_max = max(curr_max, a + b)
        if curr_max > a + b:
            curr_course = curr_course
        else:
            curr_course = (course_a, course_b)
        #print(i, a, max_work - i, b )

        #advisor_mem[tuple(subjects), max_work] = (curr_max, curr_course)
    return curr_max, curr_course

subjects = loadSubjects(SUBJECT_FILENAME)
subject_set = set()
#printSubjects(bruteForceAdvisor(subjects,6))
advisor_mem = dict()
max_value = advisor(subjects, 20)
print(max_value)



