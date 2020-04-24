import pandas as pd
import numpy as np

"""Reading Input from excel file having Floor,Room No and Max_no can fit"""
df = pd.read_excel('C:\Python39\CONFERENCEROOMS.xlsx',index = False)
#print(df)

newind = 'df1 df2 df3 df4 df5 df6'.split()
df['CASE'] = newind

"""Stting up the index as CASE"""
#print(df)
df.set_index('CASE')

"""Sort the rows with given number of people##"""
#print("Enter Input")
print("Enter Input Members,FloorNo,StarTime and EndTime ")
temp_mem = input()
temp_floor = input()
temp_start_time = input()
temp_end_time = input()
# newdf = df[(df['MAX_NO']> int(temp_mem))]
newdf = df[(df['MAX_NO']> int(temp_mem))]
#print(newdf)
newdf.set_index('CASE')

result_df_op= pd.DataFrame()

## Sort the rooms with nearest floor##

# n=int(temp_floor)
n=int(temp_floor)
newdf2 = newdf[(newdf['FLOOR']==(n))]
newdf3 = newdf[(newdf['FLOOR']==(n+1))]
newdf4 = newdf[(newdf['FLOOR']==(n-1))]
newdf5 = newdf2.append(newdf3)
newdf6 = newdf5.append(newdf4)
newdf7 = newdf6.sort_index(ascending=True)
#print(newdf7)


##Choosing the start and end date to check the timeslots
# start = pd.to_timedelta('10:30:00')
# end = pd.to_timedelta('11:30:00')
#print(str(temp_start_time))

start = pd.to_timedelta(temp_start_time)
end = pd.to_timedelta(temp_end_time)

# start = pd.to_timedelta(temp_start_time)
# end = pd.to_timedelta(temp_end_time)

## Database for different timesots from given input for each room##

df1 = pd.DataFrame(
{'Slot_no':[1,2],
'start_time':['9:00:00','14:30:00'],
'end_time':['9:15:00','15:00:00']})
f1 = df1.reindex(['Slot_no','start_time','end_time'], axis=1)

#print(df1)

#print(f1)

df1['start_time'] = pd.to_timedelta(df1['start_time'])
df1['end_time'] = pd.to_timedelta(df1['end_time'].replace('0:00:00', '24:00:00'))
mask1 = df1['start_time'].between(start, end) | df1['end_time'].between(start,end)
#print(mask1)

df2 = pd.DataFrame(
{'Slot_no':[1,2],
'start_time':['10:00:00','14:30:00'],
'end_time':['11:00:00','15:00:00']})
f2 = df2.reindex(['Slot_no','start_time','end_time'], axis=1)
df2['start_time'] = pd.to_timedelta(df2['start_time'])
df2['end_time'] = pd.to_timedelta(df2['end_time'].replace('0:00:00', '24:00:00'))
mask2 = df2['start_time'].between(start, end) | df2['end_time'].between(start,end)
#print(mask2)

df3 = pd.DataFrame(
{'Slot_no':[1,2],
'start_time':['11:30:00','17:00:00'],
'end_time':['12:30:00','17:30:00']})
f3 = df3.reindex(['Slot_no','start_time','end_time'], axis=1)
df3['start_time'] = pd.to_timedelta(df3['start_time'])
df3['end_time'] = pd.to_timedelta(df3['end_time'].replace('0:00:00', '24:00:00'))
mask3 = df3['start_time'].between(start, end) | df3['end_time'].between(start,end)
#print(mask3)

df4 = pd.DataFrame(
{'Slot_no':[1,2,3],
'start_time':['9:30:00','12:00:00','15:15:00'],
'end_time':['10:30:00','12:15:00','16:15:00']})
f4 = df4.reindex(['Slot_no','start_time','end_time'], axis=1)
df4['start_time'] = pd.to_timedelta(df4['start_time'])
df4['end_time'] = pd.to_timedelta(df4['end_time'].replace('0:00:00', '24:00:00'))
mask4 = df4['start_time'].between(start, end) & df4['end_time'].between(start,end)
#print(mask4)

