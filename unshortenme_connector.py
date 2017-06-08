
# --
# File: proofpoint_connector.py
#
# Copyright (c) Phantom Cyber Corporation, 2017
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

# Phantom imports
import phantom.app as phantom

import requests
from bs4 import BeautifulSoup
from HTMLParser import HTMLParseError

from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

requests.packages.urllib3.disable_warnings()

UNSHORTEN_ME_BASE_URL = 'https://unshorten.me/json/'


class UnshortenmeConnector(BaseConnector):
    def _make_rest_call(self, action_result, endpoint, params=None):
        url = UNSHORTEN_ME_BASE_URL + endpoint
        if not params:
            params = {}

        try:
            res = requests.get(url, params=params)
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            # a status code outside of the 200s occured
            res_text = res.text.replace('{', '{{').replace('}', '}}')
            message = ('Error response from server. Status code: {0}'
                       'Response: {1}').format(res.status_code, res_text)
            return action_result.set_status(phantom.APP_ERROR, message), None
        except requests.exceptions.RequestException as e:
            message = 'Error connecting to the url ({0})'.format(url)
            return (action_result.set_status(phantom.APP_ERROR, message, e),
                    None)

        content_type = res.headers.get('Content-Type', '')
        if 'html' not in content_type and 'json' not in content_type:
            # this API always returns text/html even with a JSON response
            res_text = res.text.replace('{', '{{').replace('}', '}}')
            message = 'Unexpected response from server: {0}'.format(res_text)
            return action_result.set_status(phantom.APP_ERROR, message), None

        try:
            data = res.json()
        except ValueError as e:
            try:
                soup = BeautifulSoup(res.test, 'html.parser')
                error_text = soup.text
                split_lines = error_text.splitlines()
                split_lines = [x.strip() for x in split_lines if x.strip()]
                error_text = '\n'.join(split_lines)
            except HTMLParseError as e:
                error_text = 'Cannot parse error details: {}'.format(e.msg)

            message = ('Error response from server. Status code: {0}'
                       'Response: \n{1}\n').format(res.status_code, error_text)
            return action_result.set_status(phantom.APP_ERROR, message), None

        if 'error' in data:
            message = 'API returned error: {0}'.format(data['error'])
            return action_result.set_status(phantom.APP_ERROR, message), data

        return phantom.APP_SUCCESS, data

    def _test_connectivity(self, param):
        action_result = self.add_action_result(ActionResult(param))

        url = 'goo.gl/IGL1lE'

        # Connect to the server
        ret_val, data = self._make_rest_call(action_result, url)

        if phantom.is_fail(ret_val):
            message = ('Test Connetivity failed. '
                       'Error: {0}'.format(action_result.get_message()))
            self.save_progress(message)
            return action_result.get_status()

        # Sanity check
        if data.get('resolved_url') != 'https://unshorten.me/':
            message = 'API returned invalid data.'
            return self.set_status_save_progress(phantom.APP_ERROR, message)

        message = 'Connection seccessful.'
        return self.set_status_save_progress(phantom.APP_SUCCESS, message)

    def _unshorten_url(self, param):
        action_result = self.add_action_result(ActionResult(param))
        url = param.get('url')

        if url.startswith('http://'):
            url = url[7:]
        elif url.startswith('https://'):
            url = url[8:]

        ret_val, data = self._make_rest_call(action_result, url)

        if data is not None:
            action_result.add_data(data)
        if phantom.is_fail(ret_val):
            return action_result.get_status()
        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, param):
        """Function that handles all the actions

        Args:

        Return:
            A status code
        """

        result = None
        action = self.get_action_identifier()

        if action == phantom.ACTION_ID_TEST_ASSET_CONNECTIVITY:
            result = self._test_connectivity(param)
        elif action == 'unshorten_url':
            result = self._unshorten_url(param)
        return result
