#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import importlib
import logging
import pkgutil
from typing import Any, Dict

import click
from colorama import Fore, Style
from flask import current_app
from flask.cli import FlaskGroup, with_appcontext

from superset import app, appbuilder, cli, security_manager
from superset.cli.lib import normalize_token
from superset.extensions import db

logger = logging.getLogger(__name__)


@click.group(
    cls=FlaskGroup,
    context_settings={"token_normalize_func": normalize_token},
)
@with_appcontext
def superset() -> None:
    """This is a management script for the Superset application."""

    @app.shell_context_processor
    def make_shell_context() -> Dict[str, Any]:
        return dict(app=app, db=db)


# add sub-commands
for load, module_name, is_pkg in pkgutil.walk_packages(
    cli.__path__, cli.__name__ + "."
):
    module = importlib.import_module(module_name)
    for attribute in module.__dict__.values():
        if isinstance(attribute, click.core.Command):
            superset.add_command(attribute)


@superset.command()
@with_appcontext
def init() -> None:
    """Inits the Superset application"""
    appbuilder.add_permissions(update_perms=True)
    security_manager.sync_role_definitions()


@superset.command()
@with_appcontext
@click.option("--verbose", "-v", is_flag=True, help="Show extra information")
def version(verbose: bool) -> None:
    """Prints the current version number"""
    print(Fore.BLUE + "-=" * 15)
    print(
        Fore.YELLOW
        + "Superset "
        + Fore.CYAN
        + "{version}".format(version=app.config["VERSION_STRING"])
    )
    print(Fore.BLUE + "-=" * 15)
    if verbose:
        print("[DB] : " + "{}".format(db.engine))
    print(Style.RESET_ALL)


@superset.command("create-superadmin")
@click.option("--username", default="admin", prompt="Username")
@click.option("--firstname", default="admin", prompt="User first name")
@click.option("--lastname", default="user", prompt="User last name")
@click.option("--cn_name", default="cn_name", prompt="Chinese name")
@click.option("--email", default="admin@fab.org", prompt="Email")
@click.password_option()
@with_appcontext
def create_admin(username, firstname, lastname, cn_name, email, password):
    """
        Creates an admin user
    """
    AUTH_OID = 0
    AUTH_DB = 1
    AUTH_LDAP = 2
    AUTH_REMOTE_USER = 3
    AUTH_OAUTH = 4

    auth_type = {
        AUTH_DB: "Database Authentications",
        AUTH_OID: "OpenID Authentication",
        AUTH_LDAP: "LDAP Authentication",
        AUTH_REMOTE_USER: "WebServer REMOTE_USER Authentication",
        AUTH_OAUTH: "OAuth Authentication",
    }
    click.echo(
        click.style(
            "Recognized {0}.".format(
                auth_type.get(current_app.appbuilder.sm.auth_type, "No Auth method")
            ),
            fg="green",
        )
    )
    user = current_app.appbuilder.sm.find_user(username=username)
    if user:
        click.echo(click.style(f"Error! User already exists {username}", fg="red"))
        return
    user = current_app.appbuilder.sm.find_user(email=email)
    if user:
        click.echo(click.style(f"Error! User already exists {username}", fg="red"))
        return
    role_admin = current_app.appbuilder.sm.find_role(
        current_app.appbuilder.sm.auth_role_admin
    )
    user = current_app.appbuilder.sm.add_user(
        username, firstname, lastname, email, role_admin, True, cn_name, password
    )
    if user:
        click.echo(click.style("Admin User {0} created.".format(username), fg="green"))
    else:
        click.echo(click.style("No user created an error occured", fg="red"))

