import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def read_excel_data(file_name):
    data_frame = pd.read_excel(file_name)
    return data_frame

# @@@@ eXTRACT FROM eXCEL in form of dataframe

if __name__ == '__main__':             #read phython files
    file_name = "WindSpeed.xlsx"
    data_frame = read_excel_data(file_name)
    #print(data_frame)
    wind_speed = data_frame ['Wind Speed'].values[1:]  #extract the values from first column- copy and paste the same (Wind Speede is copied from excel)
    electric_power = data_frame ['pow_hv'].values[1:]
    #x = round(np.mean(wind_speed[:601]), 2)
    #print(x)
    #exit()


# @@@@@@ How to plot

    # plt.plot(wind_speed)
    # plt.xlabel('Time [s]')
    # plt.ylabel('Wind Speed [m/s]')
    # plt.title('Wind Speed Profile')
    # plt.ylim (0,max(wind_speed)+5)    #to limit the y axis by adding 5 units
    # plt.xlim (0,len(wind_speed))      #to limit the lentgh of the x axis

    # plt.show()                       #print the figure
    # plt.savefig('WS.png')            #To save as a pictur file

# @@@@@@ How to smaple from second into 10 minute
ten_min_averageWS=[]
slice_size= int (len(wind_speed)/600)

for i in range (slice_size):

    y = wind_speed[600*i:600*(i+1)]
    average= round(np.mean(y),1)
    ten_min_averageWS.append(average)
#same process for electric power
ten_min_averageEP=[]
slice_size= int (len(electric_power)/600)

for i in range (slice_size):

    y = electric_power[600*i:600*(i+1)]
    average= round(np.mean(y),1)
    ten_min_averageEP.append(average)

#@@@@Single plot
# plt.plot(ten_min_averageWS)
# plt.xlabel('Time [min]')
# plt.ylabel('Wind Speed [m/s]')
# plt.title('Wind Speed Profile adjusted to 10 min data')
# plt.ylim (0,max(ten_min_averageWS)+5)
# plt.xlim (0,len(ten_min_averageWS))
# plt.grid(b=True, which='major', color='#666666', linestyle='--')
# plt.legend(['Wind Speed'])
#
# plt.show()

#@@@@ Multi line plot

fig, ax = plt.subplots()
plt.plot(ten_min_averageWS, '-r', label='Wind Speed')
plt.legend()
#ax.tick_params('vals', colors='r')

# Get second axis
ax2 = ax.twinx()
plt.plot(ten_min_averageEP, '-k', label='Electric Power')
plt.legend()
plt.grid()
plt.show()
#ax.tick_params('vals', colors='b')

# @@@@@@ How to average
 # average=np.mean(wind_speed)
 # print ( average )
