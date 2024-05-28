class OperationResponse:
    def __init__(self, operation_code, return_code, debug_message, parameters):
        self.operation_code = operation_code
        self.return_code = return_code
        self.debug_message = debug_message
        self.parameters = parameters