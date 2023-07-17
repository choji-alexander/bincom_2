from django.db import models


class AgentName(models.Model):
    firstname = models.CharField(max_length=250, null=False)
    lastname = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=250, null=True, default='random@gmail.com')
    phone = models.CharField(max_length=13, null=False)
    pollingunit_uniqueid = models.IntegerField(null=False)


class Announced_lga_results(models.Model):
    lga_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, default='N/A', null=False)


class Announced_state_results(models.Model):
    state_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, null=False)


class Announced_ward_results(models.Model):
    ward_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, null=False)


class States(models.Model):
    state_name = models.CharField(max_length=50, null=False)


class Lga(models.Model):
    lga_id = models.IntegerField(null=False)
    lga_name = models.CharField(max_length=50, null=False)
    state_id = models.ForeignKey(States, related_name='lga_state_id', on_delete=models.SET_NULL, null=True)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, null=False)


class Party(models.Model):
    party_id = models.CharField(max_length=11, null=False)
    party_name = models.CharField(max_length=11, null=False)


class Ward(models.Model):
    ward_id = models.IntegerField(null=False)
    ward_name = models.CharField(max_length=50, null=False)
    lga_id = models.ForeignKey(Lga, related_name='ward_lga_id', on_delete=models.SET_NULL, null=True)
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, null=False)


class Polling_unit(models.Model):
    polling_unit_id = models.ForeignKey(Ward, related_name='polling_unit_uniqueid', on_delete=models.SET_NULL, null=True
                                        )
    ward_id = models.ForeignKey(Ward, related_name='polling_ward_id', on_delete=models.SET_NULL, null=True)
    lga_id = models.ForeignKey(Lga, related_name='polling_lga_id', on_delete=models.SET_NULL, null=True)
    uniquewardid = models.ForeignKey(States, related_name='polling_state_id', on_delete=models.SET_NULL, null=True)
    polling_unit_number = models.CharField(max_length=50, default='N/A', null=True)
    polling_unit_name = models.CharField(max_length=50, default='N/A', null=True)
    polling_unit_description = models.TextField(null=True)
    lat = models.CharField(max_length=255, default='N/A', null=True)
    long = models.CharField(max_length=255, default='N/A', null=True)
    entered_by_user = models.CharField(max_length=50, default='N/A', null=True)
    date_entered = models.DateTimeField(auto_now_add=True, null=True)
    user_ip_address = models.CharField(max_length=50, default='N/A', null=True)


class Announced_pu_results(models.Model):
    polling_unit_uniqueid = models.ForeignKey(Polling_unit, related_name='polling_unit_uniqid',
                                              on_delete=models.SET_NULL, null=True)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, null=False)

