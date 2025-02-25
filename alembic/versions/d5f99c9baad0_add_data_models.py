"""add data models

Revision ID: d5f99c9baad0
Revises: 
Create Date: 2025-01-08 11:18:20.894840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5f99c9baad0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('department', sa.Enum('OPTOMETRY', 'GYNAECOLOGY', 'GENERAL', 'CARDIOLOGY', 'NEUROLOGY', 'PEDIATRICS', 'ORTHOPEDICS', name='departmentenum'), nullable=True),
    sa.Column('speciality', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('visit_date', sa.DateTime(), nullable=True),
    sa.Column('condition', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review', sa.String(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('appointment')
    op.drop_table('user')
    op.drop_table('patient')
    op.drop_table('doctor')
    # ### end Alembic commands ###
