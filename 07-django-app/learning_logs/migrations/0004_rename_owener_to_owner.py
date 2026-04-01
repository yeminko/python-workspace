from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owener'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='owener',
            new_name='owner',
        ),
    ]
