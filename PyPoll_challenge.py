# The data we need to retrieve:
# 1. The total number of votes cast
# 2a. A complete list of candidates who received votes
# 2b. A complete list of counties who voted
# 3a. The total number of votes each candidate won
# 3b. The total number of votes per county
# 4a. The percentage of votes each candidate won
# 4b. The percentage of votes per county
# 5a. The winner of the election based on popular votes
# 5b. The largest county turnout

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path (DIRECT method)
file_to_load = os.path.join("Resources_challenge/election_results_challenge.csv")

# Assign a variable to save the file to a path (INDIRECT method)
file_to_save = os.path.join("Analysis_challenge", "election_analysis_challenge.txt")

# Initialize a total vote counter
total_votes = 0

# Initialize Candidate Options list
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save,"w") as txt_file:

    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")

    #Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the % of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]

        # Calculate the percentage of votes
        vote_percentage = int(votes) / int(total_votes) * 100

        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determin if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning candidate equal to the candidate's name
            winning_candidate = candidate
        
    # Print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

print("----------------------------------------------------------------------------------------------------------)") 


