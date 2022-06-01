# Generated by Django 3.2.5 on 2022-06-01 09:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_num', models.AutoField(primary_key=True, serialize=False)),
                ('product_price', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('product_stock', models.IntegerField(default=0)),
                ('product_date', models.DateField(auto_now_add=True)),
                ('product_thumnail', models.BinaryField(null=True)),
                ('product_rate', models.FloatField(default=0)),
                ('product_image', models.BinaryField(null=True)),
                ('product_color', models.CharField(max_length=50, null=True)),
                ('product_size', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품(들)',
                'db_table': 'P2_Product',
            },
        ),
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('category_code', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '상품카테고리',
                'verbose_name_plural': '상품카테고리(들)',
                'db_table': 'P2_Product_category',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('nickname', models.CharField(max_length=32, unique=True)),
                ('email', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=200, null=True)),
                ('mobile', models.CharField(max_length=16, unique=True)),
                ('gender', models.CharField(max_length=2, null=True)),
                ('age', models.CharField(max_length=8, null=True)),
                ('sociallogin', models.CharField(max_length=16)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('receive_marketing', models.BooleanField()),
            ],
            options={
                'verbose_name': '회원',
                'verbose_name_plural': '회원(들)',
                'db_table': 'P2_user',
            },
        ),
        migrations.CreateModel(
            name='User_order',
            fields=[
                ('order_num', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('adress', models.CharField(max_length=200)),
                ('receive_name', models.CharField(max_length=32)),
                ('receive_phone', models.CharField(max_length=16)),
                ('orderstatus', models.IntegerField(choices=[('1', '주문접수'), ('2', '배송준비'), ('3', '출고완료'), ('4', '배송중'), ('5', '배송완료'), ('6', '주문취소'), ('7', '교환/환불대기'), ('8', '교환/환불완료')])),
                ('received_date', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문(들)',
                'db_table': 'P2_User_order',
            },
        ),
        migrations.CreateModel(
            name='User_order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_count', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('order_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user_order')),
                ('product_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name': '주문상세정보',
                'verbose_name_plural': '주문상세정보(들)',
                'db_table': 'P2_User_order_detail',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product_category'),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('product_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
            options={
                'verbose_name': '상품평점',
                'verbose_name_plural': '상품평점(들)',
                'db_table': 'P2_Grade',
            },
        ),
        migrations.CreateModel(
            name='Customer_inquiry',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=500)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('answer', models.CharField(max_length=500, null=True)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
            options={
                'verbose_name': '문의사항',
                'verbose_name_plural': '문의사항(들)',
                'db_table': 'P2_Customer_inquiry',
            },
        ),
        migrations.CreateModel(
            name='Cuppon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_rate', models.FloatField()),
                ('cuppon_num', models.IntegerField(default=0)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
            options={
                'verbose_name': '쿠폰',
                'verbose_name_plural': '쿠폰(들)',
                'db_table': 'P2_cuppon',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_count', models.IntegerField()),
                ('product_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
            options={
                'verbose_name': '장바구니',
                'verbose_name_plural': '장바구니(들)',
                'db_table': 'P2_Cart',
            },
        ),
    ]
