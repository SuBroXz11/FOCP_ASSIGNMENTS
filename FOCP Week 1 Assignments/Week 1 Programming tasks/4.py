# In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate
# and display Boycott's batting average.

total_matches=609
total_batted=1014
not_out=162
total_scored=48426
batting_avg=round(total_scored/(total_batted - not_out),2)
print(f"Boycott's batting average is {batting_avg}")