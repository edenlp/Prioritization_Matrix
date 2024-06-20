# Eden Pardo
# Prioritization Matrix

# Numpy package is used to obtain the indices of an array
import numpy

# input_tasks() is used to obtain the user inputs
def input_tasks():
    tasks = []
    task_amt = int(input('How many tasks do you have? (2-10) '))
    if 2 <= task_amt <= 10:
        for i in range(1, task_amt+1):
            str_task = str(input(f'Please input task #{i}: '))
            tasks.append(str_task)
        return task_amt, tasks
    else:
        print('Please enter 2-10 tasks to use prioritization matrix.')

# create_matrix() creates the intial 'empty' matrix that has the users respective tasks
def create_matrix(user_task_amt, user_tasks):
    letter_list = ['A', 'B' ,'C' ,'D' ,'E' ,'F' ,'G','H' ,'I' ,'J']
    master_list = []

    # Creating the master task list (matrix)
    for tasks in range(1, user_task_amt+1):
        temp_list = []
        for task in range(tasks-1):
            temp_list.append('*')
        temp_list.append(letter_list[tasks-1])
        temp_list.append("--> "+ user_tasks[tasks-1])
        master_list.append(temp_list)

    return master_list

# fill_matrix() asks the user each task comparison, then fills out the matrix according to their answers
def fill_matrix(user_task_amt, master_list):
    fill_dict = { 0:'a', 1:'b' , 2:'c' , 3:'d' , 4:'e' , 5:'f' , 6:'g', 7:'h' , 8:'i' , 9:'j' }
    user_picks = [] # Is used to calculate each task's priority

    for i in range(user_task_amt):
        for j in range(i+1, user_task_amt):
            # Add in a failsafe to make sure the user enters a proper answer?
            user_pick = str(input(f'Which is more important? Task "{fill_dict[i]}" or task "{fill_dict[j]}" ? '))
            master_list[j][i] = user_pick # Reassign matrix values with the users comparison pick
            user_picks.append(user_pick)

    return user_picks, master_list

# calculate_totals() determines which task is more important and gives the user a ranked list
def calculate_totals(user_picks, user_tasks, file_object):
    fill_dict = { 0:'a', 1:'b' , 2:'c' , 3:'d' , 4:'e' , 5:'f' , 6:'g', 7:'h' , 8:'i' , 9:'j' }
    values = [] # Used to store the number of occurences of each comparison pick

    for i in range(len(user_tasks)):
        count = user_picks.count(fill_dict[i])
        values.append(count)

    array_values = numpy.array(values)
    sorted_values = numpy.argsort(array_values)
    desc_sorted_values = sorted_values[::-1] # An array of the indices of pick occurences in descending order
    
    for i in range(len(user_tasks)):
        file_object.write(f'Task {i+1}: {user_tasks[desc_sorted_values[i]]}\n')
        print(f'Task {i+1}: {user_tasks[desc_sorted_values[i]]}')
    file_object.write('\n')

# print_matrix() simply prints the list for the user to visualize
def print_matrix(master_list):
    print(master_list)
    # Printing out the matrix
    for ind_list in master_list:
        for j in ind_list:
            print(j, end = ' ')
        print()

def main():
    task_file = open("MyPrioritizedTasks.txt","a")

    user_task_amt, user_tasks = input_tasks()
    matrix = create_matrix(user_task_amt, user_tasks)
    #print_matrix(matrix)
    picks, final_matrix = fill_matrix(user_task_amt, matrix)
    print_matrix(final_matrix)

    task_file.write('Tasks ToDo: \n')
    calculate_totals(picks, user_tasks, task_file)

    task_file.close()
main()