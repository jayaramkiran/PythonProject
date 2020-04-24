# PythonProject
Conference schedule Programming python script

##Code is created in Python 3 using Pandas Data frame:
##Before running the code Need to run the following steps
1.	Install Pandas package if not there else you will get module not present error (pip install pandas)
a.	It will help us to create objects in the data frames as it’s quite easy to understand and code.
2.	Copy the CONFERENCEROOMS.xlsx to your directory it’s currently using from my local python directory (
pd.read_excel('C:\Python39\CONFERENCEROOMS.xlsx',index = False)

#Please replace the directory path with your local directory path in quotes at line no 5 in the script.
3.	Copy the python script to your python path from where you are accessing python 3. 
a.	If you are running from terminal need to mention full path like below
 

Got to your Python 3 Directory like cd C:\Python3 Run the Python script 
#python conference_room_schedule.py
It will popup one input message Enter Input Members,FloorNo,StartTime and Endtime
pass the input one by one like below
5
8
10:30:00
11:30:00

Your script will run and it will provide you the expected output: for this case it is 9.547



Code Logic for conference rooms scenario:
We are creating a data frame using .xlxs file as our input file with the help of pandas module.
df = pd.read_excel('C:\Python39\CONFERENCEROOMS.xlsx',index = False)
Our Input will be Floor_no followed by Room_no and Max_no as per the given scenario
We are storing the input provided by the user in the below variables:
temp_mem = input() ---this is the first input
temp_floor = input()---this is the second input
temp_start_time = input() –this is the third input
temp_end_time = input() –this is the fourth input.

We are creating the cases and splitting in each sub data frames in this code
newind = 'df1 df2 df3 df4 df5 df6'.split()

We are using MAX_NO for sorting and filtering based on Members.
 
newdf = df[(df['MAX_NO']> int(temp_mem))]

This will be our final data frames for populating the output
Sorting the rooms with nearest floor

newdf2 = newdf[(newdf['FLOOR']==(n))]
newdf3 = newdf[(newdf['FLOOR']==(n+1))]
newdf4 = newdf[(newdf['FLOOR']==(n-1))]
newdf5 = newdf2.append(newdf3)
newdf6 = newdf5.append(newdf4)
newdf7 = newdf6.sort_index(ascending=True)

In the cases we have created we are assigning the slots as per the given question 
df1 = pd.DataFrame(
{'Slot_no':[1,2],
'start_time':['9:00:00','14:30:00'],
'end_time':['9:15:00','15:00:00']})
f1 = df1.reindex(['Slot_no','start_time','end_time'], axis=1)

Similarly we are creating for df2,df3 df4 df5 and df6
We are assigning values in mask which will be having slot and start time and end time details for each case
 mask1 = df1['start_time'].between(start, end) | df1['end_time'].between(start,end)

Note: for df1 we have created mask1 for df2 mask2 like that for easily understanding the logic.

In the For loop we are iterating for the closest rooms available as per the time slots 
for row in newdf7['CASE']:
    #print(row)
    if row == 'df1':
        if str(mask1[0]) == 'True' or str(mask1[1]) == 'True':
            oup_df = df.loc[df['CASE'] == 'df1']
            rslt_df1 = oup_df[['FLOOR', 'ROOM_NO', 'MAX_NO']]
            result_df_op = result_df_op.append(rslt_df1)
	……..
We are checking time slots in each cases this is for df1 similarly we are checking in all cases df2,df3,df4,df5 and df6 using condition.

As this will always return bool value (True or False) we are checking for Match values only i.e True.


This code will give us the available rooms:

Note: from result_df we can have our output but as its mentioned in the question if we have more than one room available we should assign room on which team is present so for our case we are providing the room which is on 8th floor 
"""Assigning the room to the floor numbers if we have more than one room available"""
if result_df_op.empty != 'True' and n in result_df_op['MAX_NO'].values:
    #print(n)
    oup = result_df_op.loc[df['MAX_NO'] == n]
    final_output = oup[['FLOOR', 'ROOM_NO']]
    print(final_output['FLOOR'].to_string(index=False) + '.' + final_output['ROOM_NO'].to_string(index=False))
elif result_df_op.empty != 'True' and n not in result_df_op['MAX_NO'].values:
    oup = result_df_op.loc[df['MAX_NO'] != n]
    final_output = oup[['FLOOR', 'ROOM_NO']]
    print(final_output['FLOOR'].to_string(index=False) + '.' + final_output['ROOM_NO'].to_string(index=False))
else:
    print("Room Not Found ")

We are also handeling the code if we don’t get any available rooms as per the inputs.


For reference I am attaching the below outputs with respect to input I have provided and verified.

Note: Below code output generated from Pycharm tool
 



 
 
