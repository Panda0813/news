"""empty message

Revision ID: 5ebc37685dd6
Revises: 230e90f5c618
Create Date: 2018-05-30 17:50:54.653107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ebc37685dd6'
down_revision = '230e90f5c618'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('origin', sa.String(length=50), nullable=True),
    sa.Column('cate_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cate_id'], ['news_category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_article')
    # ### end Alembic commands ###
