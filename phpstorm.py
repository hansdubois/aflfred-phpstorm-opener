import sys
import glob
import json
from workflow import Workflow, ICON_WEB, web

def main(wf):
    with open('config.json') as data_file:
        data = json.load(data_file)

        for dir in data['ProjectDirectories']:
            ProjectDirectories = glob.glob(dir + '/*/.idea')

            for project in ProjectDirectories:
                projectDirectory = project[:-6]
                folderList = projectDirectory.split('/')
                projectName = folderList[-1]

                wf.add_item(title=projectName,
                            subtitle=projectDirectory,
                            icon=ICON_WEB,
                            arg=projectDirectory,
                            valid=True)

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
