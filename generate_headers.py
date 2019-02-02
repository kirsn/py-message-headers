# -*- coding: utf-8 -*-

"""
Generate one or more headers files, by referring to the definitions from here: https://www.iana.org/assignments/message-headers/message-headers.xhtml
Save the csv files to the references folder, and run this generate function.
Run the `black` formatter on this package
The `headers` package contains the constants
"""

from __future__ import print_function

from collections import defaultdict
from csv import DictReader
from datetime import datetime as dtdt
import os

opj = os.path.join

CSV_NAME = "Header Field Name"
CSV_TEMPLATE = "Template"
CSV_PROTOCOL = "Protocol"
CSV_STATUS = "Status"
CSV_REFERENCE = "Reference"
CSV_HEADERS = [CSV_NAME, CSV_TEMPLATE, CSV_PROTOCOL, CSV_STATUS, CSV_REFERENCE]
IGNORE_STATUS = ["obsoleted", "deprecated"]

DEFINITION_FORMAT = '# %(status)s, %(reference)s\n%(const)s = "%(value)s"\n'
PACKAGE_IMPORT_FORMAT = "from %s import *"
PACKAGE_NAME = "headers"
MODULE_DOC = "# Generated on %s\n\n" % dtdt.now().isoformat()


def _constant(value):
    _const = value.replace("-", "_")
    return _const.upper()


def _references():
    return os.path.abspath(
        opj(os.path.dirname(os.path.realpath(__file__)), "references")
    )


def _package(name=""):
    _name = opj(PACKAGE_NAME, name)
    if not os.path.exists(_name):
        os.makedirs(_name)
    return _name


def _extract_definitions():
    _pth, _, _fls = os.walk(_references()).next()
    definitions = defaultdict(list)
    for _fl in _fls:
        with open(opj(_pth, _fl), "rb") as headers_csv:
            reader = DictReader(headers_csv, fieldnames=CSV_HEADERS)
            for row in reader:
                if row[CSV_STATUS] not in IGNORE_STATUS:
                    defn = DEFINITION_FORMAT % {
                        "const": _constant(row[CSV_NAME]),
                        "value": row[CSV_NAME],
                        "status": row[CSV_STATUS] or "standard",
                        "reference": row[CSV_REFERENCE],
                    }
                    definitions[row[CSV_PROTOCOL]].append(defn)

    return definitions


def _generate_modules(definitions):
    package_imports = []
    for _prot, _defns in definitions.iteritems():
        if _prot != "none":
            _protocol = _prot.lower()
            with open(opj(_package(), "%s.py" % _protocol), "wb") as hpy:
                hpy.write(MODULE_DOC)
                hpy.write("\n".join(_defns))
            print("Generate file %s" % _protocol)
            package_imports.append(PACKAGE_IMPORT_FORMAT % _protocol)

    return package_imports


def _generate_package(package_imports):
    with open(opj(_package(), "__init__.py"), "wb") as pkg:
        pkg.write(MODULE_DOC)
        pkg.write("\n".join(package_imports))


def generate():
    definitions = _extract_definitions()
    package_imports = _generate_modules(definitions)
    _generate_package(package_imports)


if __name__ == "__main__":
    generate()
