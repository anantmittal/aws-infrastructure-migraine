from aws_infrastructure.tasks.collection import compose_collection
from invoke import Collection

import tasks.celery
import tasks.database
import tasks.database_tests
import tasks.dependencies
import tasks.flask
import tasks.helm
import tasks.helmfile
import tasks.terraform.dns
import tasks.terraform.ecr
import tasks.terraform.eip
import tasks.terraform.instance
import tasks.terraform_old.ecr
import tasks.terraform_old.eip
import tasks.terraform_old.instance

ns = Collection()

# Compose from database.py
compose_collection(ns, tasks.database.ns, name='database')
compose_collection(ns.collections['database'], tasks.database_tests.ns, name='tests')

# Compose from dependencies.py
compose_collection(ns, tasks.dependencies.ns, name='depend')

# Compose from helm.py
compose_collection(ns, tasks.helm.ns, name='helm')

# Compose from helmfile.py
compose_collection(ns, tasks.helmfile.ns, name='helmfile')

#
# A collection in each of development and production
#
ns_dev = Collection('dev')
ns_prod = Collection('prod')

# # Compose from celery.py
# compose_collection(
#     ns_dev,
#     tasks.celery.ns.collections['dev'],
#     name='flask',
# )
# compose_collection(
#     ns_prod,
#     tasks.celery.ns.collections['prod'],
#     name='flask',
# )

# Compose from flask.py
compose_collection(
    ns_dev,
    tasks.flask.ns.collections['dev'],
    name='flask',
)
compose_collection(
    ns_prod,
    tasks.flask.ns.collections['prod'],
    name='flask',
)

# Compose development and production
compose_collection(ns, ns_dev, name='dev')
compose_collection(ns, ns_prod, name='prod')

#
# Terraform infrastructure
#

ns_terraform = Collection('terraform')

compose_collection(ns_terraform, tasks.terraform.dns.ns, name='dns')
compose_collection(ns_terraform, tasks.terraform.ecr.ns, name='ecr')
compose_collection(ns_terraform, tasks.terraform.eip.ns, name='eip')
compose_collection(ns_terraform, tasks.terraform.instance.ns, name='instance')

ns.add_collection(ns_terraform, 'terraform')

#
# Old Terraform infrastructure
#

ns_terraform_old = Collection('terraform-old')

compose_collection(ns_terraform_old, tasks.terraform_old.ecr.ns, name='ecr')
compose_collection(ns_terraform_old, tasks.terraform_old.eip.ns, name='eip')
compose_collection(ns_terraform_old, tasks.terraform_old.instance.ns, name='instance')

ns.add_collection(ns_terraform_old, 'terraform-old')
