# Process each test case
for _ in range(int(input())):
    quiz_result = input()
    consecutive_correct = 0
    total_score = 0
    
    # Iterate through each problem result
    for answer in quiz_result:
        if answer == 'O':
            # Correct: increment streak and add to score
            consecutive_correct += 1
            total_score += consecutive_correct
        else:
            # Wrong: reset the consecutive streak
            consecutive_correct = 0
    
    print(total_score)