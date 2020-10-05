
import  os
import csv
import math

changes = []
ammount = []
sustrahend = []
minuend = []
pair = []

print("""
-----------------------------------------------------------------------------------------
            Financial Analysis
-----------------------------------------------------------------------------------------
""")

file_csv = os.path.join("..","Resources", "budget_data.csv")

# OPENING THE DOOR
with open(file_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header=next(csv_reader)
    csv_reader= list(csv_reader)
# Getting the number of lines no header = number of months
    num_months = len(csv_reader)
    print(f"Total months: {num_months}")
# Go for the total ammount
    for obs in csv_reader:
        ammount.append(obs[1])
        total_ammount = [float(obs1) for obs1 in ammount]
        total_ammount1 = sum(total_ammount)
    print(f"Total: {total_ammount1}")
# Get averange of the changes
# SUSTRAHEND
    for row in ammount:
        sustrahend.append(row)
        if row == "671099":
            sustrahend.remove(row)
    total_sustrahend = [float(row) for row in sustrahend]

# MINUEND
    for x in ammount:
        minuend.append(x)
        if x == "867884":
            minuend.remove(x)

    total_minuend = [float(x) for x in minuend]

#making a zip object, looking for a tuple

    zip_object = zip(total_sustrahend, total_minuend)

    for total_sustrahend, total_minuend in zip_object:
        changes.append(total_minuend-total_sustrahend) 
    
    total_changes = sum(changes)
    average_changes = total_changes/len(changes)

    print(f"Average change: ${average_changes}")

# Going for greatest increase and decrease using the index of the list changes
    maximu = math.trunc(max(changes))
    minimu = math.trunc(min(changes))
        
    index_max = changes.index(maximu)
    index_min = changes.index(minimu)

    worst_change = changes[int(index_min)]
    worst_month = csv_reader[int(index_min)+1]

    best_change = changes[int(index_max)]
    best_month = csv_reader[int(index_max)+1]

    print(f"Greatest Increase in Profits: {best_month[0]} (${math.trunc(best_change)})")
    print(f"Greatest Decrease in Profits: {worst_month[0]} (${math.trunc(worst_change)})")


# Export into a text file with the results
budget_final = os.path.join("..","Resources","budget_data_final.txt")

with open(budget_final, "w") as file_final:

    file_final.write("Financial Analysis\n")
    file_final.write("-----------------------------------------------\n")
    file_final.write(f"Total months: {num_months}\n")
    file_final.write(f"Total: ${total_ammount1}\n")
    file_final.write(f"Average Change: ${average_changes}\n")
    file_final.write(f"Greatest Increase in Profits:  {best_month[0]} (${math.trunc(best_change)})\n")
    file_final.write(f"Greatest Decrease in Losses:  {worst_month[0]} (${math.trunc(worst_change)})\n")


print("""
-----------------------------------------------------------------------------------------
            We've finished!
-----------------------------------------------------------------------------------------
""")



