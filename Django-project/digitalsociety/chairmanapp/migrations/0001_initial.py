# Generated by Django 4.1.7 on 2023-03-21 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verify', models.BooleanField(default=False)),
                ('otp', models.IntegerField(default=456)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Societymember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=20)),
                ('occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('block_no', models.CharField(max_length=10)),
                ('no_of_familymembers', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, max_length=20, null=True)),
                ('vehicle_details', models.CharField(blank=True, max_length=10, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('house_ownership', models.CharField(blank=True, max_length=20, null=True)),
                ('pic', models.FileField(default='media/default.png', upload_to='media/upload')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeViewDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.notice')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='notice',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user'),
        ),
        migrations.CreateModel(
            name='Maintainance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('duedate', models.DateField(max_length=30)),
                ('status', models.CharField(default='PENDING', max_length=30)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.societymember')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='EventViewDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user'),
        ),
        migrations.CreateModel(
            name='ComplaintViewDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.complaint')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='complaint',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user'),
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=20)),
                ('pic', models.FileField(default='media/default.pic.png', upload_to='media/upload')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
    ]
