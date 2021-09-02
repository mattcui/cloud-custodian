from c7n_ibmcloud.query import QueryResourceManager, TypeInfo
from c7n_ibmcloud.provider import resources
from c7n.utils import local_session
from c7n.utils import type_schema
from c7n.filters import Filter
from c7n.filters import AgeFilter


@resources.register('server')
class VirtualServer(QueryResourceManager):
    class resource_type(TypeInfo):
        enum_spec = ('search', {'query':'type:instance AND family:is'}, {'fields':['*']}, {'limit':10})
        id = 'doc.id'
        name = 'name'
        crn = 'doc.crn'
        status = 'doc.status'

        default_report_fields = ['id', 'name', 'crn', 'status']
