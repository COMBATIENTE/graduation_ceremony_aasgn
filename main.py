import sys

class GraduationCeremoneyAttendance:
    def __init__(self, days):
        self.days = days
        self.attendance = self.ways_to_attend_classes()


    def possible_attendence(self, days, pattern, arr):
        ''' possible_attendence: Recursive function to find all possible ways to attend classes over given days'''
        if days == 0:
            arr.append(pattern)
        else:
            self.possible_attendence(days - 1, pattern + 'A', arr)
            self.possible_attendence(days - 1, pattern + 'P', arr)

    def ways_to_attend_classes(self):
        ''' ways_to_attend_classes: Returns all possible ways to attend classes over given days'''
        arr = []
        pattern = ""
        self.possible_attendence(self.days, pattern, arr)
        return arr
    
    def ways_to_miss_graduation_ceremoney(self):
        ''' ways_to_miss_graduation_ceremoney: Returns all possible ways to miss graduation ceremony'''
        return list(filter(lambda way: "AAAA" in way, self.attendance))

    def total_ways_to_attend_classes(self):
        ''' total_ways_to_attend_classes: Returns total number of ways to attend classes over given days'''
        return len(self.attendance)
    
    def prob_to_miss_gradution_ceremony(self):
        ''' prob_to_miss_gradution_ceremony: Returns probability to miss graduation ceremony'''
        ineligible_ways = self.ways_to_miss_graduation_ceremoney()
        return f"{len(ineligible_ways)}/{self.total_ways_to_attend_classes()}"
    



if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
        print("Total No. of days: {}".format(days))
    except IndexError:
        print("Please pass 'Total days' arg in command line")
    except ValueError:
        print("'Days' argument must be of integer type or string type of integer number")
    except Exception as e:
        print(e)
    else:
        graduation_ceremoney_attendance = GraduationCeremoneyAttendance(days)
        print("Number of ways to attend classes over {} days is {}".format(days, graduation_ceremoney_attendance.total_ways_to_attend_classes()))
        print("probability to miss graduation ceremony is {}".format(graduation_ceremoney_attendance.prob_to_miss_gradution_ceremony()))
    
    