
import pandas as pd
import glob

## dataset 

def integration_xls(directory_path):
    ### multiple split files -> one file
    ### used in data directory

    file_paths = glob.glob(f"{directory_path}/*.xls")

    data_frames = []
    for file in file_paths:
        df = pd.read_excel(file)
        data_frames.append(df)

    merged_df = pd.concat(data_frames, ignore_index=True)

    file_name = directory_path.split('/')[-1]

    output_file = f"C:/Users/TAKO/Desktop/yanolja/data/tourAPI/{file_name}.xls"
    return merged_df.to_excel(output_file, index=False)


## API

def make_url_params(url):
    ### url -> params
    ### used in make API

    base_url = url.split('?')[0]
    params_li = url.split('?')[1]

    params_dict = {}
    for param in params_li.split('&'):
        key_, value_ = param.split("=")

        if all(48 <= ord(char) <= 57 for char in value_):
            params_dict[key_] = int(value_)
        else:
            params_dict[key_] = value_

    return base_url, params_dict


    