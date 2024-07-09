from SublimeLinter.lint import PythonLinter, util


class Bandit(PythonLinter):
    cmd = ("bandit", "${args}", "-n", "1", "-f", "txt", "-")
    regex = (
        r"^>>\sIssue:\s\[(?P<code>[B]\d+):.+\]\s(?P<message>.+)$\r?\n"
        r"^.*Severity:\s(?:(?P<error>High)|(?P<warning>(Medium|Low))).*$\r?\n"
        r"(.*\r?\n)*^.*Location:.*?:(?P<line>\d+)(:\d+)?$\r?\n"
    )
    multiline = True
    error_stream = util.STREAM_BOTH
    defaults = {"selector": "source.python", "--tests,": "", "--skips,": ""}
