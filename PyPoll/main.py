# Import modules
import csv
import os

# Create variables to write csv data to
candidates = []
votes = []

# Create path to csv file
csvpath = os.path.join("Resources", "election_data.csv")

# Read the csv
with open(csvpath, 'r') as csvfile:
    
    # Create the csvreader object
    csvreader = csv.reader(csvfile)

    # Store the header and iterate past it
    header = next(csvreader)

    # iterate through the csv
    for row in csvreader:

        # Store current vote
        current_selection = row[2]

        # Check if this is a new candidate
        if current_selection not in candidates:
            candidates.append(current_selection)
        
        # Add current vote to votes list
        votes.append(current_selection)

# Store total votes
total_votes = len(votes)

# Create a dictionary to hold votes for each candidate and start vote count at 0
vote_dict = {}
for candidate in candidates:
    vote_dict[candidate] = 0

# Iterate through all votes to tally up totals
for vote in votes:
    vote_dict[vote] += 1

# Determine winner and create final outcome string
final_outcomes = []
winning_total = 0

for candidate in candidates:

    # Create final outcome string
    outcome = f"{candidate}: {str(round((vote_dict[candidate] * 100 / total_votes), 3))}% ({vote_dict[candidate]})"
    final_outcomes.append(outcome)

    # Determine winner
    if vote_dict[candidate] > winning_total:
        winner = candidate
        winning_total = vote_dict[candidate]

# Build report lines
report_header = "Election Results"
breaker = "-------------------------"
total_votes_str = f"Total Votes: {total_votes}"
winner_str = f"Winner: {winner}"

report = [report_header, breaker, total_votes_str, breaker]

# Put report lines in a list
for result in final_outcomes:
    report.append(result)

report.append(breaker)
report.append(winner_str)
report.append(breaker)

# Print the final results
for line in report:
    print(line)

# Create outfile path
outfile_path = os.path.join("analysis", "analysis.txt")

# Zip up report for export
report_zip = zip(report)

# Print report and export a text file with results
with open(outfile_path, "w") as txtfile:
    # Create writer
    writer = csv.writer(txtfile)

    # Write rows to outfile
    writer.writerows(report_zip)


    



