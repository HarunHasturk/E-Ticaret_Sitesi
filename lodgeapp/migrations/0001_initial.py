# Generated by Django 4.1.3 on 2022-12-24 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=255)),
                ('about_content', models.TextField()),
                ('about_url', models.URLField(blank=True)),
                ('about_image', models.ImageField(upload_to='lodgeapp/static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='BestPrices',
            fields=[
                ('price_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price_assessment', models.CharField(max_length=255)),
                ('price_image', models.ImageField(upload_to='lodgeapp/static/images/')),
                ('price_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_image', models.ImageField(upload_to='lodgeapp/static/images/')),
                ('product_price', models.CharField(max_length=255)),
                ('product_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('slider_id', models.IntegerField(primary_key=True, serialize=False)),
                ('slider_collection', models.CharField(max_length=255)),
                ('slider_title', models.CharField(max_length=255)),
                ('slider_content', models.TextField()),
                ('slider_url', models.URLField(blank=True)),
                ('slider_image', models.ImageField(upload_to='lodgeapp/static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_title', models.CharField(max_length=255)),
                ('special_url', models.URLField(blank=True)),
                ('special_image', models.ImageField(upload_to='lodgeapp/static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('testimonial_id', models.IntegerField(primary_key=True, serialize=False)),
                ('testimonial_image', models.ImageField(upload_to='lodgeapp/static/images/')),
                ('testimonial_name', models.CharField(max_length=255)),
                ('testimonial_recommendation', models.CharField(max_length=255)),
                ('testimonial_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lodgeapp.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lodgeapp.product')),
            ],
        ),
    ]