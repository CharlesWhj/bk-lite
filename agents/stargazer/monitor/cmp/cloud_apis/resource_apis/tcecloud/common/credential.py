#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from monitor.cmp.cloud_apis.resource_apis.tcecloud.common.exception.tce_cloud_sdk_exception import TceCloudSDKException


class Credential(object):
    def __init__(self, secretId, secretKey, token=None):
        """Tce Cloud Credentials.

        Access https://console.cloud.tce.com/cam/capi to manage your
        credentials.

        :param secretId: The secret id of your credential.
        :type secretId: str
        :param secretKey: The secret key of your credential.
        :type secretKey: str
        :param token: The federation token of your credential, if this field
                      is specified, secretId and secretKey should be set
                      accordingly, see: https://cloud.tce.com/document/product/598/13896
        """
        if secretId is None or secretId.strip() == "":
            raise TceCloudSDKException("InvalidCredential", "secret id should not be none or empty")
        if secretId.strip() != secretId:
            raise TceCloudSDKException("InvalidCredential", "secret id should not contain spaces")
        self.secretId = secretId

        if secretKey is None or secretKey.strip() == "":
            raise TceCloudSDKException("InvalidCredential", "secret key should not be none or empty")
        if secretKey.strip() != secretKey:
            raise TceCloudSDKException("InvalidCredential", "secret key should not contain spaces")
        self.secretKey = secretKey

        self.token = token
