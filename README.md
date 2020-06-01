# EMC Unity API Testing

I'm just trying out the [storops](https://github.com/emc-openstack/storops) and figured I'd share
my work.

-Kyle



## Running the python script

Set the environment variables

```bash
export UNITY_SAN_IP=""
export UNITY_USER=""
export UNITY_PASSWORD=""
```

Create a virtualenv

```bash
virtualenv --python=python3 env/
source env/bin/activate
```

Install deps

```bash
pip install -r requirements.txt
```

Run the script

```bash
./unity_api_test.py
```
