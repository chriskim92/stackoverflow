def nearest_time_one_min_ago(df,
                             current_timestamp):  # current_timestamp would be applied to individual peak in the overall function.

    df = df.reset_index(drop=True)
    key_of_data = []
    one_min_ago_data_list = []
    two_min_ago_data_list = []
    peak_time = []
    peak_time_list = []
    dataframe = []

    ts_index = df.columns.get_loc("Timestamp")
    val_index = df.columns.get_loc("Temperature")

    for i in range(2, len(df.index) - 2):
        if (df.loc[i, 'Temperature'] > df.loc[i - 1, 'Temperature']) & (
                df.loc[i, 'Temperature'] > df.loc[i + 1, 'Temperature']):
            peak_time = df.loc[i, 'Timestamp']
            peak_temp = df.loc[i, 'Temperature']

            time_one_min_ago = df.loc[i, 'Timestamp'] - datetime.timedelta(minutes=1)
            time_two_min_ago = df.loc[i, 'Timestamp'] - datetime.timedelta(minutes=2)

            # left_timestamp = df.loc[i-200:i-1, 'Timestamp'] # Take the past 200 values from the current data point.
            left_timestamp = df.loc[i - 200:i - 1]
            # no columnar selection

            # right_timestamp = df.loc[i+1:i+200, 'Timestamp'] # Take the next 200 values from the current data point.
            right_timestamp = df.loc[i + 1:i + 200]
            # no columnar selection

            # key_of_data = min(np.hstack([left_timestamp, right_timestamp]) , key=lambda x: abs(x - peak_time)) # original solution
            one_min_ago_data = min(left_timestamp.append(right_timestamp).to_numpy(),
                                   key=lambda x: abs(x[ts_index] - time_one_min_ago))
            two_min_ago_data = min(left_timestamp.append(right_timestamp).to_numpy(),
                                   key=lambda x: abs(x[ts_index] - time_two_min_ago))

            #             one_min_ago_data_value = min(left_timestamp.append(right_timestamp).to_numpy() ,
            #                                          key=lambda x: abs(x - time_one_min_ago))[2]
            #             two_min_ago_data_value = min(left_timestamp.append(right_timestamp).to_numpy() ,
            #                                          key=lambda x: abs(x - time_two_min_ago))[2]
            one_min_ago_data_value = one_min_ago_data[val_index]
            two_min_ago_data_value = two_min_ago_data[val_index]

            one_min_ago_data_list.append(one_min_ago_data)  # When append no need to assign.
            two_min_ago_data_list.append(two_min_ago_data)
            peak_time_list.append(peak_time)

            dataframe.append([peak_time, peak_temp, one_min_ago_data, two_min_ago_data, one_min_ago_data_value])

    dataframe1 = pd.DataFrame(dataframe, columns=['peak_time', 'peak_temp', 'one_min_ago_data', 'two_min_ago_data',
                                                  'one_min_ago_data_value'])

    # df.columns.get_loc("value")

    print(len(one_min_ago_data_list), len(two_min_ago_data_list), len(peak_time_list))

    return dataframe1
