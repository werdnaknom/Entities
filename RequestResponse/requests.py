import collections


class RequestObject(object):

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class InvalidRequestObject(RequestObject):
    '''
    Can be converted to a "False" boolean for request validation.
    Contains validation errors to track why the request was invalid
    '''
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter,
                            'message': message})

    def has_errors(self):
        return len(self.errors) > 0

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__


class ValidRequestObject(RequestObject):
    '''
    Valid request object that can be a "True" boolean for request validation
    methods must be overridden by children or raises NotImplementedError
    '''

    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError


class ListRequestObject(ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return ListRequestObject(filters=adict.get('filters', None))


class UpdatePickleRequestObject(ListRequestObject):
    pass
