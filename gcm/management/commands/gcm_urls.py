from django.core.management.base import NoArgsCommand
from django.core.urlresolvers import reverse
from django.conf import settings


class Command(NoArgsCommand):
    help = "Show GCM urls"

    def show_line(self):
        self.stdout.write("%s\n" % ("-" * 30))

    def handle_noargs(self, **options):
        if(settings.INSTALLED_APPS.count('tastypie')>0):
            register_url = reverse("register-device", kwargs={'resource_name': 'device', 'api_name': 'v1'})
            unregister_url = reverse("unregister-device", kwargs={'resource_name': 'device', 'api_name': 'v1'})
        if(settings.INSTALLED_APPS.count('rest_framework')>0):
            register_url = reverse("register-device", kwargs={})
            unregister_url = reverse("unregister-device", kwargs={})



        self.show_line()
        self.stdout.write("GCM urls:\n")
        self.stdout.write("* Register device\n    %s\n" % register_url)
        self.stdout.write("* Unregister device\n    %s\n" % unregister_url)
        self.show_line()
