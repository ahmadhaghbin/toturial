import pandas as pd
import matplotlib.pyplot as plt

def read_excel_data(file_name):
    data_frame = pd.read_excel(file_name)
    return data_frame


if __name__ == '__main__':                 #read phython files
    file_name = "WindSpeed.xlsx"
    data_frame = read_excel_data(file_name)
#    print(data)
    wind_speed = data_frame ['Wind Speed'].values[1:]  #extract the values from first column
    plt.plot(wind_speed) #plot command
    plt.xlabel('Time [s]')
    plt.ylabel('Wind Speed [m/s]')
    plt.title('Wind Speed Profile')
    plt.ylim (0,max(wind_speed)+5)
    plt.xlim (0,len(wind_speed))
    #plt.show()          #print the figure
    plt.savefig('WS.png')
    #print(wind_speed)
    #columns = list(data.columns)
    # wind_speed = list(data["Wind Speed"])
#
#     data2 = data.loc[14:6,"Wind Speed":"wd68"].values
#     print(data2)
