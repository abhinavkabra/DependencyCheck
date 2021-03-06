# MavenDependencyCheck
An automation Script to run [OWASP Dependency-Check](https://www.owasp.org/index.php/OWASP_Dependency_Check) on Maven Based projects.

This script basically clones the given repositories and builds them using maven. Once successful, it runs dependency-check on them and generates the reports

## Requirements
* Python modules: [os](https://docs.python.org/2/library/os.html) & [shutil](https://docs.python.org/2/library/shutil.html)
* Maven: Installation instructions can be found [here](https://maven.apache.org/install.html)
* [``` repo.conf```](https://github.com/abhinavkabra/DependencyCheck/blob/main/repo.conf) containing the git commands to be run for cloning the projects

Example commands for ```repo.conf```
 
 ```git clone https://github.com/elderstudios/uni-dvwa-spring.git```
 
## Usage
```python depcheck.py```

And let the script do the magic  

##### Tested and working fine on Windows / Python 2.7.18.   
Note: Dependency check might need internet access to update the NVD Database for which a proxy might needed if you are in a restricted environment. To configure this script to use proxy for this use this sample code to configure your proxy settings and uncomment line [57] and comment out line [56]. Refer: [Dependency check Command Line Arguments](https://jeremylong.github.io/DependencyCheck/dependency-check-cli/arguments.html)  
For running the mvn command using a proxy refer this [article](https://medium.com/@petehouston/execute-maven-behind-a-corporate-proxy-network-5e08d075f744)  

##### Also I know there is a [maven plugin](https://jeremylong.github.io/DependencyCheck/dependency-check-maven/) available for dependency check which can directly be injected to the project's pom.xml, but the use case for me was such that I did not have write access to the code repo and injecting the maven script for dependency check after cloning the projects and then building them was a bit time consuming.

