import os
import csv

# Path to collect data from the Analysis folder
csvpath = os.path.join("Module 3", "Analysis", "election_data.csv")

# Open and read the csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)

    # Initialize variables
    total_votes = 0
    candidates = {}
    winner = ""
    winner_votes = 0

    # Loop through rows in csv file
    for row in csvreader:
        # Add to total vote count
        total_votes += 1

        # Get candidate name from row
        candidate = row[2]

        # Add candidate to dictionary or update their vote count
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

    # Print election results header
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # Loop through candidates and print their results
    for candidate in candidates:
        votes = candidates[candidate]
        percent = "{:.3%}".format(votes / total_votes)
        print(f"{candidate}: {percent} ({votes})")

        # Check if candidate has most votes
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    # Print winner results
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
