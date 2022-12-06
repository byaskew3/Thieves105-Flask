"""empty message

Revision ID: 952ff5a2a6bb
Revises: 
Create Date: 2022-12-05 17:38:44.506626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '952ff5a2a6bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('img_url',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('caption',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=300),
               nullable=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.String(length=150),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=250),
               existing_nullable=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('caption',
               existing_type=sa.String(length=300),
               type_=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('img_url',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    op.drop_table('followers')
    # ### end Alembic commands ###