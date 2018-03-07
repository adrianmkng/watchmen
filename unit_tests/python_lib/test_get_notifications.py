# Copyright 2017 Insurance Australia Group Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import python_lib.get_notifications as notifications

def test_get_notification_email():
    assert notifications.get_notification_email()

def test_get_notification_slack():
    assert notifications.get_notification_slack()

def test_get_slack_channel_hook_url():
    assert notifications.get_slack_channel_hook_url()
