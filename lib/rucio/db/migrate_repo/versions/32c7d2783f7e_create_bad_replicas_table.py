# Copyright European Organization for Nuclear Research (CERN)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Authors:
# - Vincent Garonne, <vincent.garonne@cern.ch>, 2014
# - Cedric Serfon, <cedric.serfon@cern.ch>, 2015

"""create bad replicas table

Revision ID: 32c7d2783f7e
Revises: 384b96aa0f60
Create Date: 2015-02-13 16:22:05.154112

"""

# revision identifiers, used by Alembic.
revision = '32c7d2783f7e'
down_revision = '384b96aa0f60'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('bad_replicas',
                    sa.Column('scope', sa.String(25)),
                    sa.Column('name', sa.String(255)),
                    sa.Column('rse_id', sa.GUID()),
                    sa.Column('reason', sa.String(255)),
                    sa.Column('state', sa.String(1)),
                    sa.Column('account', sa.String(25)),
                    sa.Column('updated_at', sa.DateTime),
                    sa.Column('created_at', sa.DateTime))

    op.create_primary_key('BAD_REPLICAS_STATE_PK', 'bad_replicas', ['scope', 'name', 'rse_id', 'created_at'])
    op.create_check_constraint('BAD_REPLICAS_SCOPE_NN', 'bad_replicas', 'scope is not null')
    op.create_check_constraint('BAD_REPLICAS_NAME_NN', 'bad_replicas', 'name is not null')
    op.create_check_constraint('BAD_REPLICAS_RSE_ID_NN', 'bad_replicas', 'rse_id is not null')
    op.create_foreign_key('BAD_REPLICAS_ACCOUNT_FK', 'bad_replicas', 'accounts', ['account'], ['account'])
    op.create_index('BAD_REPLICAS_STATE_IDX', 'bad_replicas', ['rse_id', 'state'])


def downgrade():
    op.drop_table('bad_replicas')