total_bugs_collected=0
for days in range(1,6):
    print('day', days, ':', end=' ')
    bugs_collected=int(input('How many bugs did you collect in today?'))
    total_bugs_collected+=bugs_collected
print('You collected in total', total_bugs_collected, 'bugs')

