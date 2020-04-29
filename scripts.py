import os
import sys

new_app = "newApp"
new_app_name = "newAppName"


urls_string = "path('APP_TEMPLATE/', include('portals.APP_TEMPLATE.urls'))".replace("APP_TEMPLATE", new_app)
installed_apps_string = "portals.APP_TEMPLATE".replace("APP_TEMPLATE", new_app)


