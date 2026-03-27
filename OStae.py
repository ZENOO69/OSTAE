# Simple Memory Allocation (First Fit)
#Prajwalit and Mithilesh CS24249 and CS25D008
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112]

allocation = [-1] * len(processes)

print("\n--- Initial Allocation ---\n")

# Allocation
for i in range(len(processes)):
    for j in range(len(blocks)):
        if blocks[j] >= processes[i]:
            allocation[i] = j
            print("Process P", i+1, "allocated to Block", j+1)
            print("Internal Fragmentation =", blocks[j] - processes[i])
            blocks[j] = 0   # mark block as used
            break

# Deallocation
print("\n--- Deallocation ---\n")

print("Process P1 completed and memory freed")
blocks[1] = 500   # freeing block 2

# External Fragmentation Check
print("\n--- External Fragmentation ---\n")

new_process = 550
total_free = sum(blocks)

print("Total Free Memory =", total_free)

allocated = False

for j in range(len(blocks)):
    if blocks[j] >= new_process:
        print("Process P4 allocated in Block", j+1)
        allocated = True
        break

if not allocated:
    print("Process P4 cannot be allocated")

    if total_free >= new_process:
        print("External Fragmentation Occurs")
    else:
        print("Not enough memory")
