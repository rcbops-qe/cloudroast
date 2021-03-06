"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from cloudroast.stacktach.fixtures import StackTachComputeIntegration,\
    StackTachTestAssertionsFixture


class StackTachDBCreateServerTests(StackTachComputeIntegration,
                                   StackTachTestAssertionsFixture):
    """
    @summary: With Server Create, test the entries created in StackTach DB.
    """
    @classmethod
    def setUpClass(cls):
        cls.create_server()
        cls.stacktach_events_for_server(server=cls.created_server)

    def test_launch_entry_on_create_server_response(self):
        """
        Verify the Launch parameters are being returned in the initial response
        of Server Creation
        """
        self.validate_attributes_in_launch_response()

    def test_launch_entry_fields_on_create_server_response(self):
        """
        Verify that the Launch entry will have all expected fields
        after Server Creation
        """
        self.validate_launch_entry_field_values(server=self.created_server)

    def test_no_delete_entry_on_create_server_response(self):
        """Verify that there is no delete entry on a newly created server"""
        self.validate_no_deletes_entry_returned()

    def test_no_exist_entry_on_create_server_response(self):
        """Verify that there is no exist entry on a newly created server"""

        self.validate_no_exists_entry_returned()
