from dynamic.models import Subdomain
from user.models import Profile


class WhiteLabelService:

    @staticmethod
    def get_administrated_subdomains(request):
        administrated_subdomains = []
        subdomains = Subdomain.objects.all()
        for subdomain in subdomains:
            admins = [i.user.username for i in subdomain.admins.all()]
            if request.user.username in admins:
                administrated_subdomains.append(subdomain.sub_name)
        return administrated_subdomains

    @staticmethod
    def get_subdomain_users(subdomain):
        users = Profile.objects.filter(whitelabel_portal=subdomain)
        return users

    @staticmethod
    def get_users_by_subdomains(request):
        admin_subdomains = WhiteLabelService.get_administrated_subdomains(request)
        response = []
        for i in admin_subdomains:
            subdomain_users = {
                'sub_name': i,
                'users': WhiteLabelService.get_subdomain_users(i)
            }
            response.append(subdomain_users)
        return response
