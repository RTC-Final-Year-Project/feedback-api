import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.main import create_app

app = create_app()

# This commands file allow you to create convenient CLI commands for testing controllers

# This command creates and initializes the database
# @app.cli.command("init", help="Creates and initializes the database")
# def initialize():
#     create_db(app)
#     print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("rule", help="Run specific rule tests")
@click.argument("rule", default="")
@click.argument("type", default="all")
def Rule_CK_tests_command(rule, type):
    if rule:
        rule = rule + "_"        
    if type == "unit":
        sys.exit(pytest.main(["-k", rule + "Unit_Tests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", rule + "Integration_Tests"]))
    else:
        sys.exit(pytest.main(["-k", rule]))

@test.command("rules", help="Run all rule tests")
@click.argument("type", default="all")
def Rule_CK_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "Unit_Tests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "Integration_Tests"]))
    else:
        sys.exit(pytest.main(["-k", "Tests"]))

@test.command("meta", help="Run meta rule tests")
def Rule_CK_tests_command():
    sys.exit(pytest.main(["-k", "Rules_Meta"]))    
    
    

app.cli.add_command(test)