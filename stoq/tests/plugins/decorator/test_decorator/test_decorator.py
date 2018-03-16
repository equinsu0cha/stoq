#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Overview
========

Test stoQ decorator

"""

from stoq.plugins import StoqDecoratorPlugin


class TestDecorator(StoqDecoratorPlugin):

    def __init__(self):
        super().__init__()

    def activate(self, stoq):
        self.stoq = stoq

        super().activate()

    def decorate(self, results, **kwargs):
        """
        Test stoQ decorator

        :param bytes payload: Combined stoQ results to decorate
        :param **kwargs kwargs: Additional attributes (unused)

        :returns: Decorated results

        """

        return results