df5 = pd.DataFrame(
{'Slot_no':[1,2],
'start_time':['9:00:00','11:00:00'],
'end_time':['14:00:00','16:00:00']})
f5 = df5.reindex(['Slot_no','start_time','end_time'], axis=1)
df5['start_time'] = pd.to_timedelta(df5['start_time'])
df5['end_time'] = pd.to_timedelta(df5['end_time'].replace('0:00:00', '24:00:00'))
mask5 = df5['start_time'].between(start, end) | df5['end_time'].between(start,end)
#print(mask5)

df6 = pd.DataFrame(
{'Slot_no':[1,2,3],
'start_time':['10:30:00','13:30:00','16:30:00'],
'end_time':['11:30:00','15:30:00','17:30:00']})
f6 = df6.reindex(['Slot_no','start_time','end_time'], axis=1)
df6['start_time'] = pd.to_timedelta(df6['start_time'])
df6['end_time'] = pd.to_timedelta(df6['end_time'].replace('0:00:00', '24:00:00'))
mask6 = df6['start_time'].between(start, end) | df6['end_time'].between(start,end)
#print(mask6)

for row in newdf7['CASE']:
    #print(row)
    if row == 'df1':
        if str(mask1[0]) == 'True' or str(mask1[1]) == 'True':
            oup_df = df.loc[df['CASE'] == 'df1']
            rslt_df1 = oup_df[['FLOOR', 'ROOM_NO', 'MAX_NO']]
            result_df_op = result_df_op.append(rslt_df1)

        #print(rslt_df1)
            #temp_df = oup_df[['FLOOR', 'ROOM_NO', 'MAX_NO']]
        # else:
        #     print("Not in Slot")

    elif row == 'df2':
        if str(mask1[0]) == 'True' or str(mask1[1]) == 'True':
            oup_df = df.loc[df['CASE'] == 'df2']
            rslt_df2 = oup_df[['FLOOR', 'ROOM_NO', 'MAX_NO']]
            result_df_op = result_df_op.append(rslt_df2)

            #rslt_df.append(rslt_df)
        # else:
        #     print("Not in Slot")
    elif row == 'df3':
        if str(mask3[0]) == 'True' or str(mask3[1]) == 'True':
            oup_df = df.loc[df['CASE'] == 'df3']
            rslt_df3 = oup_df[['FLOOR', 'ROOM_NO', 'MAX_NO']]
            result_df_op = result_df_op.append(rslt_df3)
        # else:
        #     print("Not in Slot")
    elif row == 'df4':
        if str(mask4[0]) == 'True' or str(mask4[1]) == 'True' or str(mask4[2]) == 'True':
            oup_df = df.loc[df['CASE'] == 'df4']
            rslt_df4 = oup_df[['FLOOR', 'ROOM_NO', 'MAX_NO']]
            result_df_op = result_df_op.append(rslt_df4)
            #rslt_df.append(rslt_df)
        # else:
        #     print("Not in Slot")
    elif row == 'df5':
        if str(mask5[0]) == 'True' or str(mask5[1]) == 'True':
            oup_df = df.loc[df['CASE'] == 'df5']
            rslt_df5 = oup_df[['FLOOR', 'ROOM_NO', 'MAX_NO']]
            result_df_op = result_df_op.append(rslt_df5)
        # else:
        #     print("Not in Slot")
    elif row == 'df6':
        if str(mask6[0]) == 'True' or str(mask6[1]) == 'True' or str(mask6[2]) == 'True':
            oup_df = df.loc[df['CASE'] == 'df6']
            rslt_df6 =oup_df[['FLOOR', 'ROOM_NO','MAX_NO']]
            result_df_op = result_df_op.append(rslt_df6)
            #rslt_df.append(rslt_df)
            #print(rslt_df)
        # else:
        #     print("Not in Slot")
    else:
        print ('Conference Room Not Available')


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
