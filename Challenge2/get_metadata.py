import requests
import json

def get_value(json_data, key):
  if isinstance(json_data, dict):
    for k, v in json_data.items():
      if k == key:
        return v
      else:
        val = get_value(v, key)
        if val is not None:
          return val
  elif isinstance(json_data, list):
    for item in json_data:
      val = get_value(item, key)
      if val is not None:
        return val
  else:
    return None

def get_azure_vm_metadata(subscriptionId, resourceGroupName, vmName, accessToken):
    url = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}?api-version=2023-07-01'
    headers = {'Authorization': f'Bearer {accessToken}'}
    response = requests.get(url, headers=headers)
    json_data = response.json()

    return json_data
    
if __name__ == "__main__":
    subscriptionId = "8cd81a6a-32c1-4c0d-858a-672a5fa6d0e3"
    resourceGroupName = "rg-test1"
    vmName = "VMFrontEnd"
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldC8iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83OTliNDY0NC1hOTc3LTQ1NjktOTQzNi05MWZjMGUwYjk5YWQvIiwiaWF0IjoxNjk4NjkyNTkwLCJuYmYiOjE2OTg2OTI1OTAsImV4cCI6MTY5ODY5NzczMiwiYWNyIjoiMSIsImFpbyI6IkFXUUFtLzhVQUFBQVlqZEVHUU0vTHJjcHhqMEZsOHpyTDN3c1g5akg2cldzVi8rQ1p0MDRKMVkwZW16b3kvZ0NvamRLM3FCbjR0R04reG9FNm81aVFadm1hMTc0dUVEcURTUDZsa1R5RzlBcUFYNXhMV3hPb2lWbmVVSzNvaUJEdVlkNE5GZDV6T1MxIiwiYWx0c2VjaWQiOiIxOmxpdmUuY29tOjAwMDM3RkZFMDcwN0I5NkUiLCJhbXIiOlsicHdkIl0sImFwcGlkIjoiYjY3N2MyOTAtY2Y0Yi00YThlLWE2MGUtOTFiYTY1MGE0YWJlIiwiYXBwaWRhY3IiOiIwIiwiZW1haWwiOiJha2FzaHRlbG90ZUBvdXRsb29rLmNvbSIsImZhbWlseV9uYW1lIjoiVGVsb3RlIiwiZ2l2ZW5fbmFtZSI6IkFrYXNoIiwiZ3JvdXBzIjpbIjhiMzdiYTgzLTRmOTktNGY3OS1hNGMwLTVmOGRmZmQ1NWM5OCJdLCJpZHAiOiJsaXZlLmNvbSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjIwMy4xOTQuMTA3LjI0IiwibmFtZSI6IkFrYXNoIFRlbG90ZSIsIm9pZCI6IjdmOGVlMDJlLTI3NjItNGQ1Ni05N2I5LWEwODc1OTc3NmY1OSIsInB1aWQiOiIxMDAzMjAwMzBCNDBERDE5IiwicmgiOiIwLkFTc0FSRWFiZVhlcGFVV1VOcEg4RGd1WnJVWklmM2tBdXRkUHVrUGF3ZmoyTUJQQ0FHYy4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJwNFNQdWpkMlBoVFFGejlXRGdreDQ1YXd2SVB2N3lLbHI1eVVNQkZIRnBFIiwidGlkIjoiNzk5YjQ2NDQtYTk3Ny00NTY5LTk0MzYtOTFmYzBlMGI5OWFkIiwidW5pcXVlX25hbWUiOiJsaXZlLmNvbSNha2FzaHRlbG90ZUBvdXRsb29rLmNvbSIsInV0aSI6IlhaOHZyWjZoVWt5ZkhycGZKQWdBQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjYyZTkwMzk0LTY5ZjUtNDIzNy05MTkwLTAxMjE3NzE0NWUxMCIsImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2FlIjoiMSIsInhtc190Y2R0IjoxNjk4Mzk4MDEzfQ.YM8n_IBwH7QSAUVMN9eFYAsOjbxlWxwcHbQwP-e3RBFVJ3qwICLqSnnh-0GQprXCykWKknLk5TdqEKWsHyw_AZ73_jAjYVS-EqCK80JnVZ7e7a22qEv7uCdc4po3lnwSd2J_mcS0VJ54zuwHgggwWEYcyGoC1biYGUx-yhXgx89FsTvheHX4ZpSxyUSC3kgoar00zWdlx55tkyWO6J756JPgoUVHk3WkaWWMkmo9N5yn1h8B2_51QdvRCb-BjdoFMDB1KK4Mn69BVcNhWLgfXQqStXY_S54Ee0l5fRzkgTCTmhI2aSkLRheDtJSmyVo-iaNs19cW6KwWjFe1u40dZw"
    key = None
    
    json_data = get_azure_vm_metadata(subscriptionId, resourceGroupName, vmName, access_token)
    
    print(json.dumps(json_data, indent=4))
    
    if key :
        value = get_value(json_data, key)
        print(value)
