import getdinerotoday.settings.settings as settings
import shutil
import os
import argparse


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


def create_new_portal(new_app, new_app_name, img_url):
    html_card = f"""
                <div class="col-md-3 col-sm-6">
                <div class="card mb-4 shadow-sm">
                    <img src="{img_url}]"
                         height="270px" width="100%" alt="">
                    <div class="card-body">
                        <p class="card-text">Click The Button Below To Enter The {new_app_name} Portal</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="btn-group">
                                <a href="/{new_app}" target="_blank" class="btn btn-primary">Enter Portal</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    """

    if f'portals.{new_app}' not in settings.INSTALLED_APPS:
        try:
            urls_string = "path('APP_TEMPLATE/', include('portals.APP_TEMPLATE.urls'))".replace("APP_TEMPLATE", new_app)
            installed_apps_string = "portals.APP_TEMPLATE".replace("APP_TEMPLATE", new_app)
            shutil.copytree("portals/APP_TEMPLATE", f"portals/{new_app}")
            os.rename(f"portals/{new_app}/templates/APP_TEMPLATE", f"portals/{new_app}/templates/{new_app}")
            dir_list = getListOfFiles(f"portals/{new_app}")
            for i in dir_list:
                try:
                    with open(i, "r") as f:
                        data = f.read().replace("{{ APP_TEMPLATE_NAME }}", new_app_name).replace("APP_TEMPLATE",
                                                                                                 new_app).replace(
                            "{{ PORTAL_IMAGE_URL }}", img_url)
                    with open(i, "wt") as f:
                        f.write(data)
                except Exception as e:
                    print("could not check", i, ", skipping.")

            for i in dir_list:
                if "APP_TEMPLATE" in i:
                    os.rename(i, i.replace("APP_TEMPLATE", new_app))

            with open('getdinerotoday/settings/settings.py', "r") as f:
                data = f.read()
                index = data.index("INSTALLED_APPS = [") + len("INSTALLED_APPS = [")
                data = data[:index] + f"\n    '{installed_apps_string}'," + data[index:]
            with open('getdinerotoday/settings/settings.py', "w") as f:
                f.write(data)

            with open('getdinerotoday/urls.py', "r") as f:
                data = f.read()
                index = data.index("urlpatterns = [") + len("urlpatterns = [")
                data = data[:index] + f"\n    {urls_string}," + data[index:]
            with open('getdinerotoday/urls.py', "w") as f:
                f.write(data)

            with open('getdinerotoday/templates/homepage.html', "r") as f:
                data = f.read()
                index = data.index("<!-- ANCHOR_FOR_NEW_CARDS -->")
                data = data[:index] + f"\n {html_card} \n" + data[index:]
            with open('getdinerotoday/templates/homepage.html', "w") as f:
                f.write(data)

        except Exception as e:
            print(e)
    else:
        print('app with that name is already installed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List the content of a folder')
    parser.add_argument('Action', metavar='action', type=str, help='An action you would like to perform')
    parser.add_argument('-n', action='store', type=str, nargs='?',
                        help='Name of the new portal, should not contain any special chars')
    parser.add_argument('-dn', action='store', type=str, nargs='?', help='Displayed name of the new portal')
    parser.add_argument('-img', action='store', type=str, nargs='?', help='Image url')

    args = parser.parse_args()
    action = args.Action

    if action == 'createportal':
        app = args.n
        app_name = args.dn
        imgurl = args.img

        if app and app_name and imgurl:
            create_new_portal(app, app_name, imgurl)
            parser.exit(0, message=f'Successfully created new portal {app_name}')

        else:
            parser.format_help()
            parser.exit(1, message='Check action, app, and displayname')
