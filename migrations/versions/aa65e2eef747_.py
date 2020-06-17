"""empty message
Revision ID: aa65e2eef747
Revises: Create Date: 2020-06-16 13:23:04.185315
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'aa65e2eef747'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tenders',
                    sa.Column('tenderID',
                              sa.Integer(), nullable=False),
                    sa.Column('tenderNumber',
                              sa.String(length=25), nullable=False),
                    sa.Column('tenderDescription',
                              sa.String(length=80), nullable=False),
                    sa.Column('category',
                              sa.String(length=40), nullable=False),
                    sa.Column('datePublished',
                              sa.String(length=15), nullable=False),
                    sa.Column('closingDate',
                              sa.String(length=15), nullable=False),
                    sa.Column('tenderStatus',
                              sa.String(length=10), nullable=False),
                    sa.Column('nameOfInstitution',
                              sa.String(length=60), nullable=False),
                    sa.Column('officalLocation',
                              sa.String(length=60), nullable=False),
                    sa.Column('InstitutionContactPerson',
                              sa.String(length=60), nullable=False),
                    sa.Column('InstitutionPersonEmail',
                              sa.String(length=60), nullable=False),
                    sa.Column('InstitutionPersonPhone',
                              sa.String(length=60), nullable=False),
                    sa.Column('companyNames',
                              sqlite.JSON(), server_default='{}',
                              nullable=True),
                    sa.PrimaryKeyConstraint('tenderID'),
                    sa.UniqueConstraint('tenderNumber')
                    )
    op.create_table('users',
                    sa.Column('id',
                              sa.Integer(), nullable=False),
                    sa.Column('email',
                              sa.String(length=60), nullable=True),
                    sa.Column('username',
                              sa.String(length=50), nullable=True),
                    sa.Column('first_name',
                              sa.String(length=60), nullable=True),
                    sa.Column('last_name',
                              sa.String(length=60), nullable=True),
                    sa.Column('password_hash',
                              sa.String(length=128), nullable=True),
                    sa.Column('is_admin',
                              sa.Boolean(), nullable=True),
                    sa.Column('created_at',
                              sa.DateTime(), nullable=True),
                    sa.Column('updated_at',
                              sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_users_email'),
                    'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'),
                    'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_last_name'),
                    'users', ['last_name'], unique=False)
    op.create_index(op.f('ix_users_username'),
                    'users', ['username'], unique=True)
    op.create_table('company',
                    sa.Column('companyID',
                              sa.Integer(), nullable=False),
                    sa.Column('companyName',
                              sa.String(length=60), nullable=False),
                    sa.Column('companyRegistrationNo',
                              sa.String(length=50), nullable=False),
                    sa.Column('directors',
                              sa.String(length=60), nullable=False),
                    sa.Column('companyPhoneNumber',
                              sa.String(length=15), nullable=False),
                    sa.Column('companyAddress',
                              sa.String(length=50), nullable=False),
                    sa.Column('applyCount',
                              sa.Integer(), nullable=True),
                    sa.Column('winningCount',
                              sa.Integer(), nullable=True),
                    sa.Column('isWinner',
                              sa.Unicode(), nullable=True),
                    sa.Column('awardedPoint',
                              sa.Integer(), nullable=True),
                    sa.Column('tenderNumber',
                              sa.String(length=25), nullable=False),
                    sa.Column('tenderID',
                              sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['tenderID'],
                                            ['tenders.tenderID'], ),
                    sa.PrimaryKeyConstraint('companyID'),
                    sa.UniqueConstraint('applyCount')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('tenders')
    # ### end Alembic commands ###