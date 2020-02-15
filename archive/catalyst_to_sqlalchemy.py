#!/usr/bin/env python3
#########################################################################
# Generate SQLAlchemy table definition code from Catalyst schemas(?)
# Authors: Chris Hodapp
# 2020-01-18, Hive13 Cincinnati
#########################################################################

"""This script parses YAML files which express a database schema for
Perl's Catalyst::Model::DBIC::Schema (?), and tries to generate Python
code with Table and Column definitions for SQLAlchemy.

It depends on PyYAML for parsing.

Generated code depends on 'sqlalchemy' and 'sqlalchemy-citext'
packages.

"""

# https://www.postgresql.org/docs/9.1/citext.html
# Perhaps just use below?
# https://github.com/mahmoudimus/sqlalchemy-citext

import json
import time
import sys

import yaml

# Mapping from Catalyst schema datatype to a SQLAlchemy type:
datatypes = {
    "integer":                  "sqlalchemy.Integer",
    "boolean":                  "sqlalchemy.Boolean",
    "text":                     "sqlalchemy.Text",
    "bigint":                   "sqlalchemy.BigInteger",
    "char":                     "sqlalchemy.CHAR",
    "character":                "sqlalchemy.CHAR",
    "varchar":                  "sqlalchemy.VARCHAR",
    "date":                     "sqlalchemy.Date",
    "timestamp with time zone": "sqlalchemy.DateTime(timezone=True)",
    "uuid":                     "sqlalchemy.dialects.postgresql.UUID",
    "character varying":        "sqlalchemy.VARCHAR",
    "inet":                     "sqlalchemy.dialects.postgresql.INET",
    "bytea":                    "sqlalchemy.dialects.postgresql.BYTEA",
    "jsonb":                    "sqlalchemy.dialects.postgresql.JSONB",
    "citext":                   "citext.CIText",
}

# Just here for debugging at the moment...
unknown = set()

def field2column(fieldname, field):
    """Returns code for a Column definition from a field.

    Inputs:
    fieldname -- Field/column name
    field -- Field dictionary from Catalyst schema.

    Output:
    String with a Python expression for sqlalchemy.Column
    """
    options = []
    if field["is_primary_key"]:
        options.append("primary_key=True")
    if not field["is_nullable"]:
        options.append("nullable=False")
    if field["is_unique"]:
        options.append("unique=True")
    if options:
        options = [""] + options
    opt_str = ", ".join(options)
    t_perl = field["data_type"]
    if t_perl in datatypes:
        t = datatypes[t_perl]
    else:
        t = "(unknown type '{}')".format(t_perl)
        unknown.add(t_perl)
    return "sqlalchemy.Column('{}', {}{}),".format(fieldname, t, opt_str)

def yaml2python(fname):
    """Generates Python code from a YAML file for a Catalyst schema.

    The result is a generator of strings; each string should be taken
    as a line of Python code.

    Inputs:
    fname -- Input YAML filename
    """
    with open(fname) as f:
        # This .yml appears to include 'blessed' Perl objects and
        # PyYAML doesn't want to touch them.  The
        # add_multi_constructor below is to shut it up.
        yaml.add_multi_constructor('', lambda loader, suffix, node: None)
        y = yaml.unsafe_load(f)
    yield("#" * 70)
    yield("# Input filename: {}".format(fname))
    yield("# Generated on {} by {}".format(time.asctime(), sys.argv[0]))
    yield("# Begin automatically generated code:")
    yield("#" * 70)
    yield("import sqlalchemy")
    yield("import sqlalchemy.dialects.postgresql")
    yield("import citext")
    yield("")
    yield("metadata = sqlalchemy.MetaData()")
    yield("")
    for tablename, table in y["schema"]["tables"].items():
        yield("{} = sqlalchemy.Table('{}', metadata,".format(tablename, tablename))
        for fieldname, field in table["fields"].items():
            yield("    {}".format(field2column(fieldname, field)))
        yield(")")
        yield("")
    if unknown:
        yield("# Types still unknown: {}".format(unknown))
    yield("#" * 70)
    yield("# End automatically generated code")
    yield("#" * 70)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <input YAML filename>".format(sys.argv[0]))
        print("Generates Python code from a Catalyst schema YAML file")
    else:
        for line in yaml2python(sys.argv[1]):
            print(line)
