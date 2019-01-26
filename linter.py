from SublimeLinter.lint import PythonLinter, util


class Bandit(PythonLinter):
    cmd = ('bandit', '${args}', '-n', '1', '-f', 'custom',
           '--msg-template', '[{line}][{test_id}][{severity}] {msg}', '-')
    regex = (r'^\[(?P<line>\d+)\]'
             r'\[(?P<code>[B]\d+)\]'
             r'\[(?:(?P<error>HIGH)|(?P<warning>(MEDIUM|LOW)))\]'
             r'\s(?P<message>.+)$')
    error_stream = util.STREAM_STDOUT
    defaults = {
        'selector': 'source.python',
        '--tests,': '',
        '--skips,': ''
    }
