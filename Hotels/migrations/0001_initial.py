# Generated by Django 3.2.8 on 2021-11-04 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('Content', models.TextField(default='Start and end in San Francisco! With the in-depth cultural .', max_length=200)),
                ('Banner_Image', models.ImageField(upload_to='')),
                ('Gallery', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('Facilities', models.ManyToManyField(to='Hotels.Facilities')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField()),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('room_no', models.CharField(max_length=5)),
                ('room_type', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('price', models.FloatField(default=1000.0)),
                ('no_of_days_advance', models.IntegerField()),
                ('start_date', models.DateField()),
                ('room_image', models.ImageField(default='0.jpeg', upload_to='media')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotels.hotel')),
                ('room_attribute', models.ManyToManyField(to='Hotels.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(upload_to='media')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotels.rooms')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='Hotel_service',
            field=models.ManyToManyField(to='Hotels.Hotel_service'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='Property_type',
            field=models.ManyToManyField(to='Hotels.Property_type'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_attribute',
            field=models.ManyToManyField(to='Hotels.Attribute'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('amount', models.FloatField()),
                ('booked_on', models.DateTimeField(auto_now=True)),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotels.rooms')),
            ],
        ),
    ]
