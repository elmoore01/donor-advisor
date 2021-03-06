from django.forms import ModelForm

from .models import Organization, Donation, BoardMember

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        labels = {
            'description': 'About Us',
            'mission_statement': 'Mission Statement'
        }
        fields = [
            'name', 'fiscal_sponsor', 'ein', 'contact_name', 'contact_title', 'contact_email', 'address', 'city', 
            'state', 'zip_code', 'phone', 'website_url', 'category', 'guidestar_url', 'logo_url', 'mission_statement', 'description',
        ]

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        labels = {
            'amount': 'Donation amount',
            'anonymous': 'Remain Anonymous?'
        }
        fields = ['amount', 'anonymous']

class BoardMemberForm(ModelForm):
    class Meta:
        model = BoardMember
        labels = {
            'member': 'Full Name',
        }
        fields = ['member', 'company', 'title']