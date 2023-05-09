## A playbook to install and configure node_exporter with a self-signed SSL certificate and Basic Authentication

> **Note:** 
> This has been tested on Debian Bullseye & Sid. Results may vary on other distributions

All node_exporter hosts must be reachable from the prometheus hosts on port 9100.

Steps for getting up and running:

1. Open inventory.yaml and populate the node_exporters host group with hosts you want to install node_exporter on.

2. Add hosts you run Prometheus on to the prometheus host group. 

3. Install the bcrypt module for Python with `pip3 install bcrypt`.

4. Run the `gen_pass.py` script from the root of this folder to generate a hash from the password you'd like to use for basic authentication. This will populate `vars.yaml` for you with the specified password and the hashed version.

5. Open `vars.yaml` and modify to your needs (username and configuration directory). Note that `prom_config_dir` should lead to a folder where Prometheus will look for `prometheus.yaml`.

6. Open `files/prom_config.yaml` and modify to your liking. The part that this playbook will need to function is enclosed between two comment lines.

7. Run the playbook with
```
ansible-playbook -i inventory.yaml playbook.yaml -K
```

If all goes well, all your node_exporter hosts will be configured, your Prometheus config updated, and reloaded.