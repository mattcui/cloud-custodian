from c7n_ibmcloud.query import QueryResourceManager, TypeInfo
from c7n_ibmcloud.provider import resources
from c7n.utils import local_session
from c7n.utils import type_schema
from c7n.filters import Filter
from c7n.filters import AgeFilter


@resources.register('virtual_server')
class VirtualServer(QueryResourceManager):
    class resource_type(TypeInfo):
        enum_spec = ('search', {'query':'type:instance AND family:is', 'fields':['*'], 'limit':10})
        service = 'ibmcloud.vpc.instance'
        id = 'resource_id'

        default_report_fields = ['doc.id', 'name', 'doc.crn', 'doc.status', 'region']
