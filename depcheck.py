# Project : MavenDependencyCheck
# Description: An automation Script to run OWASP Dependency-Check on Maven Based projects.
# Version : 1.5
# Authors" Abhinav Kabra

import os
import shutil

def init_pull():
    "Downloads Dependency-check and creates directories"
    report_dir = "depcheckreports"
    project_dir = "projects"
    dependency_check_launcher = "dependency-check"
    if not os.path.exists(report_dir):
        print ("## The result directory not present so creating directory")
        os.makedirs(report_dir)
    if not os.path.exists(project_dir):
        print ("## The project directory not present so creating directory for project repository")
        os.makedirs(project_dir)
    if not os.path.exists(dependency_check_launcher):
        print ("## The dependency_check_launcher directory not present , pulling launcher")
        #launcher_pull = "curl -L https://dl.bintray.com/jeremy-long/owasp/dependency-check-6.0.2-release.zip"
        #os.system(launcher_pull)
        unzip_launcher = "unzip dependency-check-6.5.0-release.zip"
        os.system(unzip_launcher)

def read_conf():
    "Runs the git commands from the repo.conf file to clone the projects"
    print ("## Start Pulling Repo successfully")
    with open('repo.conf') as f:
        for line in f:
            print (line)
            linevar = " " + line
            os.chdir("./projects/")
            os.system('%s' % linevar)
            print ("## Repo pulled successfully")
            os.chdir("../")

def launcher():
    "Pulling the latest repo and building the project using mvn"
    laucher_path = "dependency-check/bin/dependency-check.sh"
    print ("#### Pulling git for latest repo and building the project using maven")
    os.system('ls ./projects/ > project_name.txt')
    report_dir = "result"
    with open('project_name.txt') as p:
    	for pname in p:
            print (pname)
            build_path = "./projects/" + pname.rstrip("\n")
            os.chdir(build_path)
            os.system('git pull')
            os.system('mvn clean install -DskipTests=true')
            project_path = "./projects/" + pname
            result_path = "./depcheckreports/" + pname
            print ("#### launching Dependency Check ..." + project_path)
            os.chdir("../../")
            os.system('bash dependency-check/bin/dependency-check.sh --project test --disableNodeAudit --disableNodeJS --format ALL -s %s ' % project_path)
            # os.system('bash dependency-check/bin/dependency-check.sh --project test --disableNodeAudit --disableNodeJS --format ALL --proxyserver <proxy ip> --proxyport <port>-s %s ' % project_path)
            print ("## Latest Repo Pulled successfully")
            extlists=['.csv','.html','.xml','.json']
            for ext in extlists:
                src = "dependency-check-report" + ext
                dst = "./depcheckreports/" + pname.strip() + ext
                shutil.move(src, dst)
    os.chdir("../")
           
def main():
    init_pull()
    read_conf()
    launcher()

if __name__ == "__main__":
    main()

