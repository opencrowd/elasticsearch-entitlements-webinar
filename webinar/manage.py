#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    import logging
    logging.getLogger().setLevel(logging.INFO)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webinar.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
