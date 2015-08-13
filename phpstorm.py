import sys
import glob
import json
from workflow import Workflow, ICON_WEB, web

def getProjectDirectories():
    with open('config.json') as data_file:
        data = json.load(data_file)
        projects = {}

        for dir in data['ProjectDirectories']:
            ProjectDirectories = glob.glob(dir + '/*/.idea')

            for project in ProjectDirectories:
                projectDirectory = project[:-6]
                folderList = projectDirectory.split('/')
                projectName = folderList[-1]

                projects[projectName] = projectDirectory

        return projects

def urlSearch(project):
    return project

def main(wf):
    allProjects = wf.cached_data('allProjects', getProjectDirectories, max_age= -1)

    """ Filter the projects """
    if len(wf.args):
        projects = wf.filter(wf.args[0], allProjects, key=urlSearch)
    else:
        projects = allProjects

    for project in projects:
        wf.add_item(title=project,
                    subtitle=allProjects[project],
                    icon="phpstorm.png",
                    arg=allProjects[project],
                    valid=True)

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
