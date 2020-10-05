
import os
import csv

path = os.path.join("..", "Resources", "election_data.csv")

vote_list = []
candidates_list = []
unique_candidate = []
Candidato1 = []
Candidato2 = []
Candidato3 = []
Candidato4 = []
percentage = []

# Open de the door
with open(path, "r", encoding="utf-8") as csv_files:
    csv_reader = csv.reader(csv_files, delimiter=",")
    header = next(csv_reader)
# getting the complete list
    for vote in csv_reader:
        vote_list.append(vote)
# go for the total number of votes
    size = len(vote_list)
    print("""
        Election Results:
    --------------------------------------""")
    print(f"""        Total voters: {size}
    --------------------------------------    
    """)
# the list of candidates
    for cand in vote_list:
        candidates_list.append(cand[2])

# getting candidates with set function
    unique = list(set(candidates_list))
    print(f"        Candidate: {unique[0]}")
    print(f"        Candidate: {unique[1]}")
    print(f"        Candidate: {unique[2]}")
    print(f"        Candidate: {unique[3]}")

#calculating total votes by candidate 
    for i in candidates_list:
        if i == unique[0]:
            Candidato1.append(i)
            candidato1_sum = len(Candidato1)
            candidato1_porcent = (int(candidato1_sum)/int(size))*100 
    print(f"""
    ---------------------------------------
        {unique[0]}: {round(candidato1_porcent)}% ({candidato1_sum})""")

    for j in candidates_list:
        if j == unique[1]:
            Candidato2.append(j)
            candidato2_sum = len(Candidato2)
            candidato2_porcent = (int(candidato2_sum)/int(size))*100 
    print(f"        {unique[1]}: {round(candidato2_porcent)}% ({candidato2_sum})")

    for k in candidates_list:
        if k == unique[2]:
            Candidato3.append(k)
            candidato3_sum = len(Candidato3)
            candidato3_porcent = (int(candidato3_sum)/int(size))*100 
    print(f"        {unique[2]}: {round(candidato3_porcent)}% ({candidato3_sum})")

    for l in candidates_list:
        if l == unique[3]:
            Candidato4.append(l)
            candidato4_sum = len(Candidato4)
            candidato4_porcent = (int(candidato4_sum)/int(size))*100 
    print(f"        {unique[3]}: {round(candidato4_porcent)}% ({candidato4_sum})")

# defining the Winner

    list_percent = [candidato1_porcent,candidato2_porcent,candidato3_porcent, candidato4_porcent]
    champion = max(list_percent)
    
    for m in list_percent:
        if m==champion:
            index_champion=list_percent.index(m)
            winner = unique[int(index_champion)]

    print(f"""
    ---------------------------------------
            Winner:  {winner}
    ---------------------------------------        
            """)

# Export in to a text file with the results
election_results = os.path.join("..", "Resources", "election_results.txt")

with open(election_results, "w") as file_end:

    file_end.write("Election Results:\n")
    file_end.write("--------------------------------------\n")
    file_end.write(f"Total voters: {size}\n")
    file_end.write("--------------------------------------\n")
    file_end.write(f"Candidate: {unique[0]}\n")
    file_end.write(f"Candidate: {unique[1]}\n")
    file_end.write(f"Candidate: {unique[2]}\n")
    file_end.write(f"Candidate: {unique[3]}\n")
    file_end.write("--------------------------------------\n")
    file_end.write(f"{unique[0]}: {round(candidato1_porcent)}% ({candidato1_sum})\n")
    file_end.write(f"{unique[1]}: {round(candidato2_porcent)}% ({candidato2_sum})\n")
    file_end.write(f"{unique[2]}: {round(candidato3_porcent)}% ({candidato3_sum})\n")
    file_end.write(f"{unique[3]}: {round(candidato4_porcent)}% ({candidato4_sum})\n")
    file_end.write("--------------------------------------\n")
    file_end.write(f"Winner:  {winner}\n")
    file_end.write("--------------------------------------\n")