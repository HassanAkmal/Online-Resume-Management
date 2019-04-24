# Generated by Django 2.1.7 on 2019-04-24 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='no-img.jpg', upload_to='images/')),
                ('date_of_birth', models.DateField(default='1999-12-31')),
                ('gender', models.CharField(default='M', max_length=2)),
                ('contact_num1', models.PositiveIntegerField(default='03162082420', max_length=11)),
                ('contact_num2', models.PositiveIntegerField(default='03162082420', max_length=11)),
                ('address', models.CharField(max_length=264)),
                ('city', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Databackup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasize', models.CharField(max_length=50)),
                ('lastUse_date', models.DateField()),
                ('notification_sent_status', models.PositiveIntegerField()),
                ('notification_date', models.DateField()),
                ('notification_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_summary', models.TextField()),
                ('experience_years', models.FloatField()),
                ('previous_employer', models.CharField(max_length=50)),
                ('previous_designation', models.CharField(max_length=50)),
                ('previous_organization_experience', models.FloatField()),
                ('previous_responsibilities', models.CharField(max_length=50)),
                ('date_of_leaving_job', models.DateField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Hr_Manger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, default='no-img.jpg', upload_to='images/')),
                ('date_of_birth', models.DateField(default='1999-12-31')),
                ('gender', models.CharField(default='M', max_length=2)),
                ('contact_num1', models.PositiveIntegerField(default='03162082420', max_length=11)),
                ('contact_num2', models.PositiveIntegerField(default='03162082420', max_length=11)),
                ('address', models.CharField(max_length=264)),
                ('city', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('duration', models.TimeField()),
                ('required_skills', models.CharField(max_length=20)),
                ('locations', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('details_document', models.ImageField(blank=True, default='no-img.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_acknowledged', models.CharField(max_length=2)),
                ('started_at', models.DateTimeField()),
                ('interview_question_candidate_answer', models.PositiveIntegerField()),
                ('job_status', models.CharField(max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_question', models.CharField(max_length=50)),
                ('question_correct_answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('descriptions', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50)),
                ('required_skills', models.CharField(max_length=50)),
                ('locations', models.CharField(max_length=50)),
                ('min_education', models.CharField(max_length=50)),
                ('min_experience', models.CharField(max_length=50)),
                ('age_requirements', models.CharField(max_length=50)),
                ('gender', models.CharField(default='M', max_length=2)),
                ('closing_date', models.DateField()),
                ('status', models.CharField(max_length=2)),
                ('salary', models.PositiveIntegerField()),
                ('additional_benefits', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='none@email.com', max_length=254)),
                ('sequarity_question', models.CharField(default='', max_length=255)),
                ('sequarity_answer', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_last_degree', models.CharField(max_length=50)),
                ('institute_last_degree', models.CharField(max_length=50)),
                ('performance_second_last_degree', models.FloatField()),
                ('performance_last_degree', models.FloatField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Applicant')),
                ('hr_manger', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Hr_Manger')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_refrence', models.CharField(max_length=20)),
                ('affiliation_of_reference', models.CharField(max_length=20)),
                ('contact_of_reference', models.PositiveIntegerField(max_length=11)),
                ('email_of_reference', models.EmailField(default='fast@gmail.com', max_length=254)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Applicant')),
                ('hr_manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Hr_Manger')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_employer', models.CharField(max_length=20)),
                ('current_designation', models.CharField(max_length=20)),
                ('current_organization_experience', models.CharField(max_length=10)),
                ('objective', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('joining_date', models.DateField()),
                ('skills', models.CharField(max_length=20)),
                ('min_salary', models.PositiveIntegerField()),
                ('extra_curricular', models.CharField(max_length=50)),
                ('other_interests', models.CharField(max_length=50)),
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Applicant')),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Internship')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Job')),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='interview_question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.InterviewQuestion'),
        ),
        migrations.AddField(
            model_name='interview',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Job'),
        ),
        migrations.AddField(
            model_name='experience',
            name='hr_manger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Hr_Manger'),
        ),
    ]
