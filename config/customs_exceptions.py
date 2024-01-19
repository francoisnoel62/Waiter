import json


class ObjectDoesNotExistsException(Exception):
    def __init__(self, message="Object not found"):
        self.message = message
        super().__init__(self.message)

        def __str__(self):
            err = {
                'error': self.message,
            }
            return json.dumps(err, indent=4)
