# Generated by Django 3.2.7 on 2021-10-10 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_product_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_case_name', models.CharField(max_length=200, verbose_name='用例名称')),
                ('web_test_result', models.BooleanField(verbose_name='测试结果')),
                ('web_tester', models.CharField(max_length=200, verbose_name='测试负责人')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'web测试用例',
                'verbose_name_plural': 'web测试用例',
            },
        ),
        migrations.CreateModel(
            name='WebCaseStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_case_name', models.CharField(max_length=200, verbose_name='web测试用例名称')),
                ('web_case_step', models.CharField(max_length=200, verbose_name='web测试用例步骤')),
                ('web_case_obj_name', models.CharField(max_length=200, verbose_name='web测试对象名称')),
                ('web_case_find_method', models.CharField(max_length=200, verbose_name='定位方式')),
                ('web_case_element', models.CharField(max_length=200, verbose_name='控件元素')),
                ('web_case_opt_method', models.CharField(max_length=200, verbose_name='操作方法')),
                ('web_case_test_data', models.CharField(max_length=200, verbose_name='测试数据')),
                ('web_case_assert_data', models.CharField(max_length=200, verbose_name='验证数据')),
                ('web_case_result', models.CharField(max_length=200, verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('web_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_test.webcase')),
            ],
        ),
    ]
