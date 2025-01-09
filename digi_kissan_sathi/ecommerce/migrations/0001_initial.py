# Generated by Django 5.1.4 on 2025-01-04 09:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_Seller_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busines_name', models.CharField(max_length=150)),
                ('business_name_nepali', models.CharField(blank=True, max_length=150, null=True)),
                ('business_address', models.TextField()),
                ('busines_contact_number', models.CharField(max_length=15)),
                ('business_email', models.EmailField(max_length=254)),
                ('citizenship_number', models.CharField(blank=True, max_length=20, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=20, null=True)),
                ('goverment_id', models.FileField(blank=True, upload_to='documents/')),
                ('verification_status', models.CharField(choices=[('pending', 'pending'), ('Verified', 'Verified'), ('Rejected', 'Rejected')], default='pending', max_length=20)),
                ('bank_account_number', models.CharField(max_length=30)),
                ('bank_name', models.CharField(blank=True, choices=[('Rastriya Banijya', 'Rastriya Banijya'), ('Nabil Bank', 'Nabil Bank'), ('Himalaya Bank', 'Himalaya Bank'), ('Global IME', 'Global IME'), ('Nepal Investment', 'Nepal Investment'), ('Agriculture Development', 'Agriculture Development')], max_length=100, null=True)),
                ('ifcs_code', models.CharField(max_length=11)),
                ('payment_gateway_id', models.CharField(blank=True, max_length=100, null=True)),
                ('categories', models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Rice', 'Rice'), ('Spices', 'Spices'), ('Other', 'Other')], default='Other', max_length=50)),
                ('total_sales', models.PositiveIntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('reviews_count', models.PositiveIntegerField(default=0)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='seller_pictures/')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
