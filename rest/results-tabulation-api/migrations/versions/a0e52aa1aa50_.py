"""empty message

Revision ID: a0e52aa1aa50
Revises: 0829b200eb31
Create Date: 2019-10-24 18:59:59.990637

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a0e52aa1aa50'
down_revision = '0829b200eb31'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tallySheetVersionRow_CE_201_PV_1',
    sa.Column('tallySheetVersionRowId', sa.Integer(), nullable=False),
    sa.Column('tallySheetVersionId', sa.Integer(), nullable=True),
    sa.Column('ballotBoxId', sa.String(length=20), nullable=False),
    sa.Column('numberOfPacketsInserted', sa.Integer(), nullable=False),
    sa.Column('numberOfAPacketsFound', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tallySheetVersionId'], ['tallySheetVersion.tallySheetVersionId'], ),
    sa.PrimaryKeyConstraint('tallySheetVersionRowId'),
    sa.UniqueConstraint('tallySheetVersionId', 'ballotBoxId', name='BallotBoxPerCE201PV')
    )
    op.drop_table('tallySheetVersionRow_CE_201_PV')
    op.drop_index('stamp_barcodeId_fk', table_name='stamp')
    op.create_foreign_key(None, 'stamp', 'barcode', ['barcodeId'], ['barcodeId'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stamp', type_='foreignkey')
    op.create_index('stamp_barcodeId_fk', 'stamp', ['barcodeId'], unique=False)
    op.create_table('tallySheetVersionRow_CE_201_PV',
    sa.Column('tallySheetVersionRowId', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('tallySheetVersionId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('ballotBoxStationaryItemId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('numberOfPacketsInserted', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('numberOfAPacketsFound', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['ballotBoxStationaryItemId'], ['ballotBox.stationaryItemId'], name='tallySheetVersionRow_CE_201_PV_ibfk_2'),
    sa.ForeignKeyConstraint(['tallySheetVersionId'], ['tallySheetVersion.tallySheetVersionId'], name='tallySheetVersionRow_CE_201_PV_ibfk_1'),
    sa.PrimaryKeyConstraint('tallySheetVersionRowId'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('tallySheetVersionRow_CE_201_PV_1')
    ### end Alembic commands ###