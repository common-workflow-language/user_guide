import csv
import os
import re
import shlex
import subprocess
import sys

from pathlib import Path

from docutils.parsers.rst import directives
from sphinx.directives import code

""""
Patched version of https://github.com/sphinx-contrib/sphinxcontrib-runcmd
with default values to avoid having to re-type in every page. Also
prepends commands with a value (``$``), see https://github.com/invenia/sphinxcontrib-runcmd/issues/1.
Finally, it also checks if the command is ``cwltool``, and if then
tries to remove any paths from the command-line (not the logs).
"""

__version__ = "0.2.0"

# CONSTANTS
RE_SPLIT = re.compile(r"(?P<pattern>.*)(?<!\\)/(?P<replacement>.*)")


# These classes were in the .util module of the original directive.
class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton("SingletonMeta", (object,), {})):
    pass


class CMDCache(Singleton):
    cache = {}
    exclude_cache_cmd = {hash("cat output.txt")}

    def get(self, cmd, working_directory):
        h = hash(cmd)
        if h in self.exclude_cache_cmd:
            return run_command(cmd, working_directory)
        elif h in self.cache:
            return self.cache[h]
        else:
            result = run_command(cmd, working_directory)
            self.cache[h] = result
            return result


def run_command(command, working_directory):
    true_cmd = shlex.split(command)
    try:
        # The subprocess Popen function takes a ``cwd`` argument that
        # conveniently changes the working directory to run the command.
        #
        # We also patched the stderr to redirect to STDOUT,
        # so that stderr and stdout appear in order, as you would see in
        # a terminal.
        #
        # Finally, note that ``cwltool`` by default emits ANSI colors in the
        # terminal, which are harder to be parsed and/or rendered in Sphinx.
        # For that reason, we define --disable-color in the CWLTOOL_OPTIONS
        # environment variable, which is used by ``cwltool``.
        env = os.environ
        cwl_options = set(env.get('CWLTOOL_OPTIONS', '').split(' '))
        cwl_options.add('--disable-color')
        env['CWLTOOL_OPTIONS'] = ' '.join(cwl_options)
        subp = subprocess.Popen(
            true_cmd,
            cwd=working_directory,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
    except Exception as e:
        out = ""
        err = e
    else:
        out, err = subp.communicate()
        encoding = sys.getfilesystemencoding()
        out = out.decode(encoding, "replace").rstrip()
        # The stderr is now combined with stdout.
        # err = err.decode(encoding, "replace").rstrip()

    if err and err != "":
        print("Error in runcmd: {}".format(err))
        out = "{}\n{}".format(out, err)

    return out


class RunCmdDirective(code.CodeBlock):
    has_content = False
    final_argument_whitespace = False
    required_arguments = 1
    optional_arguments = 99

    option_spec = {
        # code.CodeBlock option_spec
        "linenos": directives.flag,
        "dedent": int,
        "lineno-start": int,
        "emphasize-lines": directives.unchanged_required,
        "caption": directives.unchanged_required,
        "class": directives.class_option,
        "name": directives.unchanged,
        # RunCmdDirective option_spec
        "syntax": directives.unchanged,
        "replace": directives.unchanged,
        "prompt": directives.flag,
        "dedent-output": int,
        "working-directory": directives.unchanged
    }

    def run(self):
        # Grab a cache singleton instance
        cache = CMDCache()

        # The examples in our User Guide are stored in ``src/_includes/cwl``.
        # For convenience, instead of including that in every command, we
        # allow the directive to receive a working directory, so that we
        # change to that working directory before running the desired command.
        # The working directory is omitted from the final output.
        working_directory = self.options.get('working-directory', 'src/_includes/cwl/')
        if working_directory == '':
            # subprocess default value, so that we can disable it if needed.
            working_directory = None
        else:
            # You can run Sphinx from the root directory, with `make watch`
            # for instance, or from the src directory (RTD does that).
            working_directory_path = Path(working_directory)
            if not working_directory_path.exists() and str(working_directory_path).startswith('src/'):
                working_directory = Path(working_directory[4:])

        # Get the command output
        command = " ".join(self.arguments)
        output = cache.get(command, working_directory)

        # Grab our custom commands
        syntax = self.options.get("syntax", "bash")
        replace = self.options.get("replace", '')
        reader = csv.reader([replace], delimiter=",", escapechar="\\")
        # prompt = "prompt" in self.options
        # We patched this so that the prompt is displayed by default, similar
        # to how ``{code-block} console`` works.
        prompt = True
        dedent_output = self.options.get("dedent-output", 0)

        # Dedent the output if required
        if dedent_output > 0:
            output = "\n".join([x[dedent_output:] for x in output.split("\n")])

        # Add the prompt to our output if required
        if prompt:
            output = "$ {}\n{}".format(command, output)

        # Do our "replace" syntax on the command output
        for items in reader:
            for regex in items:
                if regex != "":
                    match = RE_SPLIT.match(regex)
                    p = match.group("pattern")
                    # Let's unescape the escape chars here as we don't need them to be
                    # escaped in the replacement at this point
                    r = match.group("replacement").replace("\\", "")
                    output = re.sub(p, r, output)

        # Note: Sphinx's CodeBlock directive expects an array of command-line
        #       output lines: https://github.com/sphinx-doc/sphinx/blob/c51a88da8b7b40e8d8cbdb1fce85ca2346b2b59a/sphinx/directives/code.py#L114
        #       But the runcmd original code was simply wrapping a string
        #       containing \n in the text as a one-element array, e.g.
        #       ["cwltool --debug ...\ncwltool Version..."].
        #       That caused the output to be correctly rendered, but the
        #       emphasize-lines directive parameter to fail if the lines were
        #       anything greater than 0 (as the self.content array had 1 elem).
        #       See: https://github.com/common-workflow-language/user_guide/issues/269
        output = output.split("\n")

        # Set up our arguments to run the CodeBlock parent run function
        self.arguments[0] = syntax
        self.content = output
        node = super(RunCmdDirective, self).run()

        return node


def setup(app):
    app.add_directive("runcmd", RunCmdDirective)

    return {"version": __version__}
