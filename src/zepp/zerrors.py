
class EPPError(Exception):
    code = -1
    message = 'Unknown error'

    def __init__(self, message, code=-1):
        self.code = code
        self.message = message

    def __str__(self):
        return '[%s] %s' % (self.code, self.message)


class EPPConnectionFailed(EPPError):
    pass


class EPPResponseFailed(EPPError):
    pass


class EPPBadResponse(EPPError):
    pass


class EPPCommandFailed(EPPError):
    pass


class EPPCommandInvalid(EPPError):
    pass
