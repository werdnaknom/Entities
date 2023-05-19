import logging

from RequestResponse.responses import ResponseFailure, ResponseSuccess, Responses
from RequestResponse.requests import RequestObject

logging.basicConfig(format='[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)s] : %(message)s',
                    level=logging.DEBUG)

LOG_LEVEL = logging.DEBUG


class UseCase(object):
    _name: str = "UseCase"

    @classmethod
    def log(cls):
        logging_handler = logging.getLogger(cls.__name__)
        return logging_handler

    def execute(self, request_object: RequestObject) -> Responses:
        '''
        execute validates the request object.  If valid, tries "process
        request".  If invalid, returns Response failure.

        Do not modify execute in child classes
        '''
        self.log().debug("Starting execute")
        if not request_object:
            self.log().debug("test")
            return ResponseFailure.build_from_invalid_request_object(
                request_object)

        try:
            return self.process_request(request_object)
        except Exception as exc:
            raise exc
            return ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc)))

    def process_request(self, request_object: RequestObject) -> Responses:
        '''
        Process request is the actual function that is run when a usecase is
        executed.

        This function should be modified in child classes

        Returns:: Response object, either success or failure

        '''
        raise NotImplementedError(
            "process_request() not implemented by UseCase class"
        )
