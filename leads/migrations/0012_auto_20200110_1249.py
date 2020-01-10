# Generated by Django 2.2.4 on 2020-01-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20191223_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('call', 'Cuộc gọi điện thoại'), ('email', 'Email'), ('existing customer', 'Khách hàng hiện tại'), ('partner', 'Đối tác'), ('public relations', 'Quan hệ cộng đồng'), ('campaign', 'Chiến dịch'), ('other', 'Khác')], max_length=255, null=True, verbose_name='Source of Lead'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(blank=True, choices=[('assigned', 'Assigned'), ('in process', 'Đang xử lý'), ('converted', 'Chuyển thành khách hàng'), ('recycled', 'Recycled (Xoay vòng lại)'), ('closed', 'Đã đóng')], max_length=255, null=True, verbose_name='Status of Lead'),
        ),
    ]
