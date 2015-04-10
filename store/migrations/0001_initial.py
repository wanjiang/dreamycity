# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderDate', models.DateTimeField(verbose_name=b'Order Date')),
                ('orderID', models.CharField(max_length=128)),
                ('comment', models.CharField(max_length=128)),
                ('isReturn', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemName', models.CharField(max_length=128)),
                ('cost', models.DecimalField(max_digits=16, decimal_places=2)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=20)),
                ('picture', models.CharField(max_length=128)),
                ('lackQuantity', models.IntegerField(default=0)),
                ('brokenQuantity', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoryName', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemName', models.CharField(max_length=128)),
                ('itemSName', models.CharField(max_length=128)),
                ('itemID', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('price', models.DecimalField(max_digits=16, decimal_places=2)),
                ('suggestPrice', models.DecimalField(max_digits=16, decimal_places=2)),
                ('cost', models.DecimalField(max_digits=16, decimal_places=2)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=20)),
                ('picture', models.CharField(max_length=128)),
                ('itemLink', models.CharField(max_length=128)),
                ('reoderLever', models.CharField(max_length=20)),
                ('isDeleted', models.BooleanField(default=False)),
                ('buyQuantity', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='store.StoreCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplierName', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='storeitem',
            name='supplier',
            field=models.ForeignKey(to='store.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='category',
            field=models.ForeignKey(to='store.StoreCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='itemID',
            field=models.ForeignKey(to='store.StoreItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='orderID',
            field=models.ForeignKey(to='store.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='supplier',
            field=models.ForeignKey(to='store.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(to='store.Supplier'),
            preserve_default=True,
        ),
    ]
