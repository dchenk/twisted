import sys
import os

try:
    # On Windows, stdout is not opened in binary mode by default,
    # so newline characters are munged on writing, interfering with
    # the tests.
    import msvcrt
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)  # type:ignore[attr-defined]  # noqa
except ImportError:
    pass


# Loop over each of the arguments given and print it to stdout
for arg in sys.argv[1:]:
    res = arg + chr(0)

    sys.stdout.buffer.write(
        res.encode(sys.getfilesystemencoding(), "surrogateescape")
    )
    sys.stdout.flush()