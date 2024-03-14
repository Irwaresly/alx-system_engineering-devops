from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

# Replace with your actual API and APP keys
DD_API_KEY = "21a0b21a-6330-4bae-811c-72ac1521f015"
DD_APP_KEY = "2f2eda5f-5c97-4e6f-a872-ae15a82d977b"

configuration = Configuration()
configuration.api_key['apiKeyAuth'] = DD_API_KEY
configuration.api_key['appKeyAuth'] = DD_APP_KEY

with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    
    # List all hosts
    response = api_instance.list_hosts(filter="host:web-01")

    # Check if any hosts match the desired hostname
    if response.total_returned > 0:
        print(f"Host web-01 found in Datadog!")
        for host in response.host_list:
            print(f"Host ID: {host.id}, Name: {host.name}, Alias: {host.alias}")
    else:
        print("Host web-01 not found in Datadog.")
