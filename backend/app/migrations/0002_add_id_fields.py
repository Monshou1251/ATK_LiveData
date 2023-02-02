from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial')
    ]

    operations = [
        migrations.AddField(
            model_name='cdcconn',
            name='id',
            field=models.BigAutoField(primary_key=True)
        ),
        migrations.AddField(
            model_name='cdcfields',
            name='id',
            field=models.BigAutoField(primary_key=True)
        ),
        migrations.AddField(
            model_name='cdcstatus',
            name='id',
            field=models.BigAutoField(primary_key=True)
        ),
        migrations.AddField(
            model_name='cdctables',
            name='id',
            field=models.BigAutoField(primary_key=True)
        ),
    ]