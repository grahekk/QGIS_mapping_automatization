#Step 1: Fetch and Export System Paths & OS Environment Variables from QGIS Python Console

import sys
import pandas as pd
paths = sys.path
df = pd.DataFrame({'paths':paths})
df.to_csv('./qgis_sys_paths.csv', index=False)

import os
import json
env = dict(os.environ)
rem = ['SECURITYSESSIONID', 'LaunchInstanceID', 'TMPDIR']
_ = [env.pop(r, None) for r in rem]
with open('./qgis_env.json', 'w') as f:
    json.dump(env, f, ensure_ascii=False, indent=4)

from platform import python_version
print(python_version())
