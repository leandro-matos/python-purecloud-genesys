import PureCloudPlatformClientV2, os

apiclient = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token(os.environ['client_id'], os.environ['client_secret'])
authApi = PureCloudPlatformClientV2.AuthorizationApi(apiclient)
print(authApi.get_authorization_permissions())