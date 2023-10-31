This folder contains the following challenge

Challenge #2

We need to write code that will query the meta data of an instance within AWS and provide a json formatted output. The choice of language and implementation is up to you. Bonus Points The code allows for a particular data key to be retrieved individually Hints · Aws Documentation (https://docs.aws.amazon.com/) · Azure Documentation (https://docs.microsoft.com/en-us/azure/?product=featured) · Google Documentation (https://cloud.google.com/docs)

Solution:
A python code created to fetch the metadata of given Virtual Machine.
The code following parameters as input:
    1. subscriptionId 
    2. resourceGroupName 
    3. vmName 
    4. accessToken (Can be retrieved from Azure console by command 'Get-AzAccessToken')
    5. data key to be retrieved (Optional)

A sample response is stored in response.json
