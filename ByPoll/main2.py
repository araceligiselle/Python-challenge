import os
import csv
 
election_csv = os.path.join('..', 'Resources', "election_data.csv")

row_count = 0
data = []

with open(election_csv) as election_file:
    csvelection = csv.reader(election_file, delimiter=',')

    csv_header = next(csvelection)
    print(csv_header)

    data = list(csvelection)

    for row in csvelection:
        print(row)

'Total Votes'
total_votes = len(data)
print("Total Votes: ", total_votes)

'Candidates, Percentage, Total Number of votes for each'
total_votes = 0
candidate_votes = {}
candidate_percentages = {}

for row in data:
    total_votes += 1
    candidate_name = row[2]
    candidate_votes[candidate_name] = candidate_votes.get(candidate_name,0) + 1

for candidate_name, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate_name] = percentage
    print(f"{candidate_name}: {percentage:.3f}% ({votes})")

winner = max(candidate_votes, key=candidate_votes.get)
print("Winner: ", winner)

'Export to Text file'
output_file = 'election_results.txt'
with open(output_file, 'w') as txt_file:
    first_output = (
        f'Total Votes: {total_votes}\n'
    )
    txt_file.write(first_output)
    for candidate_name, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate_name] = percentage
        next_output = (f'{candidate_name}: {percentage:.3f}% ({votes})\n')
        txt_file.write(next_output)
    final_output = (f'Winner: {winner}\n')
    txt_file.write(final_output)