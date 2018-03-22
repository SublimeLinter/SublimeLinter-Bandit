from SublimeLinter.lint import PythonLinter, util


class Bandit(PythonLinter):
    cmd = ('bandit', '${args}', '-n', '1', '-f', 'txt', '-')
    regex = (
        r'^>>\sIssue:\s\[(?P<code>[B]\d+):.+\]\s(?P<message>.+)$\r?\n'
        r'^.*Severity:\s(?:(?P<error>High)|(?P<warning>(Medium|Low))).*$\r?\n'
        r'^.*Location:.*:(?P<line>\d+)$\r?\n'
    )
    multiline = True
    error_stream = util.STREAM_BOTH
    defaults = {
        'selector': 'source.python',
        '--tests,': '',
        '--skips,': ''
    }

    def split_match(self, match):
        """
        Return the components of the error message.

        We override this to add the error code as part of the message.
        """
        match, line, col, error, warning, message, near = super(
            self.__class__, self).split_match(match)

        if match:
            code = match.group('code')
            if error:
                error = code
            if warning:
                warning = code

        return match, line, col, error, warning, message, near
