import requests
import pandas as pd
access_token='Personal Access Token'
df = pd.DataFrame()
n = 1
while requests.get(f'https://api.github.com/repos/hashicorp/consul/contrbutions?page={n}&per_page=100&access_token={access_token}').json():
    info_url = f'https://api.github.com/repos/hashicorp/consul/contributions?page={n}&per_page=100&access_token={access_token}'
    commit_info = requests.get(info_url).json()
    print(len(commit_info))
    dm = pd.DataFrame(commit_info)
    df = pd.concat([df, dm], ignore_index=True)
    n = n + 1

df.to_excel(f'hello1.xlsx',
            sheet_name='Test')

#df.reset_index(drop=True, inplace=True)
