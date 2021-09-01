from c7n_ibmcloud.query import QueryResourceManager, TypeInfo
from c7n_ibmcloud.provider import resources
from c7n.utils import local_session
from c7n.utils import type_schema
from c7n.filters import Filter
from c7n.filters import AgeFilter


@resources.register('server')
class VirtualServer(QueryResourceManager):
    class resource_type(TypeInfo):
        enum_spec = ('search', {'query':'type:volume AND family:is'}, {'fields':['*']}, {'limit':10})
        id = 'id'
        name = 'name'

        set_server_metadata = "set_server_metadata"
        delete_server_metadata = "delete_server_metadata"
        add_server_tag = "add_server_tag"
        set_server_tag = "set_server_tag"
        delete_server_tag = "delete_server_tag"

        default_report_fields = ['id', 'name', 'status', 'tenant_id']
