from kubernetes import client, config, utils
from sys import argv

def main():
    config.load_incluster_config()
    k8s_client = client.ApiClient()

    for arg in argv[1:]:
        yaml_file = arg
    	utils.create_from_yaml(k8s_client, yaml_file, verbose=True)

if __name__ == "__main__":
    main()
