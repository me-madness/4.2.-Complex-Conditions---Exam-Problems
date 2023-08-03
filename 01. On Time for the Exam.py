exam_hour = int(input())
exam_minutes = int(input())
arriving_hour = int(input())
arriving_minutes = int(input())

late = 'Late'
on_time = 'On time'
early = 'Early'

exam_time = (exam_hour * 60) + exam_minutes
arriving_time = (arriving_hour * 60) + arriving_minutes

total_minutes = arriving_time - exam_time
student_arrival = ''
result = ''

student_arrival = late
if total_minutes < -30:
    student_arrival = early
elif total_minutes <= 0:
    student_arrival = on_time
    
if total_minutes != 0:
    hours = abs(total_minutes) // 60           
    minutes = abs(total_minutes) % 60  

    if hours > 0:
        result = f"{hours}:{minutes:02}hours"             
    else:
        result = f"{minutes} minutes"
    
    if total_minutes < 0:
        result += " before the start"    
    else:
        result += " after the start"
print(student_arrival)        
if result:
    print(result)