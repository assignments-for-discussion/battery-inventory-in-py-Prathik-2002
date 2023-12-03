
def count_batteries_by_health(present_capacities):
    
    count_batteries_by_health_dictionary = {"healthy": 0,"exchange": 0,"failed": 0}
    for present_capacity in present_capacities:
        current_SoH = calculateSoH(present_capacity, 120)
        if current_SoH > 80:
            count_batteries_by_health_dictionary["healthy"] += 1
        elif current_SoH > 62:
            count_batteries_by_health_dictionary["exchange"] += 1
        else:
            count_batteries_by_health_dictionary["failed"] += 1
    return count_batteries_by_health_dictionary

def calculateSoH(present_capacity, rated_capacity):
    #`SoH% = 100 * present_capacity / rated_capacity`
    if rated_capacity == 0:
        print("Rated Capacity can not be 0\n")
        exit()
    current_SoH = 100 * present_capacity / rated_capacity
    return current_SoH
    
    
def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70, 0, 3]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 2)
    assert(counts["exchange"] == 3)
    assert(counts["failed"] == 3)
    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()