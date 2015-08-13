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

                listProject = {projectName, projectDirectory};

                projects[projectDirectory] = projectName

        return projects

def main(wf):
    projects = wf.cached_data('projects', getProjectDirectories, max_age= -1)

    for dir, name in projects.iteritems():
        wf.add_item(title=name,
                    subtitle=dir,
                    icon=ICON_WEB,
                    arg=dir,
                    valid=True)

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
